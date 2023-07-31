from zad3testy import runtests

""" prosze nie plagiat pls, własnymi rękami wsadzałem te liczby do kubłów"""

def insert_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


def merge(T, low, mid, high):
    B = [0 for _ in range(len(T))]
    i = low
    k = low
    j = mid + 1
    while i <= mid and j <= high:
        if T[i] <= T[j]:
            B[k] = T[i]
            i += 1
            k += 1
        else:
            B[k] = T[j]
            j += 1
            k += 1
    while i <= mid:
        B[k] = T[i]
        i += 1
        k += 1

    while j <= high:
        B[k] = T[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        T[i] = B[i]

def merge_sort(T, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(T, low, mid)
    merge_sort(T, mid + 1, high)
    merge(T, low, mid, high)

def SortTab(T,P):
    n = len(T)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[int(T[i])].append(T[i])
    for i in range(n - 1):
        if B[i]:
            insert_sort(B[i])
            # merge_sort(B[i], 0, len(B[i])-1)
    j = 0
    for i in range(n):
        for elem in B[i]:
            T[j] = elem
            j += 1
    return T

runtests( SortTab )