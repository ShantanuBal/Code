import math

def main():
	N = int(raw_input()); s = raw_input()
	start, score = 0, 0
	s = 'x' + s
	
	for i in range(1,N+1):
		if s[i] == '0':
			if not start:
				start = i
		elif s[i] == '1':
			if start:
				score += math.sqrt(i - start); start = 0

	if s[i] == '0':
		score += math.sqrt(i - start + 1)
	print score	
main()
