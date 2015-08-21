
def anagram(string1, string2):
	array1 = [0] * 128
	array2 = [0] * 128
	for each in string1:
		array1[ord(each)] += 1
	for each in string2:
		array2[ord(each)] += 1
	print array1
	print array2
	if array1 == array2:
		return "Yes"
	else:
		return "No"
	
string1 = raw_input()
string2 = raw_input()
print anagram(string1, string2)
