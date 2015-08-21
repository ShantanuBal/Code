dict, array, N, ans, queue, max = [], [], 0, [], [], []
import time; start = time.time()
t_limit = 8

def add():
	global dict, array
	for i in range(N):
		array.append(raw_input())
	dict = [0] * N

def execute():
	global dict, array, N, ans, queue, max
	for i in range(N):
		new_dict = dict[:]; new_dict[i] = 1
		queue.append([[array[i]],new_dict])
		while queue:
			element = queue.pop(0)
			node, dict_node = element[0], element[1]
			done = 0
			for j in range(len(dict_node)):
				if time.time() - start > t_limit:
					for each in max:
						print each
					exit()
				if not dict_node[j] and node[-1][-1] == array[j][0]:
					ele1 = dict_node[:]; ele1[j] = 1
					ele0 = node + [array[j]]
					queue.append([ele0, ele1])
					done = 1
			if not done:
				if len(node)>len(max):
					max = node


N = int(raw_input())
add()
execute()
#for each in max:
#	print each
