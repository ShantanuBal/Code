# combinations of coins

amount = int(input())
dict = {}

def check(amount, q, d, n, p):
	if amount == 0:
		if str(str(q)+str(d)+str(n)+str(p)) not in dict:
			dict[str(q)+str(d)+str(n)+str(p)] = 1
			print q, d, n, p
			return
	if amount - 25 >= 0:
		check(amount-25,q+1,d,n,p)
	if amount - 10 >= 0:
		check(amount-10,q,d+1,n,p)
	if amount - 5 >= 0:
		check(amount-5,q,d,n+1,p)
	if amount -1 >= 0:
		check(amount-1,q,d,n,p+1)

check(amount, 0, 0, 0, 0)
