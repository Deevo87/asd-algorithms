def smallest_cost(X):
    n = len(X)
    m = len(X[0])
    A = [[0 for j in range(m)] for i in range(n)]
    A[0][0] = X[0][0]
    for k in range(n-1):
        A[k+1][0] = A[k][0] + X[k+1][0]
        A[0][k + 1] = A[0][k] + X[0][k + 1]
        #print(A[k][0])
    for i in range(1, n):
        for j in range(1, n):
            A[i][j] = X[i][j] + min(A[i-1][j], A[i][j-1])
    for i in range(n):
        print(A[i])
    return A[n-1][m-1]


def smallest_cost_with_diagonal_move(X):
    n = len(X)
    m = len(X[0])
    A = [[0 for j in range(m)] for i in range(n)]
    A[0][0] = X[0][0]
    for k in range(n - 1):
        A[k + 1][0] = A[k][0] + X[k + 1][0]
        A[0][k + 1] = A[0][k] + X[0][k + 1]
        #print(A[k][0])
    for i in range(1, n):
        for j in range(1, n):
            if i+1 < n:
                A[i][j] = X[i][j] + min(A[i - 1][j], A[i][j - 1], X[i+1][j])
    for i in range(n):
        print(A[i])
    return A[n - 1][m - 1]

if __name__ == '__main__':
    cost = [
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]

    print("The minimum cost is", smallest_cost(cost))
    print("The minimum cost is", smallest_cost_with_diagonal_move(cost))


