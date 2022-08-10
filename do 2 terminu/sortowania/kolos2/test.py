def strong_string(A):
    pass

def radix_sort(A):
    longest = max(len(x) for x in A) - 1
    while longest >= 0:
        A = counting_sort(A, longest, 26)
        longest -= 1
    return A

def counting_sort(A, k, alf):
    n = len(A)
    B = [0]*n
    C = [0]*(alf + 1)
    for x in A:
        if len(x) > k:
            ind = ord(x[k])-97
        else:
            ind = 0
        C[ind] += 1
    for i in range(1, alf+1):
        C[i] += C[i-1]
    for i in range(n):
        if len(A[i]) > k:
            ind = ord(A[i][k]) - 97
        else:
            ind = 0
        B[C[ind]-1] = A[i]
        C[ind] -= 1
    return B

if __name__ == '__main__':
    tab = ['pies', 'mysz', 'kot', 'kogut', 'tok', 'seip', 'kot']
    print(radix_sort(tab))