#Rafał Laskowski
'''
Najpiew sortujemy tablicę X (ma wartości z tablicy T tylko jeszcze rozszerzone o jedną wartość w krotce, mianowicie
indeks z tablicy T), następnie zmodyfikowanym knapsackiem wyliczamy największą możliwą sumę, a na koniec funkcją
path_finder znajduję ścieżkę.
'''
from zad4testy import runtests

def path_finder(A, X, p, T):
    n = len(A)
    i = n - 1
    res_tab = []
    w = p
    j = i - 1
    while i > 0 and w > 0:
        if A[i - 1][w] < A[i][w]:
            res_tab.insert(0, X[i][4])
            w -= X[i][3]
            while j > 0 and X[i][1] <= X[j][2]:
                j -= 1
            i = j
        else:
            i -= 1
    return res_tab



def select_buildings(T, p):
    n = len(T)
    X = [0 for _ in range(n)]
    for i in range(n):
        X[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    X.sort(key=lambda Z: Z[2])
    A = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(X[0][3], p + 1):
        A[0][i] = X[0][0] * (X[0][2] - X[0][1])
    for i in range(1, n):
        field = X[i][0] * (X[i][2] - X[i][1])
        j = i - 1
        for w in range(1, p + 1):
            while j >= 0 and X[i][1] <= X[j][2]:
                j -= 1
            A[i][w] = A[i - 1][w]
            if w - X[i][3] >= 0:
                if X[i][1] > X[j][2] and j > -1:
                    A[i][w] = max(A[i][w], A[j][w - X[i][3]] + field)
                else:
                    A[i][w] = max(field, A[i - 1][w])
    res = path_finder(A, X, p, T)
    return res

runtests( select_buildings )