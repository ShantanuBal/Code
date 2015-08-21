# pond problem

a = 	[
		[0,0,1,1,1],
		[0,0,1,1,0],
		[1,1,1,0,0],
		[1,1,1,1,1],
		[0,0,0,1,0]

	]

count = 0

def fill(i,j):
	if i<0 or i>=len(a) or j<0 or j>=len(a):
		return
	if a[i][j] == 0:
		a[i][j] = 1
		fill(i+1,j); fill(i-1,j); fill(i,j+1); fill(i,j-1)
		fill(i+1,j+1); fill(i+1,j-1); fill(i-1,j-1); fill(i-1,j+1)


def find_ponds():
	global count
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i][j] == 0:
				fill(i,j)
				count += 1
				for each in a:
					print each
				print
	print "No. of ponds:",count

find_ponds()
