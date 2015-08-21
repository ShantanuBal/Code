a = ['w','x','y','z']
k = 7
dict = {}

def computer(p, array):
	"""
	if sum(array) > k:
		print array[:-1]
		return
	if array[-1] == a[-1]:
		print array
		return
	"""
	last = array[-1]
	for j in range(p+1,len(a)):
		print array+[a[j]]
		computer(j, array+[a[j]])

for i in range(len(a)):
	print [a[i]]
	computer(i, [a[i]])

