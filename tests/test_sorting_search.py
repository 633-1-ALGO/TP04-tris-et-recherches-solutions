from src.metier.LinkedList import LinkedList


class TestSortingSearch:

    def test_index_of(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        assert lk.index_of("1") == 0
        assert lk.index_of("3") == 2

    def test_index_of_return_minus_one(self):
        lk = LinkedList()
        lk.add("1")
        lk.add("2")
        lk.add("3")
        assert lk.index_of("0") == -1

    def test_insertion_sort(self):
        lk = LinkedList()
        lk.add(1)
        lk.add(3)
        lk.add(2)
        lk.insertion_sort()
        assert lk.get(0) == 1
        assert lk.get(1) == 2
        assert lk.get(2) == 3

    def test_insertion_sort2(self):
        lk = LinkedList()
        lk.add(2)
        lk.add(3)
        lk.add(1)
        lk.insertion_sort()
        assert lk.get(0) == 1
        assert lk.get(1) == 2
        assert lk.get(2) == 3

    def test_insertion_sort3(self):
        lk = LinkedList()
        lk.add(2)
        lk.insertion_sort()
        assert lk.get(0) == 2

    def test_merge_sort(self):
        lk = LinkedList()
        lk.add(1)
        lk.add(3)
        lk.add(2)
        lk.merge_sort()
        assert lk.get(0) == 1
        assert lk.get(1) == 2
        assert lk.get(2) == 3

    def test_merge_sort2(self):
        lk = LinkedList()
        lk.add(2)
        lk.add(3)
        lk.add(1)
        lk.merge_sort()
        assert lk.get(0) == 1
        assert lk.get(1) == 2
        assert lk.get(2) == 3

    def test_merge_sort3(self):
        lk = LinkedList()
        lk.add(2)
        lk.merge_sort()
        assert lk.get(0) == 2

    def test_dichotomic_search(self):
        lk = LinkedList()
        lk.add(1)
        # Il faut préalablement trier le tableau
        lk.merge_sort()
        assert lk.dichotomic_search(1) == 0

    def test_dichotomic_search2(self):
        lk = LinkedList()
        lk.add(2)
        lk.add(3)
        lk.add(1)
        # Il faut préalablement trier le tableau
        lk.merge_sort()
        assert lk.dichotomic_search(3) == 2
        assert lk.dichotomic_search(2) == 1

    def test_dichotomic_search_minus_one(self):
        lk = LinkedList()
        lk.add(1)
        lk.add(3)
        lk.add(2)
        # Il faut préalablement trier le tableau
        lk.merge_sort()
        assert lk.dichotomic_search(4) == -1
