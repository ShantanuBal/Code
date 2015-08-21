import time; start = time.time()

N, p, dict, count, done = 0, 0, [], [], []

def init():
	for i in range(N+1):
		dict.append([]); count.append(0), done.append(0)
	for i in range(p):
		x = [int(each) for each in raw_input().split(' ')]
		dict[x[0]].append(x[1]); dict[x[1]].append(x[0]); count[x[0]] += 1; count[x[1]] += 1

def print_dict():
	for i in range(N):
		print i, dict[i], count[i]

def execute():
	warehouses = 0
	while done.count(0) != 0:
		i = count.index(max(count))
		count[i] = 0
		array = dict[i]
		print i, array
		done[i] = 1
		for each in array:
			done[each] = 1
		warehouses += 1
	return warehouses

x = [each for each in raw_input().split(' ')]
N, p = int(x[0]), int(x[1])
init()
#print_dict()
print execute()
