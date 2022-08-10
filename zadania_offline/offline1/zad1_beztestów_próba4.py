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


def SortH(p, k):
    g = Node(None)
    g.next = p
    new_list = Node(None)
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
                print(najm.val, '||najm')
                print(najm_prev.val, '||najm_prev')
            q2 = p2
            print(p2.val, '||p2')
            p2 = p2.next
            cnt -= 1

        # wstawiam od końca
            # odpinam najmniejszy i wpinam do "nowej" listy
            # naprawiam starą liste
        najm_prev.next = najm.next  # w tym miejscu luka w starej liście powinna zniknąć
        printer(g)
        print(' ||actual list')
        najm.next = None
        new_list.next = najm  # wpinam najmniejszą wartość z jednej iteracji do nowej listy
        print(new_list.val, '||newlist')
        print('____')
        new_list = new_list.next  # wskaźnik wskazuje na ostatni element listy


    printer(first)
    print('')
    first = first.next
    return first


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 1, 2, 9, 7, 8, 6]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    printer(SortH(tab1_linked, 3))
