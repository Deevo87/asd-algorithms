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
    return p, q ,licz


def heigth(p):
    n = 0
    while p is not None:
        p = p.next
        n += 1
    return n


def swap(p, pmin, pmax, qmin, qmax):
    pmin_zap = pmin.next
    pmin.next = pmax.next
    qmax.next = pmin
    qmin.next = pmax
    pmax.next = pmin_zap



def heapify(p, n, i):
    g = Node()
    g.next = p
    changed_list = None
    r_i = 2*i + 2
    l_i = 2*i + 1
    p_i, q_i, licz_p = jump(p, i, n)
    r, q_r, licz_r = jump(p, r_i, n)
    l, q_l, licz_l = jump(p, l_i, n)
    max_i = i
    max_p = p_i
    #if l is not None:
        #print(l.val, '||l.val')
    if l is not None and p is not None:
        if licz_l < n and l.val >  p.val:
            q = q_l
            max_i = licz_l
            max_p = l
            print(max_i, " || max_L_i")
        if licz_r < n and  r.val >  p.val:
            q = q_r
            max_i = licz_r
            print(max_i," || max_P_i")
            max_p = p
    if max_i != i:
        swap(p, p_i, max_p, q_i, q)
        print(max_i, " || max_i")
        print(max_p.val, "||max_p")
        print('_____________________________________________')
        heapify(p, n, max_i)
    printer(p)
    print('')
    return p


def heap(p):
    n = heigth(p)
    for x in range((n-1)//2, -1, -1):
        print('dla x =', x, ' || indeks x')
        heapify(p, n, x)
    print('koniec')
    return p


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    #pminn, qminn = jump(tab1_linked, 0, 7)
    #pmaxx, qmaxx= jump(tab1_linked, 6, 7)
    #printer(swap(tab1_linked,pminn, pmaxx, qminn, qmaxx))
    printer(heap(tab1_linked))