
'''

1, Merge Two Binary Trees
2, Leaf-Similar Trees 
3, Search in a Binary Search Tree

'''

#1, Merge Two Binary Trees
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

	# method 2
	# if t1==None:
	# 	return t2
	# elif t2==None:
	# 	return t1
	# t1.val+=t2.val
	# t1.left=self.mergeTrees(t1.left, t2.left)
	# t1.right=self.mergeTrees(t1.right, t2.right)
	# return t1

#2, Leaf-Similar Trees 
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

#3, Search in a Binary Search Tree
class Tree():
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

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


if __name__ == '__main__':

	
	









