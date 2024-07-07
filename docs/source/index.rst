LightDB
=======

What is this?
-------------

**LightDB** is a simple and lightweight JSON database for Python that allows users to **efficiently** write data to a file. It is designed to be **easy to use**, making it a great choice for developers who need a fast and reliable way to store and retrieve data


Features
--------

- **Lightweight and Simple**: LightDB is a lightweight database implemented as a Python dictionary with an intuitive API for easy key-value management
- **JSON Storage and Persistence**: Data is stored and retained in a JSON file, allowing easy external editing and persistence between runs
- **Reset Capability**: Provides a reset method to clear the database and start fresh
- **Type Agnostic**: Can store any Python object as a value
- **Portable**: Easily transferable between systems, ideal for simple data storage
- **Model Support**: Supports models for structured data management, ensuring organized and maintainable code


Simple usage
------------

.. literalinclude:: ../../examples/simple_usage.py


Models usage
------------

.. literalinclude:: ../../examples/models_usage.py
