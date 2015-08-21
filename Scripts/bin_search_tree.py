class BinTree():
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

is_bst = True
def check(node):
	global is_bst
	if node.right != None:
		if node.right.value >= node.value:
			check(node.right)
		else:
			is_bst = False
	if node.left != None:
		if node.left.value <= node.value:
			check(node.left)
		else:
			is_bst = False

root = BinTree(5)
root.left = BinTree(2)
root.right = BinTree(12)
root.left.right = BinTree(1)
check(root)
print is_bst
