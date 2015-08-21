

class LL():
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

last = LL(7)
head = last
last.next = head

def print_list(head):
	while head.data != 7:
		print head.data, " ",
		head = head.next
	print head.data

def detect_loop(head):
	if head == None:
		return False
	slow = head
	fast = head

	while fast != None:
		if fast.next != None and fast.next.next != None:
			fast = fast.next.next
			slow = slow.next
		else:
			return False
		if fast == slow:
			return True
	return False

print_list(head)
print detect_loop(head)
