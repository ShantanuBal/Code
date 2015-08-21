
class setOfStacks():
	def __init__(self):
		self.stack = []

	def pop(self):
		if self.stack == []:
			return None
		element = self.stack[-1].pop()
		if len(self.stack[-1]) == 0:
			self.stack.pop()
		return element

	def push(self, data):
		if self.stack == [] or len(self.stack[-1]) == 5:
			self.stack.append([data])
		else:
			self.stack[-1].append(data)
		
	
set = setOfStacks()
while 1:
	print("1. Push\n2. Pop\n3. Peek")
	input = raw_input()
	if input == "1":
		data = raw_input()
		set.push(data)
	elif input == "2":
		set.pop()
	elif input == "3":
		print set.stack[-1][-1]
	else:
		break
	print set.stack
