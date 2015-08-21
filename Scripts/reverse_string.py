string = "I am a trojan"

def reverse(string):
	i, word, l = len(string), "", len(string)-1
	while l>=0:
		if string[l] == " ":
			string += word + " "
			word = ""
		else:
			word = string[l] + word
		l -= 1
	string += word
	print string[i:]

reverse(string)
