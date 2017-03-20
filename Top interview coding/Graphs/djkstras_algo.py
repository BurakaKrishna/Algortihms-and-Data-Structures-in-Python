from collections import defaultdict
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

g = Graph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(8)
g.add_node(7)
g.add_node(6)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1,7,11)
g.add_edge(7,8,7)
g.add_edge(7,6,1)
g.add_edge(6,8,6)
g.add_edge(8,2,2)
g.add_edge(1,2,8)
print g.distances
print g.edges
print g.nodes


