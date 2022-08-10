def partition(A, p, r):  # A - tablica, p na początek, r - wskaźnik na piwot
    x = A[r][0]
    i = p - 1  # wskaźnik na najmineszy do zamiany
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


# [[1, 6], [1, 6], [2, 5], [5, 6], [8, 9]]
def depth(L):
    n = len(L)
    quicksort(L, 0, n - 1)
    print(L)
    licz = 0
    i = 1
    j = 0
    maks = 0
    eater = L[0]

    while j != n:
        if L[j] != 0:
            while i != n:
                i_at_the_start = i
                if L[j][1] >= L[i][1]:  # j zjada i
                    licz += 1
                    L[i] = 0
                    i += 1
                elif L[j] != 0 and L[i] != 0 and L[j][1] < L[i][1] and L[j][0] >= L[i][0]:  # i zjada j
                    eater = L[i]
                    L[j] = 0
                    j = i
                    i += 1
                    licz += 1
                else:
                    i += 1
                #if L[j] != 0 and L[i] != 0 and L[j][0] < L[i][0] and L[j][1] < L[i][1]:  # j oraz i są nieporównywalne
                    #NP[push] = L[i]
                    #push += 1
                    #i += 1
            if maks < licz:
                maks = licz
        #print(L, L[j])
        j += 1
    return eater, maks


if __name__ == "__main__":
    # a = [2, 8, 7, 1, 3, 5, 6, 4]
    # n = len(a)
    # print(partition(a, 0, 7))
    # data = [8, 7, 2, 1, 0, 9, 6]
    # size = len(data)
    # print(data)
    # quicksort(data, 0, size - 1)
    # print(data)

    #L = [[1, 6], [5, 6], [2, 5], [8, 20], [1, 6], [8, 15], [1, 8]]
    L = [[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64]]
    print(depth(L))
