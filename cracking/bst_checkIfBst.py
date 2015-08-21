

class BT():
	def __init__(self, data, left = None, right = None, parent = None):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

class prev_node():
	def __init__(self, node=None):
		self.node = node

def in_order(node):
	if node == None:
		return
	in_order(node.left)
	print node.data, " ",
	in_order(node.right)

prev = prev_node()

def is_bst(node, prev):

	if node == None:
		return True
	if is_bst(node.left, prev) == False:
		return False
	if prev.node and prev.node.data > node.data:
		return False
	print prev.node.data if prev.node else "NULL", node.data
	prev.node = node
	if is_bst(node.right, prev) == False:
		return False
	return True


A = BT(50)
B = BT(30)
C = BT(20)
D = BT(40)
E = BT(70)
F = BT(45)
G = BT(90)
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
print
print is_bst(A, prev)
