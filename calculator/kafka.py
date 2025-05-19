"""Kafka middleware for the calculator microservice."""

import json
import sys

import Ice
import RemoteCalculator
from confluent_kafka import Consumer, Producer

from calculator.request import CalculatorRequest
from calculator.response import CalculatorResponse


class ClientApp(Ice.Application):
    """Ice.Application for the client."""

    def run(self, args: list[str]) -> int:
        """Execute the main client actions."""
        if len(args) < 2:
            print("Must provide the calculator proxy string as an argument.")

        proxy_str = args[1]

        calculator_prx = RemoteCalculator.CalculatorPrx.checkedCast(
            self.communicator().stringToProxy(proxy_str)
        )

        requests_topic = "requests"
        responses_topic = "responses"
        broker = "localhost:9092"
        consumer_group = "calculator"

        consumer = Consumer(
            **{
                "bootstrap.servers": broker,
                "group.id": consumer_group,
            }
        )

        publisher = Producer(
            **{
                "bootstrap.servers": broker,
            }
        )

        consumer.subscribe([requests_topic])

        while True:
            for msg in consumer.consume():
                self.handle_msg(msg, calculator_prx, publisher, responses_topic)

    def handle_msg(
        self,
        msg: bytes,
        calculator_prx: RemoteCalculator.CalculatorPrx,
        publisher: Producer,
        responses_topic: str,
    ):
        """Handle a message from the Kafka topic."""
        try:
            json_request = json.loads(msg.value())

            request = CalculatorRequest(**json_request)

            print(f"Recieved a new {request = }")

            # Dynamically call the method on calculator_prx based on request.operation
            operation_func = getattr(calculator_prx, request.operation)

            result = operation_func(request.args.op1, request.args.op2)

            publisher.produce(
                responses_topic,
                CalculatorResponse(
                    id=request.id,
                    status=True,
                    result=result,
                )
                .model_dump_json()
                .encode(),
            )
        except json.JSONDecodeError:
            print(f"invalid JSON: {msg.value()}")
        except ValueError as e:
            print(f"invalid request: {e}")

            if "id" in json_request:
                print("id in json_request")
                publisher.produce(
                    responses_topic,
                    CalculatorResponse(
                        id=json_request["id"],
                        status=False,
                        error=str(e),
                    )
                    .model_dump_json()
                    .encode(),
                )
        except RemoteCalculator.ZeroDivisionError:
            publisher.produce(
                responses_topic,
                CalculatorResponse(
                    id=request.id,
                    status=False,
                    error="ZeroDivisionError",
                )
                .model_dump_json()
                .encode(),
            )


def main():
    app = ClientApp()
    sys.exit(app.main(sys.argv))


if __name__ == "__main__":
    main()
