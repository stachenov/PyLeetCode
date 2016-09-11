import pytest

from problems.evaluate_division import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize("equations,values,query,expected", [
    ([["a", "b"], ["b", "c"]],
     [2.0, 3.0],
     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
     [6.0, 0.5, -1.0, 1.0, -1.0]),
    ([["a", "e"], ["b", "e"]],
     [4, 3],
     [["a", "b"], ["e", "e"], ["x", "x"]],
     [1.3333333333333333, 1.0, -1]),
    ([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
     [3, 4, 5, 6],
     [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]],
     [360.00000, 0.008333333333333333, 20.00000, 1.00000, -1.00000, -1.00000]),
    ([["a", "b"]],
     [2],
     [["b", "a"]],
     [0.5]),
    ([["x1", "x2"], ["x2", "x3"], ["x1", "x4"], ["x2", "x5"]],
     [3, 0.5, 3.4, 5.6],
     [["x2", "x4"], ["x1", "x5"], ["x1", "x3"], ["x5", "x5"], ["x5", "x1"], ["x3", "x4"], ["x4", "x3"], ["x6", "x6"],
      ["x0", "x0"]],
     [1.13333, 16.80000, 1.50000, 1.00000, 0.05952, 2.26667, 0.44118, -1.00000, -1.00000]),
])
def test(solution, equations, values, query, expected):
    assert all(abs(x - y) < 0.001 for x, y in zip(solution.calcEquation(equations, values, query), expected))
