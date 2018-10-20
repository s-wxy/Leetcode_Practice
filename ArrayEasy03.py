
'''
23, Sort Array By Parity II
24, Intersection of Two Arrays
25, Intersection of Two Arrays II
Each element in the result should appear as many times as it shows in both arrays.


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


if __name__ == '__main__':

	print sortArrayByParityII([4,2,5,7])