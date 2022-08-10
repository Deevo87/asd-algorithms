import sys


# Find the minimum adjustment cost of a list
def findMinAdjustmentCost(A, target):
    M = max(A)
    print(M)
    # base case
    if not A:
        return 0

    # T[i][j] stores the minimal adjustment cost on changing A[i] to j
    T = [[0 for x in range(M + 1)] for y in range(len(A))]
    for i in range(len(A)):
        T[0][i] = abs(A[0] - i)
    # do for each element in the list
    for i in range(1, len(A)):
        # replace A[i] to `j` and calculate minimal adjustment cost T[i][j]
        for j in range(M + 1):

            # separately handle the first element in the list
            if i == 0:
                T[i][j] = abs(j - A[i])
            else:
                # initialize minimal adjustment cost with `sys.maxsize`
                T[i][j] = M

                # consider all `k` such that k >= max(j - target, 0) and
                # k <= min(M, j + target) and take minimum
                for k in range(max(j - target, 0), min(M, j + target) + 1):
                    T[i][j] = min(T[i][j], T[i - 1][k] + abs(A[i] - j))
    for i in range(len(A)):
        print(T[i])
    # return minimum value from the last row of `T`
    result = sys.maxsize
    for j in range(M + 1):
        result = min(result, T[-1][j])

    return result


if __name__ == '__main__':
    A = [55, 77, 52, 61, 39, 6, 25, 60, 49, 47]
    A1 = [1, 3, 0, 3]
    target = 10

    print('The minimal adjustment cost is', findMinAdjustmentCost(A, target))
