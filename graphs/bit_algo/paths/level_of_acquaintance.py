# We define the relationship of acquaintances as symmetrical.
# Acquaintance:
#   - the first level is the direct acquaintance of the person,
#   - the second level is being a "friend of a friend" of the person, but not being directly acquaintance
# the person,
#   - third level, fourth level, fifth level, etc.,
#   - infinite level is when there is no chain of acquaintance between two people.
# Given a list of people and first level acquaintance between them, find the highest level of acquaintance
# between each of the possible pairs.
from queue import Queue
from math import inf

def level_of_acquaintance_sparse(people, A):
    return None

if __name__ == '__main__':
    people = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    acquaintance = [[1, 2, 3], [0, 2, 4, 5], [0, 1, 5, 6], [0, 6], [1, 7], [1, 2, 7], [2, 3, 8],
                    [4, 5, 9], [6, 9], [7, 8, 10], [9]]
    print(level_of_acquaintance_sparse(people, acquaintance))
