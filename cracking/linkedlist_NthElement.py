class LL():
        def __init__(self, data, next = None):
                self.data = data
                self.next = next

N = 4
head = LL(2, LL(3, LL(4, LL(5, LL(6, LL(7, LL(8, LL(9, LL(8, LL(4, LL(10, None)))))))))))

def print_list(head):
	current = head
	while current != None:
		print current.data
		current = current.next

def find_element(head, n):
	current = head
	i = 0
	while i < n:
		current = current.next
		i += 1
	
	follower = head
	while current != None:
		follower = follower.next
		current = current.next

	print follower.data

find_element(head, N)

