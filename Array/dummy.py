# using default dict because we have to store the connections some where
from collections import defaultdict
# {1:[2,3],0:[1,2]}
# declare a graph
class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def DFS_helper(self,s,visited):
    	# make visited vertice marked
    	# print the node
    	visited[s] = True
    	print s
    	for i in self.graph[s]:
    		if visited[i] == False:
    			self.DFS_helper(i,visited)

    def DFS(self,s):
        visited = [False]*len(self.graph)
        self.DFS_helper(s,visited)

g = Graph()
g.addedge(0,2)
g.addedge(0,1)
g.addedge(2,2)
g.addedge(1,3)
g.addedge(3,3)
print g.DFS(0)