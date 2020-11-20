from pytest import raises

from src.metier.LinkedList import LinkedList


class TestGet:

    def test_get(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        assert lk.get(0) == "1"
        assert lk.get(1) == "2"
        assert lk.get(2) == "3"

    def test_get_raise(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        with raises(IndexError):
            lk.get(10)
        with raises(IndexError):
            lk.get(-1)

    def test_contains(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        assert lk.contains("1") == True
        assert lk.contains("0") == False