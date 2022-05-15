"""The main file for the LightDB project.

:copyright: (c) 2021-2022 by Fl1yd.
:license: MIT, see LICENSE for more details.
"""

import os
import json

from typing import Union, Dict


class LightDB(dict):
    """Light DataBase
    ~~~~~~~~~~~~~~

    `SET` method usage:

        >>> from lightdb import LightDB
        >>> db = LightDB("/path/to/file.json")  # or a non-existent file, it will be created automatically
        >>> data = {
                "key1": "value1",
                "key2": [
                    "value2",
                    "value3",
                    ...
                ],
                ...
            }
        >>> db.set("key3", data)
        True
        >>> data = ["value4", "value5"]
        >>> db.set("key4", data)
        True

    ... or `GET`:

        >>> db.get("key3")
        {"key1": "value1", "key2": ["value2", "value3"]}
        >>> db.get("key4")
        ["value4", "value5"]
    """

    def __init__(self, location: str) -> None:
        """Initialize the LightDB object

        Params:
            location (``str``):
                The location of the database file

        Returns:
            None
        """
        super().__init__()
        self.location = location
        self.update(**self._load())

    def __repr__(self) -> str:
        return object.__repr__(self)

    def _load(self) -> Dict[str, Union[str, int, float, list, dict]]:
        """Load the data from a file

        Returns:
            The data from the file
        """
        return (
            json.load(open(self.location, "r"))
            if os.path.exists(self.location)
            else {}
        )

    def save(self) -> bool:
        """Save the current data to a file

        Returns:
            bool
        """
        json.dump(
            self, open(self.location, "w+"),
            ensure_ascii=False, indent=4
        )
        return True

    def set(
        self, key: str, value: Union[str, int, float, list, dict]
    ) -> bool:
        """LightDB `SET` method

        Params:
            key (``str``):
                The keyname of the item you want to set

            value (``str`` | ``int`` | ``float`` | ``list`` | ``dict``):
                The value of the item you want to set

        Returns:
            bool

        Usage:
            >>> data = {
                    "key1": "value1",
                    "key2": [
                        "value2",
                        "value3"
                    ]
                }
            >>> db.set("key3", data)
            True
        """
        self[str(key)] = value
        return self.save()

    def get(
        self, key: str, default: Union[str, int, float, list, dict] = None
    ) -> Dict[str, Union[str, int, float, list, dict]]:
        """LightDB `GET` method

        Params:
            key (``str``):
                The keyname of the item you want to get

            default (``str`` | ``int`` | ``float`` | ``list`` | ``dict``, optional):
                The default value if the key doesn't exist

        Returns:
            The value of the item with the specified key

        Usage:
            >>> result = db.get("key3")
            >>> result
            {"key1": "value1", "key2": ["value2", "value3"]}
            >>> result["key2"].remove("value3")
            >>> result
            {"key1": "value1", "key2": ["value2"]}
        """
        return dict(self).get(str(key), default)

    def pop(
        self, key: str
    ) -> Dict[str, Union[str, int, float, list, dict]]:
        """LightDB `POP` method

        Params:
            key (``str``):
                The keyname of the item you want to pop

        Returns:
            The value of the item with the specified key

        Usage:
            >>> db.pop("key1")
            {"key1": "value1", "key2": ["value2", "value3"]}
        """
        popped = self[str(key)]
        del self[str(key)]
        self.save()
        return popped

    def set_key(
        self, name: str, key: str, value: Union[str, int, float, list, dict]
    ) -> bool:
        """Set a key from a specific item

        Params:
            name (``str``):
                The name of the item

            key (``str``):
                The keyname of the item you want to set

            value (``str`` | ``int`` | ``float`` | ``list`` | ``dict``):
                The value of the item you want to set

        Returns:
            bool

        Usage:
            >>> data = {
                    "key1": "value1",
                    "key2": [
                        "value2",
                        "value3",
                        ...
                    ],
                    ...
                }
            >>> db.set("key3", data)
            True
            >>> db.set_key("key3", "key2", "value4")
            True
        """
        self.setdefault(str(name), {})[str(key)] = value
        return self.save()

    def get_key(
        self, name: str, key: str, default: Union[str, int, float, list, dict] = None
    ) -> Dict[str, Union[str, int, float, list, dict]]:
        """Get a key from a specific item

        Params:
            name (``str``):
                The name of the item

            key (``str``):
                The keyname of the item you want to get

            default (``str`` | ``int`` | ``float`` | ``list`` | ``dict``, optional):
                The default value if the key doesn't exist

        Returns:
            The value of the item with the specified key

        Usage:
            >>> result = db.get_key("key3", "key2")
            >>> result
            ["value2", "value3"]
        """
        return self.get(name, {}).get(key, default)

    def pop_key(
        self, name: str, key: str
    ) -> Dict[str, Union[str, int, float, list, dict]]:
        """Pop a key from a specific item

        Params:
            name (``str``):
                The name of the item

            key (``str``):
                The keyname of the item you want to pop

        Returns:
            The value of the item with the specified key

        Usage:
            >>> db.pop_key("key3", "key2")
            ["value2", "value3"]
        """
        popped = self[str(name)][str(key)]
        del self[str(name)][str(key)]
        self.save()
        return popped

    def reset(self) -> bool:
        """Reset database data"""
        self.clear()
        return self.save()
