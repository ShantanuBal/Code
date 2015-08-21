dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i']}

def find(a, b, c):
	for x in a:
		for y in b:
			for z in c:
				print x,y,z

find(dict[2],dict[3],dict[4])
