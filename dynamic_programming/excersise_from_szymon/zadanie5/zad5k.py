from zad5ktesty import runtests

def garek (A):
    n = len(A)
    T = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        T[i][i] = A[i]
    for i in range(n):
        print(A[i])


    return 0

runtests ( garek )