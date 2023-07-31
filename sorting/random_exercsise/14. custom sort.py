def custom(X): #działa dla nie ujemnych
    maks = max(X)
    n = len(X)
    A = [0 for _ in range(n)]
    B = [[0, _, 0] for _ in range(maks+1)]
    for x in range(n):
        if B[X[x]][0] == 0:
            B[X[x]][2] = x
        B[X[x]][0] += 1
    bg = -1
    bg_ind = -1
    #print(B)
    for i in range(len(B)):
        for j in range(i, len(B)):
            if bg < B[j][0]:
                bg = B[j][0]
                bg_ind = j
            elif bg == B[j][0] and B[bg_ind][2] > B[j][2]:
                #print(B[bg_ind], B[i][2], 'esssssa')
                bg = B[j][0]
                bg_ind = j
            #print(B[bg_ind])
        print(B[bg_ind], bg_ind, B[i], B)
        if bg >= B[i][0]:
            B[i], B[bg_ind] = B[bg_ind] , B[i]
        bg, bg_ind = -1, -1
    i = j = 0
    #print(B)
    while i < n:
        if B[j][0] != 0:
            while B[j][0] != 0:
                A[i] = B[j][1]
                B[j][0] -= 1
                i += 1
        else: break
        j += 1
    return A

if __name__ == '__main__':
    Y = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
    X2 = [5, 8, 4, 0, 9, 5, 1, 4]
    print(custom(X2))
