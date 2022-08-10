def partition(A, p, r):  # A - tablica, p na początek, r - wskaźnik na piwot
    x = A[r]
    i = p - 1  # wskaźnik na najmineszy do zamiany
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


def depth2(L):
    n = len(L)
    quicksort(L, 0, n - 1)
    k = maks = 0
    p = 0
    while k < n - maks:
        cnt = 0
        while L[p][0] != L[k][0] or p > n - 1:  # to nie chodzi o tego while
            p += 1
        x = p

        while x < n - 1 and L[x + 1][0] == L[k][0]: # tutaj też wszystko działa
            cnt += 1
            x += 1
        k = x  # zaaktualizowane k
        x += 1
        # print(L[k], "**")
        tmp_k = 0
        flag = False
        while x < n:  # to gówno ssie chuja
            if L[k][1] >= L[x][1]:
                cnt += 1
            elif L[k][1] <= L[x][0]:
                break
            elif L[k][1] < L[x][1] and tmp_k == 0: #wstawienie tmp_k do tego elifa nic nie daje generalnie
                # if tmp_k == 0:
                flag = True
                tmp_k = x
                # print("______")
                print(L[k], L[tmp_k])
                # print("______")
            x += 1
        # print("----------")
        if maks < cnt:
            maks = cnt
        if not flag:
            # print(L[tmp_k])
            k += 1  # k się powiększa o jeden czyli np z końca [1, ...] na początek [2, ...]
        else:
            k = tmp_k
    return maks


###
A = [[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64],
     [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76],
     [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41],
     [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74],
     [24, 51], [17, 90], [28, 71]]
print(depth2(A))
# [[1, 14], [1, 74], [2, 53], [2, 77], [3, 8], [4, 55], [6, 41], [6, 53], [6, 81], [6, 81], [6, 85], [6, 93], [7, 52],
# [7, 64], [9, 14], [9, 38], [9, 58], [10, 29], [10, 81], [17, 90], [20, 55], [22, 85], [23, 72], [24, 51], [24, 79],
# [27, 76], [28, 31], [28, 71], [30, 41], [31, 72], [34, 37], [35, 60], [35, 88], [36, 67], [38, 77], [41, 42], [43, 64],
# [43, 72], [47, 84], [53, 58], [56, 67], [56, 99], [60, 91], [61, 82], [61, 98], [68, 75], [71, 80], [72, 79], [80, 87], [82, 97]]
