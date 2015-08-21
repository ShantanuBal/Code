# convert bst to double linked list

class BST():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.value, 
	traverse(node.right)

def convert(node):
	global last, first
	if node == None:
		return
	convert(node.left)
	if last == None:
		last = node
		first = node
	else:
		last.right = node
		node.left = last
		last = node
	convert(node.right)

def trav_l(node):
	if node == None:
		return
	print node.value, 
	trav_l(node.left)

def trav_r(node):
	print node.value,
	if node.right == None:
		print "\n"
		trav_l(node.left)
	else:
		trav_r(node.right)

last = None
first = None
root = BST(20)
root.left = BST(10)
root.right = BST(30)
root.left.right = BST(15)
root.right.right = BST(35)
root.right.left = BST(25)

print "\nIn Order traversal:",
traverse(root)

print "\n\nConvert:", 
convert(root)
trav_r(first)

print "\n"
