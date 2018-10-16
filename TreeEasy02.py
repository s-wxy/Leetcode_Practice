
'''
1, N-ary Tree Preorder Traversal
2, N-ary Tree Level Order Traversal - BFS
3, N-ary Tree Postorder Traversal, recursion & iterative extend() VS append()
4, Trim a Binary Search Tree - DFS
5, Invert Binary Tree - iterative, BFS(queue), DFS(stack)
6, Employee Importance - DFS

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

# 5, Invert Binary Tree 
def invertTree(self,root):
	# recursively 
	if root:
		root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
		return root

def invertTree01(self,root):
	# BFS
	queue = collections.deque([root])
	while queue:
		node = queue.popleft()
		if node:
			node.left, node.right = node.right, node.left
			queue.append(node.left)
			queue.append(node.right)
	return root 

def inverTree02(self,root):
	# DFS
	stack = [root]
	while stack:
		node = stack.pop()
		if node:
			node.left, node.right = node.right, node left
			stack.extend([node.right,node.left])
	return root 

# 6, Employee Importance
def getImportance(self, employees, id):
	d = {e.id:e for e in employees}	
	ret=0
	stk=[d[id]] #we can go straight to the employee since we have a map already
	while stk: 
		top = stk.pop()
		ret+=top.importance
		for n in top.subordinates:
			stk.append(d[n])
	return ret

def getImportance01(self, employees, id):
	self.e_dict = dict()
	for e in employees:
		self.e_dict[e.id] = e
def dfs(self, e_node):
	if not e_node: return 0
	else:
		sub_sum = 0
		for e in e_node.subordinates:
			sub_sum += self.dfs(self.e_dict[e])
		return sub_sum + e_node.importance

def getImportance02(self, employees, id):
	emps = {employee.id: employee for employee in employees}
	def dfs(id):
		sum = emps[id].importance
		for sub_id in emps[id].subordinates:
			sum += dfs[sub_id]
		return sum 
	return dfs(id)






