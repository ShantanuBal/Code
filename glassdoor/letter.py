
def combo(string, array):
	if string == "":
		print array
		return
	if len(string) >= 2 and int(string[0] + string[1]) <= 26:
		combo(string[2:], array + [string[0:2]] )
	combo(string[1:], array + [string[0]] )

combo("113", [])
