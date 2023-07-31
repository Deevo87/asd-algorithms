def minimal_adj(T, t):
    n = len(T)
    M = max(T) # maksymalna wartość z tablicy T
    A = [[0 for _ in range(M+1)] for _ in range(n)] # wszystkie możlwie sumy na wszystkie elementy z T
    for i in range(n):
        A[0][i] = abs(i-T[0])
    #print(A[0])
    for i in range(1, n):
        for j in range(M+1):
            #print(T[i][j])
            A[i][j] = M + 1
            for k in range(max(0, j-t), min(M, j+t) + 1):
                A[i][j] = min(A[i][j], A[i-1][k] + abs(T[i] - j))
    for i in range(n):
        print(A[i])
    return min(A[n-1])


if __name__ == '__main__':
    X = [55, 77, 52, 61, 39, 6, 25, 60, 49, 47]
    X2 = [1, 3, 0, 3]
    X3 = [2, 3, 2, 3]
    target = 10
    print(minimal_adj(X, target))