class LL():
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

head = LL(2, LL(3, LL(4, LL(5, LL(6, LL(7, LL(8, LL(9, LL(8, LL(4, LL(10, None)))))))))))

def print_list(head):
	current = head
	while current != None:
		print current.data," ",
		current = current.next


def remove_dup(head):
	if head == None:
		return None
	prev = head
	current = head.next
	while current != None:
		runner = head
		while runner != current:
			if runner.data == current.data:
				prev.next = current.next
				current = prev
				break

			runner = runner.next
		
		prev = current
		current = current.next
	print_list(head)
	
print_list(head)
print
remove_dup(head)
