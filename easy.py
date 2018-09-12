
# 38, Shortest Distance to a Character
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


if __name__ == '__main__':

	
	# print numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
	# print reverseWords('ok haha')
	print reverseStr("abcdefg", 2)




