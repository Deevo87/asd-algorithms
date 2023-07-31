# Given set of ranges [ai, bi]. Two ranges can be combined if they have exactly one
# common point. Find algorithm that checks if it is possible to get range [a, b] by
# combining ranges together.
def find_range(R, vertexes):
    n = len(R)
    maks = 0
    for i in range(n):
        maks = max(R[i][0], R[i][1], maks)
    G = [[] for _ in range(maks+1)]
    print(maks)
    for i in range(n):
        G[R[i][0]].append(R[i][1])
        G[R[i][1]].append(R[i][0])
    visited = [False]*maks
    return dfs_visit(G, visited, vertexes[0], vertexes[1])

def dfs_visit(G, visited, start, end):
    visited[start] = True
    for x in G[start]:
        if x == end:
            return True
        if not visited[x]:
            return dfs_visit(G, visited, x, end)
    return False

if __name__ == '__main__':
    ranges = [[1, 3], [2, 3], [4, 5], [5, 7], [0, 6], [6, 7], [0, 2], [3, 4], [8, 9]]
    interval = [0, 1]
    ranges2 = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
    interval2 = [1, 6]
    print(find_range(ranges2, interval2))