from Exercise_1_tests import runtests

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

def chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = T[i], i
    merge_sort(T, 0, n-1)
    maks_jump = 0
    print(T)
    for i in range(n):
        maks_jump = max(maks_jump, abs(i - T[i][1]))
    return maks_jump

runtests(chaos_index)

