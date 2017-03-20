# using default dict because we have to store the connections some where
from collections import defaultdict
# {1:[2,3],0:[1,2]}
# declare a graph
class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited = [False]*len(self.graph)
        queue = []
        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.pop(0)
            print s
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addedge(0,2)
g.addedge(0,1)
g.addedge(2,2)
g.addedge(1,3)
g.addedge(3,3)

print g.graph
g.BFS(0)