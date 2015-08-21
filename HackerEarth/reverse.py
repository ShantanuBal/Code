import time; start = time.time()
x = 10000000

def sieveOfEratosthenes(n):
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return sieve

sieve = sieveOfEratosthenes(x)

def reverse(x):
	r = 0
	while x != 0:
		r = r*10 + x%10
		x /= 10
	return r

for each in sieve[4:]:
	rev = reverse(each)
	if (rev%10) % 2 and sieve[(rev-3)/2] != 0:
		print each; sieve[(rev-3)/2] = 0; sieve[(each-3)/2] = 0
print time.time() - start
