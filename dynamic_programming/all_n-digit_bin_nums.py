def printer(n, A, tmp=' ', last=0): #nie dynamicznie
    if n == 0:
        A.append(tmp)
        return
    printer(n-1, A, tmp + '0', 0)
    if last == 0:
        printer(n-1, A, tmp + '1', 1)

def n_digit_nums(n):
    A = [[0 for _ in range(2)] for _ in range(n+1)]
    A[1][0] = 2
    A[1][1] = 1
    for i in range(2, n+1):
        A[i][0] = A[i-1][0] + A[i-1][1]
        A[i][1] += A[i-1][0]
    for g in range(len(A)):
        print(A[g])
    return A[n][0]

if __name__ == '__main__':
    Z = []
    printer(5, Z)
    for g in range(len(Z)):
        print(Z[g])
    print(n_digit_nums(10))
