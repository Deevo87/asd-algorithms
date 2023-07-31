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



def jump(p, i, n):
    licz = 0
    guard = Node()
    guard.next = p
    q = guard
    while p is not None and licz < i:
        q = p
        p = p.next
        licz += 1
    if licz >= n:
        licz = 10000000000
        return p, q, licz
    return p, q #licz


def heigth(p):
    n = 0
    while p is not None:
        p = p.next
        n += 1
    return n


def swap(p, pmin, pmax, qmin, qmax):
    first = Node()
    first.next = p
    pmax_zap = pmax.next
    pmax.next = pmin.next
    printer(p)
    print('PPPPPPPPP')
    qmin.next = pmax

    pmin.next = pmax_zap
    qmax.next = pmin
    return p


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    pminn, qminn = jump(tab1_linked, 0, 7)
    pmaxx, qmaxx= jump(tab1_linked, 6, 7)
    printer(swap(tab1_linked,pminn, pmaxx, qminn, qmaxx))
    print('|| swap')