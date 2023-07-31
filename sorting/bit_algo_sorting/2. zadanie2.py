def partition(A, p, r):
    x = A[r]
    j = p - 1
    for i in range(p, r):
        if A[i] <= x:
            j += 1
            A[i], A[j] = A[j], A[i]
    A[j+1], A[r] = A[r], A[j+1]
    return j + 1

def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1

def zad2(A): #n jest zawsze parzyste
    n = len(A)
    if n%2 != 0:
        return False
    quick_sort(A, 0, n-1)
    i = 0
    j = n-1
    cnt = 0
    pairs = [None] * (n//2)
    while i < j:
        pairs[cnt] = [A[i], A[j], A[i]+A[j]]
        i += 1
        j -= 1
        cnt += 1
    return pairs

if __name__ == '__main__':
    tab = [1, 3, 5, 9]
    print(zad2(tab))