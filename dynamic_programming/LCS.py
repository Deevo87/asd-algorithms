
#LCS nie optymalny
def LCS1(X, Y, m, n):
    if m <= 0 or n <= 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return LCS1(X, Y, m - 1, n - 1) + 1
    else:
        q = max(LCS1(X, Y, m - 1, n), LCS1(X, Y, m, n - 1))
        return q

#LCS programowaniem dynamicznym
def LCS2(X, Y):  # memoization
    m = len(X)
    n = len(Y)

    A = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                A[i][j] = A[i - 1][j - 1] + 1
            else:
                A[i][j] = max(A[i - 1][j], A[i][j - 1])


    for i in range(m+1):
        for j in range(n+1):
            print('|' ,A[i][j], end='')
        print('\n')
    return A[m][n]


#LCS on digits
def LCS_dig(X, Y):
    m = len(X)
    n = len(Y)

    A = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                A[i][j] = A[i - 1][j - 1] + 1
            else:
                A[i][j] = max(A[i - 1][j], A[i][j - 1])
    for i in range(m):
        for j in range(n):
            print('|' ,A[i][j], end='')
        print('\n')

    return A[m-1][n-1]


def LCS_of_kseq(X, Y, Z):
    n = len(X)
    m = len(Y)
    o = len(Z)
    A = [[[0 for _ in range(o+1)] for _ in range(m+1)] for _ in range(n+1)]
    for x in range(1, n+1):
        for y in range(1, m+1):
            for z in range(1, o+1):
                if X[x-1] == Y[y-1] == Z[z-1]:
                    A[x][y][z] = A[x-1][y-1][z-1] + 1
                else:
                    A[x][y][z] = max(A[x-1][y][z], A[x][y-1][z], A[x][y][z-1])
    return A[n][m][o]

#longest repeated subsequence problem
def LCS_repeated(X):
    n = len(X)
    A = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if X[i-1] == X[j-1] and i != j:
                A[i][j] = A[i-1][j-1] + 1
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])

    for i in range(n+1):
        for j in range(n+1):
            print('|' ,A[i][j], end='')
        print('\n')

    return A[n][n]




if __name__ == '__main__':
    #X = [1, 7, 2, 3, 4, 90]
    #Y = [2, 5, 3, 1, 4, 99]
    X = 'abcbdab'
    Y = 'bdcaba'
    Z = 'BADACB'
    print('The length of the LCS is', LCS2(X, Y))
    #print(LCS_repeated(X))
    #print('The length of the LCS is', LCS_dig(X, Y))
    #print('The length of the LCS is', LCS_of_kseq(X, Y, Z))
