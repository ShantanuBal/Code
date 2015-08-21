

class LL():
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

def print_list(head):
	while head != None:
		print head.data," ",
		head = head.next
	print

def mergeList(head1, head2):
	if head1 == None:
		return head2
	if head2 == None:
		return head1
	if head1.data < head2.data:
		head1.next = mergeList(head1.next, head2)
		return head1
	else:
		head2.next = mergeList(head1, head2.next)
		return head2

def getListHalves(head):
	slow = head
	fast = head
	while fast.next != None and fast.next.next != None:
		slow = slow.next
		fast = fast.next.next
	back_head = slow.next
	slow.next = None
	return back_head

def mergeSort(head):
	print "mergeSort: "
	print_list(head)
	print

	if head.next == None:
		return head

	head_back = getListHalves(head)
	head_front = head

	new_head1 = mergeSort(head_front)
	new_head2 = mergeSort(head_back)
	new_head = mergeList(new_head1, new_head2)
	print "mergedList: "
	print_list(new_head)
	print

	return new_head

head = LL(7, LL(6, LL(5, LL(4, LL(3, LL(2, LL(1)))))))
final_head = mergeSort(head)
print_list(final_head)
