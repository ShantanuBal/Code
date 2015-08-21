import pdb
N = int(raw_input())
for i in range(N):
	pattern, text = [i for i in raw_input()], [i for i in raw_input()]
	text.append('z')
	dict_p, dict_t = [0]*26, [0]*26 	
	for each in pattern:
		dict_p[ord(each)-97] += 1
	count = 0
	while count<len(text) and not dict_p[ord(text[count])-97]:
		count += 1
	for j in range(len(pattern)):
		dict_t[ord(text[count+j])-97] += 1
	j = len(pattern)-1+count
	#pdb.set_trace()
	while j<len(text)-1:
		if dict_p == dict_t:
       			print "YES"; break
		j += 1; flag = text[j-len(pattern)]	
		dict_t[ord(flag)-97] -= 1; dict_t[ord(text[j])-97] += 1
		if not dict_p[ord(text[j])-97]:
			if j+1+len(pattern) >= len(text):
				print "NO"; break
			count = 0
        		while count<len(text) and not dict_p[ord(text[count])-97]:
                		count += 1
			dict_t = [0]*26
			for k in range(j+1,j+1+len(pattern)):
				dict_t[ord(text[k])-97] += 1
			j += len(pattern)
	else:
		print "NO"
