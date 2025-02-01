"""Example module demonstrating type hints, doctests, and error handling.

This module provides a simple calculator implementation to demonstrate Python best practices:
- Type hints for better code understanding and static type checking
- Doctests for documentation and testing
- Error handling for robust code
- Clear documentation
"""

from typing import Union, List


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> add(1, 2)
        3
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Divide first number by second number.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division a / b

    Raises:
        ValueError: If b is zero
        TypeError: If inputs are not numbers

    Examples:
        >>> divide(6, 2)
        3.0
        >>> divide(5, 2)
        2.5
        >>> divide(1, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a) / b


def average(numbers: List[Union[int, float]]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers to average

    Returns:
        Arithmetic mean of input numbers

    Raises:
        ValueError: If the input list is empty
        TypeError: If any input is not a number

    Examples:
        >>> average([1, 2, 3])
        2.0
        >>> average([1.5, 2.5])
        2.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: Cannot calculate average of empty list
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")

    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All inputs must be numbers")

    return sum(numbers) / len(numbers)
