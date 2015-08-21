# nth ranking element from 2 sorted arrays

a = [4,6,9,10,12,20,25,30]
b = [1,2,3,22,23,29,31]
rank = 10

def find(a,b,rank):
	i = 0 
	j = 0
	count = rank/2
	while count:
		if a[i+count-1] < b[j+count-1]:
			i = i+count
		else:
			j = j+count
		count = count / 2

	while i+j < rank-1:
		if a[i+1] < b[j+1]:
			i += 1
		else:
			j += 1

	return min(a[i],b[j])

print a
print b
print "rank:", rank
print find(a,b,rank)
