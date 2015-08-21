p = []
a = [1] * 20
for i in range(20):
	p.append(a)

count = 0
while (count < 100):
	if count != 0:
		print "------------------------------------------------------------------------------------------------"
	for each in p:
		count += 1
		if each[count%20] == 0:
			each[count%20] = 1
		else:
			each[count%20] = 0
		for every in each:
			print every," ",
		print
		count += 1
