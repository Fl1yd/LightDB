"""A file contains custom exceptions"""

class Error(Exception):
    """Base class for all errors related to the database models"""


class ValidationError(Error, TypeError):
    """Error raised when validation of a field fails"""


class FieldNotFoundError(Error, ValueError):
    """Exception raised when a field specified in the model does not exist in the table"""


class NoArgsProvidedError(Error, TypeError):
    """Exception raised when no arguments are provided to a method that requires at least one argument"""
