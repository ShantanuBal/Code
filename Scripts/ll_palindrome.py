# check i fpalindrome or not

class LL():
	def __init__(self, key, next=None):
		self.key = key
		self.next = next

root = LL(1,LL(1,LL(1,LL(1,LL(1)))))
node = root
while( node != None):
	print node.key, 
	node = node.next

pointer = root
def check_rev(node):
	global pointer
	if node == None:
		return True 
	val = check_rev(node.next)
	if val == False:
		return False
	if node.key == pointer.key:
		pointer = pointer.next
		return True
	else:
		return False

print
print check_rev(root)
