from collections import Counter

# 41, Single Number
def singleNumber(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key
	
    # using bitwise
	res = 0
	for num in nums:
		res ^= num
	return res

# 42, Toeplitz Matrix
def isToeplitzMatrix(m):
	for i in range(len(m) - 1):
		for j in range(len(m[0]) - 1):
			if m[i][j] != m[i + 1][j + 1]:
				return False
	return True

	# in one line
	return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))


# 43, Distribute Candies
def distributeCandies(candies):
	return min(len(candies)/2, len(set(candies)))

# 44, Next Greater Element I
def nextGreaterElement(findNums, nums):
	out = []
	for num in findNums:
		i = nums.index(num)
		if i == len(nums)-1:
			out.append(-1) 
		else:
			flag = 0	
			for g in range(i+1,len(nums)):				
				if nums[g] > num:
					flag = 1					
					out.append(nums[g])
					break
			if flag == 0:
				out.append(-1)
	return out

# 45, Nim Game
def canWinNim(n):
	return False if int(n % 4) == 0 else True

# 46, Reshape the Matrix 
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

# 47, Non-decreasing Array
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

# 48, Merge Sorted Array - only modify nums1 in-place
def merge(nums1,m,nums2,n):
	nums[m:]=nums2
	return nums1.sort() 

# 49, Rotate Array 
def rotate(nums,k):
	n = len(nums)
	k = n%k # in case k is bigger than len
	nums[:] = nums[n-k:] + nums[:n-k]

# 50, Third Maximum Number
def thirdMax(nums):
	if len(set(nums)) < 3:
		return max(nums)
	else:
		return sorted(set(nums),reverse=True)[2]

	# write in one line 
	# value_when_true if condition else value_when_false
	return max(nums) if len(set(nums)) < 3 else sorted(set(nums),reverse=True)[2]

if __name__ == '__main__':

	#print singleNumber([2,2,1])
	#print isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
	#print nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])
	#print matrixReshape([[1,2,3],[4,5,6]],3,2)
	#print checkPossibility([2,3,4])
	print rotate([1,2,3,4],6)
	#print thirdMax([2,2,3,1])
	





