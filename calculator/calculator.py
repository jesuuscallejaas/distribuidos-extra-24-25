"""Calculator implementation."""

import Ice
import RemoteCalculator


class Calculator(RemoteCalculator.Calculator):
    """Calculator implementation."""

    def add(self, a: float, b: float, current: Ice.Current = None) -> float:
        """Add two floats."""
        return a + b

    def subtract(self, a: float, b: float, current: Ice.Current = None) -> float:
        """Subtract two floats."""
        return a - b

    def multiply(self, a: float, b: float, current: Ice.Current = None) -> float:
        """Multiply two floats."""
        return a * b

    def divide(self, a: float, b: float, current: Ice.Current = None) -> float:
        """Divide two floats."""
        if b == 0.0:
            raise RemoteCalculator.ZeroDivisionError()
        return a / b
