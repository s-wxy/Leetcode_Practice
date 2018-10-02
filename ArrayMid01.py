
'''
1, Find All Duplicates in an Array


'''

# 1, Find All Duplicates in an Array
def findDuplicates(nums):
	# time limit exceeded 
	res = []
	for n in set(nums):
		if nums.count(n) == 2:
		    res.append(n)
	return res

def findDuplicates01(nums):
	# "1 < "
	# set *-1, as flag 
	res = []
	for n in nums:
		idx = abs(n) - 1
		if nums[idx] < 0:
			res.append(idx+1)
		else:
			nums[idx] *= -1
	return res 



if __name__ == "__main__": 

	print findDuplicates01([4,3,2,7,8,2,3,1])
