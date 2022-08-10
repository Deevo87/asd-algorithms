def LBS(X):
    n = len(X)
    A = [0 for _ in range(n)]
    B = [0 for _ in range(n)]
    A[0] = B[0] = 1
    lng = 0
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and A[j] > A[i]:
                A[i] = A[j]
        A[i] += 1
        #print(A)\
    #B[n-1] = 1
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if X[j] < X[i] and B[j] > B[i]:
                #print('chuj')
                B[i] = B[j]
        B[i] += 1
    print(B)
    for i in range(n):
        lng = max(lng, A[i] + B[i] - 1)
    return lng


if __name__ == '__main__':
    T = [4, 2, 5, 9, 7, 6, 10, 3, 1]
    T2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(LBS(T))