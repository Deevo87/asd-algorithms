# Algocia is placed on a great dessert and consists of cities and oases connected by roads. There is
# exactly one road leading from each gate to one oasis (but any given oasis can have any number of roads
# leading to them, oases can also be interconnected by roads). Algocian law requires that if someone
# enters a city through one gate, they must leave the other. Check of Algocia decided to send a bishop
# who will read the prohibition of formulating tasks "about the chessboard" (insult majesty) task in
# every city. Check wants the bishop to visit each city exactly once (but there is no limit how many
# times the bishop will visit each oasis). Bishop departs from the capital of Algocia city x, and after
# visiting all cities the bishop has to come back to city x. Find algorithm that determines if there
# is a suitable route for bishop.

def check_and_bishop(G, O):
    #nic nie kumam
    pass



if __name__ == '__main__':
    oasis = [2, 4, 5, 7, 9]
    graph = [[2, 4], [2, 9], [0, 1, 3, 9], [2, 5], [0, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1, 2]]
    print(check_and_bishop(graph, oasis))
    multi_ver = []
    oasis_check = [False]*(max(oasis)+1)
    for i in range(len(oasis)):
        for j in graph[oasis[i]]:
            if oasis[i] != j and oasis[i] < j and  j in oasis:
                multi_ver.append([oasis[i], j])
                oasis_check[oasis[i]] = True
                oasis_check[j] = True
    for i in oasis:
        if not oasis_check[i]:
            multi_ver.append([i])
    print(multi_ver)
