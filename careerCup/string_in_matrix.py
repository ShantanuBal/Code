a = 	[
	['A','C','F','R','C'],
	['X','S','O','T','C'],
	['V','O','R','N','I'],
	['W','F','C','M','N'],
	['Q','A','T','I','M']
	]
word = "MICROSOFT"

def search(i,j,word,coords):
	global a
	if word == "":
		for each in coords:
			print each,
		print
		return
	if j+1<len(a[i]) and a[i][j+1] == word[0]:
		search(i,j+1,word[1:],coords + [[i,j+1]])
	if j-1>=0 and a[i][j-1] == word[0]:
		search(i,j-1,word[1:],coords + [[i,j-1]])
	if i-1>=0 and a[i-1][j] == word[0]:
		search(i-1,j,word[1:],coords + [[i-1,j]])
	if i+1<len(a) and a[i+1][j] == word[0]:
		search(i+1,j,word[1:],coords + [[i+1,j]])
	if i-1>=0 and j-1>=0 and a[i-1][j-1] == word[0]:
		search(i-1,j-1,word[1:],coords + [[i-1,j-1]])
	if i+1<len(a) and j+1<len(a[i]) and a[i+1][j+1] == word[0]:
		search(i+1,j+1,word[1:],coords + [[i+1,j+1]])
	if i-1>=0 and j+1<len(a[i]) and a[i-1][j+1] == word[0]:
		search(i-1,j+1,word[1:],coords + [[i-1,j+1]])
	if i+1<len(a) and j-1>=0 and a[i+1][j-1] == word[0]:
		search(i+1,j-1,word[1:],coords + [[i+1,j-1]])

def find(a,word):
	positions = []
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j] == word[0]:
				search(i,j,word[1:],[[i,j]])
		
find(a,word)
