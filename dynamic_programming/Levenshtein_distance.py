def dist(X, Y):
    m = len(X)
    n = len(Y)
    A = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        A[i][0] = i
    for j in range(1, n+1):
        A[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                A[i][j] = A[i-1][j-1]
                cost = 0
            else:
                cost = 1
            A[i][j] = min(A[i-1][j-1] + cost, A[i-1][j] + 1, A[i][j-1] + 1)
    for i in range(m+1):
        print(A[i])
    return A[m][n]


if __name__ == '__main__':
    X = 'kitten'
    Y = 'sitting'

    print('The Levenshtein distance is', dist(X, Y))


