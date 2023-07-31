#Rafał Laskowski

'''
    Algorytm wyszukuje palindromy od środka, biorąc pod uwagę że szukamy tylko nieparzystych palindromów przyjmuje że
    palindrom ma tylko jeden "środek" (i=j) i rozchodze się w prawo i w lewo, aż skończy się string lub palindrom.
     Pomijam przypadek, w którym palindromy są parzyste.
    Złożoność algorytmu to O(n^2).
'''

from zad1testy import runtests

def ceasar(s):
    n = len(s)
    first_longest = 0
    for i in range(n):
        length = 0
        j = i
        if s[i] == s[j]:
            length += 1
            i -= 1
            j += 1
        while i >= 0 and j <= n - 1 and s[i] == s[j]:
            i -= 1
            j += 1
            length += 2
        if length > first_longest:
            first_longest = length
    return first_longest


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
