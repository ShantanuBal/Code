adj = {'a':['b', 'd'], 'b':['c','e'], 'c':[], 'e':[], 'd':[]}
#adj = {'a':{'left':'b', 'right':'d'}, 'b':{'left':'c','right':'e'}, 'c':[], 'e':[], 'd':[]}

visited = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
parent = {}

stack = ['a']
prev = ['']
height = [0]

def DFS():
	while stack:
		node = stack.pop()
		prev_n = prev.pop()
		height_n = height.pop()
		if not visited[node]:
			parent[node] = prev_n
			print node, height_n
			for each in adj[node][::-1]:
				stack.append(each)
				prev.append(node)
				height.append(height_n + 1)

DFS()
#in_order('a')
