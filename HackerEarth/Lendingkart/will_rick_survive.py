def check(a):
	size = 3
	count = 0; i = 1; last_reload = 0
	while i < len(a):
		if a[i]:
			reload = (count + a[i] - 1) / size
			if count + a[i] + reload > i:
				buggers = count % size
				rem = i-((size+1)*last_reload)
				rem_reload = ( rem / (size+1) )
				rem_walker = rem - rem_reload
				print "last reload", last_reload
				print "Goodbye Rick"; print count + rem_walker - buggers; return
			count += a[i]
			last_reload = reload
		i += 1
	print "Rick now go and save Carl and Judas"

def main():
	T = int(raw_input())
	for i in range(T):
		n = int(raw_input())
		x = [0] * 50001
		s = [int(each) for each in raw_input().split()]
		for each in s:
			x[each] += 1
		check(x)
main()
