from heapq import heappush, heappop

def heapify(A, i, n):  # tworze min heap
    left = 2 * i + 1
    right = 2 * i + 2
    maks_ind = i
    if left < n and A[maks_ind].value > A[left].value:
        maks_ind = left
    if right < n and A[maks_ind].value > A[right].value:
        maks_ind = right

    if maks_ind != i:
        A[maks_ind], A[i] = A[i], A[maks_ind]
        heapify(A, maks_ind, n)


def heap_pop(A, n):
    if n <= 0:
        return -1
    top = A[0]
    A[0] = A[n - 1]
    heapify(A, 0, n-1)
    return top


def heap_push(A, elem, n):
    A[n-1] = elem
    ind = (n - 2) // 2
    heapify(A, ind, n)


# A class to store a heap node
class Node:
    def __init__(self, value, list_num, index):
        # `value` stores the element
        self.value = value

        # `list_num` stores the list number of the element
        self.list_num = list_num

        # `index` stores the column number of the list from which element was taken
        self.index = index

    # Override the `__lt__()` function to make `Node` class work with min-heap
    def __lt__(self, other):
        return self.value < other.value


# Function to merge `M` sorted lists of variable length and
# print them in ascending order
def print_sorted(lists):
    A = []
    # push the first element of each list into the min-heap
    # along with the list number and their index in the list
    pq = [Node(lists[i][0], i, 0) for i in range(len(lists)) if len(lists[i]) >= 1]
    n = len(pq)
    heapify(pq, (n-2)//2, n)
    # run till min-heap is empty
    while pq:

        # extract the minimum node from the min-heap
        min = heappop(pq)
        #min = heap_pop(pq, n)

        # print the minimum element
        print(min.value, min.index,  end=' ')
        #A.append(min.value)

        # take the next element from the 'same' list and insert it into the min-heap
        if min.index + 1 < len(lists[min.list_num]):# or len(lists[min.list_num]) == 0:
            min.index = min.index + 1
            #print(min.index)
            min.value = lists[min.list_num][min.index]
            #print(min.value)
            heappush(pq, min)
            #heapify(A, (min.index - 2)//2, n)
    return A


if __name__ == '__main__':
    list = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
    print(print_sorted(list))
