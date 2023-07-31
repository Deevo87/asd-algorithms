# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby są
# parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak aby
# elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
# podać złożoność czasową i pamięciową zaproponowanego algorytmu.
from zad1_testy import runtests

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def median(T):
    n = len(T)
    N = n*n
    tab = []
    for i in range(n):
        for j in range(n):
            tab.append(T[i][j])
    quick_sort(tab, 0, N-1)
    over_and_under = int((n*n - n) / 2)
    print(over_and_under)
    under = 0
    diagonal = over_and_under
    over = over_and_under + n
    for x in range(n):
        for y in range(n):
            if x == y:
                T[x][y] = tab[diagonal]
                diagonal += 1
            elif y > x:
                T[x][y] = tab[over]
                over += 1
            else:
                T[x][y] = tab[under]
                under += 1
    return T

runtests(median)
