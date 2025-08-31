# Simple Calculator App

A simple wordplay package built in Python.  
Supports the following operations: acronyms, anagrams, text cleaning, and text shuffling.  
Built as part of the **uv-assignment** project.

---

## Screenshot

![Wordplay Screenshot](../assets/screenshot.png)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/uv-assignment.git
   cd uv-assignment/simple-app
    ```

2. Install application:
   ```bash
   uv sync --frozen
   ```

---

## CLI Usage

Run the app from the command line:

```bash
$ uv run wordplay anagram listen
uv-assignment - PIAIC258257

Results:
 • silent
 • eslint

$ uv run wordplay acronym "As soon as possible"
uv-assignment - PIAIC258257

Result: ASAP (As soon as possible)
```

### API Usage
You can also use the functions directly in your Python code:

```python
from wordplay import make_anagrams, make_acronym
from wordplay.utils import clean_text, shuffle_word

# Example usage

print(make_anagrams("listen", limit=5))
# Output: ['silent', 'enlist', 'tinsel', 'inlets', 'listen']

print(make_acronym("As soon as possible"))
# Output: 'ASAP'

print(clean_text("Hello, World!"))
# Output: 'Hello World'

print(shuffle_word("example"))
# Output: 'pxmaele'
```

---

## License

MIT License.