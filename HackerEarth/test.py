def f(x):
	p = 1
        while x != 0:
                p *= x
                x -= 1
        return p

def c(n,r):
        return (fact(n) / (f(r) * f(n-r)))

N = int(raw_input())
for i in range(N):
        [n,r] = [int(j) for j in raw_input().split(' ')]
        print c(n,r)
