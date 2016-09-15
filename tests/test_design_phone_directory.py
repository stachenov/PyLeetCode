import pytest
from problems.design_phone_directory import PhoneDirectory


@pytest.mark.parametrize("max_numbers,operations", [
    (1, [("check", (0,), True), ("get", (), 0), ("release", (0,), None)]),
    (1, [("check", (0,), True), ("get", (), 0), ("check", (0,), False), ("get", (), -1)]),
])
def test(max_numbers, operations):
    directory = PhoneDirectory(max_numbers)
    for op, args, expected in operations:
        assert directory.__class__.__dict__[op](directory, *args) == expected
