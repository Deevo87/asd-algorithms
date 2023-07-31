def Knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0], B+1):
        F[0][b] = P[0]
    for i in range(n):
        print(F[i])
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i-1][b], F[i-1][b-W[i]] + P[i])
    for i in range(n):
        print(F[i])
    return F[n-1][B]

if __name__ == '__main__':
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]
    W = 10

    print('Knapsack value is', Knapsack(w, v, W))