
'''
1, Flipping an Image
2, Remove Duplicates from Sorted Array
3, Array Partition I
4, Transpose Matrix 
5, Toeplitz Matrix
6, Reshape the Matrix 
7, Monotonic Array 
8, Majority Element
9, Plus one
10, Search Insert Position

'''

# 1, Flipping an Image
def flipAndInvertImage_l(A):
	new = []
	for p in A:
		p = p[::-1]
		new_p = []
		for i in p:
			i = 1-i
			new_p.append(i)
		new.append(new_p)
	return new

def flipAndInvertImage(A):
	return [[1-i for i in row[::-1]] for row in A]

# 2, Remove Duplicates from Sorted Array
# modify on the input array, time:O(n), space:O(1)
def removeDuplicates(nums):
	l_nums = len(nums)
	if l_nums == 0:
		return 0

	count = 0 
	for i in range(l_nums):
		if nums[count] != nums[i]:
			nums += 1
			nums[count] = nums[i]
	return count+1

# return the size chaning of the un-duplicated list 
def removeDuplicates01(nums):
	l_nums = len(nums)
	d_len = set()
	i = 0
	
	while i+1 < l_nums:
		count = 1
		if nums[i] == nums[i+1]:	
			count = 1		
			d_len.add(count)
			i += 1
		else:
			count += 1
			d_len.add(count)
			i += 1
	return list(d_len)

# 3, Array Partition I
def arrayPairSum(nums):
	return sum(sorted(nums)[::2])
	# list[start:end:step]

# 4, Transpose Matrix 
def transpose(A):
	# zip(*A)

	# initialize output matrix
	t=[[0]*len(A) for j in range(len(A[0]))]
	for i in range(len(A)):
		for j in range(len(A[0])):
			t[j][i]=A[i][j]               
	return t

def transpose01(A):
	lA = len(A)
	lN = len(A[0])
	out = []
	for i in range(lN):
		new = []
		for j in range(lA):
			new.append(A[j][i])
		out.append(new)
	return out
 
# 5, Toeplitz Matrix
def isToeplitzMatrix(m):
	for i in range(len(m) - 1):
		for j in range(len(m[0]) - 1):
			if m[i][j] != m[i + 1][j + 1]:
				return False
	return True

def isToeplitzMatrix01(m):
	# in one line
	return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))

# 6, Reshape the Matrix 
def matrixReshape(nums,r,c):
	if r*c != len(nums)*len(nums[0]):
		return nums 
	else:
		out = []
		temp = []
		count = 0
		for i in range(len(nums)):
			for j in range(len(nums[0])):
				temp.append(nums[i][j])
				count += 1
				if count == c:
					out.append(temp)
					temp = []
					count = 0
		return out 

# 7, Monotonic Array 
def isMonotonic(A):
	# cmp(), compare two variables (x,y), if x<y return -1, if x=y, return 0, if x>y return 1
	return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}

	# comapre each element from two ends
	if len(A) < 2: return True 
	l, r = 0, len(A) - 1
	J = True if A[l] < A[r] else False 
	while l < r: 
		if J == True: 
			# increading trend 
			if A[l] > A[r] or A[l] > A[l+1] or A[r-1] > A[r]:
				return False
			l += 1
			r -= 1
		elif J == False: 
			# decreasing trend 
			if A[l] < A[r] or A[l] < A[l+1] or A[r-1] < A[r]:
				return False
			l += 1
			r += 1
	return True 

def isMonotonic01(A):
	# using Flag
	if len(A) <= 2: return True
	Flag = None
	for i in range(1,len(A)):
		if A[i] != A[i-1] and Flag == None:
			Flag = (A[i] > A[i-1])
		if Flag:
			temp = (A[i] >= A[i-1])
			if temp != Flag: return False
		elif Flag != None:
			temp = (A[i] > A[i-1])
			if temp != Flag: return False
	return True

# 8, Majority Element 
def majorityElement(nums):
	return max(set(nums), key=nums.count)

# 9, Plus one
def plusOne(digits):

	len_d = len(digits)
	temp = 0
	for i in range(len_d):
		temp = temp + digits[i]* (10**(len_d-i-1))
	temp += 1
	temp2 = temp

	n_digits = []
	numRange = 1
	while temp/ 10 > 0:
		numRange += 1
		temp = temp / 10
	i = 0
	while i < numRange:
		dig = temp2 % 10
		n_digits.append(dig)
		temp2 = temp2 /10 
		i += 1

	return n_digits[::-1]

def plusOne_r(digits):
	# using recursion
	if len(digits) == 0:
		digits = [1]
	elif digits[-1] == 9:
		digits = self.plusOne(digits[:-1])
		digits.extend([0])
	else:
		digits[-1] += 1
	return digits

# 10, Search Insert Position
def searchInsert(nums, target):

	for i in range(len(nums)):
		if nums[i] == target:
			return i
		elif target > nums[len(nums)-1]:
			return len(nums)
		else:
			while nums[i] < target:
				i += 1
			return i 

if __name__ == '__main__':

	# print matrixReshape([[1,2,3],[4,5,6]],3,2)
	# print plusOne([1,2,3,0])
	# print searchInsert([1,3,5,6],7)
	




