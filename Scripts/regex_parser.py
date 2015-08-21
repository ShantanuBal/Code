s1 = raw_input("s1: ")
s2 = raw_input("s2: ")

def parse(s1,s2):
	print s1,s2
	if not s1 and not s2:
		return True
	elif not s1 and s2:
		return False
	else:
		if s1[-1] == "*":
			if s2 and s1[-2] == s2[-1]:
				return parse(s1[:-2],s2) or parse(s1,s2[:-1])
			else:
				return parse(s1[:-2],s2)
		else:
			if s2 and s1[-1] == s2[-1]:
				return parse(s1[:-1],s2[:-1])
			else:
				return False


		

print parse([each for each in s1],[each for each in s2])
