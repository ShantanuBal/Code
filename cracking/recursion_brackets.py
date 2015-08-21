 
def brackets(pattern, l, r):
	if l == r == 0:
		print pattern
		return
	if l > 0:
		brackets(pattern + '(', l-1, r)
	if l < r:
		brackets(pattern + ')', l, r-1)

brackets("", 3, 3)
