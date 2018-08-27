# 01 Two Sum
def twoSum(nums, target):
        s = []      
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    s.append(i)
                    s.append(j)
                    return s

# 02 Reverse Integer
def reverse(x):	
	if x > 0:	
		x = str(x)	
		if x[-1] == '0':
			x = x[:-1][::-1]
		else:
			x = x[::-1]
	elif x < 0:
		x = str(x)
		if x[-1] == '0':
			x = '-' + x[1:][:-1][::-1]
		else:
			x = '-' +  x[1:][::-1]
	x = int(x)
	if x > -2**31 and x < ((2**31) -1):
		return x
	else:
		return 0 

# 03 Sqrt(x)
def mySqrt(x):
	return int(x**0.5)

# 04 Implement strStr()
def strStr(haystack, needle):
	if needle in haystack:
		return haystack.find(needle)
	else:
		return -1

# 05 Longest Common Prefix
def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	else:
		s1 = min(strs)
		s2 = max(strs)
		for i, c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]
		return s1

# 06 Valid Parentheses
def isValid(s):
	stack = []
	dict = {"]":"[", "}":"{", ")":"("}
	for char in s:
		if char in dict.values():
			stack.append(char)
		elif char in dict.keys():
			if stack == [] or dict[char] != stack.pop():
				return False
		else:
			return False
	if stack == []:
		return True
	else:
		return False

# 07 Length of the Last Word
def lengthOfLastWord(s):
	arr = s.strip(' ').split(' ')
	lword = arr[-1]
	return len(lword)

# 08 Palindrome Number
def isPalindrome(x):
	if x < 0:
		return False
	numRange = 1 
	while x/ numRange >= 10:
		numRange *= 10 
	while x:		
		num_f = x / numRange
		num_l = x % 10 
		if num_l != num_f:
			return False
		# update x - remove the first and the last digit 
		x = (x % numRange) / 10
		# update range - since remove two digits, range need low 2 level 
		numRange /= 100
	return True

# 09 Remove Duplicates from Sorted Array
# modify on the input array, time:O(n), space:O(1)
def removeDuplicates(nums):
	l_nums = len(nums)
	if l_nums == 0:
		return 0

	count = 0 
	for i in range(l_nums):
		if nums[count] != nums[i]
			nums += 1
			nums[count] = nums[i]
	return count+1


# 09 - 01, return the size chaning of the un-duplicated list 
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


# 10 Count and Say
def countAndSay(n):
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n - 1)
            if len(s) > 0:
                current = s[0]
                count = 0
                r = ""
                for i in range(len(s)):
                    if s[i] == current:
                        count += 1
                    else:
                        r = r + str(count) + current
                        current = s[i]
                        count = 1
                r = r + str(count) + current 
                return r



if __name__ == '__main__':

	#print twoSum([2, 7, 11, 15], 9)
	#print reverse(1534236469)
	#print strStr("hello", "ll")
	#print longestCommonPrefix(["dog","racecar","car"])
	#print isValid("((")
	#print lengthOfLastWord('a ')
	print removeDuplicates01([1,2])



	