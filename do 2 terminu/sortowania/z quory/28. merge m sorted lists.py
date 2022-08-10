#POLECENIE
#mam zmergować k list, takie samo jak offline z k chaotycznymi listami tylko że na zwykłych listach a nie odsyłaczowych

#POMYSŁ
#1. biorę po jednym elemencie z każdej listy i go dodaje do min heapa
#2. sciągam najmniejszy element z heapa i dodaje do heapa element z listy do której wcześniej należał ściągnięty element
#3. wszyscy żyli długo i szczęśliwie


def left_ind(A,i):
    n = len(A)
    parent = n - i - 1
    return n - (2*parent + 2)-1

def right_ind(A,i):
    n = len(A)
    parent = n - i - 1
    return n-(2*parent + 1)-1

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def heapify(A, i):
    n = len(A)
    left = left_ind(A,i)
    right = right_ind(A,i)
    maks_ind = i
    if left >= 0 and A[maks_ind][0] < A[left][0]: #max-heap
        maks_ind = left
    if right >= 0 and A[maks_ind][0] < A[right][0]:
        maks_ind = right
    if maks_ind != i:
        swap(A, i, maks_ind)
        heapify(A, maks_ind)

def insert(A, x):
    A.append(x)
    child = len(A) - 1
    parent = (child-1)//2
    while child > 0 and A[parent][0] < A[child][0]:
        A[parent], A[child] = A[child], A[parent]
        child = parent
        parent = child//2
    heapify(A, 0) # te heapify nie chce mi działać :(
    print(A, 'insert')

# def insert(A, x):
#     A.append(x)
#     heapify(A, len(A)-1, len(A))

def pop(A, n):
    if n <= 0:
        return -1
    top = A[0]
    print(A, 'przed heaipfy w popie')
    del A[0]
    heapify(A, 0) # te heapify też nie działa tak jak trzeba :((((
    print(A, 'po heapify popie')
    return top

def merge(listy):
    n = len(listy)
    A = []
    length = 0
    for i in range(n):  # obliczam długość listy wynikowej
        length += len(listy[i])
    INDEX = [len(listy[i]) - 1 for i in range(n)]  # tablica indeksów żeby pamiętać gdzie skończyliśmy
    for i in range(n):
        A.append((listy[i][INDEX[i]], i))
        INDEX[i] -= 1
    parent = 0
    while parent < n:  # | tutaj stworzyłem już wcześniej wspominany kopiec
        heapify(A, parent)  # |
        parent += 1  # |
    count = length - 1
    C = [0] * length
    while count >= 0:
        x = A.pop()
        C[count] = x[0]
        count -= 1
        if INDEX[x[1]] > -1:  # kiedy w liście są jeszcze elementy
            A.append((listy[x[1]][INDEX[x[1]]], x[1]))  # dodaje nowy element do heapu
            INDEX[x[1]] -= 1
        heapify(A, len(A) - 1)
    return C
    # n = len(listy)
    # A = []
    # length = 0
    # for i in range(n): # obliczam długość listy wynikowej
    #     length += len(listy[i])
    # for i in range(n):             # dodaje elementy do listy z której stworzę kopiec
    #     A.append((listy[i][0], i)) # (elemnt z listy, numer listy z której wziąłem element)
    #     del listy[i][0]            # usuwam elementy które wstawiłem
    # parent = (n - 2) // 2           #|
    # while parent >= 0:              #| tutaj stworzyłem już wcześniej wspominany kopiec
    #     heapify(A, parent, len(A))  #|
    #     parent -= 1                 #|
    # count = 0           # iterator do listy wynikowej
    # C = [0] * length    # sama lista wynikowa
    # while A: # dopóki na kopcu coś jest
    #     x = pop(A, len(A))
    #     C[count] = x[0]
    #     count += 1
    #     if listy[x[1]]: # kiedy w liście są jeszcze elementy
    #         insert(A, (listy[x[1]][0], x[1])) # dodaje nowy element do heapu
    #         del listy[x[1]][0]
    #     else:
    #         tmp = x[1]
    #         flag = True # jeżeli flaga False to znaczy że zatoczyłem koło (sprawdzam pustą listę jeszcze raz)
    #         while not listy[tmp]: # szukam listy w której są jeszcze elementy
    #             tmp += 1
    #             if tmp >= n:
    #                 if not flag: # jeżeli zatoczyłem koło to po prostu wychodzę
    #                     tmp = x[1]
    #                     break
    #                 tmp = 0
    #                 flag = False
    #         if listy[tmp]:
    #             insert(A, (listy[tmp][0], tmp)) # dodaje nowy element do heapu
    #             del listy[tmp][0]
    #     print(C ,'||output||\n', listy, '||stan wejściowych list||\n', A, '||heap||')
    # return C


if __name__ == '__main__':
    listy1 = [[0, 24, 45, 69, 83, 96], [0, 62, 65], [0, 86], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    print(merge(listy1))




