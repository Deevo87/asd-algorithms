def garek (A):
    n = len(A)
    T = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        T[i][i] = A[i]
    for i in range(n):
        print(T[i])
    for i in range(n):
        for j in range(n):
            print('jebać to')
    return 0


if __name__ == '__main__':
    X = [8, 15, 3, 7]
    print(garek(X))