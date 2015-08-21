# reverse a linked list

class LL():
        def __init__(self, key, next=None):
                self.key = key
                self.next = next

root = LL(1,LL(2,LL(3,LL(4,LL(5)))))

def reverse():
