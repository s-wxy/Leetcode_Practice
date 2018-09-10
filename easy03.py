
# 21, Peak Index in a Mountain Array
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

# 22, Array Partition I
def arrayPairSum(nums):
	return sum(sorted(nums)[::2])
	# list[start:end:step]

# 23, self dividing numbers 
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

# 24, Transpose Matrix 
def transpose(A):
	# zip(*A)

	# initialize output matrix
	# t=[[0]*len(A) for j in range(len(A[0]))]
	# for i in range(len(A)):
	# 	for j in range(len(A[0])):
	# 		t[j][i]=A[i][j]               
	# return t

	lA = len(A)
	lN = len(A[0])
	out = []
	for i in range(lN):
		new = []
		for j in range(lA):
			new.append(A[j][i])
		out.append(new)
	return out 	

# 25, Middle of the Linked List 
def middleNode(head):
	tmp = head
	while tmp and tmp.next:
		head = head.next
		tmp = tmp.next.next
	return head

	# set two pointers, one is head with one step each iteration 
	# the other is tmp, with two steps each iteration 
	# when tmp reach the end, head just reaches the half of it 

	if head == None:
		return head
	if head.next == None:
		return head
	p = head
	q = head
	while q.next:
		p = p.next
		q = q.next
		if q.next != None:
			q = q.next
	return p

# 26, Number of lines To Write String - 
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

# 27, Longest Uncommon Subsequence
# For strings A, B, when len(A) > len(B), the longest possible subsequence 
# of either A or B is A, and no subsequence of B can be equal to A. Answer: len(A).
# When len(A) == len(B), the only subsequence of B equal to A is B; 
# so as long as A != B, the answer remains len(A).
# When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.

def findLUSlength(A,B)
	return -1 if A==B else max(len(A),len(B))


# 28, Monotonic Array 
def isMonotonic(A):
	# cmp(), compare two variables (x,y), if x<y return -1, if x=y, return 0, if x>y return 1
	return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}

	# comapre each element from two ends
	if len(A) < 2: return True 
	l, r = 0, len(A) - 1
	J = True if A[l] < A[r] else False 
	while l < r: 
		if J == True: 
			# increading trend 
			if A[l] > A[r] or A[l] > A[l+1] or A[r-1] > A[r]:
				return False
			l += 1
			r -= 1
		elif J == False: 
			# decreasing trend 
			if A[l] < A[r] or A[l] < A[l+1] or A[r-1] < A[r]:
				return False
			l += 1
			r += 1
	return True 

	# using Flag
	if len(A) <= 2: return True
	Flag = None
	for i in range(1,len(A)):
		if A[i] != A[i-1] and Flag == None:
			Flag = (A[i] > A[i-1])
		if Flag:
			temp = (A[i] >= A[i-1])
			if temp != Flag: return False
		elif Flag != None:
			temp = (A[i] > A[i-1])
			if temp != Flag: return False
	return True

# 29, Reverse Words in a String III
def reverseWords(s):
	out = ""
	for w in s.split(' '):
		w = w[::-1]
		out = out + w + " "
	return out[:-1]

	# using join to add space 
	return " ".join([ x[::-1] for x in s.split(" ") ])

# 30, Reverse String II
def reverseStr(s,k):
	b = 0
	e = 2*k
	out = "" 
	if len(s) <= k:
		return s[::-1] 
	else:
		while e < len(s):
			new = s[b:e][:k][::-1]
			new = new + s[b:e][k:]
			out += new 
			b += 2*k
			e += 2*k
		print b
		if b+k < len(s):
			left = s[b:len(s)][:k][::-1]
			left = left + s[b:len(s)][k:]
			out += left
		else:
			out = out + s[b:len(s)][::-1]
		return out 

	s = list(s)
	for i in xrange(0, len(s), 2*k):
		s[i:i+k] = reversed(s[i:i+k])
	return "".join(s)


if __name__ == '__main__':

	# print selfDividingNumbers(1,22)
	# print numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
	# print reverseWords('ok haha')
	print reverseStr("abcdefg", 2)




