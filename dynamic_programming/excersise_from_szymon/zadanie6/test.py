def haslo ( S ):
    n = len(S)
    A = [0 for _ in range(n)]
    if S == '': # dla pustego stringa
        return 1
    for i in range(n): # jeżeli są dwa 0 pod rząd
        if S[i] == '0' and i + 1 < n:
            #print(S[i])
            if S[i+1] == '0':
                return 0
    print(S)
    A[1] = 1
    if int(S[0:2]) <= 26 and int(S[:1]) != 10:
        print(S[0:2])
        A[1] = 2
    A[0]= 1
    for i in range(2, n):
        if int(S[i-1]) >= 3:
            A[i] = A[i - 1]
        elif (i + 1 < n and S[i+1] == '0') or S[i-1] == '0' or S[i] == '0':
            A[i] = A[i - 1]
        elif int(S[i-1:i+1]) <= 26:
            print(S[i-1:i+1])
            A[i] = A[i-1] + A[i-2]
        else:
            A[i] = A[i - 1]
    print(A)
    return max(A)



if __name__ == '__main__':
    X = '619873241351034132207161'
    X2 = '1111019'
    print(haslo(X))