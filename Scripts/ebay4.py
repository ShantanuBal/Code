# graphs

class GraphNode():
	def __init__(self, value):
		self.value = value
		self.adj = []

visited_DFS = {}
def DFS(node):
	if node.value not in visited_DFS:
		print node.value
		visited_DFS[node.value] = 1
		for each in node.adj:
			DFS(each)

visited_BFS = {}
queue = []
def BFS():
	while queue:
		node = queue.pop(0)
		if node.value not in visited_BFS:
			print node.value
			visited_BFS[node.value] = 1
			for each in node.adj:
				queue.append(each)


a = GraphNode('a')
b = GraphNode('b')
a.adj.append(b)
c = GraphNode('c')
a.adj.append(c)
d = GraphNode('d')
b.adj.append(d)
c.adj.append(d)

print "DFS"
DFS(a)

print "\nBFS"
queue.append(a)
BFS()
