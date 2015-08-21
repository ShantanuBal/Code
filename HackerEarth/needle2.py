def execute():
	pattern, text = [i for i in raw_input()], [i for i in raw_input()]
        dict_p, dict_t = [0]*26, [0]*26
        for each in pattern:
                dict_p[ord(each)-97] += 1
	length = len(pattern)
	count, word, i = 0, [], 0
	while i<len(text):
		val = ord(text[i])-97
		if not dict_p[val]: #or dict_p[val] > dict_t[val]:
			dict_t = [0] * 26; count = 0; word = []; i += 1
			continue
		count += 1; dict_t[val] += 1; word.append(val)
		if count == length:
			if dict_p == dict_t:
				print "YES"; return
			else:
				dict_t[word[0]] -= 1; count -= 1; word = word[1:]
		i += 1	
        else:
                print "NO"

N = int(raw_input())
for i in range(N):
	execute()
