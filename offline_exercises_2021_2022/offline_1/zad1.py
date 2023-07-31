#Rafał Laskowski

'''
    Algorymt sortuje liste k-chaotyczną poprzez wybieranie
    z n k elementów i wybieranie z k najmniejszego elemnetu
    potem wstawia go na koniec nowej linked listy, następnie przesuwa
    k o jeden indeks do przodu i powtarza tą czynność, aż nieposortuje
    całej listy.

    Pierwsza pętla while służy do przesuwania elemntów w nieposortowanej linked lisćie
    natomiast druga do szukania najmniejszej wartości, po wyjściu z drugiej pętli while
    następuje wstawianie do już nowej linked listy, która będzie posortowana.
    Złożoność cłego algortymu to nk bo dla każdego elementu szukam najmiejszej wartości w odległości k

    dla k = Θ(1) złożonść to O(n),
    dla k = Θ(log n) złożonść to O(nlogn),
    dla k = Θ(n) złożoność to O(n^2)
'''

from zad1testy import Node, runtests



def SortH(p, k):
    g = Node()
    g.next = p
    new_list = Node()
    first = new_list
    q = g
    while g.next is not None:
        najm = g.next
        p2 = g.next
        q2 = q
        cnt = k + 1
        while cnt != 0 and p2 is not None:
            if najm.val >= p2.val:
                najm_prev = q2
                najm = p2
            q2 = p2
            p2 = p2.next
            cnt -= 1

        najm_prev.next = najm.next
        najm.next = None
        new_list.next = najm
        new_list = new_list.next
    first = first.next
    return first


runtests(SortH)
