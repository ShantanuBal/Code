# trees

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left  = None
		self.right = None

def traversal(node):
	if node == None:
		return
	traversal(node.left)
	print node.value, 
	traversal(node.right)


equal = True
def is_equal(node1, node2):
	global equal
	if node1 == node2 == None:
		return
	elif node1 == None or node2 == None:
		equal = False
		return
	if node1.value == node2.value:
		is_equal(node1.left, node2.left)
		is_equal(node1.right, node2.right)
	else:
		equal = False
		return

sym = True
def is_sym(node1, node2):
	global sym
	if node1 == node2 == None:
		return
	elif node1 == None or node2 == None:
		sym = False
		return
	if node1.value == node2.value:
		is_sym(node1.left, node2.right)
		is_sym(node1.right, node2.left)
	else:
		sym = False
		return

root = BinaryTree(20)
root.left = BinaryTree(10)
root.right = BinaryTree(30)
root.right.right = BinaryTree(40)
root.right.left = BinaryTree(25)

root2 = BinaryTree(20)
root2.right = BinaryTree(10)
root2.left = BinaryTree(30)
root2.left.left = BinaryTree(40)
root2.left.right = BinaryTree(25)

traversal(root)
print
traversal(root2)

is_equal(root, root2)
print "\nIs equal?", equal

is_sym(root, root2)
print "Is symmetric?", sym
