import os
import pytest

from lightdb import LightDB


@pytest.fixture
def db():
    """Fixture that creates an instance of LightDB for testing"""
    test_db_location = "test_db.json"
    yield LightDB(test_db_location)
    if os.path.exists(test_db_location):
        os.remove(test_db_location)


def test_set_get(db: LightDB):
    db.set("key1", "value1")
    assert db.get("key1") == "value1"


def test_set_nested_get_nested(db: LightDB):
    db.set_key("nested_dict", "key1", "value1")
    assert db.get_key("nested_dict", "key1") == "value1"


def test_remove_key(db: LightDB):
    db.set("key1", "value1")
    db.pop("key1")
    assert db.get("key1") is None


def test_remove_nested_key(db: LightDB):
    db.set_key("nested_dict", "key1", "value1")
    db.pop_key("nested_dict", "key1")
    assert db.get_key("nested_dict", "key1") is None


def test_default_value(db: LightDB):
    assert db.get("nonexistent_key", "default_value") == "default_value"


def test_reset(db: LightDB):
    db.set("key1", "value1")
    db.reset()
    assert db.get("key1") is None
