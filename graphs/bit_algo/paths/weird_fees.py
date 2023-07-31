# Public transport in a certain city is quite strangely organized. There is a separate charge for
# each section between two stations. However, the total cost incurred from the start of the journey
# is subtracted from this amount (if it is negative you just pay nothing). We are given a connection
# graph in any representation (undirected, weighted). Find the minimum cost of driving this route.

#SOLUTION
# perform dijkstra with modified dijkstra to save only the highest cost from the cheapest path (relax2)
# or save the current cost by calculating it (relax1)
# both solutions are the same and there is no difference in their time complexity
# time complexity O(ElogV)

from queue import PriorityQueue
from math import inf

def relax1(graph, cost, parent, u, v, dist):
    if cost[v[0]] > cost[u] + max(0, v[1] - dist):
        cost[v[0]] = cost[u] + max(0, v[1] - dist)
        parent[v[0]] = u
        return True
    return False

def relax2(cost, parent, u, v, dist):
    if cost[u] < v[1] < cost[v[0]]:
        cost[v[0]] = v[1]
        parent[v[0]] = u
        return True
    elif v[1] < cost[u] < cost[v[0]]:
        cost[v[0]] = cost[u]
        parent[v[0]] = u
        return True
    return False

def weird_fees(graph, s):
    n = len(graph)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    cost = [inf for _ in range(n)]
    q = PriorityQueue()
    cost[s] = 0
    q.put((0, s))

    while not q.empty():
        dist, u = q.get()
        for v in graph[u]:
            if not visited[v[0]] and relax2(cost, parent, u, v, dist):
                # q.put((dist + max(0, v[1] - dist), v[0]))
                q.put((cost[v[0]], v[0]))
        visited[u] = True
    return cost

if __name__ == '__main__':
    G = [[(1, 60), (3, 120), (4, 40)],
             [(0, 60), (2, 80)],
             [(1, 80), (4, 100), (7, 70)],
             [(0, 120), (6, 150)],
             [(0, 40), (2, 100), (5, 90)],
             [(4, 90), (6, 60)],
             [(3, 150), (5, 60), (7, 90)],
             [(2, 70), (6, 90)]]
    print(weird_fees(G, 0))