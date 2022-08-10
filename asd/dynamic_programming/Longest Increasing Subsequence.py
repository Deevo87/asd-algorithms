def LIF(X): #O(n^2)
    n = len(X)
    A = [0 for _ in range(n)]
    A[0] = 1
    for i in range(1, n):
        for j in range(i):
            if X[j] < X[i] and A[j] > A[i]:
                A[i] = A[j]
        A[i] += 1
    print(A)
    return max(A)

def LIF_2(X):
    n = len(X)
    maxi = 0
    P = [-1 for i in range(n)]
    A = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if X[i] > X[j] and A[j] + 1 > A[i]:
                A[i] = A[j] + 1
                P[i] = j
        if A[i] > A[maxi]:
            maxi = i
    print(P)
    return maxi, A, P,

def printSol(A, P, i):
    if P[i] != -1:
        printSol(A, P, P[i])
    print(A[i])


def binary_search(A, low, high, k):
    #print(A)
    if high >= low:
        mid = (high + low) // 2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            return binary_search(A, low, mid-1, k)
        else:
            return binary_search(A, mid+1, high, k)
    else:
        return low


def LIF_replace(X):
    A = [X[0]]
    n = len(X)
    for i in range(1, n):
        if X[i] > A[len(A)-1]:
            A.append(X[i])
        else:
            ind = binary_search(A, 0, len(A)-1, X[i]) #najmniejszy element większy lub równy X
            print(A)
            print(ind)
            A[ind] = X[i]
    print(A)
    return len(A)


if __name__ == '__main__':
    T = [4, 2, 5, 9, 7, 6, 10, 3, 1]
    T2 = [2, 6, 3, 4, 1, 2, 9, 5, 8]
    print(LIF_2(T))
    i, A, P = LIF_2(T)
    printSol(A, P, i)
