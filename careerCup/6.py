#Find all possible interpretations of an array of digits

array = [1,1,1]
r = len(array) - 1

def compute(left, string):
	if left > r:
		print string
	if left == r:
		print string + chr(array[left]+96)
	if left < r and array[left] * 10 + array[left+1] <= 26:
		compute(left + 2, string + chr(array[left] * 10 + array[left+1] + 96))
	if left < r:
		compute(left + 1, string + chr(array[left] + 96))
		
compute(0,"")
