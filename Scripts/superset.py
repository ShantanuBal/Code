#print super set
import time
start = time.time()

sum_set = [0] * 20
def find(array, set):
	if not len(array):
		print sum(set)
		#sum_set[sum(set)] = 1
	else:
		find(array[1:],set+[array[0]])
		find(array[1:],set)

find([1]*20,[])
print 
print sum_set

print time.time() - start
