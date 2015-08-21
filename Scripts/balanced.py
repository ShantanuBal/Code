# is balanced tree?

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

def check_balance(node):
	if node == None:
		return -1

	h1 = check_balance(node.left)
	h2 = check_balance(node.right)

	if abs(h1-h2) > 1:
		print "\nNot balanced at:", node.key
		#exit(0)
	return 1+max(h1,h2)

root = BinTree(10); root.right = BinTree(20); root.left = BinTree(5); root.right.right = BinTree(30); root.right.left = BinTree(15); root.left.left = BinTree(1); root.left.right = BinTree(8); root.right.right.right = BinTree(35); root.right.right.left = BinTree(25); root.right.right.right.right = BinTree(100); traverse(root)

print "\n"
print check_balance(root)
