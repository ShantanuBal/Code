N = int(raw_input())

for i in range(N):
	[k,n] = [int(j) for j in raw_input().split(' ')]
	count = (k**(n+1) - 1)/(k - 1)
	w = 0
	while count!=0:
		w += count%10
		count /= 10
	print w	
