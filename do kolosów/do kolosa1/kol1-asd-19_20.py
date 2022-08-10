def swap(A, i, j, n):
    tmp = A[i//n][i%n]
    A[i // n][i % n] = A[j//n][j%n]
    A[j // n][j % n] = tmp

def partition(A, p, r,n):
    i = p - 1
    for j in range(p, r):
        if A[j//n][j%n] <= A[r//n][r%n]:
            i += 1
            #print(A[j // n][j % n], A[r//n][r%n])
            A[j//n][j%n], A[i//n][i%n] = A[i//n][i%n], A[j//n][j%n]
            #print(A)
    A[r//n][r%n], A[(i+1)//n][(i+1)%n] = A[(i+1)//n][(i+1)%n], A[r//n][r%n]
    #print(T,'*************************')
    return i + 1

def select(A, p, k, r, n):
    if p == r:
        return A[p//n][p%n]
    if p < r:
        q = partition(A, p, r, n)
        if q == k:
            return A[q//n][q%n]
        elif q < k:
            return select(A, q+1, k, r, n)
        else:
            return select(A, p, k, q-1, n)

def Median(T):
    n = len(T)
    mid = (n*n)//2
    pp = select(T, 0, mid-(n//2), (n*n)-1, n)
    pk = select(T, 0, mid+(n//2), (n*n)-1, n)
    res = [[0 for _ in range(n)] for _ in range(n)]
    bel = mid+(n//2) + 1
    ab = mid-(n//2) - 1
    p = ab + 1
    for i in range(n*n):
        if T[i//n][i%n] < pp:
            if bel < n*n:
                res[bel//n][bel%n] = T[i//n][i%n]
                bel += 1
        elif T[i//n][i%n] > pk:
            if ab >= 0:
                res[ab//n][ab%n] = T[i//n][i%n]
                ab -= 1
        elif pp <= T[i//n][i%n] <= pk:
            if p < n*n:
                res[p//n][p%n] = T[i//n][i%n]
                p += 1
    T = res
    return res


if __name__ == "__main__":
    T = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
    print(Median(T))
    print(T)