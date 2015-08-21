# least common ancestor

# a and b are the search nodes
a = 15
b = 45

class BinaryTree():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# in order traversal
def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.value,
	traverse(node.right)

# finding lowest common ancestor in binary SEARCH tree
def find_common_bst(x, y, node):
	if node == None:
		return
	if node.value < x and node.value < y:
		find_common_bst(x, y, node.right)
	if node.value > x and node.value > y:
		find_common_bst(x, y, node.left)
	if ( x <= node.value <= y ) or ( y <= node.value <= x ):
		print "\nThe answer is:", node.value
		return
	
# finding lowest common ancestor in binary tree
def find_common_btree(x, y, node):
	if node == None:
		return None

	if node.value == x:
		return x

	if node.value == y:
		return y

	left = find_common_btree(x, y, node.left)
	right = find_common_btree(x, y, node.right)

	if left and right:
		print "The answer is:", node.value
	if left:
		return left
	if right:
		return right

# main function starts here

# This represents the following binary tree (which is also a binary search tree)
#			20
#		10		30
#	    5       15                40
#				   35    45

root = BinaryTree(20)
root.left = BinaryTree(10)
root.right = BinaryTree(30)
root.left.left = BinaryTree(5)
root.left.right = BinaryTree(15)
root.right.right = BinaryTree(40)
root.right.right.right = BinaryTree(45)
root.right.right.left = BinaryTree(35)

# in - order traversal
traverse(root)

# find common ancestor in BST
find_common_bst(a, b, root)

# find common ancestor in Binary Tree
find_common_btree(a, b, root)
