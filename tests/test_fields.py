import pytest
from typing import List

from lightdb.fields import Field
from lightdb.exceptions import ValidationError


def test_field_initialization():
    field = Field(name="test", annotation=str, default="default")
    assert field.name == "test"
    assert field.annotation == str
    assert field.default == "default"
    assert field.value is None


def test_field_validation():
    field = Field(name="test", annotation=int)
    field.validate(10)
    
    with pytest.raises(ValidationError):
        field.validate("string")


def test_field_validation_list():
    field = Field(name="test", annotation=List[int])
    field.validate([1, 2, 3])
    
    with pytest.raises(ValidationError):
        field.validate([1, "string", 3])
