class BinTree():
        def __init__(self, key, left=None, right=None):
                self.key = key
                self.left = left
                self.right = right

def build_tree():
        root = BinTree(30,
                        BinTree(20,
                                BinTree(10,
                                        BinTree(5,None,None),
                                        BinTree(15,None,None)
                                        ),
                                BinTree(25,None,None)
                                ),
                        BinTree(50,
                                BinTree(40,
                                        BinTree(35,None,None),
                                        BinTree(45,None,None)
                                        ),
                                BinTree(55,None,None)
                                )
                        )
        return root

def find_height(node):
	if node == None:
		return -1

	left = find_height(node.left)
	right = find_height(node.right)
	
	return max(left,right)+1

root = build_tree()
print find_height(root)
