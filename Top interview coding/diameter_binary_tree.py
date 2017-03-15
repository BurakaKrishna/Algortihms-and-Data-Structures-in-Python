class Node():
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

def height(Node):
	if Node is None:
		return 0
	l = height(Node.left)
	r = height(Node.right)
	if l > r:
		return l+1
	else:
		return r+1

def diameter(Node):
	if Node is None:
		return 0	
	ldia = diameter(Node.left)
	rdia = diameter(Node.right)
	lheight = height(Node.left)
	rheight = height(Node.right)
	return max(lheight+rheight+1,max(ldia,rdia))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Diameter of given binary tree is %d" %(diameter(root))