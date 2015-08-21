x = 1000000

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

for each in sieve[4:]:
        if int(str(each)[0]) % 2 and sieve[(int(str(each)[::-1])-3)/2] != 0:
                        print each; sieve[(int(str(each)[::-1])-3)/2] = 0; sieve[(each-3)/2] = 0
