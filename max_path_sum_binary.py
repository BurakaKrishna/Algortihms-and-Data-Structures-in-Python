class Tree():
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

t= Tree(1)
t.left = Tree(2)
t.right = Tree(3)
t.left.left = Tree(4)

def max_path_sum(node):
	if node is None:
		return 0
	l = max_path_sum(node.left)
	r = max_path_sum(node.right)
	# needed for node having atleast a child, subtree
	max_simple = max(max(l,r)+node.data,node.data)
	# needed for node having when compared subtrees and the node
	max_top = max(max_simple,l+r+node.data)
	max_path_sum.res = max(max_top,max_path_sum.res)
	print "THe max top is %d" %max_top
	return max_simple
# print max_path_sum(t)

def max_path(node):
	max_path_sum.res = float("-inf")
	max_path_sum(node)
	return max_path_sum.res

root = Tree(10)
root.left = Tree(2)
root.right   = Tree(11);
root.left.left  = Tree(20);
root.left.right = Tree(1);
root.right.right = Tree(-25);
root.right.right.left   = Tree(3);
root.right.right.right  = Tree(4);
print max_path(root);