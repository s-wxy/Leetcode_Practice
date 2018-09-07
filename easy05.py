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

if __name__ == '__main__':

	#print singleNumber([2,2,1])
	#print isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
	print nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])




