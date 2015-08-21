#given n, print all valid 2*n paranthesis combos

def paran(left, right, string):
	if left > right:
		return
	if left == right == 0:
		print string
	if left > 0:
		paran(left-1,right,string+"(")
	if right > 0:
		paran(left, right-1, string+")")

def main():
	n = int(raw_input("Enter n value: "))
	paran(n,n,"")

main()
