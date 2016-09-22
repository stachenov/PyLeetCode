import pytest
from problems.multiply_strings import Solution


@pytest.mark.parametrize("num1, num2", [
    ("0", "0"),
    ("0", "1"),
    ("1", "0"),
    ("1", "1"),
    ("1", "2"),
    ("2", "1"),
    ("2", "2"),
    ("4", "5"),
    ("11", "9"),
    ("1235", "943"),
    ("1235", "0"),
    ("0", "1234"),
    ("999", "999"),
    ("999", "9"),
    ("9", "999"),
])
def test_multiply(num1, num2):
    assert Solution().multiply(num1, num2) == str(int(num1) * int(num2))
