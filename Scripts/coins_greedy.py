n = 40

def opt(cash, coins):
	if cash == 0:
		print coins
		exit()
	if cash >= 25:
		opt(cash - 25, coins + 1)
	elif cash >= 20:
		opt(cash - 20, coins + 1)
	elif cash >= 10:
		opt(cash - 10, coins + 1)
	elif cash >= 5:
		opt(cash - 5, coins + 1)
	elif cash >= 1:
		opt(cash - 1, coins + 1)


opt(n, 0)
