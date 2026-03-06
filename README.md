
# Expression and Statement Interpreter

## Description
This project implements an interpreter for a custom expression and statement language using Python and the Lark parsing library. The parser is designed in distinct components to handle standard arithmetic, logical, and relational operations, as well as a full suite of control flow statements including variable assignments, conditionals, and loops. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Installation 🛠️

To run this project, you will need Python 3 and the `lark` parsing library installed.

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>

```

2. **Install dependencies:**
It is recommended to use a virtual environment. Install `lark` via pip:
```sh
pip install lark

```



## Usage 🚀

The repository provides several interactive interpreter scripts. You can run them directly from your command line.

* **Standard Expression Evaluator:**
Evaluates basic arithmetic, logical, and strict relational operations.
```sh
python expr.py

```


* **Chained Expression Evaluator:**
Evaluates expressions and allows for continuous chained relational operations (e.g., `1 < 2 < 3`).
```sh
python expr2.py

```


* **Statement Interpreter:**
Executes full programming statements including variable assignments, while loops, and block statements.
```sh
python stmt.py

```



## Features ✨

* **Arithmetic Evaluation:** Accurately processes addition, subtraction, multiplication, and division.
* **Relational and Logical Operations:** Supports equality checking (`==`, `!=`), inequalities (`<`, `>`, `<=`, `>=`), and logic parsing (`and`, `or`, `not`).
* **Expression Chaining:** Includes a secondary evaluator (`expr2.py`) specifically configured to handle chained relational operations.
* **Control Flow Execution:** The `stmt.py` interpreter natively parses and executes conditional `if`/`else` branches, `while` loops, and `print` statements.
* **Variable State Management:** Supports assigning values to variable identifiers and storing them in an environment dictionary during runtime.

## Technologies Used 💻

* **Language:** Python 3
* **Library:** Lark (Parsing Toolkit)

## Contributing 🤝

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.





