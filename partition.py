# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):
        isroom1 = True
        visited = []
        perimeter = []
        visited.append(s)
        perimeter.append([s, isroom1])
        room1 = []
        room2 = []

        while perimeter:
            x = perimeter.pop(0)
            vfrom = x[0]
            isroom1 = x[1]
            isroom1 = not isroom1
            for i in self.graph[vfrom]:
                print(i)
                if i not in visited:
                    if isroom1:
                        room1.append(i)
                        print ("room1", i)
                    else:
                        room2.append(i)
                        print("room2", i)
                    perimeter.append([i, isroom1])
                    visited.append(i)


# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 8)
g.addEdge(1, 7)
g.addEdge(2, 5)
g.addEdge(2, 6)
# print (g)
g.BFS(0)