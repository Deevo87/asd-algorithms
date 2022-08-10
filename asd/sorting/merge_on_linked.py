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
    B = Node(None)
    B.next = first
    return B


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.val, end='')
        p = p.next


def merge(l1, l2):
    head = Node()
    tail = head
    while l1.next is not None and l2.next is not None:
        if l1.next.val <= l2.next.val:
            tail.next = l1.next
            l1.next = l1.next.next
        else:
            tail.next = l2.next
            l2.next = l2.next.next
        tail = tail.next
        tail.next = None
    if l1.next is not None:
        tail.next = l1.next
        l1.next = None
    if l2.next is not None:
        tail.next = l2.next
        l2.next = None
    while tail.next is not None:
        tail = tail.next
    return head, tail


def n_series(l):
    head = Node()
    head.next = l.next
    tail = head.next
    l.next = l.next.next
    while l.next is not None and l.next.val >= tail.val:
        tail.next = l.next
        l.next = l.next.next
        tail = tail.next
    tail.next = None
    return head


def n_m_sort(l):
    head = Node()
    while True:
        n = 0
        tail = head
        while l.next is not None:
            s1 = n_series(l)
            if l.next is None:
                tail.next = s1
            else:
                s2 = n_series(l)
                n += 1
                n_head, n_tail = merge(s1, s2)
                tail.next = n_head.next
                tail = n_tail
            l.next = head.next
            head.next = None
            if n <= 1: return

if __name__ == '__main__':
    # tab1 = [3, 4, 5, 0, 1, 2, 9, 7, 8, 6]
    # tab1_linked = linked_list_maker(tab1)
    # printer(tab1_linked)
    # print('')
    # printer(n_m_sort(tab1_linked))
    # printer(tab1_linked)
    list1 = [1, 3, 5]
    list2 = [2, 6, 7, 10]
    list1_linked = linked_list_maker(list1)
    list2_linked = linked_list_maker(list2)
    printer(list1_linked)
    print('')
    printer(list2_linked)
    print('')
    printer(merge(list1_linked, list2_linked))