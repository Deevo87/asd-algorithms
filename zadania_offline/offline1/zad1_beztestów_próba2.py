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
    guardian = Node(None)
    guardian.next = first
    return guardian

def printer(first):
    p = first
    while p is not None:
        print(' ->', p.val, end='')
        p = p.next

def SortH(p, k):
    to_return = p
    first = p.next
    q = p
    while first is not None:
        p = first #to jest git
        p_tmp = p #to jest git
        q_tmp = q #to jest git
        cnt = k #to jest git
        smls = p

        #szukam najmniejszej wartości w odległości max 3 (łącznie 4 elementy)
        while cnt +1 != 0 and p_tmp is not None:
            if smls.val > p_tmp.val:
                smls = p_tmp
            cnt -= 1
            if cnt != -1:
                q_tmp = p_tmp
                p_tmp = p_tmp.next
            #if p_tmp is not None:
                #print(p_tmp.val, "p_tmp", cnt)
        #print("real smallest:", smls.val)

        #przeminam najmniejszą wartość ze stojącą na samym przodzie (smls od smallest i smlst_res od reserve)
        smls_res = p_tmp
        q.next = smls
        smls.next = p.next
        q_tmp.next = p
        if smls_res is not None:
            p.next = smls_res.next
            #print(smls_res.next.val)
        else:
            p.next = smls_res
        #print(smls.val)

        #przesuwam "wskaźnik"
        q = first
        #print(first.val, "first")
        first = first.next
    return to_return


if __name__ == '__main__':
    tab1 = [3, 4, 5, 0, 1, 2, 9, 7, 8, 6]
    tab1_linked = linked_list_maker(tab1)
    printer(tab1_linked)
    print('')
    printer(SortH(tab1_linked, 3))
