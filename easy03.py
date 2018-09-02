
# 21, Peak Index in a Mountain Array
def peakIndexInMountainArray(A):
	# return A.index(max(A))

	# check the neighbor of mid
	l, r = 0, len(A)-1
	while l + 1 < r:
		mid = (l+r)/2
		if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
			return mid
		if A[mid]<A[mid+1]:
			l = mid
		else:
			r = mid
	if A[l] < A[r]:
		return r
	return l

# 22, Array Partition I
def arrayPairSum(nums):
	return sum(sorted(nums)[::2])
	# list[start:end:step]

# 23, self dividing numbers 
def selfDividingNumbers(left,right):
	out = []
	for num in range(left,right+1):
		s_num = str(num)
		l_num = len(s_num)
		count = 0
		if "0" in s_num:
			continue
		else:
			for d in s_num:
				if num % int(d) == 0:
					count += 1 
			if count == l_num:
				out.append(num)
	return out

	# not invert to str
	# result = []
	# for i in range(left, right+1):
	# 	if i < 10:
	# 		result.append(i)
	# 	else:
	# 		flag = True
	# 		num = i
	# 		while num > 0:
	# 			rem = num % 10
	# 			if not rem or i % rem:
	# 				flag = False
	# 				break
	# 			num = num / 10
	# 		if flag:
	# 			result.append(i)
	# return result

# 24, Transpose Matrix 
def transpose(A):
	# zip(*A)

	# initialize output matrix
	# t=[[0]*len(A) for j in range(len(A[0]))]
	# for i in range(len(A)):
		# for j in range(len(A[0])):
			# t[j][i]=A[i][j]               
	# return t

	lA = len(A)
	lN = len(A[0])
	out = []
	for i in range(lN):
		new = []
		for j in range(lA):
			new.append(A[j][i])
		out.append(new)
	return out 	

# 25, Middle of the Linked List 
def middleNode(head):
	tmp = head
	while tmp and tmp.next:
		head = head.next
		tmp = tmp.next.next
	return head

	# set two pointers, one is head with one step each iteration 
	# the other is tmp, with two steps each iteration 
	# when tmp reach the end, head just reaches the half of it 

	# if head == None:
	# 	return head
	# if head.next == None:
	# 	return head
	# p = head
	# q = head
	# while q.next:
	# 	p = p.next
	# 	q = q.next
	# 	if q.next != None:
	# 		q = q.next
	# return p

# 26, Number of lines To Write String - 
# like this one, especially the way how to apply dictionary 
def numberOfLines(widths, S):
	l2w = dict(zip(list('abcdefghijklmnopqrstuvwxyz'),widths))
	# generate a list of corresbonding width 
	S_widths = [l2w[s] for s in S]
	rows = 1
	start = 0 
	for i, w in enumerate(S_widths):
		if sum(S_widths[start:i+1]) > 100:
			rows += 1
			start = i 
	last_row = sum(S_widths[start:])
	return [rows, last_row]

	# using ord(), return ASCII, overlaying sum of the line space
	# num_lines = 1
	# size_of_line = 0
	# idx_offset = ord('a')
	# for char in S:
	# 	idx = ord(char) - idx_offset
	# 	width = widths[idx]
	# 	proposed_size_of_line = size_of_line + width
	# 	if proposed_size_of_line <= 100:
	# 		size_of_line = proposed_size_of_line
	# 	else:
	# 		num_lines += 1
	# 		size_of_line = width        
	# return [num_lines,size_of_line]

# 27, Leaf-Similar Trees 
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

if __name__ == '__main__':

	# print selfDividingNumbers(1,22)
	# print numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
	print leafSimilar([3,5,1,6,2,9,8,null,null,7,4], [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8])






