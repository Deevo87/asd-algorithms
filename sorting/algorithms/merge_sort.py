def merge(A, B, low, mid, high): # B to tablica pmocnicza
    i = low
    k = low
    j = mid + 1
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
            k += 1
        else:
            B[k] = A[j]
            j += 1
            k += 1
    if i <= mid:
        while i <= mid:
            B[k] = A[i]
            k += 1
            i += 1
    if j <= high:
        while j <= high:
            B[k] = A[j]
            k += 1
            j += 1
    for i in range(low, high+1):
        A[i] = B[i]


def merge_sort(A, B, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(A, B, low, mid)
    merge_sort(A, B, mid + 1, high)
    merge(A, B, low, mid, high)


if __name__ == '__main__':
    tab = [12, 3, 18, 24, 0, 5, -2]
    X = [1, 9, 6, 4, 5]
    tab_zapas = [0 for _ in range(len(X))]
    merge_sort(X, tab_zapas, 0, len(X) - 1)
    print(X)