import os
import pytest
import tempfile

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


def test_lightdb_pop_with_default(db: LightDB):
    db.set("key", "value")
    assert db.pop("key") == "value"
    assert db.pop("missing", None) is None
    assert db.pop("missing", "fallback") == "fallback"


def test_lightdb_pop_raises_without_default(db: LightDB):
    with pytest.raises(KeyError):
        db.pop("nonexistent")


def test_lightdb_save_creates_parent_dirs():
    with tempfile.TemporaryDirectory() as tmpdir:
        nested_path = os.path.join(tmpdir, "a", "b", "c", "db.json")
        db = LightDB(nested_path)
        db.set("key", "value")
        db.save()
        assert os.path.exists(nested_path)

        db2 = LightDB(nested_path)
        assert db2.get("key") == "value"


def test_lightdb_context_manager():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "ctx_db.json")
        with LightDB(path) as db:
            db.set("key", "value")

        db2 = LightDB(path)
        assert db2.get("key") == "value"
