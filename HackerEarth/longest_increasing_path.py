def build(m,n):
	array = []
	for each in range(m):
		array.append([int(each) for each in raw_input().split(' ')])
	return array

def execute(array, m, n):
	queue, length = [ [ [0,0] ] ], 1
	while queue:
		element = queue.pop(0); last = element[-1]; i, j = last[0], last[1]
				
		if i+2<m and array[i+2][j] > array[i+1][j] > array[i][j]:
			queue.append(element + [[i+1,j],[i+2,j]])
		if j+2<n and array[i][j+2] > array[i][j+1] > array[i][j]:
			queue.append(element + [[i,j+1],[i,j+2]])
		if i+1<m and j+1<n:
			if array[i+1][j+1] > array[i+1][j] > array[i][j]:
				queue.append(element + [[i+1,j],[i+1,j+1]])
			if array[i+1][j+1] > array[i][j+1] > array[i][j]:
				queue.append(element + [[i,j+1],[i+1,j+1]])

		if i+1<m and array[i+1][j] > array[i][j] or j+1<n and array[i][j+1] > array[i][j]:
			length = len(element)+1
			
	return max([len(element), length])


N = int(raw_input())
for i in range(N):
	[m,n] = [int(j) for j in raw_input().split(' ')]
	array = build(m, n)
	print execute(array, m, n)
