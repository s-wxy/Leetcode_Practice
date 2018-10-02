
'''
11, Two Sum
12, Merge Sorted Array - only modify nums1 in-place
13, Third Maximum Number
14, Rotate Array 
15, Non-decreasing Array
16, Move Zeros
17, Fair Candy Swap 
18, Max Consecutive Ones
19, Sort Array By Parity
20, Maximum Average Subarray I
21, Find All Numbers Disappeared in an Array
22, Max Area of Island 

'''

# 11, Two Sum
def twoSum(nums, target):
        s = []      
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    s.append(i)
                    s.append(j)
                    return s

# 12, Merge Sorted Array - only modify nums1 in-place
def merge(nums1,m,nums2,n):
	nums[m:]=nums2
	return nums1.sort() 

# 13, Third Maximum Number
def thirdMax(nums):
	if len(set(nums)) < 3:
		return max(nums)
	else:
		return sorted(set(nums),reverse=True)[2]

	# write in one line 
	# value_when_true if condition else value_when_false
	return max(nums) if len(set(nums)) < 3 else sorted(set(nums),reverse=True)[2]

# 14, Rotate Array 
def rotate(nums,k):
	n = len(nums)
	k = n%k # in case k is bigger than len
	nums[:] = nums[n-k:] + nums[:n-k]

# 15, Non-decreasing Array
def checkPossibility(nums):	
	count = 0
	for i in range(len(nums)-1):
		if nums[i] <= nums[i+1]:
			continue
		else:
			if i == 0:
				nums[i] = nums[i+1]
				count += 1
			else:
				if nums[i+1] >= nums[i-1]:
					nums[i] = nums[i-1]
					count += 1
				else:
					nums[i+1] = nums[i]
					count += 1
		if count >= 2:
			return False 
	return True

def checkPossibility01(nums):	
	cnt = 0
	for i in range(1, len(nums)):
		if cnt==2:
			break
		if nums[i]>=nums[i-1]:
			continue
		cnt += 1
		if i-2>=0 and nums[i-2]>nums[i]:
			nums[i]=nums[i-1]
		else:
			nums[i-1]=nums[i]
	return cnt<=1

# 16, Move Zeros 
def moveZeroes(nums):
	i,j = 0,0
	while i < len(nums):
		if nums[i] != 0:
			nums[i],nums[j] = nums[j],nums[i]
			j += 1
		i += 1
		print nums
	return nums

# 17, Fair Candy Swap 
# check any element in A, if the restOfA + anyElementInB == change
# then return this element and the one in B 
def fairCandySwap(A, B):
	change = (sum(A) + sum(B))/2
	B = set(B)
	for i in set(A):
		if change - (sum(A)-i) in B:
			return [i, change - (sum(A)-i)]

# 18, Max Consecutive Ones
def findMaxConsecutiveOnes(nums):
	out, count = 0, 0
	for num in nums:
		if num == 1:
			count += 1			
		else:
			out = max(out,count)
			count = 0 

			# can also code as:
			# if count > out:
			# 	out = count
			# count = 0 

	return max(out,count)

# 19, Sort Array By Parity 
def sortArrayByParity(A):
	oddA, evenA = [],[]
	for c in A:
		if c % 2 == 0:
			evenA.append(c)
		else:
			oddA.append(c)
	return evenA + oddA

def sortArrayByParity01(A):
	# use two pointers, in-place sort array 
	i, j = 0, len(A)-1
	while i < j:
		if A[i] % 2 == 0:
			i += 1
			continue
		if A[j] % 2 == 1:
			j -= 1
			continue
		A[i], A[j] = A[j], A[i]
		i += 1
		j -= 1
	return A

# 20, Maximum Average Subarray I
def findMaxAverage(nums,k):
	numsL, mean = len(nums),[]
	for i in range(0, numsL - k + 1):
		mean.append(sum(nums[i:i+k]))	
	return float(max(mean))/float(k)

def findMaxAverage01(nums,k):
	maxi = sum(nums[:k])
	temp = maxi 
	for i in range(len(nums)-k):
		temp = temp - nums[i] + nums[i+k]
		if temp > maxi:
			maxi = temp 
	return float(maxi) / float(k) 

# 21, Find All Numbers Disappeared in an Array
def findDisappearedNumbers(nums):
	# Time Limit Exceeded
	res = []
	for i in range(len(nums)):
		n = i + 1
		# we should have set(nums) outside the loop to reduce complexity
		if n not in set(nums):
			res.append(n)
	return res 

def findDisappearedNumbers01(nums):
	if len(nums) == 0: return nums
	b,c = set(nums), []
	for i in range(1,len(nums)+1):
		if i not in b:
			c.append(i)
	return c


def findDisappearedNumbers02(nums):
	return list(set(range(1, len(nums)+1)) - set(nums))

def findDisappearedNumbers03(nums):
	for i in range(len(nums)):
		idx = abs(nums[i]) - 1
		nums[idx] = - abs(nums[idx])
	return [i+1 for i in range(len(nums)) if nums[i] > 0]

# 22, Max Area of Island 
def maxAreaOfIsland(grid):
	m,n = len(grid),len(grid[0])
	def dfs(i,j):
		if 0 <= i < m and 0 <= j <= n and grid[i][j]:
			grid[i][j] = 0 
		return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
	return 0 

	areas = [dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]]
	return max(areas) if areas else 0 

def maxAreaOfIsland01(self,grid):

	ret = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				n = self.findSize(grid,i,j)
				if n > ret:
					ret = n
	return ret 
def findSize(self,grid,i,j):
	grid[i][j],n = 0,1
	if i-1 >= 0 and grid[i-1][j] == 1:
		n += self.findSize(grid,i-1,j)
	if i+1 < len(grid) and grid[i+1][j] == 1:
		n += self.findSize(grid,i+1,j)
	if j-1 >= 0 and grid[i][j-1] == 1:
		n += self.findSize(grid,i,j-1)
	if j+1 < len(grid) and grid[i][j+1] == 1:
		n += self.findSize(grid,i,j+1)
	return n 



if __name__ == '__main__':

	# print twoSum([2, 7, 11, 15], 9)
	# print thirdMax([2,2,3,1])
	# print rotate([2,3,4,5,1,6],3)
	# print checkPossibility01([4,3,2,3])
	# print moveZeroes([0,1,0,3,12])
	# print fairCandySwap([1,1],[2,2])
	# print findMaxConsecutiveOnes([1,1,0,1,1,1])
	# print sortArrayByParity([3,1,2,4])
	# print findMaxAverage([1,12,-5,-6,50,3],4)





