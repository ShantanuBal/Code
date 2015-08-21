# Regex parser

a = raw_input()
b = raw_input()

def find(a,b):
	if (not a and not b) :
		return True
	
	if (not a and b):
		return False
	
	if len(a)==1 or (a[1] not in ['+','*']):
		if a[0] == b[0]:
			return find(a[1:], b[1:])
		else:
			return False
	if a[1] == '*':
		if a[0] == b[0]:
			return find(a,b[1:]) or find(a[2:],b[1:])
		else:
			return find(a[2:],b)
	if a[1] == '+':
		if a[0] == b[0]:
			return find(a,b[1:]) or find(a[2:],b[1:])
		else:
			return False


print find(a,b)
