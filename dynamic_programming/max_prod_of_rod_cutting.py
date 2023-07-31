def rod_cutter(l):  # no need for table for prices bcs price of rod is his length
    # max prod of is calculated by multiply it's lenght
    A = [i for i in range(l+1)]
    print(A)
    for i in range(2, l+1):
        for j in range(1, i + 1):
            A[i] = max(A[i], j * A[i-j])
    print(A)
    return A[l]


if __name__ == '__main__':
    n = 15

    print('The maximum profit is', rod_cutter(n))
