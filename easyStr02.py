
'''
16, Detect Capital
17, Count Binary Substrings

'''

# 16, Detect Capital
def detectCapitalUse(word):
	if word.isupper() or word.islower():
		return True
	elif word[0].isupper and word[1:].islower():
		return True
	else:
		return False

# 17, Count Binary Substrings
# The answer can be simply to sum the min of length of neighboring chunks together.
# '00001111' => [4, 4] => min(4, 4) => 4
# '00110' => [2, 2, 1] => min(2, 2) + min(2, 1) => 3
# '10101' => [1, 1, 1, 1, 1] => 4
def countBinarySubstrings(s):
	res, subCount, out = [],1,0
	for i in range(1,len(s)):
		if s[i] == s[i-1]:
			subStr += 1
		else:
			res.append(subCount)
			subCount = 1
	res.append(subCount)
	for i in range(1,len(res)):
		out += min(res[i],res[i-1])
	return out

def countBinarySubstrings01(s):
	# better soluntion with lower time complexity **
	if len(s) == 1:
		return 0
	ct,sec1,sec2,_d = -1,0,0,None
	for d in s:
		if _d == d:
			sec1 += 1
			if sec2 >= sec1:
				ct += 1
		else:
			sec2 = sec1
			sec1 = 1
			ct += 1
			_d = d
	return ct 




if __name__ == '__main__':


	# print detectCapitalUse("hasdA")
	# print countBinarySubstrings("00110011")


