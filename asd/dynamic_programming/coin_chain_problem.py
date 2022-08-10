def coin_change(M, c):
    n = len(M)
    A = [c for _ in range(c+1)]
    for i in range(n):
        A[M[i]] = 1
    print(A)
    for i in range(1, c+1):
        for j in range(n-1, -1, -1):
            if i - M[j] > 0:
                A[i] = min(A[i], A[M[j]] + A[i-M[j]])
    print(A)
    return A[c]

if __name__ == '__main__':
    S = [1, 7, 10, 11]
    print(coin_change(S, 17))