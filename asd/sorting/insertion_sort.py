def insert_sort(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

if __name__ == '__main__':
    tab = [8, 2, 4, 5, 1, 2, 6, 12]
    insert_sort(tab)
    print(tab)