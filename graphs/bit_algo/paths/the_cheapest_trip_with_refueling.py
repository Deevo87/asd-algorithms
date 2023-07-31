# We are given a graph, in which the vertices are cities and the edges are roads between them. We know
# the fuel price in per liter for each city and the length in kilometers for each road. Our car has
# a 100 liter tank and burns one liter per kilometer. We start from city_A with an empty tank. What is
# the minimum cost that we have to pay for fuel to get to the city_B?
from math import inf
from queue import PriorityQueue


# SOULTION
# 1) We need to change the structure of our graph that we can find the cheapest possible way to travel. To do that
#    we have to make as many vertices as there is fuel in tank. So for example if the tank capacity is 5 every vertex
#    will have 5 edges with the possible fuel he can travel from that vertex to another.
# 2) We have to change the relaxation so that check if we are able to travel to next vertex with current fuel in the tank.
# Time complexity: O(tank * ElogV), where tank is constant.


def relax(graph,cost, u, v, fuel, parent):
    actual_fuel = fuel - v[1]
    print(u, v, actual_fuel)
    c = v[1] * graph[v[0]][1]
    if cost[v[0]][actual_fuel] > cost[u][fuel] + v[1] * graph[v[0]][1]:
        cost[v[0]][actual_fuel] = cost[u][fuel] + v[1] * graph[v[0]][1]
        parent[v[0]][actual_fuel] = u, fuel
        return True
    return False


def cheapest_trip_with_refueling(graph, s, end, tank):
    n = len(graph)
    cost = [[inf for _ in range(tank + 1)] for _ in range(n)]
    visited = [[False for _ in range(tank + 1)] for _ in range(n)]
    parent = [[(None, None) for _ in range(tank + 1)] for _ in range(n)]
    q = PriorityQueue()
    for fuel in range(tank + 1):
        q.put((fuel * graph[s][1], fuel, s))  # cost, amount of fuel in the tank, current vertex
        cost[s][fuel] = fuel * graph[s][1]

    while not q.empty():
        curr_cost, fuel, u = q.get()
        for v in graph[u][0]:
            # print(v, fuel)
            if tank >= v[1] and fuel >= graph[v[0]][1]:
                for f in range(fuel, tank + 1):
                    # print(f - v[1], u, "--------------")
                    if f - v[1] >= 0 and not visited[v[0]][f] and relax(graph, cost, u, v, f, parent):
                        q.put((curr_cost + f * graph[v[0]][1], f, v[0]))
        visited[u][fuel] = True

    min_cost = inf
    for i in range(n):
        print(cost[i])
    for i in range(tank + 1):
        min_cost = min(min_cost, cost[end][i])
    return min_cost


if __name__ == '__main__':
    G = [[[(1, 5), (2, 7)], 8],
         [[(0, 5), (2, 3), (3, 5)], 5],
         [[(0, 7), (1, 3), (3, 4)], 3],
         [[(1, 5), (2, 4), (4, 6)], 2],
         [[(3, 6)], 1]]
    print(cheapest_trip_with_refueling(G, 0, len(G) - 1, 6))
