import argparse
from rich.console import Console

console = Console()
console.print('[u]uv-assignment[/u] - [i]PIAIC258257[/i]')

def calculate(a: float, b: float, operation: str) -> float:
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")


def main():
    parser = argparse.ArgumentParser(
        description="A simple calculator application"
    )
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform",
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")

    args = parser.parse_args()

    try:
        result = str(calculate(args.a, args.b, args.operation))

        console.print(f'[bold green]Result:[/bold green] [i][u]{result}[/u][/i]')

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")


if __name__ == "__main__":
    main()
