from lightdb import LightDB

# Create a new database object, or load an existing one from file
db = LightDB("my_database.json")

# Set a key-value pair
db.set("name", "Alice")

# Get the value associated with a key
name = db.get("name")
print(name)  # Output: "Alice"

# Set a key-value pair in a nested dictionary
db.set_key("person", "age", 30)

# Get the value associated with a key in a nested dictionary
age = db.get_key("person", "age")
print(age)  # Output: 30

# Remove a key-value pair from the database
db.pop("name")

# Remove a key-value pair from a nested dictionary
db.pop_key("person", "age")

# Reset the database to an empty state
db.reset()
