"""A simple command-line calculator.

Deliberately avoids eval(): passing user input to eval() would let
anyone run arbitrary Python code on the machine.
"""

import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": None,  # handled by divide() so we can check for zero
}


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(expression: str) -> float:
    """Evaluate a simple expression like '3 + 4' safely."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Use the format: number operator number (e.g. 3 + 4)")

    left, op, right = parts
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")

    try:
        a, b = float(left), float(right)
    except ValueError:
        raise ValueError("Both sides must be numbers") from None

    functions = {"+": add, "-": subtract, "*": multiply, "/": divide}
    return functions[op](a, b)


def main() -> None:
    print("Simple calculator. Type an expression like '3 + 4', or 'quit' to exit.")
    while True:
        expression = input("> ").strip()
        if expression.lower() in {"quit", "exit"}:
            break
        try:
            print(calculate(expression))
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
