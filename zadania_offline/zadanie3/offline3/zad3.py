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


def SortTab(T,P):
    n = len(T)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[int(T[i])].append(T[i])
    for i in range(n - 1):
        if B[i]:
            insert_sort(B[i])
    j = 0
    for i in range(n):
        for elem in B[i]:
            T[j] = elem
            j += 1
    return T

runtests( SortTab )