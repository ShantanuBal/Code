def main():
	N = int(raw_input()); s = 'x' + raw_input()
	score = 0

	i = 1
	while i<N+1:
		if s[i] == '1':
			i += 1
		# 0 encountered
		else:
			# check if next index exists
			if i+1<N+1:
				# check if next index is '1'
				if s[i+1] == '1':
					if i+2<N+1:
						if s[i+2] == '1':
							score += 1 ** 0.5; i += 3
						else:
							score += 3 ** 0.5; i += 3
					else:
						score += 1 ** 0.5; i += 2
				else:
					if i+2<N+1:
						if s[i+2] == '1':
							score += 2 ** 0.5; i += 3
						else:
							j = i+3
                                                	while j<N+1 and s[j] == '0':
                                                        	j += 1
                                                	score += (j-i) ** 0.5
                                                	i = j
					else:
						score += 2 ** 0.5; i += 2
			else:
				score += 1 ** 0.5; i += 1
				
	print round(score,4)
main()
