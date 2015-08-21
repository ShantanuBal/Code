

array = []
N = int(raw_input())
for i in range(N):
	array.append(raw_input())

for i in range(N):
	if array[i][::-1] in array[i+1:]:
		print array[i][len(array[i])/2]
