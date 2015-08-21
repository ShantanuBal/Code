# evaluating expressions
import re
exp = "1+(1+(5+9)/2)/2*3*2"

pre = {"/":4, "*":3, "-":2, "+":1}
s1 = []
s2 = []

def solve():
	array = []
	term = ""
	for each in exp:
		if each not in ['(',')','/','*','+','-']:
			term += each
		else:
			if term:
				array = array + [term]
			array = array + [each]
			term = ""
	array = array + [term]
	print array
	
	s1.append(array.pop(0))
	s2.append(array.pop(0))
	while array:
		incoming = array.pop(0)
		if incoming == '(':
			s2.append(incoming)
			s1.append(array.pop(0))
			s2.append(array.pop(0))
		
		elif incoming == ')':
			s1.append( str(eval( s1.pop() + s2.pop() + s1.pop() )) )
			s2.pop()

		elif incoming not in ['/','*','+','-']:
			s1.append(incoming)
		
		else:
			# if incoming has higher precedence
			if pre[incoming] > pre[s2[-1]]:
				inc_elem = array.pop(0)
				t1 = s1.pop()
				s1.append( str(eval( t1 + str(incoming) + inc_elem )) )
			else:
				t1 = s1.pop(); t2 = s1.pop(); op = s2.pop()
				s1.append( str(eval(t1 + op + t2)) )
				s2.append(incoming)
		print array, s1, s2

solve()
print eval(s1.pop() + s2.pop() + s1.pop())
