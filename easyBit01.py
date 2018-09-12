
import operator

'''
bitwise operator, https://wiki.python.org/moin/BitwiseOperators

1, Hamming Distance
2, Number Complement
3, Single Number
4, Find the Difference

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
	prime = [2,3,5,7]
	count = 0
	for num in range(L,R+1):
		if str(bin(num)).count("1") in prime:
			count += 1
	return count



if __name__ == '__main__':

	# print hammingDistance_s(1,4)
	# print hammingDistance(1,4)
	# print findComplement(5)
	# print singleNumber([2,2,1])
	# print findTheDifference("abcd","abecd")
	# print findTheDifference01("abcd","abecd")
	print countPrimeSetBits(990, 1048)





	