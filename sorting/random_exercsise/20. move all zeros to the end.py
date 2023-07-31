def moving(A):
    n = len(A)
    count = 0
    i = 0
    while i < n:
        if A[i] == 0:
            del A[i]
            count += 1
            i -= 1
            n -= 1
        i += 1
    for j in range(count):
        A.append(0)
    return A

if __name__ == '__main__':
    tab = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    print(moving(tab))