from queue import Queue
from math import inf
from copy import deepcopy


def bfs(G, s, des, P):  # s to źródło, des to ujście
    n = len(G)
    V = [False for _ in range(n)]
    q = Queue()
    q.put(s)
    V[s] = True
    while not q.empty():
        u = q.get()
        for v in range(n):
            if not V[v] and G[u][v] > 0:
                V[v] = True
                P[v] = u
                q.put(v)
                if v == des:
                    # print(P)
                    return True
    return False


def max_flow(G, s):
    # zamiana na macierz
    wierzch = max(G, key=lambda k: k[1])[1]
    # print(wierzch)
    P = [-1 for _ in range(wierzch + 1)]
    graph = [[0 for _ in range(wierzch + 1)] for _ in range(wierzch + 1)]  # krawędzie są w drugą stronę
    for i in range(len(G)):
        graph[G[i][0]][G[i][1]] = G[i][2]
    for i in range(wierzch + 1):
        print(graph[i])
    graph_to_copy = []
    graph_to_copy = deepcopy(graph)
    result = 0
    v_to_del = -1
    to_return = 0
    i = 4
    path = bfs(graph, s, i, P) # s to źródło, i to ujście
    while path:
        print(P, '____________')
        des = i
        cnt_flow = inf
        while des != s:
            print('sss')
            cnt_flow = min(cnt_flow, graph[P[des]][des])
            # if cnt_flow > graph[P[des]][des]:
            #     cnt_flow = graph[P[des]][des]
            #     v_to_del = i
            des = P[des]
        result += cnt_flow
        x = i
        print(x, i)
        while x != s:
            print('xssx')
            y = P[x]
            graph[y][x] -= cnt_flow
            graph[x][y] += cnt_flow
            x = P[x]
        path = bfs(graph, i, s, P)
    return result


if __name__ == '__main__':
    X = [(0, 1, 7), (0, 3, 3), (1, 3, 4), (1, 4, 6), (2, 0, 9), (2, 3, 7), (2, 5, 9),
         (3, 4, 9), (3, 6, 2), (5, 3, 3), (5, 6, 4), (6, 4, 8)]
    print(max_flow(X, 2))
