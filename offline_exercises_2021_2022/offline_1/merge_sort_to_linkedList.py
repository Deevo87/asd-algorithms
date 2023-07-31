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

# funckcja scalająca dwie listy

def merge(first1, first2):
    p1, p2 = first1, first2
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if p1.val <= p2.val:
        new_list = p1
        p1 = p1.next
        new_list.next = None
    else:
        new_list = p2
        p2 = p2.next
        new_list.next = None

    k = new_list
    while p1 is not None and p2 is not None:
        if p1.val <= p2.val:
            k.next = p1
            p1 = p1.next
            k = k.next
            k.next = None
        else:
            k.next = p2
            p2 = p2.next
            k = k.next
            k.next = None
    if p1 is not None:
        k.next = p1
    if p2 is not None:
        k.next = p2
    return new_list


def merge_sort(p):
    sorted_lists = [p]
    if p.next is None:
        return 0
    while p.next is not None:
        if p.next.val < p.val:
            sorted_lists.append(p.next)
            tmp = p.next
            p.next = None
            p = tmp
        else:
            p = p.next
    n = len(sorted_lists)
    while n > 1:
        new_sorted_lists = []
        for i in range(0, n - 1, 2):
            new_sorted_lists.append(merge(sorted_lists[i - 1], sorted_lists[i]))
        if n % 2 == 1:
            new_sorted_lists.append(sorted_lists[-1])
        sorted_lists = new_sorted_lists
    return sorted_lists[0]



if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 10, 2, 9]
    tab2 = [1, 3, 5, 7, 9]
    tab3 = [2, 4, 6, 8, 9]
    tab2_linked, tab3_likned = linked_list_maker(tab2), linked_list_maker(tab3)
    tab1_linked = linked_list_maker(tab1)
    #printer(tab1_linked)
    print('')
    printer(merge(tab2_linked, tab3_likned))
    #Merge_sort(tab1_linked)
    #printer(tab1_linked)
