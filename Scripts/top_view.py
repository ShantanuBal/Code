# top view
"""
			20
	10				30
5		15		25		35

"""
class BinTree():
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

root = BinTree(20, BinTree(10, BinTree(5), BinTree(15)), BinTree(30, BinTree(25), BinTree(35)))

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.key,
	traverse(node.right)

traverse(root)
print
