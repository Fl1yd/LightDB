from lightdb import LightDB

# Create a new database object, or load an existing one from file
db = LightDB("my_database.json")

# Set a key-value pair
db.set("name", "Alice")

# Get the value associated with a key
name = db.get("name")
print(name)  # Output: "Alice"

# Remove a key-value pair from the database
db.pop("name")

# Reset the database to an empty state
db.reset()

# After this, you need to save changes
db.save()
