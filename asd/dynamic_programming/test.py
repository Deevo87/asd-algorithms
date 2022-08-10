def isKPalindrome(s, k):
    m = s[::-1]
    x = len(m)
    T = [[0 for _ in range(x + 1)] for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, x + 1):
            if s[i - 1] == m[j - 1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i - 1][j] + 1, T[i][j - 1] + 1)
    for i in range(x + 1):
        print(T[i])
    return x - T[x][x] <= k


if __name__ == '__main__':
    A = 'ADCB'
    print(isKPalindrome(A, 2))
