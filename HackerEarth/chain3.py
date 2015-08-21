import copy, time
start = time.time()
dict, array, N, queue, max = [], [], 0, [], []

def add():
	global dict, array
	for i in range(26):
		dict.append([])
	for i in range(N):
		x = raw_input()
		dict[ord(x[0])-65].append(x)
		array.append(x)

def execute(dict):
	global array, N, queue, max
	for i in range(N):
		new_dict = copy.deepcopy(dict); val = ord(array[i][0])-65; new_dict[val].remove(array[i])
		queue.append([[array[i]],new_dict])
		while queue:
			element = queue.pop(0)
			node, dict_node = element[0], element[1]
			val = ord(node[-1][-1])-65
			for each in dict_node[val]:
				if time.time() - start > 5:
					for each in max:
						print each
					exit()
				ele1 = copy.deepcopy(dict_node); ele1[val].remove(each)
				ele0 = node + [each]
				queue.append([ele0, ele1])
			if not dict_node[val]:
				if len(node)>len(max):
					max = node

N = int(raw_input())
add()
execute(dict)
for each in max:
	print each
