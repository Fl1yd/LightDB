<p align="center">
    <img src="docs\source\_static\logo_light.svg">
    <br>
    <b>LightDB</b>: Lightweight JSON Database for Python
</p>


<h1>What is this?</h1>

LightDB is a simple and lightweight JSON database for Python that allows users to <b>efficiently</b> write data to a file. It is designed to be <b>easy to use</b>, making it a great choice for developers who need a fast and reliable way to store and retrieve data.


<h1>Installing</h1>

You can install LightDB using <code>pip</code>:

<pre lang="bash">
pip install LightDB
</pre>


<h1>Usage</h1>

To use LightDB, first import the <code>LightDB</code> class from the <code>lightdb</code> package:

<pre lang="python">
from lightdb import LightDB
</pre>

Then, create a <code>LightDB</code> object by passing in the path to a JSON file where the database will be stored:

<pre lang="python">
db = LightDB("db.json")
</pre>

You can then set key-value pairs in the database using the <code>set()</code> method:

<pre lang="python">
db.set("name", "Alice")
db.set("age", 30)
</pre>

To save the changes, use the <code>save()</code> method:

<pre lang="python">
db.save()
</pre>


<h1>Using Models</h1>

LightDB supports defining models for more structured and convenient data management. Here’s how to use models with LightDB:

First, import the necessary classes:

<pre lang="python">
from typing import List, Dict, Any

from lightdb import LightDB
from lightdb.models import Model
</pre>

Define your model by extending the <code>Model</code> class:

<pre lang="python">
class User(Model, table="users"):
    name: str
    age: int
    items: List[str] = []
    extra: Dict[str, Any] = {}
</pre>

Create a new instance of the model and save it to the database:

<pre lang="python">
user = User.create(name="Alice", age=30)
</pre>

Retrieve a user from the database:

<pre lang="python">
user = User.get(User.name == "Alice")
# or user = User.get(name="Alice")
print(user.name, user.age)
</pre>

Update a user’s information and save it:

<pre lang="python">
user.name = "Kristy"
user.save()
</pre>

Filter users based on certain criteria:

<pre lang="python">
users = User.filter(User.age >= 20)
for user in users:
    print(user.name)
</pre>

Delete a user:

<pre lang="python">
user.delete()
</pre>

<h1>License</h1>
LightDB is licensed under the MIT License.
