<p align="center">
    <img src="https://x0.at/Dzzm.png">
    <br>
    <b>LightDB</b>: Lightweight JSON Database for Python
</p>


<h1>What is this?</h1>
LightDB is a simple and lightweight JSON database for Python that allows users to <b>efficiently</b> write data to a file. It is designed to be <b>easy to use</b>, making it a great choice for developers who need a fast and reliable way to store and retrieve data.


<h1>Installing</h1>

You can install LightDB using pip:

<pre lang="bash">
pip install lightdb
</pre>


<h1>Usage</h1>

To use LightDB, first import the <code>LightDB</code> class from the <code>lightdb</code> package:

<pre lang="python">
from lightdb import LightDB
</pre>

Then, create a <code>LightDB</code> object by passing in the path to a JSON file where the database will be stored:

<pre lang="python">
db = LightDB("my_database.json")
</pre>

You can then set key-value pairs in the database using the <code>set()</code> method:

<pre lang="python">
db.set("name", "Alice")
db.set("age", 30)
</pre>

You can get the value associated with a key using the <code>get()</code> method:

<pre lang="python">
name = db.get("name")
age = db.get("age")
</pre>

You can also remove a key-value pair using the <code>pop()</code> method:

<pre lang="python">
db.pop("age")
</pre>

To reset the database to an empty state, use the <code>reset()</code> method:

<pre lang="python">
db.reset()
</pre>


<h1>License</h1>
LightDB is licensed under the MIT License.
