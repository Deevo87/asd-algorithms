
from collections import deque


def to_return(G, D, x):
    for u in G[x]:
        if D[u] == D[x] - 1:
            if u > x:
                return x, u
            return u, x
    return None


def longer(G, s, t):
    n = len(G)
    que = deque()
    V = [False for _ in range(n)]
    D = [0 for _ in range(n)]
    V[s] = True
    que.append(s)
    while que:
        w = que.popleft()
        for u in G[w]:
            if not V[u]:
                V[u] = True
                D[u] = D[w] + 1
                que.append(u)
    que2 = deque()
    que2.append(t)
    tmp = -1
    licz = 0
    if D[t] - 1 == D[s]:
        return s, t
    while que2:
        p = que2.popleft()
        for u in G[p]:
            if u == tmp:
                licz1 = 0
                x = tmp
                for v in G[x]:
                    if D[v] == D[x] - 1:
                        licz1 += 1
                        que2.append(x)
                if licz1 == 1:
                    return to_return(G, D, tmp)
            if D[p] - 1 == D[u]:
                tmp = u
                licz += 1
                que2.append(u)
        if licz == 1:
            licz1 = 0
            x = tmp
            for v in G[x]:
                if D[v] == D[x] - 1:
                    licz1 += 1
                    que2.append(x)
            if licz1 == 1:
                return to_return(G, D, tmp)

G = [[8, 1], [0, 2, 3], [1, 4], [1, 4, 9], [2, 3, 6, 5], [4, 7], [4, 7], [5, 6], [0 ,9], [8, 3]]
print(longer(G, 0, 7))

# zmien all_tests na True zeby uruchomic wszystkie testy

