# Regex parser

is_regex = False
def parse(string, regex):
	global is_regex
	if (not string and not regex) or (string == regex):
		is_regex = True
	if not string or not regex:
		return
	if len(regex)>1:
		if regex[1] == "+":
			if string[0] == regex[0]:
				parse(string[1:], regex)
				parse(string[1:], regex[2:])
		else:
			if string[0] == regex[0]:
				parse(string[1:], regex[1:])

parse(raw_input(),raw_input())
print "Is regex:", is_regex
