
'''
23, Sort Array By Parity II

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

if __name__ == '__main__':

	print sortArrayByParityII([4,2,5,7])