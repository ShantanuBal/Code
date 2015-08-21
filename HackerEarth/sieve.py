import time
start = time.time()
x = 1000000000

def sieveOfEratosthenes(n):
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
	    print si
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

primes = sieveOfEratosthenes(x)
print "COUNT: ", len(primes)
print time.time() - start
