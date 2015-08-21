v1 = 20
v2 = 40

class BT():
        def __init__(self, data, left = None, right = None, parent = None):
                self.data = data
                self.left = left
                self.right = right


def in_order(node, list, sum):
        if node == None:
                return
        in_order(node.left, list, sum)
        list.append(node.data)
	sum += node.data
	print node.data, " ",
        in_order(node.right, list, sum)

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

list = []
sum = 0
in_order(A, list, sum)

print "\n", list, "\n", sum
