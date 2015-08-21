

class BT():
	def __init__(self, data, left = None, right = None, parent = None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent


def in_order(node):
	if node == None:
		return
	in_order(node.left)
	print node.data, " ",
	in_order(node.right)

def find_next(node):
	print 
	if node == None:
		return "Invalid Node"
	if node.right != None:
		next = node.right
		while next.left != None:
			next = next.left
		return next.data
	
	while node.parent != None:
		if node.parent.left == node:
			return node.parent.data
		if node.parent.right == node:
			node = node.parent
	return "this node has no parent"

A = BT(50)
B = BT(30)
C = BT(20)
D = BT(40)
E = BT(70)
F = BT(60)
G = BT(80)
A.left = B
A.right = E
B.left = C
B.right = D
B.parent = A
E.left = F
E.right = G
E.parent = A
C.parent = B
D.parent = B
F.parent = E
G.parent = E

in_order(A)
print find_next(G)
