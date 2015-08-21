array = [3, 2, 1]

def subset(set, list):
	if list == []:
		print set
		return
	top = list[-1]
	subset(set+[top], list[:-1])
	subset(set, list[:-1])

subset([], array)
