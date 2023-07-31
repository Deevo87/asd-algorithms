from queue import PriorityQueue

def plan(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    k = T[0][0]
    i, cnt = 1, 0
    A = [T[0][1]]
    q = PriorityQueue()
    while k < n-1:
        q.put((-T[i][0], T[i][1]))
        if i == k:
            item = q.get()
            k -= item[0]
            A.append(item[1])
            i = k - 1
        i += 1
    A.sort()
    return A

if __name__ == '__main__':
    X = [3, 0, 2, 1, 2, 5, 0]
    X2 = [7, 0, 0, 1, 0, 3, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0]
    print(plan(X2))