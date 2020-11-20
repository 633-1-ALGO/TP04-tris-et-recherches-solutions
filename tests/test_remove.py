from pytest import raises

from src.metier.LinkedList import LinkedList


class TestRemove:

    def test_remove_with_index(self):
        lk = LinkedList()
        value = "1"
        lk.add(value)
        lk.remove(None, 0)
        assert lk.size() == 0

    def test_remove_with_index_when_multiple_nodes(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        lk.remove(None, 2)
        assert lk.size() == 3
        assert lk.get(0) == values[0]
        assert lk.get(1) == values[1]
        assert lk.get(2) == values[3]

    def test_remove_with_value(self):
        lk = LinkedList()
        value = "1"
        lk.add(value)
        lk.remove("1")
        assert lk.size() == 0

    def test_remove_with_value_when_multiple_nodes(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        lk.remove("3")
        assert lk.size() == 3
        assert lk.get(0) == values[0]
        assert lk.get(1) == values[1]
        assert lk.get(2) == values[3]

    def test_raise_when_no_value(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        with raises(ValueError):
            lk.remove("5")

    def test_raise_when_bad_index(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        with raises(IndexError):
            lk.remove(None, 10)
        with raises(IndexError):
            lk.remove(None, -1)

    def test_clear(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        lk.clear()
        assert lk.size() == 0
        with raises(IndexError):
            lk.get(0)

    def test_is_empty(self):
        lk = LinkedList()
        assert lk.is_empty() == True
        lk.add("1")
        assert lk.is_empty() == False
        lk.clear()
        assert lk.is_empty() == True
