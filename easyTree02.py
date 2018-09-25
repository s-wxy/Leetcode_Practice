
'''
1, N-ary Tree Preorder Traversal
2, N-ary Tree Level Order Traversal - BFS
3, N-ary Tree Postorder Traversal, recursion & iterative extend() VS append()

'''

# 1, N-ary Tree Preorder Traversal
def preorder(self,root):
	if not root: return []
	


# 2, N-ary Tree Level Order Traversal
def levelOrder(self,root):
	# BFS
	stack,res = [root],[]
	while any(stack):
		res.append([node.val for node in stack])
		stack = [child for node in stack for child in node.children if child]
	return res 

def levelOrder01(self,root):
	if not root: return []
	stack,res = [root],[]
	while stack:
		temp,next_stack = [],[]
		for node in stack:
			temp.append(node.val)
			for child in node.children:
				next_stack.append(child)
		stack = next_stack
		res.append(temp)
	return res 

# 3, N-ary Tree Postorder Traversal
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









