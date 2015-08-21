#no recursion while traversing tree

class BinTree():
	def __init__(self, key, left = None, right = None):
		self.key = key
		self.left = left
		self.right = right

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.key,
	traverse(node.right)

def no_rec(node):
	stack = [node]
	while stack:
		print "stack len: ", len(stack)
		elem = stack.pop()
		#if elem in [30,20,10,25,50,40,55,52]:
		if not isinstance( elem, BinTree):
			print elem,
		else:
			if elem.right != None:
				stack.append(elem.right)
			stack.append(elem.key)
			if elem.left != None:
				stack.append(elem.left)

root = BinTree(30, BinTree(20, BinTree(10), BinTree(25)), BinTree(50, BinTree(40), BinTree(55, BinTree(52))))
traverse(root)
print
no_rec(root)
