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
	if node.left is None and node.right is None:
		return node.data
	if node.left is not None and node.right is not None:
		print node.data
		return max(max_path_sum(node.right)+node.data,max_path_sum(node.left)+node.data,max_path_sum(node.right)+max_path_sum(node.left)+node.data,node.data)
	if node.left is None:
		# print 3
		return max_path_sum(node.right)+node.data

# print max_path_sum(t)




root = Tree(10)
root.left = Tree(2)
root.right   = Tree(11);
root.left.left  = Tree(20);
root.left.right = Tree(1);
root.right.right = Tree(-25);
root.right.right.left   = Tree(3);
root.right.right.right  = Tree(4);
print max_path_sum(root);