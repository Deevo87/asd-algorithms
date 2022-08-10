class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def linked_list_maker(tab): #bez wartownika
    n = len(tab)
    first = None
    for i in range(n - 1, -1, -1):
        new_node = Node(tab[i])
        p = new_node
        p.next = first
        first = p
    B = first
    return B


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.data, end='')
        p = p.next
    print('')


def lenght(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count


def split_in_half(head):
    if head is None or head.next is None:
        return head, None
    slow, fast = head, head.next #fast skacze co dwa nody, slow co jeden, w taki sposób slow jest idealnie
                                #przed połową albo równo w niej
    while fast is not None:
        fast = fast.next
        if fast is not None:
            slow = slow.next
            fast = fast.next
    to_return = head, slow.next
    slow.next = None
    return  to_return #slow.next to mid + 1, a head to początek listy

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
    #printer(head_merged.next)
    return head_merged_saver.next


def merge_sort_linekd(head):
    if head is None or head.next is None:
        return head
    front, back = split_in_half(head)
    front = merge_sort_linekd(front)
    back = merge_sort_linekd(back)
    return merge_linked(front, back)




if __name__ == '__main__':
    tab = [-1, 3, 4, 8, 2, 9]
    tab_linked = linked_list_maker(tab)
    printer(tab_linked)
    printer(merge_sort_linekd(tab_linked))