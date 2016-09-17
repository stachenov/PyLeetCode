import pytest
from problems.zigzag_conversion import Solution


@pytest.mark.parametrize("s,numRows,expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 1, "PAYPALISHIRING"),
    ("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG"),
    # P   I   N
    # A  LS  IG
    # Y A H R
    # P   I
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    # P    H
    # A   SI
    # Y  I R
    # P L  IG
    # A    N
    ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
])
def test(s, numRows, expected):
    assert Solution().convert(s, numRows) == expected
