

def MSIS(X):
    n = len(X)
    A = [0 for _ in range(n)]
    #P = [-1 for i in range(n)]
    A[0] = X[0]
    for i in range(1, n):
        suma = X[i]
        for j in range(i):
            if X[j] < X[i] and A[j] > A[i]:#X[i]+X[j] > suma:
                #suma = X[i] + X[j]
                A[i] = A[j]
        A[i] += X[i]
    print(A)
    return max(A)


if __name__ == '__main__':
    nums = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
    print('The maximum sum of the increasing subsequence is', MSIS(nums))
