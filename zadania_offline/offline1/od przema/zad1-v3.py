


def left(p, i):  # indeks p
    for j in range(i):
        p = p.next
    return p.next, 2 * i + 1, p  # przed i element left


def right(p, i):  # indeks p
    for j in range(i + 1):
        p = p.next
    return p.next, 2 * i + 2, p  # przed i element left


def parent(i, A, n):  # indeks p
    for j in range((i - 1) // 2):
        A = A.next
    return A.next, (i - 1) // 2, A


def swap(p, q, mn, qmn):  # q to element przed
    if p == qmn:
        p.next = mn.next
        mn.next = p
        q.next = mn
        return mn
    else:
        tmp = p.next
        p.next = mn.next
        mn.next = tmp
        qmn.next = p
        q.next = mn
        return qmn


def heapify(A, p, q, i, n):  # A - poczatek, p - wskaznik od ktorego mamy naprawiac kopiec, q - poprzedni w liscie do p, i - indeks p, n - długość listy
    mn = (p, i, q)
    # print(mn[0].val,mn[2].val,'  ',mn[1])
    if 2 * i + 1 < n:
        l = left(p, i)
        if mn[0].val > l[0].val:
            mn = l
    if 2 * i + 2 < n:
        r = right(p, i)
        if mn[0].val > r[0].val:
            mn = r
    if mn[0] != p:
        q = swap(p, q, mn[0], mn[2])
        heapify(A, p, q, mn[1], n)
    return i


def p_ost(A, n):
    for i in range(n - 1):
        A = A.next
    return A


def build_heap(A, n):
    T = parent(n - 1, A, n)
    p = T[0]
    q = T[2]
    for i in range(T[1], -1, -1):
        # print("==",p.val,q.val)#
        T = heapify(A, p, q, i, n)
        p = q
        q = p_ost(A, T)


def SortH(a, k):
    A = Node()
    B = Node()
    b = B
    A.next = a
    i = 1
    while i < k + 1 and a.next != None:
        a = a.next
        i += 1
    tmp = a.next
    a.next = None
    a = tmp
    build_heap(A, i)
    while a != None:
        tmp = a.next
        b.next = A.next
        b = b.next
        a.next = A.next.next
        A.next = a
        a = tmp
        heapify(A, A.next, A, 0, i)
    while i > 2:
        b.next = A.next
        b = b.next
        q = p_ost(A, i)
        q.next.next = A.next.next
        A.next = q.next
        q.next = None
        heapify(A, A.next, A, 0, i - 1)
        i -= 1
    b.next = A.next
    return B.next


runtests(SortH)
