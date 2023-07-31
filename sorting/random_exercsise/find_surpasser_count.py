# Given an integer array having distinct elements, find the surpasser count for each element in it. In other words,
# for each array element, find the total number of elements to its right, which are greater than it.

def partition(A, p, r):
    x = A[r][0]
    i = p-1
    for j in range(p, r):
        if A[j][0] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def find_surpasser_count(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i], i
    quick_sort(A, 0, n - 1)
    res = [0 for _ in range(n)]
    for j in range(n):
        i = A[j][1]
        if i > j:
            res[i] = n - i - 1
        else:
            res[i] = n - j - 1
    return res

if __name__ == '__main__':
    tab = [4, 6, 3, 9, 7, 10]
    print(find_surpasser_count(tab))