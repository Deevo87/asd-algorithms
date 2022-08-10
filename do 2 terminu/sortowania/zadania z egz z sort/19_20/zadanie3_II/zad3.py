from zad3testy import runtests

#to nie jest dobrze zrobione, poprawne rozwiązanie to zrobienie sortowania topoligcznego

def counting_sort(A, k, p):
    n = len(A)
    B = [0]*n
    C = [0]*k
    for x in A:
        C[x[p]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i][p]]-1] = A[i]
        C[A[i][p]] -= 1
    for i in range(n):
        A[i] = B[i]


def tasks(T):
    n = len(T)
    A = [[0, 0, 0] for _ in range(n)]
    for x in range(n):
        A[x][2] = x
        for y in range(n):
            if T[x][y] == 1:
                A[x][0] += 1
            elif T[x][y] == 2:
                A[x][1] += 1
    k = 2*n
    counting_sort(A, k, 1)
    A = A[::-1]
    counting_sort(A, k, 0)
    B = [0 for _ in range(n)]
    for i in range(n):
        B[n-i-1] = A[i][2]
    return B


runtests( tasks )
