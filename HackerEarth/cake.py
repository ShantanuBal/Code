

def sieveOfEratosthenes(n):
    sieve = range(3, n, 2)
    #print sieve
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return sieve

primes = sieveOfEratosthenes(10)
print primes
N = int(raw_input())
for i in range(N):
	x = int(raw_input())
	j = 0
	while primes[j] <= x/2:
		if primes[(x-primes[j]-3)/2]:
			print "Deepa"; break
		j += 1
	else:
		if x-2 == 2:
			print "Deepa"
		elif (x-2)%2 and primes[(x-2-3)/2]:
			print "Deepa"
		else:
			print "Arjit"
