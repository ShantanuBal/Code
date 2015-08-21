import math as m

def find_lowest(a, no_of_lowest):
	terms = []
	for i in range(no_of_lowest):
		terms.append(a.pop(a.index(min(a))))
	return terms

def execute():
	N = int(raw_input())
	for i in range(N):
		[n,r] = [int(j) for j in raw_input().split()]
		a = [int(j) for j in raw_input().split()]
		no_of_lowest = (n-1) - (r-1) + 1
		lowest_terms = find_lowest2(a, no_of_lowest)
		n = n-1; r = r-1; sum = 0

		if r == 0:
			for each in lowest_terms:
				sum += each
		elif r == 1:
			com = n
			for each in lowest_terms:
				sum += each*com
				com -= 1
		
		else:
			num = 1; j=0; nn = n
			while j<r:
				num *= n
				j += 1; n -= 1
			den = m.factorial(r)
			com = num / den
			for each in lowest_terms:
				#print com
				sum += each * com
				com *= (nn-2); com /= nn
				nn -= 1

		print sum % 1000000007

execute()
