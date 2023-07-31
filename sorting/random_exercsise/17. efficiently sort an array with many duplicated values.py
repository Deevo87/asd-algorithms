def counting_sort(A):
    n = len(A)
    k = max(A) + 1
    B = [0]*n
    C = [0]*k
    for x in A:
        C[x] += 1
    print(C)
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]
    return A


if __name__ == '__main__':
    tab = [4, 2, 40, 10, 10, 1, 4, 2, 1, 10, 40]
    print(counting_sort(tab))
