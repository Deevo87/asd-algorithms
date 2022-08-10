from zad3testy import runtests

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
    B = B.next
    return B


def printer(first):
    p = first
    while p is not None:
        print(' ->', p.val, end='')
        p = p.next

def left_ind(A,i):
    n = len(A)
    parent = n - i - 1
    return n - (2*parent + 2)-1

def right_ind(A,i):
    n = len(A)
    parent = n - i - 1
    return n-(2*parent + 1)-1

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def heapify(A, i):
    n = len(A)
    left = left_ind(A,i)
    right = right_ind(A,i)
    maks_ind = i
    if left >= 0 and A[maks_ind][0].val > A[left][0].val: #max-heap
        maks_ind = left
    if right >= 0 and A[maks_ind][0].val > A[right][0].val:
        maks_ind = right
    if maks_ind != i:
        swap(A, i, maks_ind)
        heapify(A, maks_ind)

def build_heap(A):
    n = len(A)
    for i in range(n-1, -1, -1):
        heapify(A, i)


def merge(listy):
    n = len(listy)
    A = [] #tablica do przechowywania elementów do heapa
    res = Node()
    first = res
    for i in range(n):
        if listy[i] is not None:
            tmp = listy[i].next
            listy[i].next = None
            A.append((listy[i], i))
            listy[i] = tmp
    build_heap(A)
    heapify(A, len(A)-1)
    while len(A) != 0:
        x = A.pop()
        res.next = x[0]
        res = res.next
        if listy[x[1]] is not None:
            tmp = listy[x[1]].next          #
            listy[x[1]].next = None         # tutaj dodaje do heapa i przesuwam odpowiednią linked liste
            A.append((listy[x[1]], x[1]))   #
            listy[x[1]] = tmp               #
        else:
            cnt = x[1]
            flag = True
            while listy[cnt] is None: # szukam listy która nie jest pusta
                cnt += 1
                if cnt >= n:
                    cnt = 0
                elif cnt == x[1]:
                    flag = False
                    break
            if flag: # to oznacza że każda linked list jest już pusta
                tmp = listy[cnt].next
                listy[cnt].next = None
                A.append((listy[cnt], cnt))
                listy[cnt] = tmp
        heapify(A, len(A) - 1)
    return first.next

runtests( merge )
# if __name__ == '__main__':
#     tab = [[0, 1], [10, 20, 30, 40], [25, 27], [35, 45]]
#     tab1 = [0] * len(tab)
#     for j in range(len(tab)):
#         tab1[j] = linked_list_maker(tab[j])
#     printer(merge(tab1))