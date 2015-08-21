# find nth rank element in 2 sorted arrays
n = 8
a = [3,7,10,16,20,26,29,31,33,39]
b = [4,6,8,9,19,24,28,32,36,38]

i = n / 2
p = 0; q = 0
while i > 0:
	print "i:", i
	if a[p+i-1] < b[q+i-1]:
		p = p+i
	else:
		q = q+i
	i = i/2

while p+q < n-1:
	print "p+q:", p+q
	if a[p] < b[q]:
                p += 1
        else:
                q += 1

if a[p] < b[q]:
	print a[p]
else:
	print b[q]
