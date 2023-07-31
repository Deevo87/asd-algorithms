def binary_search(A, low, high):
    if high >= low:
        mid = (low + high)//2
        print(A[mid], mid)
        if A[mid] is None:
            return binary_search(A, low, mid-1)
        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            return binary_search(A, mid+1, high)
        else:
            return binary_search(A, low, mid-1)
    else:
        return False

def zad3(A):
    n = len(A)
    if binary_search(A, 0, n-1) is not False:
        return True
    return False

if __name__ == '__main__':
    tab = [-3, -2, 0, 3, 7, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    tab2 = [0, 1, 2, 3, 4, 5]
    tab3 = [1, 2, 3, 4, 5]
    print(zad3(tab3))