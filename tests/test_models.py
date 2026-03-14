import os
import pytest

from typing import Any, List, Dict
from lightdb.core import LightDB
from lightdb.models import MODEL, Model


@pytest.fixture
def user_model():
    test_db_location = "test_db.json"
    db = LightDB(test_db_location)

    class User(Model, table="users"):
        name: str
        age: int
        items: List[str] = []
        extra: Dict[str, Any] = {}

    yield User
    if os.path.exists(test_db_location):
        os.remove(test_db_location)


def test_model_initialization(user_model: MODEL):
    model = user_model(name="John", age=30)
    assert model.name == "John"
    assert model.age == 30


def test_model_save(user_model: MODEL):
    db = user_model.__db__
    model = user_model(name="John", age=30)
    model.save()
    
    assert len(db.get("users")) == 1
    assert db.get("users")[0]["name"] == "John"


def test_model_get(user_model: MODEL):
    user_model.create(name="John", age=30)
    fetched_model = user_model.get(name="John")
    
    assert fetched_model is not None
    assert fetched_model.name == "John"
    assert fetched_model.age == 30


def test_model_delete(user_model: MODEL):
    model = user_model.create(name="John", age=30)
    model.delete()
    
    assert user_model.get(name="John") is None


def test_model_filter(user_model: MODEL):
    user_model.create(name="John", age=30)
    user_model.create(name="Jane", age=25)
    
    results = user_model.filter(age=30)
    assert len(results) == 1
    assert results[0].name == "John"


def test_model_all(user_model: MODEL):
    user_model.create(name="John", age=30)
    user_model.create(name="Jane", age=25)
    
    results = user_model.all()
    assert len(results) == 2


def test_model_delete_correct_entry(user_model: MODEL):
    john = user_model.create(name="John", age=30)
    jane = user_model.create(name="Jane", age=25)
    john.delete()

    remaining = user_model.all()
    assert len(remaining) == 1
    assert remaining[0].name == "Jane"


def test_model_optional_field():
    import os
    from typing import Optional

    test_db_location = "test_optional_db.json"
    from lightdb.core import LightDB

    db = LightDB(test_db_location)

    class Profile(Model, table="profiles"):
        username: str
        bio: Optional[str] = None

    try:
        p = Profile.create(username="Alice")
        assert p.bio is None

        p2 = Profile.create(username="Bob", bio="Hello!")
        assert p2.bio == "Hello!"
    finally:
        if os.path.exists(test_db_location):
            os.remove(test_db_location)
