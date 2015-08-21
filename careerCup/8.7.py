cash = 10

def calculate(amt, a, b ,c ,d):
	if amt == 0:
		print a, b, c, d
		return
	if amt >= 25:
		calculate(amt - 25, a+1, b, c, d)
	if amt >= 10:
		calculate(amt - 10, a, b+1, c, d)
	if amt >= 5:
		calculate(amt - 5, a, b, c+1, d)
	if amt >= 1:
		calculate(amt - 1, a, b, c, d+1)
	
print "q d n p"
calculate(cash, 0, 0, 0, 0)
