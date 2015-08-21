
def lns(n, times):
	if times == 10:
		return
	count = 1
	char = n[0]
	word = ""
	for each in n[1:]:
		if each == char:
			count += 1
		else:	
			word += str(count) + char
			count = 1
			char = each
	word += str(count) + char
	print word
	lns(word, times + 1)

lns('1', 0)
