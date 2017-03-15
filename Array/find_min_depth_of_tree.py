class Tree():
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

t= Tree(1)
t.left = Tree(2)
t.right = Tree(3)
t.left.left = Tree(4)

def min_depth_tree(node):
	#Base case
	if node.left is None and node.right is None:
		return 1
	elif node.left is not None and node.right is not None:
		return min(min_depth_tree(node.right),min_depth_tree(node.left)) + 1
	elif node.left is None:
		return min_depth_tree(node.right)+1
	else:
		return min_depth_tree(node.left) +1

print min_depth_tree(t)
