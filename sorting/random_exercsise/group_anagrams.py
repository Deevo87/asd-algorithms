# The two strings, X and Y, are anagrams if by rearranging X's letters, we can get Y using all the original letters of X
#  exactly once. For example, all these pairs are anagrams as lhs can be rearranged to rhs and vice-versa.

def counting_sort(A, pos, k):
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]
    for x in A:
        C[x[1][pos]] += 1
    for i in range(1, n):
        C[i] = C[i] + C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i][1][pos]] - 1] = A[i]
        C[A[i][1][pos]] -= 1
    for i in range(n):
        A[i] = B[i]
    return A


def radix_sort(A):
    n = len(A)
    sortd = []
    print(A)
    for i in range(26-1, -1, -1):
        A = counting_sort(A, i, 26)
    for x in A:
        print(x)
    return A


def anagrams(words):
    n = len(words)
    B = [ (words[_].lower(), [0 for _ in range(26)]) for _ in range(n)]
    maks_len = 0
    for x in range(n):
        maks_len = max(maks_len, len(words[x]))
        for letter in words[x]:
            dna = ord(letter.lower()) - 96
            B[x][1][dna] += 1
    C = radix_sort(B)

    cnt = 1
    ind = 0
    maks_amount = 0
    for i in range(n-1):
        if C[i][1] == C[i+1][1]:
            cnt += 1
            if cnt > maks_amount:
                maks_amount = cnt
        else:
            cnt = 1
            ind = i

    most_popular_anagrams = []
    for i in range(ind, ind-maks_amount, -1):
        most_popular_anagrams.append(C[i][0])
    return most_popular_anagrams




if __name__ == '__main__':
    A = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'SCAR', 'DESIGN']
    print(anagrams(A))