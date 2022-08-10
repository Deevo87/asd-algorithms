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


def swap_last_with_first(p, zero, i):
    printer(p)
    max_p, max_q = jump(p, zero)
    swap_p, swap_q = jump(p, i)
    print(swap_q.val)

    tmp = max_p.next
    max_p.next = swap_p.next
    swap_p.next = tmp
    max_q.next = swap_p
    swap_q.next = max_p



def jump(p, i):
    licz = 0
    g = Node()
    g.next = p
    q = g
    n = length(p)
    if i < n:
        while p is not None and licz < i:
            licz += 1
            q = p
            p = p.next
    else:
        p = None
        q = None
    return p, q



def heapify(p, n, i):
    first = p
    max_p, max_q = jump(p, i)
    max_p_res = max_p
    max_ind, licz_l, licz_p = i, 2 * i + 1, 2 * i + 2
    l_p, l_q = jump(p, licz_l)
    p_p, p_q = jump(p, licz_p)
    if  l_p is not None and licz_l < n and l_p.val > max_p_res.val:
        max_p_res = l_p
        max_ind = licz_l
        swap_p, swap_q = l_p, l_q
    if p_p is not None and licz_p < n and p_p.val > max_p_res.val:
        max_p_res = p_p
        max_ind = licz_p
        swap_p, swap_q = p_p, p_q
    if max_ind != i:
        if max_p == swap_q:
            print(swap_p.val, swap_q.val, max_p.val, max_q.val)
            max_p.next = swap_p.next
            #print(max_p.next.val) git daje 3 --> 9
            swap_p.next = max_p
            #print(swap_p.next.val) git daje 10 --> 3
            max_q.next = swap_p
            print(max_q)
            print(max_p.val)
        else:
            tmp = max_p.next
            max_p.next = swap_p.next
            swap_q.next = max_p

            max_q.next = swap_p
            swap_p.next = tmp
        print("\n", max_ind)
        printer(swap_p)
        print("\n____________________________")
        heapify(p, n, max_ind)
        print("")

def build_heap(p):
    n = length(p)
    g = Node()
    g.next = p
    for i in range((n-1)//2, -1, -1):
        heapify(p, n, i)
    return g

def heap_sort(p):
    n = length(p)
    build_heap(p)
    for i in range(n-1, 0, -1):
        print(i, "swap_i")
        swap_last_with_first(p, 0, i)
        heapify(p, i, 0)
    return p


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    #p,q = jump(tab1_linked, 6)
    #print(p.val)
    #print(length(tab1_linked))
    printer(build_heap(tab1_linked))
    print("\nheapsort")
    #printer(heap_sort(tab1_linked))