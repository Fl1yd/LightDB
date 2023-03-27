"""The main file for the LightDB project.

:copyright: (c) 2021-2023 by Fl1yd.
:license: MIT, see LICENSE for more details.
"""

import json

from pathlib import Path
from typing import Dict, Any


class LightDB(dict):
    """Light Database
    ~~~~~~~~~~~~~~

    A lightweight database implemented as a dictionary with JSON file storage.

    This class extends the built-in Python `dict` class to provide a simple and easy-to-use key-value store that
    persists its data in a JSON file. The class provides methods to set, get, and remove individual key-value pairs
    as well as nested dictionaries of key-value pairs.
    """

    def __init__(self, location: str) -> None:
        """Initialize the LightDB object

        Params:
            location (``str``):
                The path to the JSON file where the database is stored

        Returns:
            None
        """
        super().__init__()
        self.location = Path(location)
        self.update(**self._load())

    def __repr__(self) -> str:
        return object.__repr__(self)

    def _load(self) -> Dict[str, Any]:
        """Load the database from a JSON file

        Returns:
            A dictionary containing the loaded key-value pairs
        """
        if self.location.exists():
            with self.location.open("r", encoding="utf-8") as file:
                return json.load(file)
        return {}

    def save(self) -> None:
        """Save the current state of the database to a JSON file

        Returns:
            None
        """
        with self.location.open("w+", encoding="utf-8") as f:
            json.dump(self, f, ensure_ascii=False, indent=4)

    def set(self, key: str, value: Any) -> None:
        """Set a key-value pair in the database

        Params:
            key (``str``):
                The key to set

            value (``Any``):
                The value to associate with the key

        Returns:
            None
        """
        self[str(key)] = value
        return self.save()

    def get(self, key: str, default: Any = None) -> Dict[str, Any]:
        """Get the value associated with a key from the database

        Params:
            key (``str``):
                The key to retrieve

            default (``Any``, optional):
                The default value to return if the key doesn`t exist

        Returns:
            The value associated with the key, or the default value if the key doesn`t exist
        """
        return dict(self).get(str(key), default)

    def pop(self, key: str) -> Dict[str, Any]:
        """Remove a key-value pair from the database

        Params:
            key (``str``):
                The key to remove

        Returns:
            The removed key-value pair
        """
        popped = self[str(key)]
        del self[str(key)]
        self.save()
        return popped

    def set_key(self, name: str, key: str, value: Any) -> None:
        """Set a key-value pair in a nested dictionary in the database

        Params:
            name (``str``):
                The name of the nested dictionary

            key (``str``):
                The key to set

            value (``Any``):
                The value to associate with the key

        Returns:
            None
        """
        self.setdefault(str(name), {})[str(key)] = value
        return self.save()

    def get_key(self, name: str, key: str, default: Any = None) -> Dict[str, Any]:
        """Get the value associated with a key in a nested dictionary in the database

        Params:
            name (``str``):
                The name of the nested dictionary

            key (``str``):
                The key to retrieve

            default (``Any``, optional):
                The default value to return if the key or the nested dictionary doesn`t exist

        Returns:
            The value associated with the key, or the default value if the key or the nested dictionary does not exist
        """
        return self.get(name, {}).get(str(key), default)

    def pop_key(self, name: str, key: str) -> Dict[str, Any]:
        """Remove a key-value pair from a nested dictionary in the database

        Params:
            name (``str``):
                The name of the nested dictionary

            key (``str``):
                The key to remove

        Returns:
            The removed key-value pair
        """
        popped = self[name][key]
        del self[name][key]
        self.save()
        return popped

    def reset(self) -> None:
        """Reset the database to an empty state

        Returns:
            None
        """
        self.clear()
        return self.save()
