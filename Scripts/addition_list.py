# adding up elements in a list

class ListElem():
	def __init__(self, key):
		self.key = key
		self.next = None


def add(node1, node2, carry):
	if node1 == node2 == None:
		if carry:
			return ListElem(carry)
		return None

	if node1 == None: first = 0
	else: first = node1.key
	
	if node2 == None: second = 0
	else: second = node2.key
	
	sum = first + second + carry
	ones = sum%10
	carry = sum/10
	head = ListElem(ones)
	
	if node1 == None:
		head.next = add(None, node2.next, carry)
	elif node2 == None:
		head.next = add(node1.next, None, carry)
	else:
		head.next = add(node1.next, node2.next, carry)
	return head

def traverse(node):
	print
	while node != None:
		print node.key,"->",
		node = node.next
	

root1 = ListElem(3)
root1.next = ListElem(1)
root1.next.next = ListElem(9)

root2 = ListElem(5)
root2.next = ListElem(9)
root2.next.next = ListElem(2)

root3 = add(root1,root2,0)
traverse(root1); traverse(root2); traverse(root3)
