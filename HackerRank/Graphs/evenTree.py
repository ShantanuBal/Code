import time
start_time = time.time()

def select_leaf(adj, m, n):
	for i in range(1,len(adj)):
		if len(adj[i]) == 1:
			return i

def start(adj, m, n):
	flag = 1
	while flag:
		p = select_leaf(adj, m, n)
		q = pop(adj[p])
		flag = 0

def main():
	[n, m] = [int(each) for each in raw_input().split()]
	adj = []
	for i in range(n):
		adj.append([])
	adj.append([])
	for i in range(m):
		[x, y] = [int(each) for each in raw_input().split()]
		adj[x].append(y); adj[y].append(x)
	"""
	#print adj list
	for i in range(1,n+1):
		print i, " -- ", adj[i]
	"""
	print 
	start(adj, m, n)

main()

print time.time() - start_time
