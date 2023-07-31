def binary_srot(A):
    n = len(A)
    count = 0
    for i in A:
        if i == 1:
            count += 1
    how_many_zeros = n - count - 1
    i = 0
    while how_many_zeros >= 0 and i < n:
        A[i] = 0
        how_many_zeros -= 1
        i += 1
    while i < n:
        A[i] = 1
        i += 1
    return A

if __name__ == '__main__':
    tab = [1, 0, 1, 0, 1, 0, 0, 1]
    print(binary_srot(tab))