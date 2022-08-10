''' Przemysław Rola

Funkcja sortowania SortH dzieli się na 3 podfunkcje:
SortB - sortowanie opierajace sie na Bubblesort'cie zamienia jedynie sasiadujace ze soba, co spełnione jest zawsze dla k = 1;
SortI - sortowanie opierajace sie na Insort'cie, wybierajace po kolei elementy z listy i wstawiajacy w posortowana na odleglosci max k od niego, gdyż o tyle moze byc przesuniety wzgledem wlasciwego miejsca;
SortM - sortowanie opierajace sie na Mergesrot'cie, sortuje dwie podlisty i laczac je rekurencyjnie na przestrzeni 2k, nastepnie k z nich mniejszych "oddaje" do wlasciwie posortowanej listy,
    a do drugiej polowy doczepia kolejne k. Jest to spowodowane tym, iz w posortowanym fragmencie 2k, k mniejszych do nastepnego wolnego miejsca ma min. k+1 miejsc,
    co bylo by sprzeczne z zalozeniami k-chaotycznej listy. Wiec k mniejszych elementow jest na dobrym miejscu, i przekazywane sa do posortowanej listy

Druga i trzeci jest wybierany na podstawie wielkosci k

dla k = teta(1) zlozonosc jest O(n)
dla k = teta(log(n)) zlozonosc nk dla n>2*30
dla k = teta(n) zlozonkosc (n/k)*k(log(2k)-1) = nlog(k) dla n>30

'''

from zad1testy import Node, runtests


def insert(A, b):
    q = A.next
    A.next = A.next.next
    while b.next != None:
        if b.next.val < q.val:
            b = b.next
        else:
            break
    q.next = b.next
    b.next = q


def SortI(p, k):
    A = Node()
    A.next = p
    B = Node()
    i = 0
    while A.next != None and i <= k:
        insert(A, B)
        i += 1
    b = B.next
    while A.next != None:
        insert(A, b)
        b = b.next
    return B.next


def Merge_sort(p, n):
    if n == 2:
        if p.val < p.next.val:
            return p, p.next
        q = p.next
        q.next = p
        return q, p
    elif n == 1:
        return p, p
    q = p
    k = ((n + 1) // 2)
    k2 = n // 2
    for i in range(k):
        q = q.next
    p = Merge_sort(p, k)[0]
    q = Merge_sort(q, k2)[0]
    A = Node()
    a = A
    pi, qi = 0, 0
    while pi < k and qi < k2:
        if p.val < q.val:
            a.next = p
            p = p.next
            pi += 1
        else:
            a.next = q
            q = q.next
            qi += 1
        a = a.next
    while qi < k2:
        a.next = q
        q = q.next
        a = a.next
        qi += 1
    while pi < k:
        a.next = p
        p = p.next
        a = a.next
        pi += 1
    return A.next, a


def SortM(p, k):
    n = 2 * k
    i = 0
    A = Node()
    a = A
    f = p
    while p != None:
        i += 1
        p = p.next
        if i == n:
            W = Merge_sort(f, n)
            a.next = W[0]
            W[1].next = p
            for j in range(k):
                a = a.next
            f = a.next
            i = k
    W = Merge_sort(f, i)
    a.next = W[0]
    W[1].next = p
    return A.next


def SortB(p):
    A = Node()
    A.next = p
    a = A
    while a.next != None and a.next.next != None:
        p = a.next
        r = p.next
        if r.val < p.val:
            tmp = r.next
            r.next = p
            p.next = tmp
            a.next = r
            a = r
        else:
            a = a.next
    return A.next


def SortH(p, k):
    if k == 0:
        return p
    if k == 1:
        return SortB(p)
    if k >= 31:
        return SortM(p, k)
    return SortI(p, k)


runtests(SortH)
