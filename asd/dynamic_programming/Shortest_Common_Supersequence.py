def LCS(X, Y): # na stringach
    n = len(X)
    m = len(Y)
    A = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[i-1] == Y[j-1]:
                A[i][j] = A[i-1][j-1] + 1
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])

    for i in range(n+1):
        for j in range(m+1):
            print('|' ,A[i][j], end='')
        print('\n')

    return A[n][m]


def SCS(X, Y):
    lcs = LCS(X, Y)
    return len(X) + len(Y) - lcs


if __name__ == '__main__':
    x = 'abcbdab'
    y = 'bdcaba'
    #A = LCS(x, y)
    print(SCS(x, y))
    print(LCS(x, y))