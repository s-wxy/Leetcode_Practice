from collections import Counter

#41, Single Number
def singleNumber(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key
	




if __name__ == '__main__':

	print singleNumber([2,2,1])