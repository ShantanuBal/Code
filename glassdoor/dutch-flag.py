

def flag(string, a, b, first, second):
	while a<b:
		while string[a] in first:
			a += 1
		while string[b] in second:
			b -= 1
		if a<b:
			#swap
			flag = string[a]; string[a]=string[b]; string[b] = flag
			a += 1
			b -= 1
	return string

array = ['r','r','w','b','w','b','w','r','b','b','w','r','w','w','w','b']
array = flag(array, 0, len(array)-1, ['r'],['w','b'])
for i in range(len(array)):
	if array[i] == 'w':
		break
print flag(array, i, len(array)-1, ['w'],['b'])

