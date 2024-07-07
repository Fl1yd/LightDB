"""
LightDB Package
~~~~~~~~~~~~~~~

This package provides a lightweight database management system implemented with JSON file storage. 
It includes the main LightDB class and related modules for field validation, model management, 
and query handling

Modules:
    core (LightDB): Main implementation of the LightDB database management system
    exceptions: Custom exceptions used in the LightDB package
    fields: Implementation of the Field class for data validation and storage
    models: Implementation of the Model class for database management
    query: Implementation of query handling for database operations

Attributes:
    __all__ (``list``): List of public objects of the module.
    __version__ (``str``): The version of the LightDB package.
"""

from .core import LightDB
from .fields import Field
from .models import Model
from .query import Query

__all__ = ["LightDB", "Field", "Model", "Query"]
__version__ = "2.0"
