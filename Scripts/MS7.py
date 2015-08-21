# Reverse words in a sentence

string = "taerg si dog"

word = ""
for i in range(len(string)-1,-1,-1):
	if string[i] == " ":
		print word,
		word = ""
	else:
		word += string[i]
print word
