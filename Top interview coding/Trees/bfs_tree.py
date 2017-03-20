class Node():
	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

# function to find height of the tree:
def height(node):
	if node is None:
		return 0
	else:
		lheight = height(node.left)
		rheight = height(node.right)
		if rheight>lheight:
			return rheight+1
		else:
			return lheight+1

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# print height(root) 
# /*Function to print level order traversal of tree*/
def printLevelorder(tree):
	for d in xrange(height(tree)):
		printGivenLevel(tree, d+1)

# /*Function to print all nodes at a given level*/
def printGivenLevel(tree, level):
	if tree is None:
		return 0
	if level == 1:
		print tree.data
	elif level >1:
		printGivenLevel(tree.left, level-1)
		printGivenLevel(tree.right, level-1)

# printGivenLevel(root,3)
printLevelorder(root)