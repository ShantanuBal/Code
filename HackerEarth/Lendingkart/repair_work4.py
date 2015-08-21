def round_off(x):
	x = round(x,4)
	x = str(x); i = x.find('.'); dec = x[i+1:]; s = ''
	for j in range(4-len(dec)):
		s += '0'
	return x+s

def main():
	N = int(raw_input()); s = raw_input()
	if '0' not in s:
		print round_off(0); return
	if '1' not in s:
		print round_off(N ** 0.5); return
	start = s.find('0'); end = N - s[::-1].find('0')
	s = s[start:end]
	if '1' not in s:
		print round_off(len(s) ** 0.5); return

	x = '0'; length = 0; tally = []
	for i in range(len(s)):
		if s[i] != x:
			x = s[i]
			tally.append(length)
			length = 1
		else:
			length += 1
	tally.append(length)
	partitions = len(tally) / 2
	seq = []
	for i in range(2**partitions):
		seq.append([int(each) for each in bin(i)[2:].zfill(partitions)])

	min = N ** 0.5
	for each in seq:
		i = 1; sum = tally[0]; score = 0
		for every in each:
			if every == 0:
				score += (sum ** 0.5)
				sum = 0
			else:
				sum += tally[i]
			sum += tally[i+1]
			i += 2
		score += (sum ** 0.5)
		if score < min:
			min = score
	print round_off(min)

main()
