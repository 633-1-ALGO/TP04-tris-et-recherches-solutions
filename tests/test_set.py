from pytest import raises

from src.metier.LinkedList import LinkedList


class TestSet:

    def test_set(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        lk.set("4", 1)
        assert lk.get(0) == "1"
        assert lk.get(1) == "4"
        assert lk.get(2) == "3"

    def test_set_first_and_last(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        lk.set("4", 0)
        lk.set("5", 2)
        assert lk.get(0) == "4"
        assert lk.get(1) == "2"
        assert lk.get(2) == "5"

    def test_raise_when_bad_index(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        with raises(IndexError):
            lk.set("4", -1)
        with raises(IndexError):
            lk.set("4", 10)
