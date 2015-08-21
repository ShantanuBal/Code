# reversing linked list

class LL():
	def __init__(self, value):
		self.value = value
		self.next  = None

def traverse(node):
	if node == None:
		return
	print node.value,
	traverse(node.next)


def reverse(root):
	pre = None
	cur = root
	nex = root.next
	while nex != None:
		cur.next = pre
		pre = cur
		cur = nex
		nex = nex.next
	cur.next = pre
	print "\n"
	traverse(cur)

root = LL(1)
root.next = LL(2)
root.next.next = LL(3)
root.next.next.next = LL(4)
root.next.next.next.next = LL(5)

traverse(root)
reverse(root)
