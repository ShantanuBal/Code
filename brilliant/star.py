def full_array(array):
    for i in xrange(len(array)):
        if array[i] == 0:
            return 0
    return 1

count = 0
n = 1000
for i in xrange(2,int(n/2)+1):
    j = 0
    array = [0] * n
    while True:
        if array[j] == 1:
            if full_array(array):
                count += 1
            break
        else:
            array[j] = 1
        if j+i >= len(array):
            j = i - (len(array) - j)
        else:
            j += i
            
print count
