def find(string):
	i = 1
	count = 1
	value = string[0]
	print string[0]
	print "value :", value
	print "count :", count
	while i<len(string):
		if string[i] == value:
			count += 1
		else:
			count -= 1
			if count == 0:
				value = string[i]
				count = 1
		print string[i]
		print "value: ", value
		print "count: ", count
		i += 1

string = raw_input("String: ")
print "length:", len(string)
find(string)
