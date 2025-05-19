"""Module for representing a request to the calculator API."""

from enum import Enum

from pydantic import BaseModel, ConfigDict


class Operation(str, Enum):
    """Enum for calculator operations."""

    sum = "sum"
    sub = "sub"
    mult = "mult"
    div = "div"


class Operands(BaseModel):
    """Operands for the calculator operations."""

    model_config = ConfigDict(extra="forbid")

    op1: float
    op2: float


class CalculatorRequest(BaseModel):
    """Request model for the calculator API."""

    model_config = ConfigDict(extra="forbid")

    id: str
    operation: Operation
    args: Operands
