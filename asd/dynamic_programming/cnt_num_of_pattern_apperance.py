def count_patterns(S, pattern):
    n = len(S)
    m = len(pattern)
    A = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(n+1):
        A[0][i] = 1
    for i in range(m+1):
        print(A[i])
    print('????????????????')
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[j-1] == pattern[i-1]:
                A[i][j] = A[i-1][j] + A[i][j-1]
            else:
                A[i][j] = A[i][j-1]
    for i in range(m + 1):
        print(A[i])
    return A[m][n]


if __name__ == '__main__':
    X = 'subsequence'  # Input string
    Y = 'sue'  # Pattern

    print(count_patterns(X, Y))