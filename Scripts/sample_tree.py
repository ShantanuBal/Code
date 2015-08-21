# find lowest common ancestor

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


root = BinTree(10); root.right = BinTree(20); root.left = BinTree(5); root.right.right = BinTree(30); root.right.left = BinTree(15); root.left.left = BinTree(1); root.left.right = BinTree(8); root.right.right.right = BinTree(35); root.right.right.left = BinTree(25); traverse(root)
