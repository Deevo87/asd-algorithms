# Given list of people who know each other. People are represented as number between 0 and n-1.
# First day person 0 passes the message to all his friends. Second day each friend passes this
# message to all their friends who doesn't know this message and so on. Find algorithm that
# returns the day when the most people knew the message and the number of people who received it
# that day.
from queue import Queue
def message(G, s):
    n = len(G)
    q = Queue()
    parent = [-1]*n
    D = [-1]*n
    visited = [False]*n
    D[s] = 1
    q.put(s)
    visited[s] = True
    while not q.empty():
        x = q.get()
        for v in G[x]:
            if not visited[v]:
                parent[v] = x
                D[v] = D[x] + 1
                q.put(v)
                visited[v] = True
    cnt = 0
    maks = maks_n = -1
    for i in range(1, n):
        if D[i] == D[i-1]:
            cnt += 1
            if maks < cnt:
                maks = cnt
                maks_n = D[i]
        else:
            cnt = 1
    return maks, maks_n

if __name__ == '__main__':
    graph = [[1, 2], [0, 3, 4], [0, 5, 6], [1, 10], [1, 5, 7, 8, 7, 9, 11],
             [2, 4, 6], [2, 5], [4], [4], [4], [3], [4]]
    print(message(graph, 0))