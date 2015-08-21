def check(a):
	count = 0; i = 1
	print a
	while i < len(a):
		if a[i]:
			count += 1
			if not count % 6:
				a = a[2:] + [0,0]
				a[i-2] -= 1
				i -= 2
			else:
				a = a[1:] + [0]
				a[i-1] -= 1
				i -= 1
			print a	
			if a[i] > i:
				print "Goodbye Rick"; print count + i; return
		else:
			i += 1
	print "Rick now go and save Carl and Judas"

def main():
	T = int(raw_input())
	for i in range(T):
		n = int(raw_input())
		x = [0] * 50001
		s = [int(each) for each in raw_input().split()]
		count,reload = 0,0
		for each in s:
			count += 1
			if count%6 == 0:
				reload += 1
			x[each] += 1
			if x[each] > each:
				print "Goodbye Rick"; print count-1; break
		else:
			print "Rick now go and save Carl and Judas"
		#check(x)
main()
