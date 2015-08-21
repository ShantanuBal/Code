
class BinTree():
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

def traverse(node):
	if node == None:
		return
	traverse(node.left)
	print node.key, 
	traverse(node.right)

def line_order(node):
	q = [node]
	while (len(q) != 0):
		node = q.pop(0)
		if node == None:
			continue
		print node.key,
		q.append(node.left)
		q.append(node.right)

def rev_order(node):
	s1, s2 = [node], []

	while len(s1) != 0 or len(s2) != 0:
		while len(s1) != 0:
			node = s1.pop()
			if node == None:
				continue
			print node.key,
			s2.append(node.right)
			s2.append(node.left)
		while len(s2) != 0:
			node = s2.pop()
			if node == None:
				continue
			print node.key,
			s1.append(node.left)
			s1.append(node.right)

def build_tree():
	root = BinTree(30,
			BinTree(20,
				BinTree(10,
					BinTree(5,None,None),
					BinTree(15,None,None)
					),
				BinTree(25,None,None)
				), 
			BinTree(50,
				BinTree(40,
					BinTree(35,None,None),
					BinTree(45,None,None)
					),
				BinTree(55,None,None)
				)
			)
	return root

root = build_tree()
print
traverse(root)
print
print
line_order(root)
print
print
rev_order(root)
print
