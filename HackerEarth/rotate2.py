N, M, dir, lef, rig, num = 0, 0, [], [], [], []
config = []

def init():
	global N, M, dir, lef, rig, num, config
	x = raw_input().split(' ')
	N, M = int(x[0]), int(x[1])
	config = ['E'] * N
	for i in range(M):
		x = [each for each in raw_input().split(' ')]
		dir.append(x[0]); lef.append(int(x[1])-1); rig.append(int(x[2])-1);
		if len(x) == 4:
			num.append(int(x[3]))
		else:
			num.append(-1)

def calculate_max(l,r):
	global config
	array = config[l:r+1]
	list = [array.count('E'),array.count('W'),array.count('N'),array.count('S')]
	return max(list)

def change_config(d,l,r,n):
	global config
	dict_c, dict_a = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}, {'E':'N', 'S':'E', 'W':'S', 'N':'W'}
	for i in range(l,r+1):
		if d == 'C':
			for j in range(n%4):
				config[i] = dict_c[config[i]]
		else:
			for j in range(n%4):
				config[i] = dict_a[config[i]]
			

def process_commands():
	global N, M, dir, lef, rig, num, config
	for i in range(M):
		if num[i] == -1:
			print calculate_max(lef[i],rig[i])
		else:
			change_config(dir[i],lef[i],rig[i],num[i])
init()
process_commands()
