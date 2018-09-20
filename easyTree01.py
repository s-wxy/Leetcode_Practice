
'''
Tree - each node could represent the subtree under it

1, Merge Two Binary Trees
2, Leaf-Similar Trees 
3, Search in a Binary Search Tree
4, Average of Levels in Binary Tree
5, Maximum Depth of N-ary Tree - DFS 
6, Maximum Depth of Binary Tree - DFS 

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

# 6, 



	
	









