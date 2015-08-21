string = "Shantanu"

def toUpper(string):
	for each in string:
		if 96<ord(each)<123:
			each = chr(ord(each)-32)
		print(each),

toUpper(string)
