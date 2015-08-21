import math as m

def execute():
	N = int(raw_input())
	for i in range(N):
		[n,r] = [int(j) for j in raw_input().split(' ')]
		no_of_terms = (n-1) - (r-1) + 1; terms = [2000000001] * no_of_terms
		for each in raw_input().split(' '):
			if int(each) < terms[0]:
				for count in range(1,no_of_terms):
					if int(each) >= terms[count]:
						break
				else:
					count += 1
				terms.insert(count,int(each)); terms.pop(0)
		terms = terms[::-1]
		n = n-1; r = r-1; sum = 0
		for each in terms:
			sum += each * (m.factorial(n)/(m.factorial(r)*m.factorial(n-r)))
			n -= 1
		print sum

execute()
