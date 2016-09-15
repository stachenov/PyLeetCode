import pytest
from problems.classes import ListNode, NestedInteger


class TestListNode:
    @pytest.mark.parametrize("val", [
        (1,),
        (-2,),
    ])
    def test_init_scalar(self, val):
        node = ListNode(val)
        assert node.val == val

    @pytest.mark.parametrize("values", [
        [1],
        [1, -2, 3],
    ])
    def test_init_list(self, values):
        node = ListNode(values)
        res = []
        while node is not None:
            res.append(node.val)
            node = node.next
        assert res == values

    @pytest.mark.parametrize("param", [
        1,
        -2,
        [1],
        [1, -2, 3],
    ])
    def test_init_iterate(self, param):
        expected = param
        if type(expected) is not list:
            expected = [expected]
        node = ListNode(param)
        res = [n for n in node]
        assert res == expected


class TestNestedInteger:
    def test_init_empty_list(self):
        ni = NestedInteger()
        assert ni.isInteger() is False
        assert ni.getList() == []

    @pytest.mark.parametrize("val", [
        1, -2, 3,
    ])
    def test_init_empty_list(self, val):
        ni = NestedInteger(val)
        assert ni.isInteger() is True
        assert ni.getInteger() == val

    @pytest.mark.parametrize("values", [
        [1],
        [1, -2, 3],
    ])
    def test_add(self, values):
        ni = NestedInteger()
        res = []
        for n in values:
            ni.add(n)
            res.append(n)
            assert ni.getList() == res

    @pytest.mark.parametrize("val, new", [
        (1, 1),
        (1, -2),
    ])
    def test_set_integer(self, val, new):
        ni = NestedInteger(val)
        ni.setInteger(new)
        assert ni.getInteger() == new

    @pytest.mark.parametrize("ni, expected", [
        (NestedInteger(1), "1"),
        (NestedInteger(), "[]"),
        (NestedInteger([NestedInteger(1)]), "[1]"),
        (NestedInteger([NestedInteger(1), NestedInteger([NestedInteger(2)])]), "[1,[2]]"),
        (NestedInteger([NestedInteger(1), NestedInteger([NestedInteger(-2)])]), "[1,[-2]]"),
    ])
    def test_str(self, ni, expected):
        assert str(ni) == expected
