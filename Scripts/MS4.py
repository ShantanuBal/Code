# Use stack to implement queue

class Queue():
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def insert(self, value=None):
		if value:
			self.s1.append(value)
	
	def delete(self):
		if not self.s1:
			return None
		while len(self.s1) > 1:
			self.s2.append(self.s1.pop())
		element = self.s1.pop()
		while self.s2:
			self.s1.append(self.s2.pop())
		return element

queue = Queue()
queue.insert(20)
queue.insert(30)
queue.insert(40)
queue.insert(50)
print "The queue:", queue.s1
queue.delete()
print "The queue:", queue.s1
