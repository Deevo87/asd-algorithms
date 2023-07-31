from collections import deque

class Edge():
    def __init__(self):
        self.v = False  # visited


def rekurE(G, T, v, Q):
    for i in T:
        if not i[1].v:
            i[1].v = True
            rekurE(G, G[i[0]], i[0], Q)
    Q.append(v)


def euler(G):
    for i in G:
        if len(i) % 2 != 0:
            return None
    n = len(G)
    E = [[] for i in range(n)]
    for i in range(n):
        for v in G[i]:
            if v > i:
                edge = Edge()
                E[i] += [(v, edge)]
                E[v] += [(i, edge)]
    Q = deque()
    print(E)
    rekurE(E, E[0], 0, Q)
    W = []
    while Q:
        W.append(Q.pop())
    return W


if __name__ == '__main__':
    edges1 = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5)]
    n = 6
    edges2 = [[2, 3], [2, 3], [0, 1, 3, 4], [0, 1, 2, 5], [2, 5], [3, 4]]
    somsiady = [[]for _ in range(n)]
    for z in range(len(edges1)):
        somsiady[edges1[z][0]].append(edges1[z][1])
        somsiady[edges1[z][1]].append(edges1[z][0])
    #print(somsiady)
    print(euler(edges2))

