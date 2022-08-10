def rod_cut(X, l):
    n = len(X)
    A = [0 for _ in range(l+1)]
    for i in range(1, l+1):
        for j in range(1, i+1):
            A[i] = max(X[j-1] + A[i-j], A[i])
    print(A)
    return A[l]

if __name__ == '__main__':
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 4

    print('Profit is', rod_cut(price, n))
