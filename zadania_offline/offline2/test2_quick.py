def partition(A, p, r):  # A - tablica, p na początek, r - wskaźnik na piwot
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][0] <= x[0]:
            i += 1
            if A[j][0] == x[0]:
                if A[j][1] > x[1]:
                    A[r], A[j] = A[j], A[r]
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

if __name__ == '__main__':
    tab = [[1,4], [1, 2], [1, 7], [1, 9], [1, 1], [1, 11], [1, 150]]
    n = len(tab)
    quicksort(tab, 0, n-1)
    print(tab)