def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        #quick_sort(A, q + 1, r)
        p = q + 1

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

if __name__ == '__main__':
    tab = [1.962, 1.936, 1.859, 1.743, 1.8, 1.939, 1.775, 1.822, 1.868, 1.903]
    n = len(tab)
    print(select(tab, 0, 3, n-1))
    quick_sort(tab, 0, n-1)
    print(tab)