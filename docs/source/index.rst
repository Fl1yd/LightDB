LightDB
=======

What is this?
-------------

LightDB is a simple and lightweight JSON database for Python that allows users to efficiently write data to a file. It is designed to be easy to use, making it a great choice for developers who need a fast and reliable way to store and retrieve data.


Features
--------

- Lightweight: LightDB is a lightweight database that is implemented as a Python dictionary, making it simple and easy to use.
- Simple API: LightDB provides a simple and intuitive API that allows users to easily set, get, and remove key-value pairs in the database.
- JSON file storage: LightDB stores its data in a JSON file, making it easy to read and edit the database outside of the Python environment.
- Nested dictionaries: LightDB supports nested dictionaries, allowing users to organize their data in a hierarchical structure.
- Persistance: LightDB's data is persisted in the JSON file, ensuring that it is retained between program runs.
- Reset: LightDB provides a reset method that allows users to clear the database and start fresh.
- Type agnostic: LightDB is type-agnostic, meaning it can store any Python object as a value in the database.
- Portable: LightDB can be easily transferred between different systems, making it a great choice for simple data storage needs.


Simple usage
------------

.. literalinclude:: ../../examples/simple_usage.py


Contents
--------

.. toctree::

    api/index
    installation
    todo
    license
