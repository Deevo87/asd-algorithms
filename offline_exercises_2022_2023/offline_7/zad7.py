# Rafał Laskowski
from zad7testy import runtests


def maze(L):
    def max_prev(row, column):
        '''
        returns max from what is achievable in previous column in this row.
        None if both are None
        '''
        if From_up[row][column - 1] != None:
            if From_down[row][column - 1] != None:
                return max(From_up[row][column - 1], From_down[row][column - 1])
            return From_up[row][column - 1]
        return From_down[row][column - 1]

    def calculate_field(row, column, table, offset):
        '''
        Gets max possible value for given field
        '''
        if L[row][column] == '#':
            return

        prev = max_prev(row, column)
        if prev:
            if table[row + offset][column]:
                table[row][column] = max(prev, table[row + offset][column]) + 1
            else:
                table[row][column] = prev + 1
        elif table[row + offset][column]:
            table[row][column] = table[row + offset][column] + 1

    n = len(L)

    # Two tables - one for going up, and second to going down
    From_up = [[None for _ in range(n)] for _ in range(n)]
    From_down = [[None for _ in range(n)] for _ in range(n)]

    # first value 
    From_up[0][0] = 0

    # values in first column
    for row in range(1, n):
        if L[row][0] == '#' or From_up[row - 1][0] == None:
            continue
        else:
            From_up[row][0] = From_up[row - 1][0] + 1

    # going left to right by column
    for column in range(1, n):
        # seting up first value in both tables
        if L[0][column] != '#':
            prev_up = max_prev(0, column)
            From_up[0][column] = prev_up + 1 if prev_up != None else None

        if L[n - 1][column] != '#':
            prev_down = max_prev(n - 1, column)
            From_down[n - 1][column] = prev_down + 1 if prev_down != None else None

        # calculating value for the rest fields in column
        for row in range(1, n):
            calculate_field(row, column, From_up, -1)
        for row in range(n - 2, -1, -1):
            calculate_field(row, column, From_down, 1)
    result = max_prev(n - 1, n)
    return result if result else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
