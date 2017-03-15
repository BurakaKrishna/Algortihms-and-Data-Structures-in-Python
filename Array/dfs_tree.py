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
def inorder_DFS(node):
	if node:
		inorder_DFS(node.left)
		print node.data
		inorder_DFS(node.right)

def postorder_DFS(node):
	if node:
		postorder_DFS(node.left)
		postorder_DFS(node.right)
		print node.data
def preorder_DFS(node):
	if node:
		print node.data
		preorder_DFS(node.left)
		preorder_DFS(node.right)

# DFS(root)
root = Node(1)
root.left	 = Node(2)
root.right	 = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal is "
preorder_DFS(root)
print "Postorder traversal is "
postorder_DFS(root)
print "Inorder traversal is "
inorder_DFS(root)