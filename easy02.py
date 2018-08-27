# 11 Search Insert Position
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

# 12 Plus one
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

# 12_using recursion
def plusOne_r(digits):

	if len(digits) == 0:
		digits = [1]
	elif digits[-1] == 9:
		digits = self.plusOne(digits[:-1])
		digits.extend([0])
	else:
		digits[-1] += 1
	return digits

# 13 Roman to Integer
def romanToInt(s):
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(0, len(s) - 1):
		if roman[s[i]] < roman[s[i+1]]:
			z -= roman[s[i]]
		else:
			z += roman[s[i]]
	return z + roman[s[-1]]

# 14 Jeswels and Stones
# map() function - applying the given function to each item of a given iterable
def numJewelsInStones(J, S):
	return sum(map(J.count, S))
	# return len([c for c in S if c in J])

# 15 To Lower Case
def toLowerCase(str):
	return str.lower()

if __name__ == '__main__':

	#print searchInsert([1,3,5,6],7)
	plusOne([1,2,3,0])
	romanToInt("III")
	print numJewelsInStones("aA","aaaaAAC")

