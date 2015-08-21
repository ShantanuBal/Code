def main():
	[N,t] = [int(each) for each in raw_input().split()]
	luck = [N] * N; luck[0] = 0
	link = []
	for each in range(N):
		link.append([])

	for each in range(t):
		[p1,p2] = [int(each) for each in raw_input().split()]
		link[p1].append(p2)
		link[p2].append(p1)
	#print "luck ", luck
	#print "link ", link

	level = 1
	queue = [link[0]]
	while queue:
		next_element = []
		element = queue.pop(0)
		#print "element", element
		for i in element:
			if level < luck[i]:
				luck[i] = level
				next_element += link[i]
		if next_element:
			queue.append(next_element)
		level += 1
	
	for each in luck[1:]:
		if each == N:
			print '-1'
		else:
			print each
main()
