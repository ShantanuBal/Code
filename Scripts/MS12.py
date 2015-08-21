# mapping phones letters to numbers

mapping = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}


def find(array):
	if len(array) > 1:
		new_array = []
		a1 = array.pop()
		a2 = array.pop()
		for each in a2:
			for every in a1:
				new_array.append(each+every)
		array.append(new_array)
		find(array)
	else:
		for each in array:
			print each

def combo(number):
	array = []
	for each in number:
		array.append(mapping[each])
	find(array)

combo("234")
