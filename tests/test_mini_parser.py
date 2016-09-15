import pytest
from problems.mini_parser import Solution


@pytest.mark.parametrize("s", [
    "1",
    "123",
    "[123]",
    "[1,[2]]",
    "[1,2,[2,[3],4]]",
    "[1,-2,[2,[-1,3,-4],4]]",
])
def test(s):
    assert str(Solution().deserialize(s)) == s
