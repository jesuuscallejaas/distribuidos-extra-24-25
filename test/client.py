"""Test client for the Ice remote calculator."""

import os
import sys

import Ice

try:
    import RemoteCalculator  # noqa: F401

except ImportError:
    slice_path = os.path.join(
        os.path.dirname(__file__),
        "remotecalculator.ice",
    )

    Ice.loadSlice(slice_path)
    import RemoteCalculator  # noqa: F401


class ClientApp(Ice.Application):
    """Ice.Application for the client."""
    def run(self, args: list[str]) -> int:
        """Execute the main client actions."""
        proxy_str = "calculator -t -e 1.1:tcp -h 127.0.0.1 -p 10000 -t 60000"

        calculator_prx = RemoteCalculator.CalculatorPrx.checkedCast(
            self.communicator().stringToProxy(proxy_str)
        )

        print(calculator_prx.sum(1.0, 2.0))
        print(calculator_prx.sub(3.0, 2.0))
        print(calculator_prx.mult(2.0, 2.0))
        print(calculator_prx.div(4.0, 2.0))

        try:
            print(calculator_prx.div(4.0, 0.0))
        except RemoteCalculator.ZeroDivisionError:
            print("ZeroDivisionError: Division by zero is not allowed.")
        return 0


if __name__ == "__main__":
    app = ClientApp()
    sys.exit(app.main(sys.argv))
