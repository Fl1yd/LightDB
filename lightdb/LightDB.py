import os
import json


class LightDB(dict):
    """
    Light Database
    ~~~~~~~~~~~~~~

    `SET` method usage:

        >>> from lightdb import LightDB
        >>> db = LightDB("/path/to/file.json") # or a non-existent file, it will be created automatically
        >>> data = {
                "key1": "value1",
                "key2": ["value2", "value3", ...],
                ...
            }
        >>> db.set("key3", data)
        True
        >>> data = ["value4", "value5"]
        >>> db.set("key4", data)
        True

    ... or `GET`:

        >>> db.get("key3")
        {"key1": "value1", "key2": ["value2", "value3", ...]}
        >>> db.get("key4")
        ["value4", "value5"]
    """

    def __init__(self, location: str):
        super().__init__()
        self.location = location
        print(self.load())
        self.update(**self.load())

    def __repr__(self):
        return object.__repr__(self)

    def load(self):
        return (
            json.load(open(self.location, "r"))
            if os.path.exists(self.location)
            else {}
        )

    def save(self):
        json.dump(
            self, open(self.location, "w+"),
            ensure_ascii = False, indent = 4
        )
        return True

    def set(self, key, value):
        """
        LightDB `SET` method

        Usage:
            >>> data = {
                "key1": "value1",
                "key2": ["value2", "value3"]
            }
            >>> db.set("key3", data)
            True

        :params: The keyname and value you want to set
        :return: True
        """

        self[key] = value
        return self.save()

    def get(self, key, default = None):
        """
        LightDB `GET` method

        Usage:
            >>> db.get("key3")
            {"key1": "value1", "key2": ["value2", "value3"]}
            >>> r = db.get("key3")
            >>> r["key2"].remove("value3")
            >>> r
            {"key1": "value1", "key2": ["value2"]}

        :params:
            key - The keyname of the item you want to return the value from
            default - A value to return if the specified key does not exist. Default value `None`
        :return: The value of the item with the specified key
        """

        return dict(self).get(key, default)

    def pop(self, key):
        """
        LightDB `POP` method

        Usage:
            >>> db.pop("key1")
            {"key1": "value1", "key2": ["value2", "value3"]}

        :params: The keyname of the item you want to remove
        :return: The value of the removed item
        """

        popped = self.get(key)
        del self[key]
        self.save()
        return popped

    def reset(self):
        self.clear()
        return self.save()