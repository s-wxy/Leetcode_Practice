
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
	


if __name__ == '__main__':