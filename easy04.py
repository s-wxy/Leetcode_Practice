# 31, Reverse String
def reverseString(s):
	return s[::-1]

# 32, Reverse Vowels of a String
def reverseVowels(s):
	vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	s = list(s)
	l = 0
	r = len(s)-1
	while l < r:
		# using while loop to find vowels 
		# time complexity is O(n), since only go through the string once 
		while l < r and s[l] not in vowels:
			l += 1
		while r > l and s[r] not in vowels:
			r -= 1
		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1
	return ''.join(s) 

# 33, Number Complement. apply BitwiseOperators
def findComplement(num):
	i = 1
	while i <= num:
		# return i iwht the bits shifted to the left by 1 place, new bits on right are 0
		i = i << 1
		# bitwise exclusive or 
	return (i-1) ^ num 

	# string modify method 
	combin = ''
	for digit in bin(num)[2:]:
		if digit=='0':
			combin += '1'
		else:
			combin += '0'
	return int(combin, 2)

# 34, Majority Element 
def majorityElement(nums):
	return max(set(nums), key=nums.count)

# 35, Subdomain Visit Count
def subdomainVisits(cpdomains):
	

if __name__ == '__main__':

	#print reverseVowels("hello")
	print findComplement(5)