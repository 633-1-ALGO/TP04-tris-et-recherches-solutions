import abc


class Collection(abc.ABC):

    @abc.abstractmethod
    def add(self, element, index: int = None) -> None:
        """
        Ajoute un élément dans la liste.
        Si l'indice n'est pas donné, l'élément est ajouté à la fin de la liste.
        :param element: L'élément à ajouter
        :param index: La position où insérer l'élément
        :raise Retourne une erreur si l'indice spécifié ne permet pas un ajout correct
        """
        pass

    @abc.abstractmethod
    def get(self, index: int):
        """
        Retourne l'élément à l'indice spécifié
        :param index: Indice de l'élément
        :return L'élément à l'indice spécifié
        :raise Retourne une erreur si l'indice spécifié n'existe pas
        """
        pass

    @abc.abstractmethod
    def set(self, element, index: int) -> None:
        """
        Défini une nouvelle valeur à l'indice spécifié
        :param element: La nouvelle valeur
        :param index: L'indice à modifier
        :raise Retourne une erreur si l'indice spécifié n'existe pas
        """
        pass

    @abc.abstractmethod
    def remove(self, element = None, index: int = None) -> None:
        """
        Supprime un élément dans la liste. Si l'élément est spécifié, il est recherché puis supprimé.
        Si l'élément n'est pas spécifié, la suppression est faite en se basant sur l'indice donné.
        IL est nécessaire d'avoir soit l'élément, soit l'indice en paramètre.
        :param element: L'élément à supprimer
        :param index: L'indice de l'élément à supprimer
        :raise Retourne une erreur si l'élément ou l'indice spécifié n'existe pas
        """
        pass

    @abc.abstractmethod
    def clear(self) -> None:
        """
        Vide la liste
        """
        pass

    @abc.abstractmethod
    def size(self) -> int:
        """
        Retourne la taille de la liste
        :return La taille de la liste
        """
        pass

    @abc.abstractmethod
    def is_empty(self) -> bool:
        """
        Vérifie si la liste est vide
        :return Retourne True si la liste est vide, False sinon
        """
        pass

    @abc.abstractmethod
    def contains(self, element) -> bool:
        """
        Vérifie si la liste contient l'élément spécifié
        :param element: L'élément à rechercher
        :return Retourne True si l'élément est dans la liste, False sinon
        """
        pass

    @abc.abstractmethod
    def index_of(self, element) -> int:
        """
        Retourne la position d'un élément dans la liste en utilisant une recherche linéaire.
        :param element: La valeur à rechercher
        :return La position dans la liste de l'élément. -1 si l'élément n'est pas présent dans la liste.
        """
        pass

    @abc.abstractmethod
    def insertion_sort(self):
        """
        Tri la collection en utilisant le tri par insertion
        """
        pass

    @abc.abstractmethod
    def merge_sort(self):
        """
        Tri la collection en utilisant le tri par fusion
        """

    @abc.abstractmethod
    def dichotomic_search(self, element) -> int:
        """
        Retourne la position de l'élément en utilisant une recherche dichotomique
        :param element: L'élément à recherche
        :return Retourne la position de l'élément. -1 si l'élément n'est pas dans la liste
        """
        pass

