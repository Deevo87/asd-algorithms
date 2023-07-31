def roznica(S):
    print(S)
    n = len(S)
    A = [0 for _ in range(n)]
    if S[0] == '1':
        A[0] = -1
    else:
        A[0] = 1
    print(A)
    for i in range(1, n):
        if S[i] == '1':
            A[i] = max(A[i], A[i-1] - 1)
        else:
            A[i] = 1
            A[i] = max(A[i], A[i-1] + 1)
        print(A[i], i, i-1, A[i] + A[i-1])
        print(A)
    print(A)
    res = max(A)
    return res


if __name__ == '__main__':
    X = '11000010001'
    X2 = '0100010010'
    X3 = '10001011111001010101'
    print(roznica(X3))
    # print('chuj')
