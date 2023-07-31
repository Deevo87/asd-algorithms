class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


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
    B = B.next
    return B


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.data, end='')
        p = p.next


def linked_list_sort(head):
    if head is None:
        return None
    p = head
    zeros = Node()
    ones = Node()
    second = Node()
    zeros_saver = zeros
    ones_saver = ones
    second_saver = second
    while p is not None:
        if p.data == 0:
            zeros.next = p
            zeros = zeros.next
        elif p.data == 1:
            ones.next = p
            ones = ones.next
        elif p.data == 2:
            second.next = p
            second = second.next
        p = p.next
    printer(ones_saver)
    print('')
    if ones_saver.next is not None:
        print('chuj')
        zeros.next = ones_saver.next
    else:
        zeros.next = second_saver.next
    ones.next = second_saver.next
    second.next = None
    return zeros_saver.next


if __name__ == '__main__':
    tab = [2, 2, 2, 2]
    tab_linked = linked_list_maker(tab)
    printer(tab_linked)
    print('')
    printer(linked_list_sort(tab_linked))
