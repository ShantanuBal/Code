#excel numbers

a = 32
#dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

dict = {0:'e',1:'a',2:'b',3:'c',4:'d'}
xls = ""

while a > 0:
	xls = dict[a%5] + xls
	if a%5 == 0:
		a /= 5
		a -= 1
	else:
		a /= 5

print xls
