# calculator repository template

Solution for the extra SSDD laboratory 2024-2025

## Installation

To locally install the package, just run

```
pip install .
```

Or, if you want to modify it during your development,

```
pip install -e .
```

## Execution

To run the Ice server, just install the package and run

```
ssdd-calculator --Ice.Config=config/calculator.config
```

This will output the stringfied proxy of the calculator. Keep it to run kafka.

You also have to start the docker kafka container. You can do it by running

```
docker compose up -d
```

And then, the kafka middleware:

```
ssdd-kafka <your-proxy-string>
```

Now you can use kcat to execute the calculator

```
kcat -b localhost:9092 -P -t requests
```

And input the following:

```json
{ "id": "first",  "operation": "sum",  "args": { "op1": 1.0, "op2": 2.0 } }
{ "id": "second", "operation": "sub",  "args": { "op1": 3.0, "op2": 2.0 } }
{ "id": "third",  "operation": "mult", "args": { "op1": 4.0, "op2": 5.0 } }
{ "id": "fourth", "operation": "div",  "args": { "op1": 6.0, "op2": 3.0 } }
{ "id": "fifth",  "operation": "div",  "args": { "op1": 6.0, "op2": 0.0 } }
{ "id": "error" }
```

The results can be seen in the `responses` topic. You can consume it with

```
kcat -b localhost:9092 -C -t results
```

Which will output something like

```json
{"id":"first","status":true,"result":3.0}
{"id":"second","status":true,"result":1.0}
{"id":"third","status":true,"result":20.0}
{"id":"fourth","status":true,"result":2.0}
{"id":"fifth","status":false,"error":"ZeroDivisionError"}
{"id":"error","status":false,"error":"2 validation errors for CalculatorRequest..."}
```

## Testing

To run the tests, you can use pytest. Just run

```
pytest
```

Also, there is a test client for the Ice calculator. You can run it by executing

```
python3 test/client.py
```
