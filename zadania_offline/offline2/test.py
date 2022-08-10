from random import randint

def partition(A, p, r):  # A - tablica, p na początek, r - wskaźnik na piwot
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x[0]:
            i += 1
            if A[j][0] == x[0]:
                if A[j][1] > x[1]:
                    A[r], A[j] = A[j], A[r]
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def depth(L):
    n = len(L)
    quicksort(L, 0, n-1)
    k = maks = 0
    while k < n:
        x = k
        tmp = L[k]
        cnt = 0
        while x < n-1:
            if L[x+1][0] == L[x][0] and L[k][1] >= L[x+1][1]:
                cnt += 1
                x += 1
            else:
                if L[k] == tmp:
                    k = x
                    tmp = [-1, -1]
                x += 1
                if L[k][1] >= L[x][1]:
                    cnt += 1
                    print(L[k], L[x],cnt)
                if L[k][1] < L[x][0]:
                    break
        if maks < cnt:
            maks = cnt
        k += 1
    return maks