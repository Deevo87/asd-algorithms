
def DFSvisit(G, u, visited, parent, times):
    visited[u] = True
    
    for i in range(len(G)):
        if visited[i] == False and G[u][i] != 0:
            parent[i] = u
            times[i] = times[u] + 1
            DFSvisit(G, i, visited, parent, times)


def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    times = [-1 for _ in range(n)]
    times[0] = 0
    
    for i in range(n):
        if visited[i] == False:
            DFSvisit(G, i, visited, parent, times)

    return visited, times
    

def s_connected(G):
    n = len(G)
    visited, times = DFS(G)
    graph_copy = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                graph_copy[j][i] = 1
    
   
    visited_array = [(times[i], i) for i in range(n)]
    parent = [None for _ in range(n)]
    
    visited_array = sorted(visited_array, key=lambda x: x[0])
    
    stack = [x[1] for x in visited_array]
    times = [-1 for _ in range(n)]
    visited_new = [False for _ in range(n)]    
        
    for i in stack:
        if visited_new[i] == False:   
            times[i] = 0
            DFSvisit(graph_copy, i, visited_new, parent, times)
    
    print(times, visited_new)            
        

#     a  b  c  d  e  f  g  h  i  j  k
G = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # a
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # b
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # c
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # d
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # e
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # f
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # g
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # h
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # i
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # j
     [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]  # k


s_connected(G)