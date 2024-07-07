import pytest
import os

from typing import Any, Dict, List

from lightdb.core import LightDB
from lightdb.query import Query, Condition
from lightdb.fields import Field
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


def test_query_initialization(user_model: MODEL):
    query = Query(user_model)
    assert query.model == user_model
    assert query.conditions == []


def test_query_where(user_model: MODEL):
    query = Query(user_model)
    query.where(name="John", age=30)
    assert len(query.conditions) == 2
    assert query.conditions[0].field.name == "name"
    assert query.conditions[0].op == "=="
    assert query.conditions[0].value == "John"


def test_query_execute(user_model: MODEL):
    user_model.create(name="John", age=30)
    user_model.create(name="Jane", age=25)
    
    query = Query(user_model)
    query.where(age=30)
    results = query.execute()
    
    assert len(results) == 1
    assert results[0].name == "John"


def test_condition_evaluate():
    field = Field(name="age", annotation=int)
    condition = Condition(field, "==", 30)
    
    class TestModelMock:
        age = 30
    
    model = TestModelMock()
    assert condition.evaluate(model) == True
