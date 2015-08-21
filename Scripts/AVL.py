class AVL():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.height = 0
root = AVL(30)

def height(node):
	if node == None:
		return -1
	return node.height

def right_rotate(y):
	x = y.left
	t = x.right

	x.right = y
	y.left = t

	y.height = max(height(y.left), height(y.right)) + 1
	x.height = max(height(x.left), height(x.right)) + 1
	
	return x

def left_rotate(x):
	y = x.right
	t = y.left

	y.left = x
	x.right = t

	y.height = max(height(y.left), height(y.right)) + 1
	x.height = max(height(x.left), height(x.right)) + 1

	return y

def insert(node, key):
	if node == None:
		return AVL(key)
	if key >= node.key:
		node.right = insert(node.right, key)
	elif key <= node.key:
		node.left = insert(node.left, key)

	node.height = max(height(node.left),height(node.right)) + 1

	balance = height(node.left) - height(node.right)

	# LL
	if balance > 1 and key < node.left.key:
		return right_rorate(node)
	# RR
	elif balance < -1 and key > node.right.key:
		return left_rotate(node)
	# LR
	elif balance > 1 and key > node.left.key:
		left_rorate(node.left)
		return right_rotate(node)
	# RL
	elif balance < -1 and key < node.right.key:
		right_rotate(node.right)
		return left_rotate(node.right)
	
	return node

def traverse(node, route=""):
	if node == None:
		return
	traverse(node.left, route+"L")
	print node.key, "\t", height(node), "\t", str(height(node.left) - height(node.right)), "\t", route
	traverse(node.right, route+"R")

while(True):
	root = insert(root,int(input("Insert element: ")))
	print "\nkey \t hei \t bal \t route"
	traverse(root)
