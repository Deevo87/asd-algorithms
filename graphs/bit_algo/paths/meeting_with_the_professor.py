# A famous professor invited you to a meeting in the Magic City. In this city some roads can only be used
# by people under the age of 30 (including us), others only by people over the age of 30 (including the
# professor). There are also roads that can be traveled by anyone. Each road has a certain length,
# expressed in a positive natural number, and roads can be one-way or two-way. These roads connect possible
# meeting locations. Among them, we distinguish your house and the professor's house. The professor asks
# us to choose a place for the meeting so that the total distance that we and the professor must travel
# is the smallest. If there is more than one such a place, list them all. If there is no such a place,
# the algorithm should consider that.
from queue import PriorityQueue
from math import inf


def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra(graph, s):
    n = len(graph)
    parent = [None for _ in range(n)]
    distance = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    q = PriorityQueue()
    q.put((0, s))
    distance[s] = 0
    while not q.empty():
        dist, u = q.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                q.put((dist + v[1], v[0]))
        visited[u] = True
    return distance


def meeting_with_the_professor(under_thirty, over_thirty, normal, student_house, professor_house):
    n = len(under_thirty)
    m = len(over_thirty)
    l = len(normal)
    maks_normal = -inf
    maks_over_thirty = -inf
    maks_under_thirty = -inf
    for i in range(l):
        maks_normal = max(maks_normal, normal[i][0], normal[i][1])
    for i in range(n):
        maks_under_thirty = max(maks_under_thirty, under_thirty[i][0], under_thirty[i][1])
    for i in range(m):
        maks_over_thirty = max(maks_over_thirty, over_thirty[i][0], over_thirty[i][1])

    professor_len = max(maks_normal, maks_over_thirty) + 1
    student_len = max(maks_normal, maks_under_thirty) + 1

    professor = [[] for _ in range(professor_len)]
    student = [[] for _ in range(student_len)]

    for edge in normal:
        professor[edge[0]].append([edge[1], edge[2]])
        professor[edge[1]].append([edge[0], edge[2]])
        student[edge[0]].append([edge[1], edge[2]])
        student[edge[1]].append([edge[0], edge[2]])

    for edge in over_thirty:
        professor[edge[0]].append([edge[1], edge[2]])
        professor[edge[1]].append([edge[0], edge[2]])

    for edge in under_thirty:
        student[edge[0]].append([edge[1], edge[2]])
        student[edge[1]].append([edge[0], edge[2]])

    professor_distance = dijkstra(professor, professor_house)
    student_distance = dijkstra(student, student_house)

    min_location = [inf, None]
    for i in range(student_len):
        if professor_distance[i] + student_distance[i] < min_location[0]:
            min_location[0], min_location[1] = professor_distance[i] + student_distance[i], i
    return min_location

if __name__ == '__main__':
    under_thirty = [(0, 2, 2), (0, 4, 4), (1, 3, 1), (3, 7, 4), (8, 10, 5), (11, 12, 1)]
    over_thirty = [(0, 1, 3), (0, 4, 4), (5, 6, 2), (6, 11, 2), (7, 8, 2), (9, 10, 2)]
    normal = [(0, 1, 3), (2, 3, 5), (4, 5, 3), (7, 9, 1), (6, 9, 3), (10, 12, 4)]
    print(meeting_with_the_professor(under_thirty, over_thirty, normal, 0, 12))
