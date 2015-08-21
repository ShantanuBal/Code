

class LL():
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

head = LL(1, LL(2, LL( 3, LL(4, LL(5, LL(6, None))))))

def print_list(head):
	while head != None:
		print head.data, " ",
		head = head.next
	print

def reverse_list(head):

	prev = None
	current = head
	while current != None:
		next = current.next
		current.next = prev
		prev = current
		current = next
	return prev
		

print_list(head)
new_head = reverse_list(head)
print_list(new_head)
