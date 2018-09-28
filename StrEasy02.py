
'''
16, Detect Capital
17, Count Binary Substrings
18, Rotated Digits
19, Ransom Note
20, First Unique Character in a String
21, Student Attendance Record I
22, Most Common Word
23, Baseball Game 

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

# 18, Rotated Digits
def rotatedDigits(N):
	count = 0
	for i in range(1,N+1):		
		if '3' in str(i) or '7' in str(i) or '4' in str(i):
			continue
		if '2' in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i):
			count += 1
	return count 

# 19, Ransom Note
def canConstrcut(ransomNote, magazine):
	if not ransomNote: return True
	note = {}
	for i in range(len(ransomNote)):
		w = ransomNote[i]
		if w not in note:
			note[w]=0
		note[w]+=1
		i+=1
	Flag = True
	for key in note:
		if key not in magazine:
			Flag = False
		if note[key] > magazine.count(key):
			Flag = False
	return Flag

def canConstrcut01(ransomNote, magazine):
	for i in set(ransomNote):
	    if ransomNote.count(i) > magazine.count(i):
	        return False
	return True

# 20, First Unique Character in a String
def firstUniqChar(s):
	i = 0
	while i < len(s):
		if s.count(s[i]) == 1:
			return i 
			break
		else:
			i+=1
	if i == len(s): return -1

def firstUniqChar01(s):
	for i in range(len(s)):
		c = s[i]
		if s.count(c) == 1:
			return i 
	return -1 

def firstUniqChar02(s):
	from collections import Counter
	sc = Counter(s)
	for i in range(len(s)):
		c = s[i]
		if sc.get(c,0) == 1:
			return i 
	return -1

def firstUniqChar03(s):
	d = {}
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	for i in range(len(s)):
		c = s[i]
		if d[c] == 1:
			return i
	return -1 

# 21, Student Attendance Record I
def checkRecord(s):     
	if s.count('A') <= 1 and 'LLL' not in s:
		return True
	else:
		return False
def checkRecord01(s):
	return s.count('A')<2 and 'LLL' not in s

# 22, Most Common Word
def mostCommonWord(paragraph, banned):
	p = paragraph.lower().split(' ')
	d = {}
	for c in p:
		if not c.isalpha():
			c = c[:-1]
		if c not in banned:
			if c in d:
				d[c] += 1
			else: 
				d[c] = 1
	return sorted(d.items(),key=lambda x:-x[1])[0][0]

# 23, Baseball Game 
def calPoints(ops):
	history = []
	ops = ["0","0"] + ops
	for op in ops:
		if op == 'C':
			history.pop()
		elif op == 'D':
			history.append(int(history[-1])*2)
		elif op == '+':
			history.append(int(history[-1])+int(history[-2]))
		else:
			history.append(int(op))
	return sum(history)



if __name__ == '__main__':


	# print detectCapitalUse("hasdA")
	# print countBinarySubstrings("00110011")
	# print rotatedDigits(857)
	# print canConstrcut("","")
	# print firstUniqChar("eee")
	# print checkRecord('PPALLL')
	# mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"])
	print calPoints(["5","2","C","D","+"])

