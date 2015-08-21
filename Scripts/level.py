class BinaryTree:
	def __init__(self, node_value):
		self.left = None
		self.right = None
		self.value = node_value

def display(root):
	print root.value
	if root.left:
		display(root.left)
	if root.right:
		display(root.right)

root = BinaryTree(1)
main_root = root
root.left = BinaryTree(2)
root.right = BinaryTree(3)
node = root.left
node.left = BinaryTree(4)
node.right = BinaryTree(5)
root = root.right
root.left = BinaryTree(6)
root.right = BinaryTree(7)
node = root.left
node.right = BinaryTree(8)
node = root.right
node.right = BinaryTree(9)
#display(main_root)

hashtable = {}
min, max = 100, -100

def find(node, dist):
	#print node.value, dist
	global max, min
	if dist > max:
		max = dist
	if dist < min:
		min = dist

	if dist in hashtable:
		hashtable[dist].append(node.value)
	else:
		hashtable[dist] = [node.value]
	if node.left != None:
		find(node.left, dist+1)
	if node.right != None:
		find(node.right, dist+1)

find(main_root,0)
for i in range(min, max+1):
	if i in hashtable:
		print hashtable[i]
"""
def insert(node, value):
	if value > node:
		if node.right == None:
			node.right = BinaryTree(value)
		else:
			insert(node.right, value)
	else:
		if node.left == None:
			node.left = BinaryTree(value)
		else:
			insert(node.left, value)
"""
