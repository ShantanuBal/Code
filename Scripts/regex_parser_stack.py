s1 = raw_input("s1: ")
s2 = raw_input("s2: ")

def parse(stack,s):
	while stack:
		top = stack.pop()
		if top == "*":
			while s2:
				if s2[-1] == stack[-1]:

		elif top == ".":
			print "#handle"
		else:
			if s and top == s[-1]:
				s.pop()
			else:
				return False
	if s:
		return False
	return True

print parse([each for each in s1],[each for each in s2])
