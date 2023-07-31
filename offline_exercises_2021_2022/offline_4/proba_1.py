def path_finder2(A, X, p, T):
    n = len(A)
    i = n-1
    res_tab = []
    w = p
    j = i-1
    while i > 0 and w > 0:
        if A[i-1][w] < A[i][w]:
            res_tab.insert(0, X[i][4])
            w -= X[i][3]
            while j > 0 and X[i][1] <= X[j][2]:
                j -= 1
            i = j
        else:
            i -= 1
    print(i, w, X[i][3], A[i][w])
    if i == 0 and A[i][w] > 0:
            res_tab.insert(0, X[i][4])
    return res_tab


def path_finder(A, X, p, T):
    n = len(A)
    res = A[n - 1][p]
    i = n - 1
    res_tab = []
    while i > 0 and p > 0 and (A[i][p - 1] == res or A[i - 1][p] == res) and res != 0:
        if A[i][p - 1] == res and A[i - 1][p] == res:
            i -= 1
        elif A[i][p - 1] == res:
            p -= 1
        elif A[i - 1][p] == res:
            i -= 1
        if i > 0 and p > 0 and A[i][p - 1] != res and A[i - 1][p] != res:
            res_tab.insert(0, X[i][4])
            p = p - X[i][3]
            res = A[i][p]
    if res != 0 and A[i][p - 1] != res and A[i - 1][p] != res:
        res_tab.insert(0, X[i][4])
    return res_tab


def select_buildings(T, p):
    # print(T)
    n = len(T)
    print(T)
    #T.sort(key=lambda Z: Z[2])
    #print(T)
    X = [0 for _ in range(n)]
    for i in range(n):
        X[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    X.sort(key=lambda Z: Z[2])
    print(X)
    #T.sort(key=lambda Z: Z[2])
    #print(T)
    A = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(X[0][3], p + 1):
        A[0][i] = X[0][0] * (X[0][2] - X[0][1])
    for i in range(1, n):
        field = X[i][0] * (X[i][2] - X[i][1])
        j = i - 1
        for w in range(1, p + 1):
            while j >= 0 and X[i][1] <= X[j][2]:
                j -= 1
            A[i][w] = A[i - 1][w]
            if w - X[i][3] >= 0:
                if X[i][1] > X[j][2] and j > -1:
                    A[i][w] = max(A[i][w], A[j][w - X[i][3]] + field)
                else:
                    A[i][w] = max(field, A[i - 1][w])
    for i in range(n):
        print(A[i])
    print('_________________________________________________________________________________________________')
    res = path_finder2(A, X, p, T)
    return res


if __name__ == '__main__':
    X = [(2, 1, 5, 3),
         (2, 8, 11, 1),
         (3, 7, 9, 2)
         ]
    X2 = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
    X3 = [(3, 3, 4, 19),
          (3, 11, 17, 7),
          (4, 8, 15, 15),
          (3, 1, 7, 15),
          (4, 12, 17, 7),
          (3, 1, 7, 3),
          (4, 8, 9, 7),
          (3, 11, 18, 15),
          (4, 20, 31, 19),
          (3, 17, 26, 7), ]
    print(select_buildings(X2, 40))


def save(T, p):
    n = len(T)
    X = [0 for _ in range(n)]
    for i in range(n):
        X[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    X.sort(key=lambda Z: Z[2])
    # for i in range(n):
    # print(T[i], T[i][0] * (T[i][2] - T[i][1]))
    A = [[0 for _ in range(p + 1)] for _ in range(n)]
    for i in range(X[0][3], p + 1):
        A[0][i] = X[0][0] * (X[0][2] - X[0][1])
    for i in range(1, n):
        field = X[i][0] * (X[i][2] - X[i][1])
        j = i - 1
        for w in range(1, p + 1):
            while j >= 0 and X[i][1] <= X[j][2]:
                j -= 1
            A[i][w] = A[i - 1][w]
            if w - X[i][3] >= 0:
                if X[i][1] > X[j][2] and j > -1:
                    A[i][w] = max(A[i][w], A[j][w - X[i][3]] + field)
                else:
                    A[i][w] = max(field, A[i - 1][w])
    return A[n - 1][p]
