import time
start = time.time()

def swap(string, i, j):
	array = [each for each in string]
	flag = array[i]; array[i] = array[j]; array[j] = flag
	string = ""
	for each in array:
		string += each
	return string

def permute(string, i, j):
	if i==j:
		print string
	else:
		for k in range(i, j+1):
			string = swap(string, i,k)
			string = permute(string, i+1,j)
			string = swap(string, i,k)
	return string

permute("abc",0,2)
