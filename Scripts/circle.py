# linked list with a cycle

class ListElem():
	def __init__(self, key, next=None):
		self.key = key
		self.next = next

def detect_cycle(root):

	fir = root.next
	sec = root.next.next
	print fir.key, sec.key
	while sec != fir:
		fir = fir.next
		sec = sec.next.next
		print fir.key, sec.key

	fir = root
	while fir != sec:
		fir = fir.next
		sec = sec.next
	print fir.key

def traverse(node):
	print 
	print node.key,
	node = node.next
	while node!= None:
		print " -> ", node.key,
		last = node
		node = node.next
	print "\n"
	return last

root = ListElem(1,ListElem(2,ListElem(3,ListElem(4,ListElem(5,ListElem(6,ListElem(7,ListElem(8,ListElem(9)))))))))
last = traverse(root)
head = root.next.next.next
last.next = head

detect_cycle(root)
print
