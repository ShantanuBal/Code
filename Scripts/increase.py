
def generate(array, length):
	global k, n
	if length == k:
		print array
		return
	for i in range(array[-1]+1,n+1):
		generate(array + [i], length + 1)


def main():
	global k, n
	k = 3; n = 5
	for i in range(1, n - k + 2):
		generate([i], 1)

main()
