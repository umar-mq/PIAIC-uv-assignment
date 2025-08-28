# Simple Calculator App

A minimal command-line calculator built in Python.  
Supports basic operations: addition, subtraction, multiplication, and division.  
Built as part of the **uv-assignment** project.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/uv-assignment.git
   cd uv-assignment/simple-app
    ```

2. Setup dependencies:
   ```bash
   uv sync --frozen
   ```

---

## Usage

Run the app from the command line:

```bash
uv run main.py add 4 7
```

### Examples

```bash
uv run main.py add 5 3
# Output: 5 + 3 = 8

uv run main.py sub 10 4
# Output: 10 - 4 = 6

uv run main.py mul 6 7
# Output: 6 * 7 = 42

uv run main.py div 15 3
# Output: 15 / 3 = 5.0
```

---

## Screenshot

![Calculator Screenshot](../assets/screenshot.png)

---

## License

MIT License.