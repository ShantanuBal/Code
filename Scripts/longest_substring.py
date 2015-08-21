a = "microsoft"
b = "mwecrosaxft"


def find(a,b):
	a = "0"+a
	b = "0"+b
	opt = [ [0 for i in range(len(a))] for j in range(len(b))]
	
	opt[1][2] = 2
	
	for each in opt:
		print each

find(a,b)
