
# 1, Shortest Distance to a Character
def shortestToChar(S,C):
	c_index = []
	out = [0]*len(S)
	for i,c in enumerate(S):
		if c == C:
			c_index.append(i)
	for i,c in enumerate(S):
		if c != C:
			out[i] = min(list(map(lambda x: abs(x-i),c_index)))
	return out 

# 2, Peak Index in a Mountain Array
def peakIndexInMountainArray(A):
	# return A.index(max(A))

	# check the neighbor of mid
	l, r = 0, len(A)-1
	while l + 1 < r:
		mid = (l+r)/2
		if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
			return mid
		if A[mid]<A[mid+1]:
			l = mid
		else:
			r = mid
	if A[l] < A[r]:
		return r
	return l 	


# 3, Number of lines To Write String - 
# like this one, especially the way how to apply dictionary 
def numberOfLines(widths, S):
	l2w = dict(zip(list('abcdefghijklmnopqrstuvwxyz'),widths))
	# generate a list of corresbonding width 
	S_widths = [l2w[s] for s in S]
	rows = 1
	start = 0 
	for i, w in enumerate(S_widths):
		if sum(S_widths[start:i+1]) > 100:
			rows += 1
			start = i 
	last_row = sum(S_widths[start:])
	return [rows, last_row]

	# using ord(), return ASCII, overlaying sum of the line space
	num_lines = 1
	size_of_line = 0
	idx_offset = ord('a')
	for char in S:
		idx = ord(char) - idx_offset
		width = widths[idx]
		proposed_size_of_line = size_of_line + width
		if proposed_size_of_line <= 100:
			size_of_line = proposed_size_of_line
		else:
			num_lines += 1
			size_of_line = width        
	return [num_lines,size_of_line]

# 4, Nim Game
def canWinNim(n):
	return False if int(n % 4) == 0 else True

# 5, Next Greater Element I
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

# 6, Fizz Buzz
def fizzBuzz(n):
	out = []
	for i in range(1,n+1):
		if i % 3 == 0 and i % 5 != 0:
			out.append("Fizz")
		elif i % 3 != 0 and i % 5 == 0:
			out.append("Buzz")
		elif i % 3 == 0 and i % 5 == 0:
			out.append("FizzBuzz")
		else:
			out.append(str(i))
	return out 





if __name__ == '__main__':

	
	# print numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
	# print reverseWords('ok haha')
	# print reverseStr("abcdefg", 2)
	print fizzBuzz(15)




