t = 5
n = t-1

def move(i, j, path):
	if i == n or j == n:
		return
	elif i == j == n-1:
		print path
	else:
		
		move(i+1,j, path+"e")
		move(i,j+1, path+"s")

move(0,0,"")
