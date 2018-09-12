
'''
11, Two Sum
12, Merge Sorted Array - only modify nums1 in-place
13, Third Maximum Number
14, Rotate Array 
15, Non-decreasing Array
16, Move Zeros

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



if __name__ == '__main__':

	# print twoSum([2, 7, 11, 15], 9)
	# print thirdMax([2,2,3,1])
	# print rotate([2,3,4,5,1,6],3)
	# print checkPossibility01([4,3,2,3])
	print moveZeroes([0,1,0,3,12])





