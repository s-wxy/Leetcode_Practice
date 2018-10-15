
import operator

'''
bitwise operator, https://wiki.python.org/moin/BitwiseOperators

1, Hamming Distance
2, Number Complement
3, Single Number
4, Find the Difference
5, Prime Number of Set Bits in Binary Representation
   recall - number of set bits an integer has is the number of 1s present when written in binary
6, Binary Number with Alternating Bits
7, Letter Case Permutation 
8, Sum of Two Integers

'''

# 1, Hamming Distance, when x and y have same distance 
def hammingDistance_s(x, y):
	diff  = 0 
	for chx, chy in zip (bin(x),bin(y)):
		if chx != chy:
			diff += 1
	return diff

def hammingDistance(x, y):
	return bin(x^y).count('1')

	# x ^ y 	
	# Does a "bitwise exclusive or". 
	# Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, 
	# and it's the complement of the bit in x if that bit in y is 1

# 2, Number Complement
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

# 3, Single Number
def singleNumber(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber01(nums):	
    # using bitwise
	res = 0
	for num in nums:
		res ^= num
	return res

# 4, Find the Difference
def findTheDifference(s, t):
	s,t = sorted(s),sorted(t)
	if s == t[:-1]:
		return t[-1]
	else:
		for w in zip(s,t):
			if w[0] != w[1]:
				return w[1]

# Using XOR
def findTheDifference01(s,t):
	return chr(reduce(operator.xor, map(ord, s + t)))

# 5, Prime Number of Set Bits in Binary Representation
def countPrimeSetBits(L, R):
	prime = [2,3,5,7,11,13,17,19]
	count = 0
	for num in range(L,R+1):
		if bin(num).count("1") in prime:
			count += 1
	return count

def countPrimeSetBits00(L, R):
	# one line 
	return len([1 for i in range(L,R+1) if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19]])

def countPrimeSetBits01(L, R):
	# in one line, use map  
	prime = [2,3,5,7,11,13,17,19]
	return sum(map(lambda x: bin(x).count('1') in prime, range(L, R+1)))

# 6, Binary Number with Alternating Bits
def hasAlternatingBits(n):
	return "11" not in bin(n) and "00" not in bin(n)

# 7, Letter Case Permutation 
def letterCasePermutation(S):
	res = [""]
	for s in S:
		if not s.isalpha():
			for i in range(len(res)):
				res[i] += s
		else:
			for i in range(len(res)):
				tmp = res[i]
				res[i] += s.lower()
				res.append(tmp + s.upper())
	return res

def letterCasePermutation01(S):
	if not S: return [""]
	index = -1
	for i in range(len(S)):
		if S[i].isalpha():
			index = i
			break
	if index == -1:
		return [S]
	else:
		tmp = seld.letterCasePermutation01(S[index+1:])
		res = []
		for s in tmp:
			res.append(S[:index]+S[index].lower()+s)
			res.append(S[:index]+S[index].upper()+s)
		return res 

def letterCasePermutation02(S):
	# seapcase(), change lower(upper) to upper(lower)
	res = [S]
	for i,c in enumerate(S):
		if c.isalpha():
			res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
	return res 

def letterCasePermutation3(S):
	# use stack
	S = list(S)
	solutions = ['']
	while S:
		last = S.pop()
		if last.isalpha():
			solutions = [last.lower() + x for x in solutions] + [last.upper() + x for x in solutions]
		else:
			solutions = [last + x for x in solutions]
	return solutions 

def letterCasePermutation04(S):
	res = ['']
	for ch in S:
		if ch.isalpha():
			res = [i+j for i in res for j in [ch.upper(),ch.lower()]]
		else:
			res = [i+ch for i in res]
	return res 

# 8, Sum of Two Integers
def getSum(a,b):
	list = [a,b]
	return sum(list)

def getSum01(a,b):
	# 32 bits interger max
	M = 0x7FFFFFFF
	# 32 bits interger min 
	N = 0x80000000
	# mask to get last 32 bits 
	mask = 0xFFFFFFFF
	while b != 0:
		# ^ get different bits and & get double 1s, << moves carry 
		a,b = (a^b) & mask, ((a&b)<<1) & mask
	# if a is negative, get a's 32 bits complement positive first 
	# then get 32-bit positive's Python complement negative 
	return a if a <= M else ~(a^mask)


if __name__ == '__main__':

	# print hammingDistance_s(1,4)
	# print hammingDistance(1,4)
	# print findComplement(5)
	# print singleNumber([2,2,1])
	# print findTheDifference("abcd","abecd")
	# print findTheDifference01("abcd","abecd")
	# print countPrimeSetBits(990, 1048)
	# print countPrimeSetBits00(990, 1048)
	# print hasAlternatingBits(11)
	print letterCasePermutation("a1b2")





	