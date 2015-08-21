def execute():
	pattern, text = [i for i in raw_input()], [i for i in raw_input()]
        dict_p, dict_t = [0]*26, [0]*26
        for each in pattern:
                dict_p[ord(each)-97] += 1
	length = len(pattern)
	
	array = []
	for i in range(len(text)):
		val = ord(text[i])-97
		if not dict_p[val]:
			array.append(i)
	array.insert(0,-1); array.append(len(text))
	print "Array: ",array
	interval = []
	for i in range(1,len(array)):
		if array[i] - array[i-1] - 1  >= length:
			interval.append([array[i-1]+1,array[i]-1])
	print "Interval: ",interval

	for each in interval:
		word, i = [], each[0]
		while i<=each[1]:
			val = ord(text[i])-97
			if not dict_p[val]: 
				dict_t = [0] * 26; word = [];
			elif dict_t[val]+1 > dict_p[val]:
				for j in range(len(word)):
					if j == val:
						word = word[j+1:]; word.append(val); break
					else:
						dict_t[j] -= 1
			else:
				dict_t[val] += 1; word.append(val)
				if len(word) == length:
					print "YES"; return
			i += 1	
        else:
               	print "NO"

N = int(raw_input())
for i in range(N):
	execute()
