"""A file containing the implementation of the Model class for database management"""

import copy
import uuid

from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

from .core import LightDB
from .exceptions import ValidationError, NoArgsProvidedError
from .fields import Field
from .query import Query

MODEL = TypeVar("MODEL", bound="Model")


class ModelMeta(type):
    """A metaclass for the Model class that ensures that required class-level attributes are present and have valid types"""

    def __new__(mcs, name: str, bases: Tuple[type, ...], attrs: Dict[str, Any], **kwargs) -> "Model":
        if name != "Model":
            table = kwargs.pop("table")
            if not table:
                raise ValueError("`table` is required for model classes")

            if not isinstance(table, str):
                raise ValidationError(f"`table` must be of type `str` (`{type(table)}` given)")

            attrs["__table__"] = table

            if not attrs.get("__db__"):
                attrs["__db__"] = LightDB.current()

            annotations: Dict[str, Any] = attrs.get("__annotations__", {})
            fields_map: Dict[str, Any] = {}

            def add_field(field_name: str, field_type: Type, field_default: Any = None) -> None:
                field = Field(name=field_name, annotation=field_type)
                if field_default is not None:
                    field.default = field_default

                attrs[field_name] = field
                fields_map[field_name] = field

            if "_id" not in annotations:
                annotations["_id"] = str
                add_field("_id", str, attrs.get("_id"))

            for field_name, field_type in annotations.items():
                if field_name != "_id":
                    add_field(field_name, field_type, attrs.get(field_name))

            attrs["_fields_map"] = fields_map

        return super().__new__(mcs, name, bases, attrs)


class Model(metaclass=ModelMeta):
    """A base model class that provides a simple interface for interacting with data in a LightDB database"""

    __table__: str = None
    __db__: LightDB = None

    def __init__(self, **kwargs) -> None:
        """Initializes a new instance of the model with the provided keyword arguments

        Params:
            kwargs (``Dict[str, Any]``): Keyword arguments representing field names and values for the model instance
        """
        self._fields_map: Dict[str, Field] = copy.deepcopy(self._fields_map)

        if "_id" not in kwargs:
            kwargs["_id"] = str(uuid.uuid4())

        for name, field in self._fields_map.items():
            value = kwargs.get(name, field.value if field.value is not None else field.default)

            field.value = value
            field.validate()

            self._fields_map[name] = field
            super().__setattr__(name, field.value)

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self._fields_map:
            field = self._fields_map[key]
            field.value = value
            field.validate()
        else:
            super().__setattr__(key, value)

    def __getattribute__(self, item: Any) -> Any:
        fields_map = super().__getattribute__("_fields_map")
        if item in fields_map:
            value = fields_map[item].value
        else:
            value = super().__getattribute__(item)

        return value

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        fields_info = [f"{name}={field.value}" for name, field in self._fields_map.items()]
        return f"{self.__class__.__name__}({', '.join(fields_info)})"

    @classmethod
    def create(cls: Type[MODEL], **kwargs) -> MODEL:
        """Creates a new instance of the model with the provided keyword arguments and saves it to the database

        Params:
            kwargs (``Dict[str, Any]``): Keyword arguments representing field names and values for the model instance

        Returns:
            ``Model``: The newly created instance of the model
        """
        if not kwargs:
            raise NoArgsProvidedError("No `kwargs` were provided")

        instance = cls(**kwargs)
        instance.save()
        return instance

    @classmethod
    def get(cls: Type[MODEL], *args, **kwargs) -> Optional[MODEL]:
        """Retrieves a single instance of the model that matches the provided filter criteria

        Params:
            kwargs (``Dict[str, Any]``): Keyword arguments representing filter criteria for the model instance

        Returns:
            ``Optional[Model]``: The matching instance of the model, or None if no matching instance is found
        """
        if not (args or kwargs):
            raise NoArgsProvidedError("No `args` or `kwargs` were provided")

        results = cls.filter(*args, **kwargs)
        if not results:
            return None

        if len(results) > 1:
            raise ValueError(f"Multiple instances of `{cls.__name__}` model found by the specified filters")

        return results[0]

    def save(self) -> None:
        """Saves the current state of the model instance to the database"""
        existing_instance = self.get(_id=self._fields_map["_id"].value)
        if existing_instance:
            existing_instance.delete()

        new_data = {name: field.value for name, field in self._fields_map.items()}
        self.__db__.setdefault(self.__table__, []).append(new_data)
        self.__db__.save()

    def delete(self) -> None:
        """Deletes the current instance of the model from the database"""
        rows = self.__db__.get(self.__table__, [])

        for item in rows:
            if item["_id"] == self._fields_map["_id"].value:
                rows.remove(item)
                self.__db__.save()

    @classmethod
    def filter(cls: Type[MODEL], *args, **kwargs) -> List[MODEL]:
        """Retrieves a list of instances of the model that matmatch thech the provided filter criteria

        Params:
            kwargs (``Dict[str, Any]``): Keyword arguments representing filter criteria for the model instances

        Returns:
            A list of instances of the model that provided filter criteria
        """
        if not (args or kwargs):
            raise NoArgsProvidedError("No `args` or `kwargs` were provided")

        query = Query(cls)
        query.where(*args, **kwargs)
        return query.execute()

    @classmethod
    def all(cls: Type[MODEL], use_db: LightDB = None) -> List[MODEL]:
        """Retrieves a list of all instances of the model from the database

        Returns:
            ``List[Model]``: A list of all instances of the model
        """
        results = []
        for row in (use_db or cls.__db__).get(cls.__table__, []):
            results.append(cls(**row))
        return results
