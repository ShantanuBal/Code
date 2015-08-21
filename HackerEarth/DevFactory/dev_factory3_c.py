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
                lowest_terms = find_lowest(a, no_of_lowest)
                n = n-1; r = r-1; sum = 0
		
		comb = (m.factorial(n)/(m.factorial(r)*m.factorial(n-r)))

                for each in lowest_terms:
                        sum += each * comb
			if r == 0:
				continue
			if r == 1:
				comb -= 1
			else:
				n -= 1
				comb *= (n-1); comb /= (n+1)
                print sum % 1000000007
execute()
