def Knapsack(X, k, w):
    n = len(X)
    A = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(k+1):
            if w[i-1] > j:
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = max(A[i-1][j], A[i-1][j - w[i-1]] + X[i-1])
    for i in range(n+1):
        print(A[i])
    return A[n][k]


if __name__ == '__main__':
    # input: a set of items, each with a weight and a value
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]

    # knapsack capacity
    W = 10

    print('Knapsack value is', Knapsack(v, W, w))