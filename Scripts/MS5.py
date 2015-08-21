# Is B-tree a BST?

class BinaryTree():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.value
	traverse(node.right)

is_bst = True

def check(node):
	global is_bst
	if node.left:
		if node.left.value > node.value:
			is_bst = False
			return
		check(node.left)
	if node.right:
		if node.right.value < node.value:
			is_bst = False
			return
		check(node.right)

root = BinaryTree(20)
root.left = BinaryTree(10)
root.right = BinaryTree(30)
root.right.right = BinaryTree(40)
root.right.left = BinaryTree(25)
root.left.left = BinaryTree(100)

traverse(root)
check(root)
print "\nIs BST?", is_bst
