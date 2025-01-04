"""Tests for the example module."""

import pytest
from package_name.example import add, divide, average


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),           # Integer addition
        (-1, 1, 0),          # Handling negative numbers
        (1.5, 2.5, 4.0),     # Float addition
        (0, 0, 0),           # Zero handling
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    """Test add function with various inputs."""
    assert add(a, b) == expected


class TestDivide:
    """Group tests for divide function to demonstrate class-based testing."""
    
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (6, 2, 3.0),     # Integer division
            (5, 2, 2.5),     # Division with remainder
            (-6, 2, -3.0),   # Negative number division
            (1.5, 2, 0.75),  # Float division
        ]
    )
    def test_basic_division(self, a: float, b: float, expected: float) -> None:
        """Test basic division operations with various inputs."""
        assert divide(a, b) == expected

    def test_divide_by_zero(self) -> None:
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)

    def test_invalid_input_type(self) -> None:
        """Test that invalid input types raise TypeError."""
        with pytest.raises(TypeError, match="Inputs must be numbers"):
            divide("1", 2)  # type: ignore
        with pytest.raises(TypeError, match="Inputs must be numbers"):
            divide(1, "2")  # type: ignore


def test_average_basic() -> None:
    """Test basic average calculations."""
    assert average([1, 2, 3]) == 2.0
    assert average([1.5, 2.5]) == 2.0
    assert average([0, 0, 0]) == 0.0


def test_average_empty_list() -> None:
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate average of empty list"):
        average([])


def test_average_invalid_input() -> None:
    """Test that invalid inputs raise TypeError."""
    with pytest.raises(TypeError, match="All inputs must be numbers"):
        average([1, "2", 3])  # type: ignore
