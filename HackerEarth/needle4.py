def execute():
        pattern, text = [i for i in raw_input()], [i for i in raw_input()]
        dict_p, dict_t = [0]*26, [0]*26
        for each in pattern:
                dict_p[ord(each)-97] += 1
        length = len(pattern)
        word, i = [], length-1
        while i<len(text):
                val = ord(text[i])-97
                if dict_p[val] == 0:
                        i += length; continue
                else:
			#pdb.set_trace()
			word.append(val); dict_t[val] += 1
                        for j in range(i-1,i-length,-1):
				val = ord(text[j])-97
                                if not dict_p[val] or dict_t[val]+1 > dict_p[val]:
					break # go forward
                                else:
                                        dict_t[val] += 1; word.insert(0,val)
			else:
				print "YES"; return
			for j in range(i+1, i+1+length-len(word)):
				val = ord(text[j])-97
				if not dict_p[val] or dict_t[val]+1 > dict_p[val]:
					break
				else:
					dict_t[val] += 1; word.append(val)
			else:
				print "YES"; return
			dict_t = [0] * 26; word = []; i += length
        else:
                print "NO"

N = int(raw_input())
for i in range(N):
        execute()

