def main():
	n = int(raw_input("Enter no. of elements: "))
	array = []
	for i in range(n):
		array.append(int(raw_input("Enter element: ")))
	
	hash_map = {}
	length = 2**n
	for i in range(length):
		b = bin(i)[2:]
		b = ('0' * (n-len(b))) + b
		set = []
		for j in range(len(b)):
			if int(b[j]):
				set.append(array[j])
		if str(set) not in hash_map:
			print str(set)
			hash_map[str(set)] = 1
		

main()
