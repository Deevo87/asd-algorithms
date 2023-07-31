from zad2testy import runtests

def merge(T, low, mid, high, pos):
    B = [0 for _ in range(len(T))]
    i = low
    k = low
    j = mid + 1
    while i <= mid and j <= high:
        if T[i][pos] <= T[j][pos]:
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

def merge_sort(T, low, high, pos):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(T, low, mid, pos)
    merge_sort(T, mid + 1, high, pos)
    merge(T, low, mid, high, pos)


#O(n^2)

def depth2(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i], abs(A[i][0] - A[i][1])
    merge_sort(A, 0, n-1, 1)
    maks = 0
    i = 0
    while i < n-1 and n - i > maks:
        j = i + 1
        cnt = 0
        while j < n:
            if A[j][0][0] >= A[i][0][0] and A[j][0][1] <= A[i][0][1]:
                cnt += 1
                maks = max(maks, cnt)
            j += 1
        i += 1

    return maks

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
# if __name__ == '__main__':
#     L = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
#     L2 = [[61, 82], [24, 79], [10, 29], [31, 72], [2, 53], [56, 99], [6, 93], [43, 72], [9, 38], [4, 55], [2, 77], [7, 64], [22, 85], [7, 52], [41, 42], [23, 72], [9, 58], [28, 31], [53, 58], [3, 8], [6, 85], [47, 84], [30, 41], [27, 76], [10, 81], [36, 67], [61, 98], [35, 88], [6, 81], [20, 55], [9, 14], [35, 60], [34, 37], [43, 64], [6, 41], [56, 67], [82, 97], [72, 79], [6, 53], [71, 80], [1, 14], [80, 87], [38, 77], [60, 91], [6, 81], [68, 75], [1, 74], [24, 51], [17, 90], [28, 71]]
#     print(depth2(L2))

