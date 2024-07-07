Examples
========

This documentation provides examples of how to use the LightDB database management system

Using Database
--------------

LightDB can be used as a simple key-value store without defining any models. Here's how to use it:

**Initialize the Database**

To create a new database object or load an existing one from a file:

.. code-block:: python

    from lightdb import LightDB

    # Create a new database object, or load an existing one from file
    db = LightDB("db.json")


**Set a Key-Value Pair**

To set a key-value pair in the database:

.. code-block:: python

    db.set("name", "Alice")


**Get the Value Associated with a Key**

To get the value associated with a key:

.. code-block:: python

    name = db.get("name")
    print(name)  # Output: "Alice"


**Remove a Key-Value Pair**

To remove a key-value pair from the database:

.. code-block:: python

    db.pop("name")


**Reset the Database**

To reset the database to an empty state:

.. code-block:: python

    db.reset()


**Save Changes**

After making changes to the database, you need to save them to the file:

.. code-block:: python

    db.save()


Using Models
------------

LightDB also supports using models for a more structured approach. Here’s how to use models with LightDB:

**Initialize the Database**

First, initialize the database:

.. code-block:: python

    from lightdb import LightDB

    db = LightDB("db.json")


**Define a Model**

Define a model class by inheriting from the `Model` class. Specify the fields and their types, as well as the table name:

.. code-block:: python

    from lightdb.models import Model
    from typing import List, Dict, Any

    class User(Model, table="users"):
        name: str
        age: int
        items: List[str] = []
        extra: Dict[str, Any] = {}


**Create a New Instance of the Model**

To create a new instance of the model and save it to the database:

.. code-block:: python

    user = User.create(name="Alice", age=30)
    print(f"Created User: {user}")


**Retrieve an Instance of the Model**

To retrieve a single instance of the model that matches the provided filter criteria:

.. code-block:: python

    retrieved_user = User.get(User.name == "Alice")
    # or retrieved_user = User.get(name="Alice")
    if retrieved_user:
        print(f"Retrieved User: {retrieved_user.name}, Age: {retrieved_user.age}")


**Update an Instance of the Model**

To update an instance of the model and save the changes:

.. code-block:: python

    retrieved_user.name = "Kristy"
    retrieved_user.save()
    print(f"Updated User: {retrieved_user}")


**Filter Instances of the Model**

To filter instances of the model based on certain criteria:

.. code-block:: python

    users_over_20 = User.filter(User.age >= 20)
    print("Users over 20:")
    for user in users_over_20:
        print(f"Name: {user.name}, Age: {user.age}")


**Delete an Instance of the Model**

To delete an instance of the model from the database:

.. code-block:: python

    retrieved_user.delete()
    print(f"Deleted User: {retrieved_user.name}")


**Verify Deletion**

To verify that the instance has been deleted:

.. code-block:: python

    deleted_user = User.get(name="Kristy")
    print(f"User exists after deletion: {deleted_user is not None}")


These examples cover the basic usage of LightDB. By following these steps, you can effectively manage your data using LightDB
