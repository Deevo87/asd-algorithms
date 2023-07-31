# There is a list of triples on the boards in the exchange office (currency_1, currency_2, exchange_rate).
# Each of those triples means that exchange office will buy n of currency_2 at the rate of
# n*currency_1.
#   1) Find the most advantageous sequence for converting currency A to currency B.
#   2) Is there such a sequence of currency exchange that starts and ends in the same currency and
# we ends up with more money than we started?
from math import inf, log2

def find_gold_path(parent, curr_b):
    path = []
    while curr_b != -1:
        if path.count(curr_b) >= 1:
            path.append(curr_b)
            break
        path.append(curr_b)
        curr_b = parent[curr_b]
    path.reverse()
    return path

def switch_prices_to_log(currencies):
    n = len(currencies)
    for i in range(n):
        currencies[i] = currencies[i][0], currencies[i][1], log2(currencies[i][2])
    return currencies

def currency_exchange(currencies, currency_a, currency_b):
    currencies = switch_prices_to_log(currencies)
    n = len(currencies)

    max_ver = max(currencies, key=lambda z: z[1])[1]
    parent = [-1 for _ in range(max_ver + 1)]
    distance = [inf for _ in range(max_ver + 1)]
    distance[currency_a] = 0

    for i in range(n-1):
        for u, v, ex_cost in currencies:
            if distance[u] != inf and distance[u] + ex_cost < distance[v]:
                distance[v] = distance[u] + ex_cost
                parent[v] = u

    for x in currencies:
        u, v, ex_cost = x
        if distance[u] != inf and distance[u] + ex_cost < distance[v]:
            print(parent)
            return True, find_gold_path(parent, currency_b)
    return False, None



if __name__ == '__main__':
    currencies = [(0, 1, 4.5),
                  (0, 2, 4),
                  (2, 0, 0.25),
                  (1, 2, 0.75),
                  (3, 2, 100),
                  (0, 3, 0.4),
                  (1, 4, 6),
                  (3, 4, 2)]

    currency_a = 0
    currency_b = 4
    print(currency_exchange(currencies, 0, 4))