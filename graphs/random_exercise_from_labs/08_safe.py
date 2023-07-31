# We are given a safe that can be unlocked with four-digit PIN (0000 - 9999). Below the
# display there are some buttons with numbers from 1 to 9999 (for example: 13, 223, 782, 3902).
# This safe works differently tha the normal one. Pressing a button with a number adds the
# number from a button to the number on the display. If sum is greater than 9999, the first
# number is cut. We know the PIN and the numbers that are currently displayed. Find the
# shortest button press sequence that will allow us to unlock the safe. If such a sequence
# doesn't exist, return None.
from queue import Queue

def count_digits(num):
    cnt = 0
    while num > 0:
        num //= 10
        cnt += 1
    return cnt

def safe(B, dis, pin):
    n = len(B)
    visited = [False]*10000
    q = Queue()
    operations = 0
    for i in range(n):
        visited[dis+B[i]] = True
        q.put(dis+B[i])
    while not q.empty():
        x = q.get()
        if x == pin:
            return True
        act_sum = x
        operations += 1
        print(operations, '.', x)
        if operations % 5 == 0:
            print('_________________________')
        for i in B:
            act_sum += i
            if act_sum > 9999:
                digits = count_digits(act_sum)
                act_sum %= 10*digits
            if not visited[act_sum]:
                q.put(act_sum)
                visited[act_sum] = True
    return False


if __name__ == '__main__':
    display = 1234
    PIN = 7384
    buttons = [13, 223, 782, 3902, 500]
    print(safe(buttons, display, PIN))