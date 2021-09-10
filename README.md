LightDB
=======


What is this?
-------------

LightDB is a lightweight JSON Database for Python
that allows you to **quickly** and **easily** write data to a file


Installing
----------
```shell
pip3 install lightdb
```

How to use
----------
```Python
from lightdb import LightDB
db = LightDB("/path/to/file.json") # or a non-existent file, it will be created automatically

# `SET` method:
data = {
    "key1": "value1",
    "key2": ["value2", "value3", ...],
    ...
}
db.set("key3", data)
data = ["value4", "value5"]
db.set("key4", data)


# or `GET`:
print(db.get("key3"))
# {"key1": "value1", "key2": ["value2", "value3", ...]}
print(db.get("key4"))
# ["value4", "value5"]
```