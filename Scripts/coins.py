n = 40
min = 1000

def opt(cash, coins):
	global min
	if cash == 0:
		if coins < min:
			min = coins
		print coins
		return 
	if cash >= 25:
		opt(cash - 25, coins + 1)
	if cash >= 20:
		opt(cash - 20, coins + 1)
	if cash >= 10:
		opt(cash - 10, coins + 1)
	if cash >= 5:
		opt(cash - 5, coins + 1)
	if cash >= 1:
		opt(cash - 1, coins + 1)


opt(n, 0)
print "Answer: ", min
