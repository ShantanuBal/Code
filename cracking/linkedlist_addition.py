class LL():
        def __init__(self, data, next = None):
                self.data = data
                self.next = next

N = 4
head1 = LL(2, LL(3, LL(4)))
head2 = LL(5, LL(7, LL(5)))

def print_list(head):
        current = head
        while current != None:
                print current.data,
                current = current.next
	print


def add(head1, head2):
	head_ans = LL(0)
	first = head_ans
	carry = 0
	print_list(head1)
	print_list(head2)
	while head1 != None or head2 != None:
		h1 = 0 if head1 == None else head1.data
		h2 = 0 if head2 == None else head2.data
		total = (h1 + h2 + carry)

		carry = total / 10
		head1 = None if head1 == None else head1.next
		head2 = None if head2 == None else head2.next
		
		new_node = LL(total % 10)
		head_ans.next = new_node
		head_ans = new_node
	if carry:
		head_ans.next = LL(1)
	print_list(first.next)

add(head1, head2)
