import math
N, R, dict, m, start, end, passengers = 0, 0, [], [], 0, 0, 0
queue, route = [], []

def add():
	for i in range(N+1):
		dict.append([]); m.append([0]*(N+1))
	for i in range(R):
		x = [int(each) for each in raw_input().split(' ')]
		dict[x[0]].append(x[1]); dict[x[1]].append(x[0]); m[x[0]][x[1]] = x[2]; m[x[1]][x[0]] = x[2]
	x = [int(each) for each in raw_input().split(' ')]
	global start, end, passengers 
	start, end, passengers = x[0], x[1], x[2]

def execute():
	queue.append([[start],1000000,dict])
	while queue:
		element = queue.pop(0)
		last = element[0][-1]
		if last == end:
			route.append(element)
		ele2 = element[2][:]
		for each in ele2[last]:
			if not ele2[each]:
				continue
			ele0 = element[0] + [each]
			if m[last][each] < element[1]:
				ele1 = m[last][each]
			else:
				ele1 = element[1]
			ele2[last] = []
			queue.append([ele0, ele1, ele2])

x = [int(each) for each in raw_input().split(' ')]
N, R = x[0], x[1]
add()
execute()

i = 0; max = route[0][1]
for j in range(1,len(route)):
	if route[j][1] > max:
		max = route[j][1]; i = j
for each in route[i][0]:
	print each,
print
print int(math.ceil(float(passengers)/(max-1)))
