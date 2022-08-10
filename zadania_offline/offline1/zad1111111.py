from zad1testy import Node, runtests

def merge(first1, first2):
    p1 = first1
    p2 = first2

    if p1 is None:
        return first2
    if p2 is None:
        return first1

    if p1.val < p2.val:
        new_list = p1
        p1 = p1.next
        new_list.next = None  # odcinamy ten jeden element, który wzięliśmy do nowej listy -> wskazuje na nic
    else:
        new_list = p2
        p2 = p2.next
        new_list.next = None

    k = new_list
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            k.next = p1
            p1 = p1.next
            k = k.next
            k.next = None
        else:
            k.next = p2
            p2 = p2.next
            k = k.next
            k.next = None

    # oprózniliśmy jedną z list, teraz sprawdzamy, która ma jeszcze elementy
    if p1 is not None:
        k.next = p1
    else:
        k.next = p2
    return new_list  # new_list wskazuje nam na początek naszej listy, k na koniec listy


def MergeSort(list):
    sorted_list = [list]
    if list is None:
        return

    # ten while na dole dzieli nam wejściowa listę na serie liczb naturalnych - tablica,
    # która trzyma wskaźniki na pierwsze elementy list (juz posortowane elementy, np 2    1 5     4) -> otrzymamy tablicę 3 elementową ze wskazaniem na pierwsze elementy
    while list.next is not None:
        if list.next.val < list.val:
            sorted_list.append(list.next)
            tmp = list.next
            list.next = None
            list = tmp
        else:
            list = list.next

    while len(sorted_list) > 1:  # bo jak będzie długość równa 1, to nie ma czego scalać
        new_sorted_list = []  # tworzymy nową tablicę, która będzie mieć o 1 komórkę mniej - 3 tablicy 3 elementowej po scaleniu będą 2
        for i in range(1, len(sorted_list) - 1, 2):  # co dwa, bo scalamy dwa sąsiednie
            new_sorted_list.append(merge(sorted_list[i - 1], sorted_list[i]))  # np range(1,4,2) -> zmergujemy 0 z 1, 3 z 2 i 4 dopiszemy ifem linijkę nizej
        if len(sorted_list % 2 == 1):
            new_sorted_list.append(sorted_list[-1])
        sorted_list = new_sorted_list
    return sorted_list[0]


def SortH(p, k):
    sorted_list = [list]
    if list is None:
        return

    # ten while na dole dzieli nam wejściowa listę na serie liczb naturalnych - tablica,
    # która trzyma wskaźniki na pierwsze elementy list (juz posortowane elementy, np 2    1 5     4) -> otrzymamy tablicę 3 elementową ze wskazaniem na pierwsze elementy
    while list.next is not None:
        if list.next.val < list.val:
            sorted_list.append(list.next)
            tmp = list.next
            list.next = None
            list = tmp
        else:
            list = list.next

    while len(sorted_list) > 1:  # bo jak będzie długość równa 1, to nie ma czego scalać
        new_sorted_list = []  # tworzymy nową tablicę, która będzie mieć o 1 komórkę mniej - 3 tablicy 3 elementowej po scaleniu będą 2
        for i in range(1, len(sorted_list) - 1, 2):  # co dwa, bo scalamy dwa sąsiednie
            new_sorted_list.append(merge(sorted_list[i - 1], sorted_list[
                i]))  # np range(1,4,2) -> zmergujemy 0 z 1, 3 z 2 i 4 dopiszemy ifem linijkę nizej
        if len(sorted_list % 2 == 1):
            new_sorted_list.append(sorted_list[-1])
        sorted_list = new_sorted_list
    return sorted_list[0]

runtests(SortH)