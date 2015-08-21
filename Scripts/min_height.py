# create BST

a = [1,2,3,4,5,6,7]

class BinTree():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.key, 
	traverse(node.right)

def create(a):
	if len(a) == 0:
		return None
	if len(a) == 1:
		return BinTree(a[0])
	m = len(a)/2
	node = BinTree(a[m])
	node.left = create(a[:m])
	node.right = create(a[m+1:])
	return node

root = create(a)
traverse(root)
