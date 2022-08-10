def partition(X):
    n = len(X)
    suma = 0
    for i in range(n):
        suma += X[i]
    if suma % 2 != 0:
        return False
    suma //= 2
    A = [[False for _ in range(suma+1)] for _ in range(n+1)]
    print(suma)
    for i in range(n+1):
        A[i][0] = True
        for j in range(1, suma + 1):
            if X[i-1] > j:
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = A[i-1][j] or A[i-1][j-X[i-1]]
        for x in range(n + 1):
            print(A[x])
        print('________________________________________________________________________________________________')
    # return maximum value
    return A[n][suma]


if __name__ == '__main__':

    # Input: a set of items
    nums = [7, 3, 1, 5, 4, 8]

    if partition(nums):
        print('Set can be partitioned')
    else:
        print('Set cannot be partitioned')