# friendly_names

[![PyPI - Version](https://img.shields.io/pypi/v/friendly-names.svg)](https://pypi.org/project/friendly-names)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/friendly-names.svg)](https://pypi.org/project/friendly-names)

A super simple random friendly name generator that creates readable, hyphenated names like "red-loop-bounty".

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Installation

```console
pip install friendly_names
```

## Usage

```python
import friendly_names

# Generate a friendly name like "red-loop-bounty"
name = friendly_names.generate()

# Customize number of words
name = friendly_names.generate(words=4)  # e.g., "happy-blue-running-fox"

# Use different separator
name = friendly_names.generate(separator="_")  # e.g., "green_swift_river"
```

## Development

To set up the development environment:

```console
pip install hatch
```

Common development tasks:

```console
# Run tests
hatch run test:test

# Run tests with coverage
hatch run test:coverage

# Run type checking
hatch run types:check
```

The project uses:
- [Hatch](https://hatch.pypa.io/) for development environment and build management
- [pytest](https://docs.pytest.org/) for testing
- [mypy](https://mypy.readthedocs.io/) for type checking

## License

`friendly_names` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
