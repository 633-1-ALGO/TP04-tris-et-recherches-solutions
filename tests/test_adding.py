from pytest import raises

from src.metier.LinkedList import LinkedList


class TestAdding:
    def test_add_first_element_without_index(self):
        lk = LinkedList()
        value = "1"
        lk.add(value)
        assert lk.size() == 1
        assert lk.get(0) == value

    def test_add_first_element_with_index(self):
        lk = LinkedList()
        value = "1"
        lk.add(value, 0)
        assert lk.size() == 1
        assert lk.get(0) == value

    def test_add_multiple_elements_without_index(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        assert lk.size() == 4
        assert lk.get(0) == values[0]
        assert lk.get(1) == values[1]
        assert lk.get(2) == values[2]
        assert lk.get(3) == values[3]

    def test_add_multiple_elements_with_index(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value, 0)
        assert lk.size() == 4
        assert lk.get(0) == values[3]
        assert lk.get(1) == values[2]
        assert lk.get(2) == values[1]
        assert lk.get(3) == values[0]

    def test_add_multiple_elements_to_end_with_index(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value, lk.size())
        assert lk.size() == 4
        assert lk.get(0) == values[0]
        assert lk.get(1) == values[1]
        assert lk.get(2) == values[2]
        assert lk.get(3) == values[3]

    def test_add_element_in_center(self):
        lk = LinkedList()
        values = ["1", "2", "3", "4"]
        for value in values:
            lk.add(value)
        lk.add("5", 2)
        assert lk.size() == 5
        assert lk.get(0) == values[0]
        assert lk.get(1) == values[1]
        assert lk.get(2) == "5"
        assert lk.get(3) == values[2]
        assert lk.get(4) == values[3]

    def test_raise_on_bad_index(self):
        lk = LinkedList()
        with raises(IndexError):
            lk.add("1", -1)
        with raises(IndexError):
            lk.add("1", 1)
