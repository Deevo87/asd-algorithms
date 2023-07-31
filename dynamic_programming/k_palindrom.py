def isKPalindrome(s, k): #przy pomocy LCS-a
    m = s[::-1]
    x = len(m)
    T = [[0 for _ in range(x + 1)] for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if s[i - 1] == m[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    for i in range(x + 1):
        print(T[i])
    return x - T[x][x] <= k


def isKPalindrome2(X, K): # przy pomocy levenstien's distance
    # 'Y' is a reverse of 'X'
    Y = X[::-1]

    n = len(X)

    # lookup table to store solution of already computed subproblems
    T = [[0 for x in range(n + 1)] for y in range((n + 1))]

    # fill the lookup table `T[][]` in a bottom-up manner
    for i in range(n + 1):
        for j in range(n + 1):
            # if either string is empty, remove all characters from the
            # other string
            if i == 0 or j == 0:
                T[i][j] = i + j

            # ignore the last characters of both strings if they are the same
            # and process the remaining characters
            elif X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1]

            # if the last character of both strings is different, consider
            # minimum by removing the last character from 'X' and 'Y'
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1])

    return T[n][n] <= 2 * k


if __name__ == '__main__':
    A = 'ADCB'
    print(isKPalindrome(A, 2))

