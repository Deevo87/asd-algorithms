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
        graph[G[i][1]][G[i][0]] = G[i][2]
    for i in range(wierzch + 1):
        print(graph[i])
    graph_to_copy = []
    graph_to_copy = deepcopy(graph)
    result = 0
    v_to_del = -1
    to_return = 0
    for essa in range(2):
        to_return += result
        for i in range(wierzch, -1, -1):
            graph = deepcopy(graph_to_copy)
            if i != v_to_del and i != s:
                print(result)
                path = bfs(graph, i, s, P)  # i to źródło, s/des to ujście
                print(path)
                result = 0
                while path:
                    print(P)
                    des = s
                    cnt_flow = inf
                    while i != des:
                        if cnt_flow > graph[P[des]][des]:
                            cnt_flow = graph[P[des]][des]
                            v_to_del = i
                        des = P[des]
                    result += cnt_flow
                    x = s
                    while x != i:
                        y = P[x]
                        graph[y][x] -= cnt_flow
                        graph[x][y] += cnt_flow
                        x = P[x]
                    for i in range(wierzch + 1):
                        print(graph[i])
                    print('ssssssssssssssssss')
                    path = bfs(graph, i, s, P)
                cnt_path = 0
                des = s
            print(G[v_to_del], v_to_del)
    return to_return

if __name__ == '__main__':
    X = [(0, 1, 15), (1, 2, 2), (1, 3, 15), (1, 4, 3), (0, 2, 7), (0, 4, 6)]
    X1 = [(0, 1, 12), (0, 2, 10), (0, 3, 12), (1, 4, 8), (2, 4, 2), (2, 5, 2), (3, 5, 8), (4, 6, 10), (4, 7, 2), (5, 7, 2),
     (5, 8, 10), (1, 6, 5)]

    print(max_flow(X1, 0))
