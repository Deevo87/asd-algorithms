from zad3testy import runtests
from math import log


def insertion_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

def fast_sort(A, a):
    b = 10  # ilość bucketów, wiem bo ile ich jest bo rozkład jest na [0, 1]
    C = [[] for _ in range(b)]
    for x in A:
        C[int(log(x, a)*b)].append(x)
    #print(C)
    for i in C:
        if len(i) != 0:
            insertion_sort(i)
    cnt = 0
    for i in C:
        tmp = len(i)
        ind = 0
        while ind < tmp:
            A[cnt] = i[ind]
            cnt += 1
            ind += 1
    return A

runtests( fast_sort )
