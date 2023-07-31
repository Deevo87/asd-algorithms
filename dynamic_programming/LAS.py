def sub_finder(T, X):
    n = len(X)
    if X[n-1][0] > X[n-1][1]:
        flag = True
    else:
        flag = False
    res = [T[n-1]]
    i = n-2
    while i > 1:
        if flag:
            if X[i][0] == X[i - 1][0]:
                while i - 1 >= 0 and X[i][0] == X[i - 1][0]:
                    i -= 1
                print(X[i][0])
                print(res)
        if not flag:
            if X[i][1] == X[i - 1][1]:
                while i - 1 >= 0 and X[i][1] == X[i - 1][1]:
                    i -= 1
            print(X[i][0], 'not flag')
            print(res)
            flag = True
    return T


def LAS(X):
    n = len(X)
    A = [[0 for _ in range(2)] for _ in range(n)]
    A[0][1] = A[0][0] = 1
    for i in range(1, n):
        for j in range(i):
            if X[i] > X[j]:
                A[i][0] = max(A[i][0], A[j][1] + 1)
            if X[i] < X[j]:
                A[i][1] = max(A[i][1], A[j][0] + 1)
    for i in range(n):
        print(A[i][0], A[i][1])
    print(sub_finder(X, A))
    return max(A[n-1][1], A[n-1][0])


if __name__ == '__main__':
    A = [8, 9, 6, 4, 5, 7, 3, 2, 4]
    print('The length of the longest alternating subsequence is', LAS(A))