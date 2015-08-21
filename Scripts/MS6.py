# prefix tree

class PT():
	def __init__(self, value, word):
		self.value = value
		self.pointers = {}
		self.word = word

def add(string, node):
	first = string[0]
	string = string[1:]
	if string:
		word = 0
	else:
		word = 1
	if first not in node.pointers:
		node.pointers[first] = PT(node.value+first,word)
	if string:
		add(string,node.pointers[first])

def traverse(node):
	print node.value, node.word
	for each in node.pointers:
		traverse(node.pointers[each])

strings = ["A", "to", "tea", "ted", "ten", "i", "in", "inn"]
root = PT("", 0)

for each in strings:
	add(each, root)

print "ROOT:",root.value," pointers:",root.pointers
traverse(root)
