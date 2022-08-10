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
    B = Node(None)
    B.next = first
    return B

def printer(first):
    p = first
    while p is not None:
        print(' ->', p.val, end='')
        p = p.next

def SortH(p, k):
    first = None
    q = p
    while p is not None:
        p_tmp = p
        k_tmp = k
        q_tmp = p
        index = 0
        while k != 0:
            q_tmp = p_tmp
            p_tmp = p.next
            index += 1
            k_tmp -= 1
        if p.val == p_tmp.val - k and index != p.val:
            # tutaj musze poprzepinać
                p_tmp_rem = p_tmp
                q.next = p_tmp
                p_tmp.next = p.next
                q_tmp.next = p
                p.next = p_tmp_rem.next
        #tutaj powinien być elif z odejmowaniem
        q = p
        p = p.next

