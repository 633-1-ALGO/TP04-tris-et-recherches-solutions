from src.metier.LinkedList import LinkedList


class TestGeneral:

    def test_to_str(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        assert str(lk) == "1 <-> 2 <-> 3"

    def test_to_str_with_one_values(self):
        lk = LinkedList()
        lk.add("1")
        assert str(lk) == "1"

    def test_to_str_with_no_values(self):
        lk = LinkedList()
        assert str(lk) == ""
