
class LL():
	def __init__(self, data, next=None, random=None):
		self.data = data
		self.next = next
		self.random = random

def print_list(node):
	while node != None:
		print node.data, "\t", node.random.data if node.random else "NULL"
		node = node.next
	print

head = LL(1, LL(4, LL(10, LL(12, LL(9, LL(5, LL(1, LL(2, LL(6, LL(8, LL(13, LL(9, LL(6, LL(2, LL(4, LL(7, LL(6, LL(2, LL(1)))))))))))))))))))

def calculate(head):
	stack = [head]
	current = head.next

	rotation = 0
	while current != None and rotation < 2:
		"""
		if current.data > prev.data:
			prev.random = current
		else:
			stack.append(prev)
		"""
		while stack and stack[-1].data < current.data:
			top = stack.pop()
			top.random = current
		stack.append(current)
		
		if current.next == None:
			current = head
			rotation += 1
		else:
			current = current.next
		
		"""
		prev = current
		current = current.next
		"""

calculate(head)
print_list(head)
