
def twoSum(nums, target):
        s = []      
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    s.append(i)
                    s.append(j)
                    return s

def reverse(x):	
	if x > 0:	
		x = str(x)	
		if x[-1] == '0':
			x = x[:-1]
			x = x[::-1]
		else:
			x = x[::-1]
	elif x < 0:
		x = str(x)
		if x[-1] == '0':
			x = x[1:]
			x = x[:-1]
			x = x[::-1]
			x = '-' + x
		else:
			x = x[1:]
			x = x[::-1]
			x = '-' + x
	x = int(x)
	if x > -2**31 and x < ((2**31) -1):
		return x
	else:
		return 0 

def mySqrt(x):
	return int(x**0.5)


if __name__ == '__main__':

	#print twoSum([2, 7, 11, 15], 9)
	#print reverse(1534236469)
	