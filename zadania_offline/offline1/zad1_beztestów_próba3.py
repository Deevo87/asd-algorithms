class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

def linked_list_maker(tab):
    n = len(tab)
    first = None
    for i in range(n-1, -1, -1):
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

def SortH(p, k):
    g = Node(None)
    g.next = p #guardian

    #mam guardiana więc przełączam na q na g
    q = g
    first = p
    while p is not None:
        first = p
        najm = p
        p2 = p
        q2 = q
        licz = k

        #szukam najmniejszej wartości
        while licz - 1 != 0:
            if najm.val > p2.val:
                najm = p2
            licz -= 1
            q2 = p2
            p2 = p2.next

        #wstwiam wskaźnik o najniejszej wartości na początek
        najm_zapasowe = najm

        #wstawiam najm na odpowiednie miejsce (np dla pierwszego rozpatrzenia zamieniam 3 z 0)
        q.next = najm
        najm.next = p.next

        #wstawiam p2 na odpowiednie miejsce
        q2.next = p
        p.next = najm_zapasowe.next

        #przsuwam first na kolejny element z listy, przesuwam q
        q = first
        first = first.next
    return g

if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 1, 2, 9, 7, 8, 6]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    #printer(SortH(tab1_linked, 3))