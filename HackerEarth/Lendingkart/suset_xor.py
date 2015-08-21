def check(n,a):
	print n, a

def main():
	t = int(raw_input())

	for i in range(t):
		n = int(raw_input())
		a = [int(each) for each in raw_input().split()]
		check(n,a)

main()
