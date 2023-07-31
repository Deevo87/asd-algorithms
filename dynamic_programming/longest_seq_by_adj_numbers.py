def longest_path(X):
    n = len(X)
    A = [[1 for _ in range(n)] for _ in range(n)]
    maks = 0
    tmp_maks = 0
    for i in range(n):
        for j in range(n):
            if j + 1 < n and X[i][j] - 1 == X[i][j + 1]:
                A[i][j] = A[i][j + 1] + 1
            elif i - 1 >=0 and X[i][j] - 1== X[i - 1][j]:
                A[i][j] = A[i - 1][j] + 1
            elif  j - 1 >= 0 and X[i][j] - 1 == X[i][j-1]:
                A[i][j]= A[i][j - 1] + 1
            elif i + 1 <= 0 and X[i][j] - 1 == X[i+1][j]:
                A[i][j] = A[i+1][j] + 1
            if j + 1 < n and X[i][j] + 1 == X[i][j + 1]:
                tmp_maks = A[i][j + 1] = A[i][j] + 1
            elif i - 1 >= 0 and X[i][j] + 1 == X[i - 1][j]:
                tmp_maks = A[i - 1][j] = A[i][j] + 1
            elif  j - 1 >= 0 and X[i][j] + 1 == X[i][j-1]:
                tmp_maks = A[i][j - 1] = A[i][j] + 1
            elif i + 1 <= 0 and X[i][j] + 1 == X[i+1][j]:
                tmp_maks = A[i+1][j] = A[i][j] + 1
            if maks < tmp_maks:
                maks = tmp_maks
    for i in range(n):
        print(A[i])
    return maks


if __name__ == '__main__':
    mat = [
        [10, 13, 14, 21, 23],
        [11, 9, 22, 2, 3],
        [12, 8, 1, 5, 4],
        [15, 24, 7, 6, 20],
        [16, 17, 18, 19, 25]
    ]

    print(longest_path(mat))