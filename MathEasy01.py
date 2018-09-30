
'''
1, Reverse Integer
2, Sqrt(x)
3, Palindrome Number
4, Roman to Integer
5, self dividing numbers 
6, Add Digits 
7, Projection Area of 3D Shapes - transpose matrix, clevel
8, Smallest Range I
9, Arranging Coins
10, Binary Gap 
11, Surface Area of 3D Shapes 

'''


# 1, Reverse Integer
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

# 2, Sqrt(x)
def mySqrt(x):
	return int(x**0.5)

# 3, Palindrome Number
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

# 4, Roman to Integer
def romanToInt(s):
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(0, len(s) - 1):
		if roman[s[i]] < roman[s[i+1]]:
			z -= roman[s[i]]
		else:
			z += roman[s[i]]
	return z + roman[s[-1]]

# 5, self dividing numbers 
def selfDividingNumbers(left,right):
	out = []
	for num in range(left,right+1):
		s_num = str(num)
		l_num = len(s_num)
		count = 0
		if "0" in s_num:
			continue
		else:
			for d in s_num:
				if num % int(d) == 0:
					count += 1 
			if count == l_num:
				out.append(num)
	return out

def selfDividingNumbers01(left,right):
	# not invert to str
	result = []
	for i in range(left, right+1):
		if i < 10:
			result.append(i)
		else:
			flag = True
			num = i
			while num > 0:
				rem = num % 10
				if not rem or i % rem:
					flag = False
					break
				num = num / 10
			if flag:
				result.append(i)
	return result

# 6, Add Digits 
def addDigits(num):
	while num >= 10:
		temp = 0
		while num >0:
			temp += num%10
			num /= 10
		num = temp 
	return num 

# 7, Projection Area of 3D Shapes 
def projectionArea(grid):
	xoy = sum(1 for i in grid for j in i if j != 0)
	xoz = sum([max(i) for i in grid])
	# using zip() and *, to tanspose matrix 
	zoy = sum([max(i) for i in list(zip(*grid))])
	return xoy + xoz + zoy 

# 8, Smallest Range I
def smallestRangeI(A,K):
	# case 1, if (max number -K ) < (min number + K), return 0
	# case 2, if (max number -K ) > (min number + K), return difference
	return max(0, (max(A)-K) - (min(A)+K))

# 9, Arranging Coins
def arrangingCoins(n):
	i,s = 1,1
	while s < n:
		i += 1
		s += i 
	return i -1 

def arrangingCoins01(n):
	return int(((8*n+1)**0.5-1)/2)

def arrangingCoins02(n):
	start, end = 0, n
	while start + 1< end:
		mid = start + (end-start)/2
		if (1+mid)*mid/2 > n:
			end = mid 
		elif (1+mid)*mid/2 < n:
			start = mid
		else: return mid
	if (1+end)*end/2 == n: 
		return end
	return start 

# 10, Binary Gap 
def binaryGap(N): 
	ic,res = [],[]
	for i,c in enumerate(bin(N)):
		if c == '1': 
			ic.append(i)
	for a,b in zip(ic,ic[1:]):
		res.append(b-a)
	if res: return max(res)
	else: return 0

def binaryGap01(N):
	# concise version 
	index = [i for i,v in enumerate(bin(N)) if v == '1']
	return max([b-a for a,b in zip(index,index[1:])] or [0])

def binaryGap02(N):
	# use & to find if bin(N) only have one '1'
	return max(len(c) for c in bin(N)[2:].strip('0').split('1') + 1 if N & (N-1) else 0)

# 11, Surface Area of 3D Shapes 
def surfaceArea(grid):
	n,res = len(grid),0
	for i in range(n):
		for j in range(n):
			if grid[i][j]: res += 2+grid[i][j]*4
			if i:res -= min(grid[i][j],grid[i-1][j]) * 2
			if j:res -= min(grid[i][i],grid[i][j-1]) * 2
	return res 

def surfaceArea01(grid):
	W = len(grid[0])
	H = len(grid)
	cnt = 0
	for in range(H):
		cnt += grid[i][0]
		for j in range(1,W):
			cnt += abs(grid[i][j]-grid[i][j-1])
		cnt += grid[i][W-1]
	




if __name__ == "__main__":

	# print reverse(1534236469)
	# print romanToInt("III")
	# print selfDividingNumbers(1,22)
	# print selfDividingNumbers01(1,22)
	# print isPalindrome(121)
	# print smallestRangeI([1,3,6],3)
	# print arrangingCoins(5)
	# print binaryGap(8)
	print surfaceArea([[2]])

