
heap = [5,6,7,8,1,2,3,4]

def make_heap():
	global heap
	print heap
	for i in range(1,len(heap)):
		parent = (i-2+(i%2)) / 2
		current = i
		while parent >= 0 and heap[parent] < heap[current]:
			flag = heap[parent]; heap[parent] = heap[current]; heap[current] = flag
			current = parent
			parent = (current-2+(current%2)) / 2
	print heap

def heap_sort(l):
	global heap
	if l == 0:
		print heap
		return
	
	flag = heap[0]; heap[0] = heap[l]; heap[l] = flag
	position = 0
	while 2*position+2 <= l-1:
		if heap[position] > heap[2*position + 1] and heap[position] > heap[2*position + 2]:
			break
		elif heap[position] < heap[2*position + 1] and heap[position] < heap[2*position + 2]:
			if heap[2*position + 1] > heap[2*position + 2]:
				flag = heap[2*position + 1]; heap[2*position + 1] = heap[position]; heap[position] = flag
				position = 2*position + 1
			else:
				flag = heap[2*position + 2]; heap[2*position + 2] = heap[position]; heap[position] = flag
				position = 2*position + 2
		elif heap[position] < heap[2*position + 1]:
			flag = heap[2*position + 1]; heap[2*position + 1] = heap[position]; heap[position] = flag
			position = 2*position + 1
		else:
			flag = heap[2*position + 2]; heap[2*position + 2] = heap[position]; heap[position] = flag
			position = 2*position + 2
	if 2*position+1 <= l-1 and heap[position] < heap[2*position+1]:
		flag = heap[2*position + 1]; heap[2*position + 1] = heap[position]; heap[position] = flag
	heap_sort(l-1)
	

make_heap()
heap_sort(len(heap)-1)
