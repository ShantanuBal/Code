# paranthesis

num = int(input())

def check(string,l,r):
	if not l and not r:
		print string; 
		return	
	if l<r:
		check(string+")",l,r-1)
	if l:
		check(string+"(",l-1,r)

check("",num,num)
