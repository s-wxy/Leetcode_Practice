
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


if __name__ == '__main__':


	print detectCapitalUse("hasdA")