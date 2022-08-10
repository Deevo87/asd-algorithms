class Node:
    def __init__(self, data=None):
        self.data = data
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
    return B.next


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.data, end='')
        p = p.next


def merge_linked(i, j):
    head_merged = Node()
    head_merged_saver = head_merged
    #printer(j)
    if i is None:
        return j
    if j is None:
        return i
    while i is not None and j is not None:
        if i.data <= j.data:
            head_merged.next = i
            i = i.next
        else:
            head_merged.next = j
            j = j.next
        head_merged = head_merged.next
    while i is not None:
        head_merged.next = i
        head_merged = head_merged.next
        i = i.next
    while j is not None:
        head_merged.next = j
        head_merged = head_merged.next
        j = j.next
    #printer(head_merged.next
    return reverse_linked_list(head_merged_saver.next)

def reverse_linked_list(head):
    if head is None:
        return None
    p = head
    q = p # tail
    tmp = p.next
    p.next = None
    p = tmp
    while p is not None:
        tmp = p.next
        p.next = q
        q = p
        p = tmp
    return q


if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6]
    list1_linked = linked_list_maker(list1)
    list2_linked = linked_list_maker(list2)
    printer(list1_linked)
    print('')
    printer(list2_linked)
    print('')
    printer(merge_linked(list1_linked, list2_linked))