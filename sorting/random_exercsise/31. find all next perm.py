def swap(s, a, b):
    tmp = s[a]
    s[a] = s[b]
    s[b] = tmp

def reverse(s, r):
    n = len(s)-1
    rev = n
    while r <= n and r < rev:
        swap(s, r, rev)
        r += 1
        rev -= 1


def next_perm(s):
    n = len(s)
    cnt = n-1
    while s[cnt-1] >= s[cnt]:
        cnt -= 1
        if cnt <= 0:
            return False
    ind = n - 1
    while ind > cnt and s[ind] <= s[cnt-1]:
        ind -= 1
    swap(s, cnt-1, ind)
    reverse(s, cnt)
    return True

def permutations(s):
    if len(s) == 1:
        return s
    if len(s) == 0:
        return None
    res = []
    A = list(s)
    while True:
        x = A[0]
        for i in range(1, len(A)):
            x += A[i]
        res.append(x)
        if not next_perm(A):
            break
    return res

if __name__ == '__main__':
    stt = 'ABCD'
    print(permutations(stt))
