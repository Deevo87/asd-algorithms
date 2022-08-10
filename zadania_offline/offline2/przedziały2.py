from random import randint

def partition(A, p, r):  # A - tablica, p na początek, r - wskaźnik na piwot
    x = A[r]
    i = p - 1  # wskaźnik na najmineszy do zamiany
    for j in range(p, r):
        if A[j][0] <= x[0]:
            i += 1
            if A[j][0] == x[0]:
                #print(A[i-1], A[j])
                #print("________")
                if A[j][1] > x[1]:
                    #print(A[i][1], "the heck?!?")
                    A[r], A[j] = A[j], A[r] # zmieniam piwot
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def depth(L):
    n = len(L)
    quicksort(L, 0, n-1)
    k = maks = 0
    while k < n:
        x = k
        #print(k,"kkkkkkkkk")
        tmp = L[k]
        cnt = 0
        while x < n-1:
            if L[x+1][0] == L[x][0] and L[k][1] >= L[x+1][1]:
                cnt += 1
                #print(L[x], cnt, "__________")
                x += 1
            else:
                if L[k] == tmp:
                    k = x
                    tmp = [-1, -1]
                    #print(k, tmp, L[k], "***********")
                x += 1
                if L[k][1] >= L[x][1]: #x=2
                    cnt += 1
                    print(L[k], L[x],cnt)
                if L[k][1] < L[x][0]:
                    break
        if maks < cnt:
            maks = cnt
        k += 1
    return maks



if __name__ == "__main__":
    # a = [2, 8, 7, 1, 3, 5, 6, 4]
    # n = len(a)
    # print(partition(a, 0, 7))
    #data = [0 for _ in range(10)]
    #for i in range(10):
        #k = randint(0, 10)
        #data[i] = [k, k + randint(0, 10)]
    #data = [[1, 7], [1, 6], [4, 8], [2, 3], [7, 9], [3, 9]]
    #data = [[9, 17], [2, 3], [6, 7], [10, 14], [9, 14], [5, 10], [1, 1], [9, 20], [8, 12], [6, 10]]
    data = [[1, 6], [5, 6], [2, 5], [2, 6], [2, 7], [8, 9], [1, 6]]
    #data = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
    print(data)
    size = len(data)
    quicksort(data, 0, size - 1)
    print(data)
    print(depth(data))
    #L = [[1, 6], [5, 6], [2, 5], [8, 20], [1, 6], [8, 15], [1, 8]]