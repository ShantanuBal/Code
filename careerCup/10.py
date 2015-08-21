a = [3,2,1]
b = []
c = []

def move(n,src,des,spr):
	if n==1:
		print "move disc from '%s' to '%s'" %(src,des)
	else:
		move(n-1,src,spr,des)
		print "move disc from '%s' to '%s'" %(src,des)
		move(n-1,spr,des,src)
		
move(len(a),'a','c','b')
