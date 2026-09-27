"""
validators.py
Custom module containing input-validation functions.
Demonstrates: custom modules, regular expressions (re module),
string methods, and required-argument functions.
"""

import re


def is_valid_roll(roll):
    """
    Validates a roll number of the pattern: 2 digits + 3 letters + 4 digits
    Example: 21BCE1234
    """
    pattern = r"^[0-9]{2}[A-Z]{3}[0-9]{4}$"
    return re.match(pattern, roll) is not None


def is_valid_name(name):
    """
    Validates that a name contains only alphabets and spaces,
    and is not empty.
    """
    pattern = r"^[A-Za-z ]+$"
    return len(name.strip()) > 0 and re.match(pattern, name) is not None


def is_valid_mark(mark_str):
    """
    Validates that the given string represents a valid mark
    between 0 and 100 (inclusive).
    """
    try:
        mark = float(mark_str)
    except ValueError:
        return False
    return 0 <= mark <= 100


def is_valid_email(email):
    """
    Validates a simple email pattern using regex.
    Example: name@example.com
    """
    pattern = r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None
