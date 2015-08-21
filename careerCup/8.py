dictionary = ["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE","MALL", "BALL", "BELL", "BELT", "BENT"]
positions = {}
for i in range(len(dictionary)):
	positions[dictionary[i]] = i

def get_words(word, pos):
	add = []
	for each in dictionary:
		if each != word and each[:pos] + each[pos+1:] == word[:pos] + word[pos+1:]:
			add.append(each)
	return add

def build(word, pos):
	if word == "BENT":
		print "YES"
		exit()
	new_words = get_words(word, pos)
	for j in range(0,4):
		if j != pos:
			for each in new_words:
				print each, j
				build(each,j)


for i in range(0,4):
	print "MALL", i
	build("MALL", i)
else:
	print "NO"
