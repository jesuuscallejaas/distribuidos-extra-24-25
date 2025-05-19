"""Test module for calculator.request"""

from calculator.request import CalculatorRequest
import pytest
import pytest


@pytest.mark.parametrize(
    "input_data, expected_error",
    [
        # Wrong operation
        (
            {
                "id": "1",
                "operation": "wrong_operation",  # Invalid operation
                "args": {"op1": 1.0, "op2": 2.0},
            },
            ValueError,
        ),
        # Missing args
        (
            {
                "id": "1",
                "operation": "sum",
                # Missing args
            },
            ValueError,
        ),
        # Missing op2 in args
        (
            {
                "id": "1",
                "operation": "sum",
                "args": {"op1": 1.0},  # Missing op2
            },
            ValueError,
        ),
        # Missing id
        (
            {
                # Missing id
                "operation": "sum",
                "args": {"op1": 1.0, "op2": 2.0},
            },
            ValueError,
        ),
        # Invalid operand type: op1
        (
            {
                "id": "1",
                "operation": "sum",
                "args": {"op1": "invalid", "op2": 2.0},  # op1 should be float
            },
            ValueError,
        ),
        # Invalid operand type: op2
        (
            {
                "id": "1",
                "operation": "sum",
                "args": {"op1": 1.0, "op2": None},  # op2 should be float
            },
            ValueError,
        ),
        # Invalid operation type
        (
            {
                "id": "1",
                "operation": 3,  # operation should be of type Operation
                "args": {"op1": 1.0, "op2": 2.0},
            },
            ValueError,
        ),
        # Extra field
        (
            {
                "id": "1",
                "operation": "sum",
                "args": {"op1": 1.0, "op2": 2.0},
                "extra_field": "extra_value",  # Extra field not defined in the model
            },
            ValueError,
        ),
        # Invalid id type
        (
            {
                "id": 1,  # id should be a string
                "operation": "sum",
                "args": {"op1": 1.0, "op2": 2.0},
            },
            ValueError,
        ),
    ],
)
def test_calculator_request_invalid_cases(input_data, expected_error):
    with pytest.raises(expected_error):
        CalculatorRequest.model_validate(input_data)
