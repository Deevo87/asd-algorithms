def parition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = parition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1

def binary_search(A, low, high, k):
    if high >= low:
        mid = (low+high)//2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            return binary_search(A, low, mid-1, k)
        else:
            return binary_search(A, mid+1, high, k)
    else:
        return False

def zad1(A, B):
    m = len(B)
    check = [False]*m
    quick_sort(B, 0, m-1)
    for i in A:
        ind = binary_search(B, 0, m-1, i)
        if ind is not False:
            check[ind] = True
    for i in check:
        if not i:
            return False
    return True

if __name__ == '__main__':
   N = [2, 1, 3, 5, 7, 11, 20]
   M = [5, 1, 2]
   print(zad1(N, M))

