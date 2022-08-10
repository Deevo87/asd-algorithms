def counting_sort(A, k, p): #k to ilość cyfr - 10, p to position
    n = len(A)
    B = [0]*n
    C = [0]*k
    for x in A:
        C[x[p]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        #print(C[A[i][p]]-1)
        B[C[A[i][p]]-1] = A[i]
        C[A[i][p]] -= 1
    for i in range(n):
        A[i] = B[i]

def zad9(A):
    n = len(A)
    tab = [0 for _ in range(n)]
    for x in range(n):
        tmp = [0] * 10
        essa = A[x]
        cnt_j = 0
        cnt_w = 0
        while essa != 0:
            #print(essa%10)
            tmp[essa%10] += 1
            essa //= 10
        for i in range(10):
            if tmp[i] == 1:
                cnt_j += 1
            elif tmp[i] > 1:
                cnt_j += 1
                cnt_w += 1
        tab[x] = (cnt_j, cnt_w, A[x])
    counting_sort(tab, 10, 1)
    tab = tab[::-1]
    counting_sort(tab, 10, 0)
    tab = tab[::-1]
    for i in range(n):
        A[i] = tab[i][2]
    return A


if __name__ == '__main__':
    test = [1266, 123, 455, 67333, 114577, 2344]
    print(zad9(test))

