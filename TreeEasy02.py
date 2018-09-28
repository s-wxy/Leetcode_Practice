
'''
1, N-ary Tree Preorder Traversal
2, N-ary Tree Level Order Traversal - BFS
3, N-ary Tree Postorder Traversal, recursion & iterative extend() VS append()
4, Trim a Binary Search Tree - DFS

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

# 4, Trim a Binary Search Tree
# case1, root.val < L, pick root.right subtree == delete all left nodes 
# case2, root.cal > R, pick root.left 
# case3, in the range [L,R], continue  
def trimBST(self,root,L,R):
	if not root: return root 
	if root.val > R: return self.trimBST(root.left,L,R)
	if root.val < L: return self.trimBST(root.right,L,R)

	root.left = self.trimBST(root.left,L,R)
	root.right = self.trimBST(root.right,L,R)

	return root 

def trimBST01(self,root,L,R):
	def trim(node):
		if not node: return None 
		node.left, node.right = trim(node.left),trim(node.right)
		# node's value is not in range
		# select one or none of its children as replacement 
		if not (L <= node.val <= R):
			node = node.left if node.left else node.right 
		return node 
	return trim(root)









