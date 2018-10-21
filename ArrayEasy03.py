
'''
23, Sort Array By Parity II
24, Intersection of Two Arrays
25, Intersection of Two Arrays II
Each element in the result should appear as many times as it shows in both arrays.
26, Two Sum II - Input array is sorted

'''

# 23, Sort Array By Parity II
def sortArrayByParityII(A):
	i,j,ans = 0,1,[None]*len(A)
	for a in A:
		if a % 2 == 0:
			ans[i] = a
			i += 2
		if a % 2 != 0:
			ans[j] = a
			j += 2
	return ans 

def sortArrayByParityII01(A):
	N = len(A)
	ans = [None] * N
	ans[::2] = (x for x in A if x % 2 == 0)
	ans[1::2] = (x for x in A if x % 2 == 1)
	return ans

# 24, Intersection of Two Arrays
def intersection(nums1, nums2):
	return [ i for i in set(nums1) if i in set(nums2)]

def intersection01(nums1, nums2):
	return list(set(nums1) & set(nums2))

def intersection02(nums1,nums2):
	hashset1 = set(nums1)
	hashset2 = set(nums2)
	res = []
	for num in nums1:
		if num in hashset1 and num in hashset2:
			res.append(num)
			hashset1.remove(num)
			hashset2.remove(num)
	return res

# 25, Intersection of Two Arrays II
def intersect(nums1,nums2):
	res = []
	for i in nums1:
		if i in nums1 and i in nums2:
			res.append(i)
			nums2.remove(i)
	return res

def intersect01(nums1,nums2):
	dic = {}
	ans = []
	for num in nums1:
		dic[num] = dic.get(num,0)+1
	for nums in nums2:
		if nums in dic and dic[nums]>0:
			ans.append(nums)
			dic[nums] -= 1
	return ans

# 26, Two Sum II - Input array is sorted
def twoSum(numbers,target): 
	# - Time Limit Exceeded
	for i,c in enumerate(numbers):
		x,rest = target-c,numbers[i+1:]
		if x in rest: return [i+1,rest.index(x)+i+2]
def twoSum01(numbers,target): 
	# two pointers
	l,r = 0, len(numbers)-1
	while l<r:
		s = numbers[l]+numbers[r]
		if s == target: return [l+1,r+1]
		elif s < target: l +=1
		elif s > target: r -=1
def twoSum02(numbers,target):
	# dictionary 
	dic = {}
	for i, num in enumerate(numbers):
		if target-num in dic:
			return[dic[target-num]+1,i+1]
		dic[num] = i 
def twoSum03(numbers,target):
	# binary search 
	for i in range(len(numbers)):
		l,r = i+1,len(numbers)-1
		tmp = target-numbers[i]
		while l<=r:
			mid = l+(r-l)//2
			if numbers[mid]==tmp:
				return [i+1,mid+1]
			elif numbers[mid]<tmp:
				l = mid+1
			else:
				r = mid-1


if __name__ == '__main__':

	# print sortArrayByParityII([4,2,5,7])
	# print intersect([1,2,2,1],[2])
	print twoSum([0,3,0,4],0)









