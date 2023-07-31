# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego
# rozkładu losowego. Ten rozkład mamy zadany jako k przedziałów (a[1], b[1]), (a[2], b[2]), ..., (a[k], b[k])
# takich, że i-ty przedział jest wybierany z prawdopodobieństwem c[i], a liczba z przedziału jest
# wybierana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić, liczby a[i], b[i]
# są liczbami naturalnymi ze zbioru {1, ..., N}. Proszę zaimplementować funkcję SortTab(T,P) sortującą
# podaną tablicę. Pierwszy argument to tablica do posortowania a drugi to opis przedziałów w postaci:
# P = [(a[1], b[1], c[1]), (a[2], b[2], c[2]), ..., (a[k], b[k], c[k])].
# Na przykład dla wejścia:
# P = [(1, 5, 0.75), (4, 8, 0.25)]
# T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
# po wywołaniu SortTab(T, P) tablica T powinna być postaci:
# T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
# Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
# zaproponowanego algorytmu.

from zad3_testy import runtests

def insertion_sort(T):
    n = len(T)
    for j in range(1, n):
        key = T[j]
        i = j - 1
        while i >= 0 and T[i] > key:
            T[i+1] = T[i]
            i -= 1
        T[i+1] = key

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


def SortTab(T, P):
    n = len(T)
    buckets = [[] for _ in range(n)]
    for x in T:
        buckets[int(x)].append(x)
    for i in range(n-1):
        if buckets[i]:
            # insertion_sort(buckets[i])
            merge_sort(buckets[i], 0, len(buckets[i])-1)
    j = 0
    for i in range(n):
        for elem in buckets[i]:
            T[j] = elem
            j += 1
    return T

runtests(SortTab)