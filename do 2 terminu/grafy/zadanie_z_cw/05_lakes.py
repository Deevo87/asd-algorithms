# Given 2D array [N][N] in which each cell has the value "W" representing water or "L"
# representing land. Lake is a group of water cells connected by their banks. Count how
# many lakes are in array and how many cells has the biggest lake.

def lakes(G):
    n = len(G)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    max_lake = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and G[i][j] == 'W':
                cnt += 1
                max_lake = max(max_lake, dfs_visit(G, visited, i, j, 0))
    return max_lake, cnt

def dfs_visit(G, visited, row, col, size):
    if row < 0 or col < 0 or col >= len(G) or row >= len(G) or G[row][col] == 'L' or visited[row][col] == 1 :
        return size
    visited[row][col] = 1
    size += 1
    actual_size = size
    actual_size = dfs_visit(G, visited, row-1, col, actual_size)
    actual_size = dfs_visit(G, visited, row+1, col, actual_size)
    actual_size = dfs_visit(G, visited, row, col-1, actual_size)
    actual_size = dfs_visit(G, visited, row, col+1, actual_size)
    return actual_size

if __name__ == '__main__':
           #0  #1   #2   #3   #4   #5   #6    #7
    T = [["L", "W", "L", "L", "L", "L", "L", "L"], #0
         ["L", "W", "L", "W", "W", "L", "L", "L"], #1
         ["L", "L", "L", "W", "W", "L", "W", "L"], #2
         ["L", "W", "W", "W", "W", "L", "W", "L"], #3
         ["L", "L", "W", "W", "L", "L", "L", "L"], #4
         ["L", "W", "L", "L", "L", "L", "W", "W"], #5
         ["W", "W", "L", "W", "W", "L", "W", "L"], #6
         ["L", "L", "L", "W", "L", "L", "L", "L"]] #7

    print(lakes(T))