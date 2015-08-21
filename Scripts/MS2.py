# strtok

def strtok(string, delim):
	hashtable = {}
	for each in delim:
		hashtable[each] = 1

	tokens = []
	tok = ""
	for each in string:
		if each in hashtable:
			tokens.append(tok)
			tok = ""
		else:
			tok += each
	if tok:
		tokens.append(tok)
	return tokens

print strtok("I am,a.good boy."," .,")
