def MCMP(n, D):
    C = [[0 for j in range(n+1)] for i in range(n+1)]
    print(C)
    for i in range(n+1):
        C[i][i] = 0
    for l in range(2, n+1): #ilość mnożonych macierzy
        for i in range(1, n-l+2):
            tmp = 100000000
            j = i+l-1
            for k in range(i, j): # żeby sprawdzać wszystkie możliwośći mnożenia
                tmp = min(tmp, C[i][k] + C[k+1][j] + D[i-1]*D[k]*D[j])

            C[i][j] = tmp
            for x in range(1, n + 1):
                print(C[x])
            print('____________________')
    return C[1][n]

if __name__ == '__main__':
    D = [2, 3, 4, 2]
    print(MCMP(3, D))