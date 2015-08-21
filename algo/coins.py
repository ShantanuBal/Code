n = 40

def main():
	global n
	a = [0] * (n+1)
	a[0], a[1] = 0, 1
	for i in range(1,n+1):
		if i>=25:
			a[i] = min(1 + a[i-1], 1 + a[i-5], 1 + a[i-10], 1 + a[i-20], 1 + a[i-25])
		elif i>=20:
			a[i] = min(1 + a[i-1], 1 + a[i-5], 1 + a[i-10], 1 + a[i-20])
		elif i>=10:
			a[i] = min(1 + a[i-1], 1 + a[i-5], 1 + a[i-10])
		elif i >= 5:
			a[i] = min(1 + a[i-1], 1 + a[i-5])
		else:
			a[i] = a[i-1] + 1
	for i in range(len(a)):
		print i , " : ", a[i]
main()
