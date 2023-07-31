# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

def partition(T, p, r):
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def select(A, p, k, r):
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, q + 1, k, r)
        else:
            return select(A, p, k ,q - 1)

def section(T, p, q):
    n = len(T)
    res = []
    for i in range(p, q+1):
        res.append(select(T, 0, i, n-1))
    return res

if __name__ == '__main__':
    tab = [10, 15, 34, 80, 97, 15, 24, 34, 11, 8, 2, 3]
    print(section(tab, 5, 8))
    tab.sort()
    print(tab)