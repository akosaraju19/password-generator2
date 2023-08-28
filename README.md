# password-generator2

Generate strong and secure passwords using this simple Python password generator

## Description

This project implements a password generator in Python. It allows you to create complex passwords with customizable length and character types

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [Contributing](#contributing)
- [Contact](#contact)

## Getting Started

To use the password generator, follow these steps:

1. Clone this repository to your local machine
2. Run the `password_generator.py` script using a Python interpreter
3. Follow the prompts to customize the password length and character types

## Usage

The password generator provides a function that you can use to generate passwords:

```python
generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True)
```

- length: Length of the generated password (default is 12)
- use_letters: Include letters (both uppercase and lowercase) in the password (default is True)
- use_digits: Include digits in the password (default is True)
- use_symbols: Include symbols in the password (default is True)

## Features

Generate passwords with varying lengths
Customize character types (letters, digits, symbols) in passwords
Simple command-line interface for easy use

## Examples

Generate a 16-character password with letters, digits, and symbols:

```python
password = generate_password(length=16, use_letters=True, use_digits=True, use_symbols=True)
print(password)
```
## Contributing

If you have any improvements or suggestions for me, feel free to open a pull request!!

## Contact

If you have any questions or feedback, feel free to contact me at a2kosara@uwaterloo.ca

