
def twoSum(nums, target):
        s = []      
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] == target - nums[i]:
                    s.append(i)
                    s.append(j)
                    return s

if __name__ == '__main__':

	print twoSum([2, 7, 11, 15], 9)
	