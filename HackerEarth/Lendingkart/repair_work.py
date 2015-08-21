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
	#print tally
	score = 0
	sum = tally[0]
	for i in range(1,len(tally),2):
		if (sum + tally[i] + tally[i+1]) ** 0.5 > sum ** 0.5 + tally[i+1] ** 0.5:
			score += sum ** 0.5; sum = tally[i+1]
		else:
			sum += tally[i] + tally[i+1]
	score += sum ** 0.5
	print round_off(score)

main()
