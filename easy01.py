

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


	#print reverse(1534236469)
	#print strStr("hello", "ll")
	#print longestCommonPrefix(["dog","racecar","car"])
	#print isValid("((")
	#print lengthOfLastWord('a ')
	print removeDuplicates01([1,2])



	