#word combinations

a = [['a','s','d'],['i','o','p'],['f','g','h']]

def find_combos(stack):
	while len(stack)>1:
		a1 = stack.pop()
		a2 = stack.pop()
		new = []
		for each in a2:
			for every in a1:
				new.append(each+every)
		stack.append(new)
	return stack

print a
for each in find_combos(a)[0]:
	print each
