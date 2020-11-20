import random
import time

from src.metier.LinkedList import LinkedList

# Afin d'avoir tout le temps les mêmes nombres aléatoires
random.seed(10)


def is_sorted(lk: LinkedList):
    n = lk.get(0)
    for i in range(1, lk.size()):
        j = lk.get(i)
        if n > j:
            return False
        n = j
    return True


def current_time():
    return int(round(time.time() * 1000))


def populate(lk: LinkedList, n: int):
    for i in range(0, n):
        lk.add(random.randint(0, 1000))


if __name__ == '__main__':
    # Vos tests ici
    lk = LinkedList()
    n: int = 1000

    print("========== BAD INSERTION SORT ==========")
    lk.clear()
    populate(lk, n)
    t = current_time()
    lk.bad_insertion_sort()
    print("Temps : {} ms\n".format(current_time() - t))
    print("Tableau trié ? ", is_sorted(lk))

    print("========== INSERTION SORT ==========")
    lk.clear()
    populate(lk, n)
    t = current_time()
    lk.insertion_sort()
    print("Temps : {} ms\n".format(current_time() - t))
    print("Tableau trié ? ", is_sorted(lk))

    print("========== BAD MERGE SORT ==========")
    lk.clear()
    populate(lk, n)
    t = current_time()
    lk.bad_merge_sort()
    print("Temps : {} ms\n".format(current_time() - t))
    print("Tableau trié ? ", is_sorted(lk))

    print("========== MERGE SORT ==========")
    lk.clear()
    populate(lk, n)
    t = current_time()
    lk.merge_sort()
    print("Temps : {} ms\n".format(current_time() - t))
    print("Tableau trié ? ", is_sorted(lk))

    print("========== BEST MERGE SORT ==========")
    lk.clear()
    populate(lk, n)
    t = current_time()
    lk.best_merge_sort()
    print("Temps : {} ms\n".format(current_time() - t))
    print("Tableau triée ? ", is_sorted(lk))

    n = 100000
    lk.clear()
    populate(lk, n)
    value_to_search = lk.get(random.randint(0, lk.size() - 1))
    print("========== LINEAR SEARCH (on unsorted list) ==========")
    t = current_time()
    index = lk.index_of(value_to_search)
    print("Valeur à rechercher: {}".format(value_to_search))
    print("Indice trouvé: {}".format(index))
    print("Valeur équivalente à l'indice trouvé: {}".format(lk.get(index)))
    print("Temps : {} ms\n".format(current_time() - t))

    lk.clear()
    for i in range(n):
        lk.add(i)
    value_to_search = lk.get(random.randint(0, lk.size() - 1))
    print("========== LINEAR SEARCH (on sorted list) ==========")
    t = current_time()
    index = lk.index_of(value_to_search)
    print("Valeur à rechercher: {}".format(value_to_search))
    print("Indice trouvé: {}".format(index))
    print("Valeur équivalente à l'indice trouvé: {}".format(lk.get(index)))
    print("Temps : {} ms\n".format(current_time() - t))

    print("========== DICHOTOMIC SEARCH (on sorted list, of course) ==========")
    t = current_time()
    index = lk.dichotomic_search(value_to_search)
    print("Valeur à rechercher: {}".format(value_to_search))
    print("Indice trouvé: {}".format(index))
    print("Valeur équivalente à l'indice trouvé: {}".format(lk.get(index)))
    print("Temps : {} ms\n".format(current_time() - t))
    print()
