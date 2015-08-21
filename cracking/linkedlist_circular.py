class LL():
        def __init__(self, data, next = None):
                self.data = data
                self.next = next

middle = LL(5)
head1 = LL(6, LL(7, LL(8, LL(9, middle))))
middle.next = head1
head = LL(2, LL(3, LL(4, LL(10, LL(11, LL(12, LL(13, LL(14, middle))))))))

def print_list(head, middle):
	current = head
	while current != middle:
		print current.data, " ",
		current = current.next
	print current.data, " ",

	current = current.next
	while current != middle:
		print current.data, " ",
		current = current.next
	print current.data
	print

def find_first_node(head):
	slow_runner = head.next
	fast_runner = head.next.next
	while fast_runner != slow_runner:
		slow_runner = slow_runner.next
		fast_runner = fast_runner.next.next
	print slow_runner.data

	runner = head
	while runner != slow_runner:
		runner = runner.next
		slow_runner = slow_runner.next
		print slow_runner.data
	print runner.data

print_list(head, middle)

find_first_node(head)
