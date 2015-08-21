

a = [1,9,10,2,3,6,20,10,12]


def find_longest(a):
	opt = [1] * len(a)

	for i in range(1, len(a)):
		max = 1
		for j in range(0,i):
			if a[j] < a[i] and opt[j] > max:
				max = opt[j]
		opt[i] = max+1
	print a
	print opt

find_longest(a)
