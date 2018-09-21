
'''
Tree - each node could represent the subtree under it

1, Merge Two Binary Trees
2, Leaf-Similar Trees 
3, Search in a Binary Search Tree
4, Average of Levels in Binary Tree
5, Maximum Depth of N-ary Tree - DFS 
6, Maximum Depth of Binary Tree - DFS 
7, Increasing Order Search Tree - DFS 
8, Construct String from Binary Tree

'''

# 1, Merge Two Binary Trees
def mergeTrees(t1,t2):
	
	# method 1
	if not t1 and not t2: return None
	if t1:
		v1, L1, R1 = t1.val, t1.left, t1.right
	else:
		v1, L1, R1 = 0, None, None
	if t2:
		v2, L2, R2 = t2.val, t2.left, t2.right
	else:
		v2, L2, R2 = 0, None, None
	node = TreeNode(v1+v2)
	node.left = self.mergeTrees(L1, L2)
	node.right = self.mergeTrees(R1, R2)
	return node

def mergeTrees01(t1,t2):
	if t1==None:
		return t2
	elif t2==None:
		return t1
	t1.val+=t2.val
	t1.left=self.mergeTrees(t1.left, t2.left)
	t1.right=self.mergeTrees(t1.right, t2.right)
	return t1

# 2, Leaf-Similar Trees 
def leafSimilar(root1, root2):
	# yield, different from return, can save the valu in memory 
	# recursive use dfs function 
	# all(), iterative judge every element if it is true 
	def dfs(node):
		if not node: return
		if not node.left and not node.right: yield node.val
		for i in dfs(node.left): yield i
 		for i in dfs(node.right): yield i
	return all(a == b for a, b in itertools.izip_longest(dfs(root1), dfs(root2)))

	# stringforward method, adding another function beside
	return self.findleaf(root1) == self.findleaf(root2)
def findleaf(self, root):
	if not root: return []
	if not (root.left or root.right): return [root.val]
	return self.findleaf(root.left) + self.findleaf(root.right)

# 3, Search in a Binary Search Tree
def searchBST(self,root,val):
		current = root 
		while current:
			if current.val == val:
				return current 
			elif current.val > val:
				current = current.left
			else:
				current = current.right 
		return None

# 4, Average of Levels in Binary Tree
def averageOfLevels(root):
	if not root:
		return []

	# read noot, since Treenode is not iterable, 
	result, currentL = [],[root]
	while currentL:
		nodes,nextL = [],[]
		for node in currentL:
			nodes.append(node.val)
			if node.left:
				nextL.append(node.left)
			if node.right:
				nextL.append(node.right)
		result.append(sum(nodes)/len(nodes)*1.0)
		currentL = nextL
	return result 

# 5, Maximum Depth of N-ary Tree - DFS 
def maxDepth(self,root):
	# if it's an empty tree, return 0
	if not root: return 0
	# if there is no children node, return 1 
	if not root.children: return 1
	out = []
	for node in root.children:
		out.append(self.maxDepth(node))
	return max(out) + 1

	# code in one line 
	return max(self.maxDepth(node) for node in root.children) + 1

def maxDepth01(self,root):
	if not root: return 0
	return self.getDepth(root)

def getDepth(self,node):
	max_depth = 0
	for c in node.children:
		d = self.getDepth(c)
		if d > max_depth:
			max_depth = d
	return max_depth + 1

# 6, Maximum Depth of Binary Tree - DFS 
def maxDepthBT(self,root):
	if not root: return 0
	return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

def maxDepthBT01(self,root):
	# stack for level order 
	if not root: return 0
	tstack,h = [root],0
	# count number of levels 
	while tstack:
		nextL = []
		while tstack:
			top = tstack.pop()
			if top.left:
				nextL.append(top.left)
			if top.right:
				nextL.append(top.right)
		tstack = nextL
		h += 1
	return h 

def maxDepthBT02(self,root):
	# queue for level order - deque is an updgrade list hahaha
	# Deque is preferred over list in the cases where we need quicker append and pop operations 
	# from both the ends of container, as deque provides an O(1) time complexity for append and 
	# pop operations as compared to list which provides O(n) time complexity.
	if not root: return 0
	tqueue,h = collections.deque(),0
	tqueue.append(root)
	while tqueue:
		nextL = collections.deque()
		while tqueue:
			front = tqueue.popleft()
			if front.left:
				nextL.append(front.left)
			if front.right:
				nextL.append(front.right)
		tqueue = nextL
		h += 1
	return h 

def maxDepthBT03(self,root):
	if root: 
		level = root
	else:
		return 0
	depth = 0
	while level:
		depth += 1
		queue = []
		for node in level:
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		level = queue
	return depth 

# 7, Increasing Order Search Tree 
def increasingBST(self,root):
	if not root: return None
	res,stack = [],[]
	while root or stack:
		if root:
			stack.append(root)
			root = root.left
		else:
			node = stack.pop()
			res.append(node.val)
			root = node.right
		# adjust node.right  
		dummy = pre = TreeNode(-1)
		i = 0
		while i < len(res):
			pre.right = TreeNode(res[i])
			pre = pre.right 
			i+=1
		return dummy.right 

def increasingBST(self, root, tail = None):
	# recursive solution 
	if not root: return tail
	res = self.increasingBST(root.left, root)
	root.left = None
	root.right = self.increasingBST(root.right, tail)
	return re

# 8, Construct String from Binary Tree
def tree2str(self,t):

	def preorder(root):
		if not root: return ""
		s = str(root.val)
		l = preorder(root.left)
		r = preorder(root.right)

		if l == "" and r == "":
			return s
		elif l == "":
			s += "()" + "("+r+")"
		elif r == "":
			s += "("+l+")"
		else:
			s += "("+l+")" + "("+r+")" 
		return s 
	return preorder(t)

def tree2str01(self, t):
	if not t: return ""
	res = ""
	left = self.tree2str(t.left)
	right = self.tree2str(t.right)
	if left or right:
	    res += "(%s)" % left
	if right:
	    res += "(%s)" % right
	return str(t.val) + res

def tree2str(self, t):
	# use format()
	if not t: return ''
	left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
	right = '({})'.format(self.tree2str(t.right)) if t.right else ''
	return '{}{}{}'.format(t.val, left, right)


	
	









