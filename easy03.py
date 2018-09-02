
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



if __name__ == '__main__':

	print selfDividingNumbers(1,22)







