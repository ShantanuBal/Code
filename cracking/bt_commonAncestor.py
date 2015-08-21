v1 = 20
v2 = 40

class BT():
        def __init__(self, data, left = None, right = None, parent = None):
                self.data = data
                self.left = left
                self.right = right


def in_order(node):
        if node == None:
                return
        in_order(node.left)
        print node.data, " ",
        in_order(node.right)

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
E.left = F
E.right = G

in_order(A)
print

def find(node, A, B):
	if node == None:
		return False
	if node.data == A:
		return A
	if node.data == B:
		return B
	
	inLeftTree = find(node.left, A, B)
	inRightTree = find(node.right, A, B)

	if isinstance(inLeftTree, BT):
		return inLeftTree
	if isinstance(inRightTree, BT):
		return inRightTree
	if (inLeftTree == A and inRightTree == B) or (inLeftTree == B and inRightTree == A):
		return node
	if inLeftTree == True or inRightTree == True:
		return True
	return False

ancestor = find(A, v1, v2)
if isinstance(ancestor, BT):
	print ancestor.data
