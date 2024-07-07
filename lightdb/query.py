"""A file containing the implementation of the Query and Condition classes for filtering and querying data"""

import operator
from typing import TYPE_CHECKING, Any, Dict, List

if TYPE_CHECKING:
    from .models import MODEL, Field


class Query:
    """A class representing a database query"""

    def __init__(self, model: "MODEL") -> None:
        """Initialize a new query object

        Params:
            model (``Model``): The model class to query against
        """
        self.model = model
        self.conditions: List[Condition] = []

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Query(model={self.model.__name__}, conditions={[repr(condition) for condition in self.conditions]})"

    def where(self, *conditions: List["Condition"], **filters: Dict[str, Any]) -> "Query":
        """Add a condition to the query

        Params:
            condition (``Condition``): The conditions to add to the query

            filters (``Dict[str, Any]``): Keyword arguments representing filter criteria for the model instances

        Returns:
            ``Query``: The updated query object
        """
        self.conditions.extend(conditions)

        for field_name, value in filters.items():
            field = getattr(self.model, field_name)
            self.conditions.append(Condition(field, "==", value))

        return self

    def execute(self) -> List["MODEL"]:
        """Execute the query and return the filtered results

        Returns:
            ```List[Model]```: The filtered results of the query
        """
        models = self.model.all()
        filtered_results = [model for model in models if self.evaluate_conditions(model)]
        return filtered_results

    def evaluate_conditions(self, model: "MODEL") -> bool:
        """Evaluate the conditions for a given model

        Params:
            model (``Model``): The model to evaluate the conditions against

        Returns:
            ``bool``: True if all conditions are met, False otherwise
        """
        return all(condition.evaluate(model) for condition in self.conditions)


class Condition:
    """A class representing a condition in a database query"""

    def __init__(self, field: "Field", op: str, value: Any) -> None:
        """Initialize a new condition object

        Params:
            field (``Field``): The field to apply the condition to

            op (``str``): The operator for the condition (e.g., "==", "!=", "<", "<=", ">", ">=")

            value (``Any``): The value to compare against
        """
        self.field = field
        self.op = op
        self.value = value

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"Condition(field={self.field}, operator='{self.op}', value={self.value})"

    def evaluate(self, model: "MODEL") -> bool:
        """Evaluate the condition for a given model

        Params:
            model (``Model``): The model to evaluate the condition against

        Returns:
            ``bool``: True if the condition is met, False otherwise
        """
        operators_map = {
            "==": operator.eq,
            "!=": operator.ne,
            "<": operator.lt,
            "<=": operator.le,
            ">": operator.gt,
            ">=": operator.ge
        }
        value = getattr(model, self.field.name)
        return operators_map[self.op](value, self.value)
