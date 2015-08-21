real_pos = 1
array = [8,9,1,2,3,4,5,6,7]
x = 9

def piv_search(l,r):
	print array[l:r+1]
	mid = (l+r)/2
	if array[l] > array[mid]:
		#pivot on left
		if array[mid+1] <= x <= array[r]:
			bin_search(mid+1,r)
		elif x == array[mid]:
			print "pos:", mid
		else:
			piv_search(l, mid-1)

	else:
		#pivot on right
		if  array[l] <= x <= array[mid-1]:
			bin_search(l, mid-1)
		elif x == array[mid]:
			print "pos:", mid
		else:
			piv_search(mid+1, r)

def bin_search(l, r):
	print array[l:r+1]
	mid = (l+r)/2
	if x<array[mid]:
		bin_search(l, mid-1)
	elif x>array[mid]:
		bin_search(mid+1, r)
	else:
		print "pos:", mid

def main():
	print array
	print x
	piv_search(0, 8)

main()
