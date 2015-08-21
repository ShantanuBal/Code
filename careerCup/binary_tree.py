class BinaryTree():
	def __init__(self, node_value):
		self.left = None
		self.right = None
		self.value = node_value

def insert(node, node_value):
	if node_value > node.value:
		if node.right == None:
			node.right = BinaryTree(node_value)
		else:
			insert(node.right, node_value)
	else:
		if node.left == None:
			node.left = BinaryTree(node_value)
		else:
			insert(node.left, node_value)

def printTree(node):
	if node.left != None:
		printTree(node.left)
	print node.value
	if node.right != None:
		printTree(node.right)

max = 0; min = 1000
def DFS(node, height):
	print node.value, "height:", height
	global max, min
	if node.left == None and node.right == None:
		if height > max:
			max = height
		if height < min:
			min = height
	if node.left != None:
		DFS(node.left, height+1)
	if node.right != None:
		DFS(node.right, height+1)

queue = []
def BFS():
	while queue:
		node = queue.pop(0)
		print node.value
		if node.left != None:
			queue.append(node.left)
		if node.right != None:
			queue.append(node.right)

root = BinaryTree(10)
insert(root,4); insert(root,0); insert(root,9); insert(root,21); insert(root,6); insert(root,11); insert(root,7); insert(root,3); #insert(root,12)
#print root.value
#printTree(root)
DFS(root, 0)
#queue.append(root)
#BFS()
print max
print min
