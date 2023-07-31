#pierwsze rozwiązanie

def binary_search(A, low, high, k):
    if high >= low:
        mid = (high+low)//2
        if A[mid] == k:
            return mid
        elif A[mid] > k:
            return binary_search(A, low, mid-1, k)
        else:
            return binary_search(A, mid+1, high, k)
    else:
        return -1

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
           i += 1
           A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q+1

def zad7(A, B, C):
    a = len(A)
    b = len(B)
    quick_sort(B, 0, b-1)
    for i in range(a):
        for j in range(b):
            if binary_search(B, 0, b-1, C[j]-A[i]) >= 0:
                return True
    return False


#drugie rozwiązanie
def zad7_v2(A, B, C):
    a = len(A)
    b = len(B)
    quick_sort(A, 0, a-1)
    quick_sort(B, 0, b-1)
    for x in C:
        i = 0
        j = b - 1
        while i < a and j >= 0:
            suma = A[i] + B[j]
            if x == suma:
                return True
            elif x < suma and A[i] < B[j]:
                j -= 1
            elif x < suma and A[i] > B[j]:
                i += 1
            elif x > suma:
                break
    return False


if __name__ == '__main__':
    AA = [17, 3, 9, 7, 1]
    BB = [12, 10, 6, 5, 4]
    CC = [1, 2, 8, 4, 11, 2]
    print(zad7(AA, BB, CC))
    print(zad7_v2(AA, BB, CC))
