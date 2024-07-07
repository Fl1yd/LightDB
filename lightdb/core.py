"""A file that containing the main implementation of the LightDB database management system"""

import json

from pathlib import Path
from typing import Any, Dict, TypeVar, Union, overload

_T = TypeVar("_T")
_VT = TypeVar("_VT")


class LightDB(dict):
    """Light Database
    ~~~~~~~~~~~~~~

    A lightweight database implemented as a dictionary with JSON file storage.

    This class extends the built-in Python `dict` class to provide a simple and easy-to-use
    key-value store that persists its data in a JSON file. The class provides methods to set, get,
    and remove individual key-value pairs.
    """

    _current_db: "LightDB" = None

    def __init__(self, location: str) -> None:
        """Initialize the LightDB object

        Params:
            location (``str``): The path to the JSON file where the database is stored
        """
        super().__init__()
        self.location = Path(location)
        self.update(**self._load())

        LightDB._current_db = self

    @classmethod
    def current(cls) -> "LightDB":
        """Returns the current instance of the LightDB class

        Returns:
            ``LightDB``: An initialized instance of the LightDB
        """
        if cls._current_db is None:
            raise ValueError("No current database has been set")
        return cls._current_db

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<LightDB: {self.location}>"

    def _load(self) -> Dict[str, Any]:
        """Load the database from a JSON file

        Returns:
            A dictionary containing the loaded key-value pairs
        """
        if not self.location.exists():
            return {}

        with self.location.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save(self) -> None:
        """Save the current state of the database to a JSON file"""
        with self.location.open("w", encoding="utf-8") as file:
            json.dump(self, file, ensure_ascii=False, indent=4)

    def set(self, key: str, value: Any) -> None:
        """Set a key-value pair in the database

        Params:
            key (``str``): The key to set

            value (``Any``): The value to associate with the key
        """
        self[key] = value

    @overload
    def get(self, key: str) -> Union[_VT, _T]:
        ...

    @overload
    def get(self, key: str, default: Union[_VT, _T]) -> Union[_VT, _T]:
        ...

    def get(self, key: str, default: Union[_VT, _T] = None) -> Union[_VT, _T]:
        """Get the value associated with a key from the database

        Params:
            key (``str``): The key to retrieve

            default (``Any``, optional): The default value to return if the key doesn`t exist

        Returns:
            ``_VT`` | ``_T``: The value associated with the key, or the default value if the key doesn`t exist
        """
        return super().get(key, default)

    def pop(self, key: str) -> Any:
        """Remove a key-value pair from the database

        Params:
            key (``str``): The key to remove

        Returns:
            ``Any``: The removed key-value pair
        """
        return super().pop(key)

    def reset(self) -> None:
        """Reset the database"""
        return self.clear()
