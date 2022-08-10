def get_list(A):
    while A.next != None and A.val <= A.next.val:
        A = A.next
    p = A.next
    A.next = None
    return p


def last(A):
    while A.next != None:
        A = A.next
    return A


def Merge1(A, B):
    C = Node()
    c = C
    while A != None and B != None:
        if A.val < B.val:
            c.next = A
            A = A.next
        else:
            c.next = B
            B = B.next
        c = c.next
    if A == None:
        c.next = B
        return (C.next, last(B))
    c.next = A
    return (C.next, last(A))


def Merge_sort(L):
    T = last(L)
    while True:
        A = L
        L = get_list(L)
        if L == None:
            return (A, T)
        B = L
        L = get_list(L)
        C, D = Merge1(A, B)
        if L == None:
            return (C, D)
        T.next = C
        T = D
