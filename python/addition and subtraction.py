SUPPORTED_OPERATORS = {"+", "-", "*", "/", "%", "**"}

a , b =  map(int , input().split())
operator = input()

def calculate(a:float, b: float, operator: str) -> float:
    """Evaluate a binary arithmetic expression."""
    if operator not in SUPPORTED_OPERATORS:
        raise ValueError(
            f"Unsupported operator '{operator}'. "
            f"Use one of: {', '.join(sorted(SUPPORTED_OPERATORS))}"
        )

    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    if operator == "%":
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")
        return a % b
    if operator == "**":
        return a ** b

    raise ValueError(f"Unsupported operator '{operator}'")

print(calculate(a,b,operator))