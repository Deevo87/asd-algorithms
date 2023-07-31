
from math import sqrt, ceil


def length(a, b):
    x = (a[0] - b[0])
    y = (a[1] - b[1])
    return ceil(sqrt(x * x + y * y))


def highway(A):
    def find_parent(x):
        nonlocal parent
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x, y):
        nonlocal parent, count, n
        x = find_parent(x)
        y = find_parent(y)
        if x == y:
            return False
        if count[x] > count[y]:
            x, y = y, x
        parent[x] = y
        count[y] += count[x]
        if count[y] == n:
            return True
        # x = find_parent(x)
        # y = find_parent(y)
        # if x == y:
        #     return False
        # if count[x] > count[y]:
        #     parent[y] = x
        #     count[x] += count[y]
        # else:
        #     parent[x] = y
        #     if count[x] == count[y]:
        #         count[y] = count[x]

    def reset_tab():
        nonlocal parent, count, n
        parent = [k for k in range(n)]
        count = [1] * n

    n = len(A)
    E = []
    for i in range(n):
        for j in range(i + 1, n):
            E.append((length(A[i], A[j]), i, j))

    E.sort()
    print(E)
    m = len(E)
    minInd = 0
    maxInd = m - 1
    solution = E[maxInd][0] - E[minInd][0]
    parent = [j for j in range(n)]
    count = [1] * n

    while True:
        reset_tab()
        i = minInd
        while i < m:
            _, x, y = E[i]
            if union(x, y):
                solution = min(solution, E[i][0] - E[minInd][0])
                maxInd = i
                break
            i += 1
        else:
            break
        print(solution)
        i = maxInd
        reset_tab()
        while i >= 0:
            _, x, y = E[i]
            if union(x, y):
                solution = min(solution, E[maxInd][0] - E[i][0])
                minInd = i + 1
                break
            i -= 1
    return solution

if __name__ == '__main__':
    X = [(23, 56), (12, 120), (45, 98), (73, 37), (1, 101)]
    X2 = [(10, 10), (15, 25), (20, 20), (30, 40)]
    print(highway(X))
