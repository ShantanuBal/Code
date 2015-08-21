count = 0
class BinaryTree():
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

def insert(node, value):
	if value < node.value:
		if node.left == None:
			node.left = BinaryTree(value)
		else:
			insert(node.left, value)
	else:
		if node.right == None:
			node.right = BinaryTree(value)
		else:
			insert(node.right, value)

def traversal(node):
	global count
	if node.left != None:
		traversal(node.left)
	count += 1
	print node.value
	if node.right != None:
		traversal(node.right)

root = BinaryTree(10)
insert(root,4); insert(root,15); insert(root,20); insert(root,1); insert(root,5); insert(root,11); insert(root,25); insert(root,14); insert(root,7);
traversal(root)

