from math import ceil, sqrt, inf
from collections import deque

# kruskal pod zadanie


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return x


def union(parent, rank, x, y):
    # x = find(parent, x)
    # y = find(parent, y)
    # if x == y:
    #     return
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def cycle(G, s, x):
    #print(G)
    n = len(G)
    q = deque()
    visited = [False for i in range(n)]
    P = [-1 for i in range(n)]
    visited[s[0]] = True
    q.append(s)
    maks = s[2]
    maks_wsp = s
    wynik_wsp = x
    while q:
        u = q.popleft()
        for v in range(n):
            if abs(maks) < abs(G[v][2]):
                maks = G[v][2]
                maks_wsp = G[v]
                wynik_wsp = v
            if not visited[G[v][0]]:
                visited[G[v][0]] = True
                P[G[v][0]] = u[0]
                q.append(G[v])
            else:
                #print(wynik_wsp)
                return maks_wsp, wynik_wsp
    return False


def highway(G):
    n = len(G)
    K = []
    wynik = []
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i != j:  # skąd wychodzi, dokąd wchodzi, waga
                K.append([i, j, -ceil(sqrt((G[i][0] - G[j][0]) ** 2 + (G[i][1] - G[j][1]) ** 2))])
   # print(K)
    K.sort(key=lambda tab: tab[2])
    print(K)
    count = 0
    i = 0
    # mi = inf
    # wsp1 = 0
    while count != n-1: #znajduje max spanning tree
        x = K[i][0]
        y = K[i][1]
        i += 1
        if find(parent, x) != find(parent, y):
            #print(K[i])
            union(parent, rank, x, y)
            count += 1
            wynik.append(K[i])
            # if mi > abs(K[i][2]):
            #     mi = abs(K[i][2])
            #     wsp1 = len(wynik) - 1
    wsp2 = len(K) - 1
    to_return = abs(K[len(K)-1][2]) + 1
    print(wynik)
    maks = -1100000
    smallest = abs(min(K, key=lambda z: abs(z[2]))[2])
    #print(smallest)
    while maks != smallest:
        maks = K[len(K)-1][2] - 1
        tmp = min(wynik, key=lambda w: abs(w[2]))
        wsp1, mi = tmp[0], tmp[2]
        for i in range(len(K)): #największa z wszystkich poza wyniku
            if abs(wynik[wsp1][2]) > abs(K[i][2]) and K[i] not in wynik: # tu może być błąd
                if maks < abs(K[i][2]):
                    maks = max(maks, abs(K[i][2]))
                    wsp2 = i
        #print(maks)
        # if maks == smallest:
        #     break
        wynik.append(K[wsp2])
        to_del = cycle(wynik, wynik[wsp1], wsp1)
        #print(wynik)
        if abs(wynik[len(wynik)-1][2] - wynik[0][2]) < to_return:
            to_return = abs(wynik[0][2]) - abs(wynik[len(wynik)-1][2])
        del wynik[to_del[1]]
    return to_return
    # print(parent)
    # print(wynik)
    # print(wynik[len(wynik)-1][2]-wynik[0][2])


    # [[0, 1, 65], [0, 2, 48], [0, 3, 54], [0, 4, 51], [1, 0, 65], [1, 2, 40], [1, 3, 104], [1, 4, 22]]

if __name__ == '__main__':
    X = [(23, 56), (12, 120), (45, 98), (73, 37), (1, 101)]
    X2 = [(10, 10), (15, 25), (20, 20), (30, 40)]
    print(highway(X))
