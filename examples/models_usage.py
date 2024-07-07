from lightdb import LightDB
from lightdb.models import Model

from typing import List, Dict, Any

# Initialize the database
db = LightDB("db.json")


# Define a User model
class User(Model, table="users"):
    name: str
    age: int
    items: List[str] = []
    extra: Dict[str, Any] = {}


# Create a new user
user = User.create(name="Alice", age=30)
print(f"Created User: {user}")

# Retrieve the user
retrieved_user = User.get(name="Alice")
if retrieved_user:
    print(f"Retrieved User: {retrieved_user.name}, Age: {retrieved_user.age}")

# Update the user's name
retrieved_user.name = "Kristy"
retrieved_user.save()
print(f"Updated User: {retrieved_user}")

# Filter users by age
users_over_20 = User.filter(User.age >= 20)
print("Users over 20:")
for user in users_over_20:
    print(f"Name: {user.name}, Age: {user.age}")

# Delete the user
retrieved_user.delete()
print(f"Deleted User: {retrieved_user.name}")

# Verify deletion
deleted_user = User.get(name="Kristy")
print(f"User exists after deletion: {deleted_user is not None}")
