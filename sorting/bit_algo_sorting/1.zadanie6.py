from math import ceil
from math import log

def binary_search(A, low, high, k):
    if high >= low:
        mid = (low + high) // 2
        print(mid)
        if A[mid] is None:
            return binary_search(A, low, mid-1, k)
        if k ==  A[mid][0]:
            return True, mid
        elif k < A[mid][0]:
            return binary_search(A, low, mid-1, k)
        else:
            return binary_search(A, mid+1, high, k)
    else:
        return False, high, low

def zad6(A):
    n = len(A)
    B = [None for _ in range(ceil(log(n, 2)))]
    for i in range(n):
        x = binary_search(B, 0, ceil(log(n, 2))-1, A[i])
        if x[0]:
            B[x[1]][1] += 1
        else:
            if B[x[2]] is not None:
                cnt = x[2]
                save = [A[i], 1]
                while cnt < ceil(log(n, 2))-1 and B[cnt] is not None:
                    save, B[cnt] = B[cnt+1], save
                    cnt += 1
            else:
                B[x[2]] = [A[i], 1]
    i = j = 0
    while i < n:
        A[i] = B[j][0]
        B[j][1] -= 1
        if B[j][1] == 0:
            j += 1
        i += 1

if __name__ == '__main__':
    tab = [1, 2, 3, 4, 1, 2, 3, 5, 1, 1, 1, 2, 3, 5, 5, 3, 3, 2, 1, 1, 4]
    zad6(tab)
    print(tab)


