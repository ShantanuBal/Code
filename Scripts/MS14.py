# Bridge game

a = [4,2,6,2,2,1,4,0,0,0,1]

def find(a):

	max = a[0]
	i = 1
	while i <= max:
		print max
		if max >= len(a):
			print "YES"
			return
		lar = max
		while i <= max:
			if a[i]+i > lar:
				lar = a[i]+i
			i += 1
		max = lar
	print "NO"
		
find(a)
