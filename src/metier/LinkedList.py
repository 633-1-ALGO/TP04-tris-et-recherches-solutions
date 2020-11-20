from src.metier.Collection import Collection
from src.domain.Node import Node


class LinkedList(Collection):
    """
    # ================ ATTENTION ================
    # Pour les méthodes de tri (insertion et fusion), j'ai créé plusieurs versions :
    # insertion_sort => meilleur tri par insertion possible
    # bad_insertion_sort => mauvais tri par insertion car utilises les méthodes get et set, augmentant ainsi la complexité
    # best_merge_sort => meilleur tri par fusion possible (à ma connaissance). N'utilise pas les méthodes get, set et remove et
    #                    ne dédouble pas les noeuds lors de la création des listes left et right, réduisant la mémoire nécessaire
    # merge_sort => bonne façon de faire le tri par fusion, sans get, set et remove mais également sans optimisation de la mémoire
    # bad_merge_sort => mauvaise façon de faire l'algorithme, avec utilisation de get, set et remove
    """

    def __init__(self):
        # J'instancie mes variables
        self.__head: Node = None  # Pointeur sur le premier noeud de ma liste
        self.__tail: Node = None  # Pointeur sur le dernier noeud de ma liste
        self.__size: int = 0
        self.__sorted: bool = False  # Permer de savoir si ma liste est triée (non obligatoire)

    def add(self, element, index: int = None) -> None:
        """
        Ajoute un élément dans la liste.
        Si l'indice n'est pas donné, l'élément est ajouté à la fin de la liste.
        :param element: L'élément à ajouter
        :param index: La position où insérer l'élément
        :raise Retourne une erreur si l'indice spécifié ne permet pas un ajout correct
        """
        # Si jamais l'index n'est pas défini, j'insère à la fin
        if index is None:
            self.__add_last(element)
        else:
            # Si l'index est défini, je vérifie d'abord si c'est 0
            # si c'est le cas, il faut que j'insère l'élément à la première position
            if index == 0:
                self.__add_first(element)
            # Si jamais l'index est égal à la taille de la liste, il faut que j'insère l'élément à la fin
            elif index == self.__size:
                self.__add_last(element)
            # Si aucune de ces conditions ne sont vrais, il faut insérer l'élément au milieu de la liste
            else:
                # __get_node() se chargera de vérifier que l'index permettent un ajout correct
                current_node: Node = self.__get_node(index)
                new_node: Node = Node(current_node.get_prev(), element, current_node)
                current_node.get_prev().set_next(new_node)
                current_node.set_prev(new_node)
                self.__size += 1
        self.__sorted = False  # Dans tous les cas, je considère la liste comme non triée

    def __add_first(self, element) -> None:
        """
        Ajout un nouveau noeud au début de la liste
        :param element: Valeur à ajouter
        """
        # Si la liste est vide, je crée le premier noeud et je le définis comme étant le head et le tail
        if self.is_empty():
            self.__head = Node(None, element, None)
            self.__tail = self.__head
        else:
            # sinon, je crée le premier noeud puis je le définis comme étant le head
            new_node = Node(None, element, self.__head)
            self.__head.set_prev(new_node)
            self.__head = new_node
        # Dans tous les cas, j'augmente la taille de la liste
        self.__size += 1

    def __add_last(self, element) -> None:
        """
        Ajoute un nouveau noeud à la fin de la liste
        :param element: Valeur à ajouter
        """
        # Si la liste est vide, je crée le premier noeud et le définis comme étant le head et le tail
        if self.is_empty():
            self.__head = Node(None, element, None)
            self.__tail = self.__head
        else:
            # sinon, je crée un nouveau noeud et je le définis comme étant le tail
            new_node = Node(self.__tail, element, None)
            self.__tail.set_next(new_node)
            self.__tail = new_node
        # Dans tous les cas, j'augmente la taille de la liste
        self.__size += 1

    def get(self, index: int):
        """
        Retourne l'élément à l'indice spécifié
        :param index: Indice de l'élément
        :return L'élément à l'indice spécifié
        :raise Retourne une erreur si l'indice spécifié n'existe pas
        """
        return self.__get_node(index).get_value()

    def __get_node(self, index: int) -> Node:
        """
        Retourne le noeud à l'indice spécifié
        :param index: L'indice du noeud
        :return: Le noeud à l'indice spécifié
        :raise Retourne une IndexError si l'indice est plus petit que 0 ou plus grand que la taille de la liste
        """
        # Je vérifie si l'index est valable
        if index >= self.__size or index < 0:
            raise IndexError("IndexOutOfBound")
        # Je récupère le noeud à l'index voulu
        node = self.__head
        for i in range(0, index):
            node = node.get_next()
        return node

    def set(self, element, index: int) -> None:
        """
        Défini une nouvelle valeur à l'indice spécifié
        :param element: La nouvelle valeur
        :param index: L'indice à modifier
        :raise Retourne une erreur si l'indice spécifié n'existe pas
        """
        self.__get_node(index).set_value(element)
        self.__sorted = False

    def remove(self, element=None, index: int = None) -> None:
        """
        Supprime un élément dans la liste. Si l'élément est spécifié, il est recherché puis supprimé.
        Si l'élément n'est pas spécifié, la suppression est faite en se basant sur l'indice donné.
        IL est nécessaire d'avoir soit l'élément, soit l'indice en paramètre.
        :param element: L'élément à supprimer
        :param index: L'indice de l'élément à supprimer
        :raise Retourne une erreur si l'élément ou l'indice spécifié n'existe pas
        """
        # Précondition
        if element is None and index is None:
            raise AttributeError("L'élément ou l'index doit être défini!")

        # Si l'élément est défini, je trouve son index grace à la méthode "index_of" puis je rapelle la méthode remove avec le bon index
        if element is not None:
            # Je trouve d'abord l'index de l'élément que je cherche
            index = self.index_of(element)
            # Si jamais l'élément n'existe pas, je raise une erreur
            if index == -1:
                raise ValueError("L'élément à supprimer n'existe pas")
            # Si l'index a été trouvé, je rappelle ma méthode en lui fournissant l'index
            self.remove(None, index)
        else:
            # Si jamais l'index est 0, je supprime le premier élément
            if index == 0:
                self.__remove_first()
                # Je ne rédéfini pas self.__sorted à False car, en ayant supprimé que le premier élément, la liste reste triée si elle l'était
            # Si jamais l'index est égal à la taille de la liste -1 (dernier élément, comme on commence à 0 ^^)
            elif index == self.__size - 1:
                self.__remove_last()
                # Je ne rédéfini pas self.__sorted à False car, en ayant supprimé que le dernier élément, la liste reste triée si elle l'était
            else:
                # Si aucune de ces conditions ne sont remplies, c'est que je dois supprimer un noeud au milieu de la liste
                node = self.__get_node(index)
                node.get_prev().set_next(node.get_next())
                node.get_next().set_prev(node.get_prev())
                node.set_next(None)
                node.set_prev(None)
                self.__size -= 1
                self.__sorted = False

    def __remove_first(self) -> None:
        """
        Supprime le premier noeud de la liste
        """
        # Si il n'y a qu'un seul élément dans la liste, je la vide entièrement
        if self.__size == 1:
            self.clear()
        elif self.__size == 2:
            # Si il y en a 2, il faut que je définisse que head = tail
            self.__tail.set_prev(None)
            self.__head.set_next(None)
            self.__head = self.__tail
            self.__size -= 1
        else:
            # sinon je supprime le premier noeud et je ne redéfini que head (je ne touche pas à tail)
            node = self.__head.get_next()
            node.set_prev(None)
            self.__head.set_next(None)
            self.__head = node
            self.__size -= 1

    def __remove_last(self) -> None:
        """
        Supprime le dernier noeud de la liste
        """
        # Pas besoin de traiter le cas de self.__size == 1 car c'est la méthode __remove_first qui le fera à chaque fois
        # On ne rentrera jamais dans cette méthode si la taille est = 1
        # S’il n'y a que 2 éléments dans la liste, il faut que je définisse tail = head
        if self.__size == 2:
            self.__head.set_next(None)
            self.__tail.set_prev(None)
            self.__tail = self.__head
        else:
            # sinon je supprime l'élément et je redéfinis tail
            node = self.__tail.get_prev()
            self.__tail.set_prev(None)
            node.set_next(None)
            self.__tail = node
        # Dans tous les cas, je réduit la taille de la liste
        self.__size -= 1

    def clear(self) -> None:
        """
        Vide la liste
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self) -> int:
        """
        Retourne la taille de la liste
        :return La taille de la liste
        """
        return self.__size

    def is_empty(self) -> bool:
        """
        Vérifie si la liste est vide
        :return Retourne True si la liste est vide, False sinon
        """
        return self.__size == 0

    def contains(self, element) -> bool:
        """
        Vérifie si la liste contient l'élément spécifié
        :param element: L'élément à rechercher
        :return Retourne True si l'élément est dans la liste, False sinon
        """
        return self.index_of(element) != -1

    def index_of(self, element) -> int:
        """
        Retourne la position d'un élément dans la liste en utilisant une recherche linéaire.
        :param element: La valeur à rechercher
        :return La position dans la liste de l'élément. -1 si l'élément n'est pas présent dans la liste.
        """
        i = 0
        node = self.__head
        while node is not None:
            if node.get_value() == element:
                return i
            i += 1
            node = node.get_next()
        return -1

    def insertion_sort(self):
        """
        Tri la collection en utilisant le tri par insertion
        """
        if not self.is_empty():  # Je ne trie que s’il y a au moins 1 noeud pour éviter les problèmes
            to_sort = self.__head  # Je récupère le noeud à trier
            # Je ne commence pas directement du deuxième noeud dans le cas ou il n'y en aurait qu'un seul
            while to_sort.have_next():  # Si il n'y a qu'un seul noeud, il est déjà trié, pas besoin de continuer
                to_sort = to_sort.get_next()  # Je stock le noeud à trier
                key = to_sort.get_value()  # Je stock la valeur du noeud à trier
                previous = to_sort.get_prev()
                # Je parcours tous les noeuds précédents en faisant les transpositions nécessaires
                while previous is not None and previous.get_value() > key:
                    previous.get_next().set_value(previous.get_value())
                    previous = previous.get_prev()
                # Si jamais on arrive au tout début de la liste, previous sera = None (le tout premier noeud n'a pas de previous)
                # Je dois alors vérifier ce cas
                if previous is not None:
                    previous.get_next().set_value(key)
                else:
                    self.__head.set_value(key)
        self.__sorted = True

    def bad_insertion_sort(self):
        """
        Tri la collection en utilisant le tri par insertion
        Cette version utilise les méthodes get et set, augmentant la complexité
        """
        # Du fait que j'utilise mes méthodes get et set, je me retrouve
        # avec beaucoup plus de boucles et donc une complexité bien plus élevée que prévu
        for i in range(1, self.__size):
            key = self.get(i)  # Get fait une boucle, je rajoute donc de la complexité
            j = i - 1
            while j >= 0 and self.get(j) > key:  # De même
                self.set(self.get(j), j + 1)  # Set et get font des boucles
                j -= 1
            self.set(key, j + 1)  # De même
        self.__sorted = True
        # Complexité :
        # Dans le pire des cas, on ne se retrouve plus avec n^2 mais n^3
        # Dans le meilleur des cas, on passe à n^2

    def merge_sort(self):
        """
        Tri la collection en utilisant le tri par fusion
        """
        # Je récupère ma liste triée en lui fournissant en paramètre la liste actuelle non triée
        new_list = self.__fusion_sort(self)
        # Je redéfini le head et le tail de ma liste actuelle avec les noeuds de la liste triée
        self.__head = new_list.__head
        self.__tail = new_list.__tail
        self.__sorted = True

    def __fusion_sort(self, lst: 'LinkedList') -> 'LinkedList':
        if lst.size() <= 1:
            # Si la taille de la liste est 1 ou plus petit, je retourne la liste
            # Ne contenant qu'un seul élément, elle est forcément triée
            return lst
        # On récupère l'index de la moitié de la liste
        middle = int(lst.size() / 2)
        # On instancie la liste "droite" et "gauche"
        left = LinkedList()
        right = LinkedList()
        node = lst.__head
        # On ajoute les bonnes valeurs dans les listes "droite" et "gauche"
        for i in range(0, middle):
            left.add(node.get_value())
            node = node.get_next()
        for i in range(middle, lst.size()):
            right.add(node.get_value())
            node = node.get_next()
        left = self.__fusion_sort(left)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        right = self.__fusion_sort(right)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        return self.__merge(left, right)  # Quand les deux listes sont triées, il suffit de les merge

    def __merge(self, left: 'LinkedList', right: 'LinkedList') -> 'LinkedList':
        """
        Merge fonction optimisée
        :param left: LinkedList gauche, triée
        :param right: LinkedList droite, triée
        :return: Fusion des deux linkedList, triée
        """
        result = LinkedList()
        left_node: Node = left.__head
        right_node: Node = right.__head
        # Je parcours les listes en utilisant get_next()
        # Tant que je n'arrive pas à la fin d'une des deux listes, je continue la boucle
        while left_node is not None and right_node is not None:
            # Je vérifie quel valeur est la plus petite et je la rajoute dans ma liste de résultat
            # Ensuite j'avance dans la liste
            if left_node.get_value() < right_node.get_value():
                result.add(left_node.get_value())
                left_node = left_node.get_next()
            else:
                result.add(right_node.get_value())
                right_node = right_node.get_next()

        # Ici, une des deux listes est vide mais pas l'autre, il faut donc que je rajoute les valeurs de la liste non vide
        while left_node is not None:
            result.add(left_node.get_value())
            left_node = left_node.get_next()
        while right_node is not None:
            result.add(right_node.get_value())
            right_node = right_node.get_next()

        return result

    def best_merge_sort(self):
        """
        Tri la collection en utilisant le tri par fusion
        Cette version n'utilises pas les get, les set et les remove (n'augmente pas la complexité)
        et réduit également au maximum la mémoire nécessaire (ne dédouble pas les noeuds lors de la création de left et right)
        """
        # Je récupère ma liste triée en lui fournissant en paramètre la liste actuelle non triée
        new_list = self.__best_fusion_sort(self)
        # Je redéfini le head et le tail de ma liste actuelle avec les noeuds de la liste triée
        self.__head = new_list.__head
        self.__tail = new_list.__tail
        self.__sorted = True

    def __best_fusion_sort(self, lst: 'LinkedList') -> 'LinkedList':
        if lst.size() <= 1:
            # Si la taille de la liste est 1 ou plus petit, je retourne la liste
            # Ne contenant qu'un seul élément, elle est forcément triée
            return lst
        # On récupère l'index de la moitié de la liste
        middle = int(lst.size() / 2)
        # On instancie la liste "droite" et "gauche"
        left = LinkedList()
        right = LinkedList()
        middle_node = lst.__get_node(middle - 1)  # On récupère le noeud du milieu (-1 car on commence de 0)
        # Je calcul les tailles des listes gauche et droite
        right_size = lst.__size - middle
        left_size = lst.__size - right_size
        # Pour définir les valeurs dans la liste de gauche et droite,
        # on ne recréer pas de nouveaux noeud mais on met juste un pointeur sur les noeuds actuels et on défini la bonne taille
        left.__head = lst.__head
        left.__tail = middle_node
        left.__size = left_size

        right.__head = middle_node.get_next()
        right.__tail = lst.__tail
        right.__size = right_size

        left = self.__best_fusion_sort(left)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        right = self.__best_fusion_sort(right)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        return self.__best_merge(left, right)  # Quand les deux listes sont triées, il suffit de les merge

    def __best_merge(self, left: 'LinkedList', right: 'LinkedList') -> 'LinkedList':
        """
        Merge fonction optimisée
        :param left: LinkedList gauche, triée
        :param right: LinkedList droite, triée
        :return: Fusion des deux linkedList, triée
        """
        result = LinkedList()
        left_node: Node = left.__head
        right_node: Node = right.__head
        # Comme j'ai construit les liste left et right en modifiant juste les pointeurs de head et tail,
        # je ne peux pas vérifier qu'ils soient égaux à None
        # Du coup, je vérifie si on dépasse le tail (cela veut dire qu'on arrive à la fin de la liste)
        while left_node != left.__tail.get_next() and right_node != right.__tail.get_next():
            if left_node.get_value() < right_node.get_value():
                result.add(left_node.get_value())
                left_node = left_node.get_next()
            else:
                result.add(right_node.get_value())
                right_node = right_node.get_next()

        while left_node != left.__tail.get_next():
            result.add(left_node.get_value())
            left_node = left_node.get_next()
        while right_node != right.__tail.get_next():
            result.add(right_node.get_value())
            right_node = right_node.get_next()

        return result

    def bad_merge_sort(self):
        """
        Tri la collection en utilisant le tri par fusion
        """
        new_list = self.__bad_fusion_sort(self)
        self.__head = new_list.__head
        self.__tail = new_list.__tail
        self.__sorted = True

    def __bad_fusion_sort(self, lst: 'LinkedList') -> 'LinkedList':
        """
        Cette manière de faire le tri par fusion utilise les méthodes get, set et remove et donc augmente la complexité de l'algorithme
        :param lst:
        :return:
        """
        if lst.size() <= 1:
            return lst
        # On récupère l'index de la moitié de la liste
        middle = int(lst.size() / 2)
        # On instancie la liste "droite" et "gauche"
        left = LinkedList()
        right = LinkedList()
        node = lst.__head
        # On ajoute les bonnes valeurs dans les listes "droite" et "gauche"
        for i in range(0, middle):
            left.add(node.get_value())
            node = node.get_next()
        for i in range(middle, lst.size()):
            right.add(node.get_value())
            node = node.get_next()

        # 4 7 8 9 10 4 5 2
        # left: 4 7 8 9
        # right: 10 4 5 2

        left = self.__bad_fusion_sort(left)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        # left: 4 7 8 9
        right = self.__bad_fusion_sort(right)  # __fusion_sort retourne la liste donnée en paramètre, mais triée
        # right: 2 4 5 10
        return self.__bad_merge(left, right)  # Quand les deux listes sont triées, il suffit de les merge
        #  4 5 7 8 9 10

    def __bad_merge(self, left: 'LinkedList', right: 'LinkedList') -> 'LinkedList':
        """
        Merge fonction faisant appel aux fonctions "get" et "remove" qui, selon leurs implémentations, augmente la complexité.
        Dans mon cas, cela n'augmente pas le nombre de boucles (avec mon implémentation) mais augmente par contre le nombre de if
        :param left: LinkedList gauche, triée
        :param right: LinkedList droite, triée
        :return: Fusion des deux linkedList, triée
        """
        result = LinkedList()
        # Tant que une de mes listes n'est pas vide, je parcours
        while not left.is_empty() and not right.is_empty():
            # Je vérifie quelle valeur est la plus petite et je l'ajoute a ma liste de résultat
            # Ensuite je supprime cette valeur de la liste
            if left.get(0) < right.get(0):
                result.add(left.get(0))
                left.remove(None, 0)
            else:
                result.add(right.get(0))
                right.remove(None, 0)

        while not left.is_empty():
            result.add(left.get(0))
            left.remove(None, 0)
        while not right.is_empty():
            result.add(right.get(0))
            right.remove(None, 0)

        return result

    def dichotomic_search(self, element) -> int:
        # if not self.__sorted:
        #     raise InterruptedError("La liste doit préalablement être triée")
        return self.__binary_search(0, self.__size - 1, element)

    def __binary_search(self, p: int, r: int, element):
        if p > r:
            return -1
        q = int((p + r) / 2)
        value = self.get(q)  # Ce get ralenti l'algorithme mais ne peux pas être supprimé
        if value == element:
            return q
        if element < value:
            # Je recherche dans la partie gauche du tableau
            return self.__binary_search(p, q - 1, element)
        # sinon je recherche dans la partie droite du tableau
        return self.__binary_search(q + 1, r, element)

    def __str__(self):
        if self.is_empty():
            return ""
        res = ""
        node = self.__head
        while node != self.__tail:
            res += str(node.get_value()) + " <-> "
            node = node.get_next()
        res += str(self.__tail.get_value())
        return res
