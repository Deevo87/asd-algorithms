def partition(A, p, r):
    piv = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= piv:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        p = q + 1


def suma(S):
    n = len(S)
    quick_sort(S, 0, n - 1)
    print(S)
    i = 0
    sm = S[0]-1
    j = 1
    for x in range(n):
        while i < n:
            if i != x and j != x and j < n and j != i:
                sm = S[i] + S[j]
            elif i == x:
                i += 1
            if sm == S[x]:
                i = 0
                j = 1
                break
            j += 1
            if j == n:
                i += 1
                j = 0
            if sm > S[x]:
                sm = 0
                i += 1
                j = 0
        if i == n:
            return False
    return True

if __name__ == '__main__':
    tab = [9, 4, -1, 2, -7, 3, -5, 5, -2]
    print(suma(tab))