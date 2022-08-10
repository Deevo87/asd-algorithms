#nie działa

class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None


def linked_list_maker(tab):
    n = len(tab)
    first = None
    for i in range(n - 1, -1, -1):
        new_node = Node(tab[i])
        p = new_node
        p.next = first
        first = p
    return first


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.val, end='')
        p = p.next




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

def MergeSort(L): #L wskaznik do linked listy
    heads = []
    heads.append(L)
    if L.next is None:
        return L
    curr = L.next
    while curr is not None:
        if curr.val >= L.val:
            L = L.next
            curr = curr.next
        else:
            heads.append(curr.val)
            L.next = None
            L = curr
            curr = curr.next
# Tutaj kompletujemy tablice wskaznikow na poczatek serii naturalnych
    while len(heads) > 1:
        heads2 = []
        while len(heads) > 1:
            merged = merge(heads[0], heads[1])
            heads2.append(merged)
            heads = heads[2:]
            heads2.extend(heads)
            heads = heads2
    return heads[0]


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab2 = [1, 3, 5, 7, 9]
    tab3 = [2, 4, 6, 8, 9]
    tab2_linked, tab3_likned = linked_list_maker(tab2), linked_list_maker(tab3)
    tab1_linked = linked_list_maker(tab1)
    #printer(tab1_linked)
    print('')
    #printer(merge(tab2_linked, tab3_likned))
    printer(MergeSort(tab1_linked))