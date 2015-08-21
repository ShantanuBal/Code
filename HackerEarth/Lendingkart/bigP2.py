def main():
	[N,t] = [int(each) for each in raw_input().split()]
	a = [-1] * N; a[0] = 0
	store = []
	for each in range(t):
		[p1,p2] = [int(each) for each in raw_input().split()]
		if a[p1] == 0:
			a[p2] = 1
		elif a[p2] == 0:
			a[p1] = 1
		else:
			store.append([p1,p2])
	print a
	for each in store:
		p1, p2 = each[0], each[1]
		print p1,p2
		if a[p1] == -1:
			a[p1] = [p2]
		else:
			a[p1].append(p2)
		if a[p2] == -1:
			a[p2] = [p1]
		else:
			a[p2].append(p1)
	print a

		
	#for each in a[1:]:
	#print each
main()
