def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1

if __name__ == '__main__':
    tab = [9, -3, 5, -2, -8, -6, 1, 3]
    #quick_sort(tab, 0, len(tab)-1)
    partition(tab, 0, len(tab)-1)
    print(tab)