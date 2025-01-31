# friendly_names

[![PyPI - Version](https://img.shields.io/pypi/v/friendly-names.svg)](https://pypi.org/project/friendly-names)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/friendly-names.svg)](https://pypi.org/project/friendly-names)

A super simple random friendly name generator that creates readable, hyphenated names like "red-loop-bounty".

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
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

## License

`friendly_names` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
