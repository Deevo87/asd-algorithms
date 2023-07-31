from math import sqrt


def dywany(N):
    cost = 0
    m = 0
    while m * m <= N:
        m += 1
    #print(m)
    # M = [i for i in range(1, m+1)]
    P = [0 for _ in range(N+1)]
    A = [0 for _ in range(N + 1)]
    p = 0
    for i in range(1, N + 1):
        A[i] = N
        for j in range(1, m):
            if i - (j * j) >= 0:
                res = A[i - j * j]
                if A[i] > res:
                    A[i] = min(A[i], res + 1)
                    p = i - j*j
        P[i] = p
    ind = len(P)-1
    print(A)
    R = []
    print(P)
    while N - P[ind]*P[ind] >= 0:
        N = N - P[ind] * P[ind]
        ind = N
        R.append(ind)
        print(ind, N)
        if ind == 1:
            R.append(ind)
            break
    return R

def dywany2(N):
    #n = len(N)
    m = 0
    res = 0
    while m * m <= N:
        m += 1
    A = [[0 for _ in range(m)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, m):
            A[i][j] = N
            if i - j*j >= 0:
                res = A[i-j*j][j]
                A[i][j] = min(res+1, A[i][j])
            else:
                A[i][j] = min(A[i][j], A[i][j-1])
    for i in range(N+1):
        print(A[i])
    small = N
    ind = N
    for i in range(1, m):
        if small > A[N][i]:
            small = min(small, A[N][i])
            ind = i

    R = []
    while N > 0:
        if N - ind*ind >= 0:
            R.append(ind)
            val = A[N-ind*ind][ind]
            N = N-ind*ind
            while ind-1 > 0 and A[N][ind-1] == val:
                ind -= 1
            if ind - 1 == 1:
                R.append(ind)
                break
        else:
            break
    print('/////////////////////////')
    print(R)
    return small


if __name__ == '__main__':
    print(dywany(6))
    #print(dywany2(248))
