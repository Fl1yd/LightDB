import os
import pytest

from pathlib import Path

from lightdb.core import LightDB


@pytest.fixture
def db():
    test_db_location = "test_db.json"
    yield LightDB(test_db_location)
    if os.path.exists(test_db_location):
        os.remove(test_db_location)


def test_lightdb_initialization(db: LightDB):
    assert db.location == Path("test_db.json")
    assert db == {}
    assert LightDB._current_db == db


def test_lightdb_set_get(db: LightDB):
    db.set("key", "value")
    assert db.get("key") == "value"


def test_lightdb_save_load(db: LightDB):
    db.set("key", "value")
    db.save()
    
    db2 = LightDB("test_db.json")
    assert db2.get("key") == "value"


def test_lightdb_reset(db: LightDB):
    db.set("key", "value")
    db.reset()
    assert db.get("key") is None
