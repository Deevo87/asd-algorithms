#Rafał Laskowski

'''
Tablice T przekształcam na tablice krotek (T[i], i) dopóki ilość zgromadzonego paliwa jest mniejsza od n-1,
szuakm najabardziej optymalnych pól z palwiem na postój. W momencie kiedy bak jest pusty, szukam najlpeszego pola
z którego powininem zebrać paliwo. Na koniec sortuje tablice wyników i ją zwaracam.

złożoność czasowa: nlogn
'''


from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    k = T[0][0]
    i, cnt = 1, 0
    A = [T[0][1]]
    q = PriorityQueue()
    while k < n - 1:
        q.put((-T[i][0], T[i][1]))
        if i == k:
            item = q.get()
            k -= item[0]
            A.append(item[1])
        i += 1
    A.sort()
    return A

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )