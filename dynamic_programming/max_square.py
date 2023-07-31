def max_square_of_1s(X, n, m):
    A = [[0 for j in range(m)] for i in range(n)]
    maks = 0
    for i in range(n):
        for j in range(m):
            A[i][j] = X[i][j]
            if i > 0 and j > 0 and X[i][j] == 1:
                A[i][j] = min(A[i-1][j-1], A[i][j-1], A[i-1][j]) + 1
            if maks < A[i][j]:
                maks = A[i][j]
    for i in range(n):
        print(A[i])
    return maks

if __name__ == '__main__':
    T = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    print(max_square_of_1s(T, len(T), len(T[0])))