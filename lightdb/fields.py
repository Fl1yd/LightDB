"""A file containing the implementation of the Field class for data validation and storage"""

from typing import Any, List, Dict, Optional, get_origin, get_args, TYPE_CHECKING

from .exceptions import ValidationError
from .query import Condition

if TYPE_CHECKING:
    from .models import Model, ModelMeta


class Field:
    """A class for representing a single field in a data model"""

    def __init__(
        self,
        name: Optional[str] = None,
        value: Optional[Any] = None,
        annotation: Optional[Any] = None,
        default: Optional[Any] = None
    ) -> None:
        """Initializes a new instance of the field with the provided arguments

        Params:
            annotation (``str``, optional): The name of the field

            annotation (``Any``, optional): The type of the field

            value (``Any``, optional): The current value of the field

            default (``Any``, optional): The default value of the field
        """
        self.name = name
        self.annotation = annotation
        self.value = value
        self.default = default

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Field(name={self.name}, annotation={self.annotation}, value={self.value}, default={self.default})"

    def validate(self, value: Any = None) -> None:
        """Validates a field value against its type annotation

        Params:
            value (``Any``, optional): The value to validate. Defaults to None
        """
        if not self.annotation:
            return

        value = value if value is not None else self.value
        expected_type = self.annotation
        origin = get_origin(expected_type)
        args = get_args(expected_type)

        if origin is None:
            if not isinstance(value, expected_type):
                raise ValidationError(f"Expected value of type `{expected_type.__name__}` for field `{self.name}`, got `{type(value).__name__}`")

        elif origin in [list, List]:
            if not isinstance(value, list):
                raise ValidationError(f"Expected value of type `list` for field `{self.name}`, got `{type(value).__name__}`")

            item_type = args[0] if args else Any

            for item in value:
                if not isinstance(item, item_type):
                    raise ValidationError(f"Expected element of type `{item_type.__name__}` in list for field `{self.name}`, got `{type(item).__name__}`")

        elif origin in [dict, Dict]:
            if not isinstance(value, dict):
                raise ValidationError(f"Expected value of type `dict` for field `{self.name}`, got `{type(value).__name__}`")

            key_type = args[0] if args else Any
            value_type = args[1] if len(args) > 1 else Any

            for k, v in value.items():
                if not isinstance(k, key_type):
                    raise ValidationError(f"Expected key of type `{key_type.__name__}` in dict for field `{self.name}`, got `{type(k).__name__}`")
                if not isinstance(v, value_type):
                    raise ValidationError(f"Expected value of type `{value_type.__name__}` in dict for field `{self.name}`, got `{type(v).__name__}`")

        else:
            raise ValidationError(f"Unsupported type annotation `{expected_type}` for field `{self.name}`")

    def __get__(self, instance: "Model", owner: "ModelMeta") -> Any:
        if instance is None:
            return self
        return self.value

    def __set__(self, instance: "Model", value: Any) -> None:
        self.validate(value)
        self.value = value

    def __eq__(self, other: Any):
        return Condition(self, "==", other)

    def __ne__(self, other: Any):
        return Condition(self, "!=", other)

    def __lt__(self, other: Any):
        return Condition(self, "<", other)

    def __le__(self, other: Any):
        return Condition(self, "<=", other)

    def __gt__(self, other: Any):
        return Condition(self, ">", other)

    def __ge__(self, other: Any):
        return Condition(self, ">=", other)
