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

def length(p):
    licz = 0
    #printer(p)
    #print("\n length list")
    while p is not None:
        licz += 1
        p = p.next
    return licz

def jump(p, i):
    licz = 0
    g = Node()
    g.next = p
    first = p
    q = g
    n = length(p)
    if i < n:
        while p is not None and licz < i:
            licz += 1
            p = p.next
    end = p
    p.next = None
    return first, end

'SCALANIE DWÓCH POSORTOWANYCH LINKED LIST'

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
        if len(sorted_list) % 2 == 1:
            new_sorted_list.append(sorted_list[-1])
        sorted_list = new_sorted_list
    return sorted_list[0]





def SortH(p, k):
    g = Node()
    g.next = p
    sorted_list = Node()
    first = p
    while p is not None:
        ind = 0
        p_big = p
        while ind != 2*k + 1 and p is not None: # +1 bo wtedy lista ma odpowiednią długość (mieści realnie 2 k-chaotyczne przejścia)
            p = p.next
            ind += 1
        #end_big = p
        p_save = p.next
        p.next = None # rozłączam listę żeby merge mi ładnie ją posortował
        MergeSort(p_big)
        p.next = p_save # łącze żeby móc dalej sortować
        ind = 0
        p1 = p_big # początek posortowanej części listy z elementami na swoim miejscu
        while ind != k:
            p_big = p_big.next
            ind += 1
        end1 = p_big # koniec posortowanej części listy z elementami na swoim miejscu
        p = end1.next
        p_big.next = None
        sorted_list.next = p1






if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab2 = [1, 3, 5, 7, 9]
    tab3 = [2, 4, 6, 8, 9]
    tab2_linked, tab3_likned = linked_list_maker(tab2), linked_list_maker(tab3)
    tab1_linked = linked_list_maker(tab1)
    #printer(tab1_linked)
    print('')
    printer(merge(tab2_linked, tab3_likned))
    #printer(MergeSort(tab1_linked))