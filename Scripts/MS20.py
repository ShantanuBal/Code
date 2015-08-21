#circular linked list

hashtable = {}

class LinkedList():
	def __init__(self,key):
		self.key = key
		self.next = None

def traverse(node):
	if node == None or node in hashtable:
		if node != None:
			print node.key
		return
	print node.key, 
	hashtable[node] = node.key
	traverse(node.next)


root = LinkedList(1); root.next = LinkedList(2); root.next.next = LinkedList(3); root.next.next.next = LinkedList(4); root.next.next.next.next = LinkedList(5); root.next.next.next.next.next = LinkedList(6); link = root.next.next

root.next.next.next.next.next.next = link
traverse(root)
print
for each in hashtable:
	print each, hashtable[each]
