


def find_den(amount_left, den):
	next_den = {.50: .25, .25: .10, .10: .05, .05:.01}
	
	if den == .01 or amount_left == 0:
		return 1
	
	count = 0
	i = 0
	while i <= amount_left:
		count += find_den(amount_left - i, next_den[den])
		i += den
	return count

count = find_den(.20, .50)
print count
