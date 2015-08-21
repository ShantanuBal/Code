def print_max(config, l, r):
	list = [0,0,0,0]
	array = config[l:r+1]
	for each in array:
		list[each%4] += 1
	print max(list)

def change_config(config,d,l,r,n):
	if d == 'C':
		for i in range(l,r+1):
			config[i] += n
	else:
		for i in range(l,r+1):
			config[i] -= n
	return config
			
def process_commands():
	[N, M] = [int(each) for each in raw_input().split()]
        config = [0] * N
	for i in range(M):
		x = [each for each in raw_input().split()]
		if x[0] == 'Q':
			print_max(config, int(x[1])-1, int(x[2])-1)
		else:
			config = change_config(config, x[0], int(x[1])-1, int(x[2])-1, int(x[3]))
process_commands()
