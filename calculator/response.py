"""Response module for the calculator application."""

from pydantic import BaseModel


class CalculatorResponse(BaseModel):
    """Response model for the calculator API."""

    id: str
    status: bool
    result: float | None = None
    error: str | None = None
