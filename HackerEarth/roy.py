def fact(x):
	p = 1
	while x != 0:
		p *= x
		x -= 1
	return p

def calc(n,i):
	par, rem = i-1, n-i
	return (fact(par+rem) / (fact(par) * fact(rem)))

def execute(n):
	sum = 0
	for i in range(2,n):
		sum += calc(n,i)
	return sum+2

N = int(raw_input())
for i in range(N):
	n = int(raw_input())
	print execute(n)
