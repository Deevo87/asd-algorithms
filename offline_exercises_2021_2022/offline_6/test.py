def BFS(G, s, t):
    n = len(G)
    que = deque()
    V = [False for _ in range(n)]
    D = [0 for _ in range(n)]
    V[s] = True
    que.append(s)
    while que:
        w = que.popleft()
        #print(G[w], 'sssssss')
        for u in G[w]:
            #print(u, 'sss')
            if not V[u]:
                V[u] = True
                #P[u][0], P[u][1] = w, P[w][1] + 1
                D[u] = D[w] + 1
                que.append(u)
    #print(D)
    m = len(D)
    que2 = deque()
    que2.append(t)
    tmp = -1
    licz = 0
    if D[t] - 1 == D[s]:
        return s, t
    while que2:
        p = que2.popleft()
        for u in G[p]:
            print(u, tmp)
            if u == tmp:
                return to_return(G, D, tmp)
            if D[p] - 1 == D[u]:
                tmp = u
                licz += 1
                que2.append(u)
        if licz == 1:
            return to_return(G, D, tmp)
