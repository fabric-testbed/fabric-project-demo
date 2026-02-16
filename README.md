# Fabric Project Demo

A sample Python library from the [FABRIC Testbed](https://fabric-testbed.net/) project.

## Installation

```bash
pip install git+https://github.com/fabric-testbed/fabric-project-demo.git
```

Or clone and install locally:

```bash
git clone https://github.com/fabric-testbed/fabric-project-demo.git
cd fabric-project-demo
pip install .
```

## Usage

```python
from fabric_demo import greet, add, slugify, truncate

# Core functions
print(greet("World"))       # "Hello, World! Welcome to FABRIC Demo."
print(add(2, 3))            # 5

# Utility functions
print(slugify("Hello World"))          # "hello-world"
print(truncate("A long string", 10))   # "A long..."
```

## Running Tests

```bash
python -m pytest tests/
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
