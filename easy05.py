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





if __name__ == '__main__':

	#print singleNumber([2,2,1])
	#print isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
	#print nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7])
	
	#print checkPossibility([2,3,4])
	print rotate([1,2,3,4],6)
	
	





