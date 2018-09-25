
'''
1, N-ary Tree Postorder Traversal, extend() VS append()

'''


# 1, N-ary Tree Postorder Traversal
def postorder(self,root):
	# recursion method, Tree traversal
	# https://en.wikipedia.org/wiki/Tree_traversal#Post-order_(LRN)
	res = []
	if root == None: return res
	def recursion(root,res):
		for child in root.children:
			recursion(child,res)
		res.append(root.val)
	recursion(root,res)
	return res

def postorder01(self,root):
	# iterative method, use of stack.extend()
	res = []
	if root == None: return res
	stack = [root]
	while stack:
		curr = stack.pop()
		res.append(curr.val)
		stack.extend(curr.children)
	return res[::-1]