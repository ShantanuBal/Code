# find lowest common ancestor
x, y = 2, 100

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

def find_ancestor(node, x, y):
	if node == None:
		return None
	if node.key in [x,y]:
		return 1

	left_tree = find_ancestor(node.left, x, y)
	right_tree = find_ancestor(node.right, x, y)

	if left_tree == right_tree == 1:
		print "\n", node.key
		exit(0)

	if left_tree == 1 and right_tree == None:
		return 1

	if right_tree == 1 and left_tree == None:
		return 1

	if right_tree == left_tree == None:
		return None

root = BinTree(10); root.right = BinTree(20); root.left = BinTree(5); root.right.right = BinTree(30); root.right.left = BinTree(15); root.left.left = BinTree(1); root.left.right = BinTree(8); root.right.right.right = BinTree(35); root.right.right.left = BinTree(25); traverse(root)

if find_ancestor(root, x, y) in [1,None]:
	print "\nNot found"
