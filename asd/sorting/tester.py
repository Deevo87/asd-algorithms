def partition(A, p, r):
    piv = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= piv:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1

def q_select(A, p, k, r):
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if k == q:
            return A[q]
        elif k < q:
            return q_select(A, p, k, q-1)
        else:
            return q_select(A, q+1, k, r)

#merge_sort

def merge(A, B, low, mid, high):
    i = low
    k = low
    j = mid + 1
    while i <= mid and j <= high:
        if A[i] > A[j]:
            B[k] = A[i]
            i += 1
            k += 1
        else:
            B[k] = A[j]
            j += 1
            k += 1
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= high:
        B[k] = A[j]
        j += 1
        k += 1
    for i in range(len(A)):
        A[i] = B[i]


def merge_sort(A, low, high):
    B = [0 for _ in range(len(A))]
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(A, low, mid)
    merge_sort(A, mid+1, high)
    merge(A, B, low, mid, high)



if __name__ == '__main__':
    tab = [1.962, 1.936, 1.859, 1.743, 1.8, 1.939, 1.775, 1.822, 1.868, 1.903]
    n = len(tab)
    print(q_select(tab, 0, 3, n-1))
    quick_sort(tab, 0, n-1)
    print(tab)