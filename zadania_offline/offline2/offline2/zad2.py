#Rafał Laskowski
'''
    Funkcja partiton i quicksort odpowiadają za sortowanie tablicy przedziałów względem dwóch wartości.
    W fukcji depth w pierwszy zagnieżdżony while szuka pierwszej wartości w tablicy, która ma taką samą pierwszą
współrzędną jak nasz element "startowy", po to aby w drugim whilu bez porównywania zliczyć ilość przedziałów o takiej
samej pierwszej współrzędnej i dojść do przedziału z najwyższą drugą współrzędną (np. zaczynamy od [6,41], ... [6,93]
i kończymy na [6, 93]). Trzeci zagnieżdżony while odpowiada za zliczanie przedziałów zawierających się w naszym przedziale
porównawczym. Zmienna flag jest zmieniana na True, wtedy gdy natrafimy na pierwszy element, który jest nieporónywalny
z naszym porównawczym (np, [6,93] i [56, 99]), wtedy też zaczynamy następną iterację od przedziału wcześniej nieporónywalnego.

    Złożoność tego algorytmu to dobrze zoptymalizowane O(n^2)
'''




from zad2testy import runtests


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][0] < x[0]:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j][0] == x[0] and A[j][1] < x[1]:
            i += 1
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
    quicksort(L, 0, n - 1)
    k = maks = 0
    p = 0
    while k < n - maks:
        cnt = 0
        while L[p][0] != L[k][0] or p > n-1:
            p += 1
        x = p
        while x < n-1 and L[x + 1][0] == L[k][0]:
            cnt += 1
            x += 1
        k = x
        x += 1
        tmp_k = 0
        flag = False
        while x < n:
            if L[k][1] >= L[x][1]:
                cnt += 1
            elif L[k][1] <= L[x][0]:
                break
            elif L[k][1] < L[x][1]:
                if tmp_k == 0:
                    flag = True
                    tmp_k = x
            x += 1
        if maks < cnt:
            maks = cnt
        if not flag:
            k += 1
        else:
            k = tmp_k
    return maks



runtests(depth)
