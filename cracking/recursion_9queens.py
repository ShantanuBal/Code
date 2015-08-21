
col = [0]*9

def isOkay(row):
	for i in range(1, row):
		if col[i] == col[row] or abs(col[i] - col[row]) == row - i:
			return False
	return True

def place_queen(row):
	if row == 9:
		print col
		return
	for i in range(1,9):
		col[row] = i
		if isOkay(row):
			place_queen(row+1)

place_queen(1)
