N, p, dict, count = 0, 0, [], []

def init():
        for i in range(N+1):
                dict.append([]); count.append(0)
        for i in range(p):
                x = [int(each) for each in raw_input().split(' ')]
                dict[x[0]].append(x[1]); dict[x[1]].append(x[0]); count[x[0]] += 1; count[x[1]] += 1

def execute():
        for i in range(1, N+1):
                print i, dict[i], count[i]

        warehouses = 0; ticker = 0; text = ''
        while ticker != N:
                longest = max(count)
                i = count.index(longest)
                for each in dict[i]:
			if count[each] == 1:
                        	count[each] = -1; dict[each] = -1; ticker += 1; text += '1'
			elif count[each] == 2:
				if dict[each][0] == i:
					element = dict[each][1]
				else:
					element = dict[each][0]
				count[element] -= 1; dict[element].remove(each)
				count[each] = -1; dict[each] = -1; ticker += 1; text += '2'
			elif count[each] >= 3:
				count[each] -= 1; dict[each].remove(i); text += '3'
                count[i] = -1; dict[i] = -1; ticker += 1
                warehouses += 1
                print dict, count, text
        return warehouses

x = [each for each in raw_input().split(' ')]
N, p = int(x[0]), int(x[1])
init()
print execute()

