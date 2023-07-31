
import heapq
from heapq import heappop, heappush

'''ogólnie do przerobienia bo używa jakichś wbudowanych funkcji z biblioteki z heapem ale
to raczej na es do zrobienia, zapisałem to żeby było'''

# Function to sort a k–sorted array
def sort_k_sorted_arr(nums, k):
    # build a min-heap from the first `k+1` elements in the list
    pq = nums[0:k + 1]
    heapq.heapify(pq)

    # do for remaining elements in the list
    index = 0
    for i in range(k + 1, len(nums)):
        # pop the top element from the min-heap and assign them to the
        # next available list index
        nums[index] = heappop(pq) #sciąga z heapa zawsze najmniejszą wartość, dlatego nie musi go naprawiać
        index = index + 1         #gdybym to robił sam zaimplementowałbym to heappop i napraiwał to zawsze heapify
                                  # żeby był posortowany i sciągałbym zawsze z samej góry
        # push the next list element into min-heap
        heappush(pq, nums[i])     #dokładnie w tym momencie bym naprawiał heapa

    # pop all remaining elements from the min-heap and assign them to the
    # next available list index
    while pq:
        nums[index] = heappop(pq)
        index = index + 1


if __name__ == '__main__':
    nums = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2

    sort_k_sorted_arr(nums, k)
    print(nums)
