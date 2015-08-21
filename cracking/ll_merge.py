

class LL():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

head1 = LL(1, LL(3, LL(5, LL(7))))
head2 = LL(2, LL(4, LL(6)))

def merge(head1, head2):
	if head1 == None:
		return head2
	if head2 == None:
		return head1
	if head1.data < head2.data:
		head1.next = merge(head1.next, head2)
		return head1
	else:
		head2.next = merge(head1, head2.next)
		return head2

head = merge(head1, head2)

while head != None:
	print head.data, " ",
	head = head.next
print


