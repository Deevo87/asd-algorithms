def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q+1

def zad8(A, k):
    n = len(A)
    quick_sort(A, 0, n-1)
    i = 0
    j = 1
    cnt = 0
    while i < j < n:
        if A[j] - A[i] == k:
            cnt += 1
            j += 1
            while j < n and A[j] == A[j - 1]:
                j += 1
        elif A[j] - A[i] < k:
            j += 1
            while j < n and A[j] == A[j-1]:
                j += 1
        elif A[j] - A[i] > k:
            i += 1
            while i-1 >= 0 and A[i] == A[i - 1]:
                i += 1
    return cnt

if __name__ == '__main__':
    tab = [7, 11, 3, 5, 9, 7]
    print(zad8(tab, 4))

