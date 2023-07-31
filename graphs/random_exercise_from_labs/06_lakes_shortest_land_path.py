# Given 2D array [N][N] in which each cell has the value "W" representing water or "L"
# representing land. Lake is a group of water cells connected by their banks. Assuming
# that array[0][0] and array[n-1][n-1] are land. Check if it is possible to go from
# [0][0] to [n-1][n-1] by land. You can only walk sideways not diagonally. Also find
# the shortest path between this cells.
from queue import Queue
from math import inf


def lake_bfs(G, row, col):
    n = len(G)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    shortest = inf
    q = Queue()
    q.put((row, col))
    while not q.empty():
        x, y = q.get()
        #nawet kurwa nie wiem co tu się dzieje ja pierdole
    return False, shortest

if __name__ == '__main__':
    T = [["L", "W", "L", "L", "L", "L", "L", "L"],
         ["L", "W", "L", "W", "W", "L", "L", "L"],
         ["L", "L", "L", "W", "W", "L", "W", "L"],
         ["L", "W", "W", "W", "W", "L", "W", "L"],
         ["L", "L", "W", "W", "L", "L", "L", "L"],
         ["L", "W", "L", "L", "L", "W", "W", "W"],
         ["W", "W", "L", "W", "L", "L", "W", "L"],
         ["L", "L", "L", "L", "L", "L", "L", "L"]]

    verdict, distance = lake_bfs(T, 0, 0)
    print(verdict, distance)