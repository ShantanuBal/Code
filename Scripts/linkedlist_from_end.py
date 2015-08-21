class List():
	def __init__(self, key, next=None):
		self.key = key
		self.next = next

k = 4

def k_from_last(k, head):
	node = head
	for i in range(k):
		if node == None:
			return "List not long enough."
		node = node.next
	start = head
	while node != None:
		node = node.next
		start = start.next
	return start

def build():
	return List(5,List(10,List(15,List(20,List(25,List(30,List(35,List(40,List(45,List(50))))))))))

def traverse(head):
	while head != None:
		print head.key, 
		head = head.next

head = build()
print
traverse(head)
print
print
print (k_from_last(k, head)).key
