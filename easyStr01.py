
'''
1, Implement strStr()
2, To Lower Case
3, Unique Morse Code Words
4, Reverse String
5, Reverse String II
6, Reverse Words in a String III
7, Groups of Special-Equivalent Strings
8, Longest Uncommon Subsequence
9, Reverse Vowels of a String
10, Count and Say
11, Valid Parentheses
12, Length of the Last Word
13, Longest Common Prefix
14, Robot Return to Origin

'''

# 1, Implement strStr()
def strStr(haystack, needle):
	if needle in haystack:
		return haystack.find(needle)
	else:
		return -1

# 2, To Lower Case
def toLowerCase(str):
	return str.lower()

# 3, Unique Morse Code Words
def uniqueMorseRepresentations(words):
	dict = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..", \
	"j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...", \
	"t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
	mors = set()
	for w in words:
		mor = ""
		for l in w:
			mor += dict[l]
		mors.add(mor)
	return len(mors)

# 4, Reverse String
def reverseString(s):
	return s[::-1]

# 5, Reverse String II
def reverseStr(s,k):
	b = 0
	e = 2*k
	out = "" 
	if len(s) <= k:
		return s[::-1] 
	else:
		while e < len(s):
			new = s[b:e][:k][::-1]
			new = new + s[b:e][k:]
			out += new 
			b += 2*k
			e += 2*k
		print b
		if b+k < len(s):
			left = s[b:len(s)][:k][::-1]
			left = left + s[b:len(s)][k:]
			out += left
		else:
			out = out + s[b:len(s)][::-1]
		return out 

	s = list(s)
	for i in xrange(0, len(s), 2*k):
		s[i:i+k] = reversed(s[i:i+k])
	return "".join(s)

# 6, Reverse Words in a String III
def reverseWords(s):
	out = ""
	for w in s.split(' '):
		w = w[::-1]
		out = out + w + " "
	return out[:-1]

def reverseWords01(s):
	# using join to add space 
	return " ".join([ x[::-1] for x in s.split(" ") ])

# 7, Groups of Special-Equivalent Strings
def numSpecialEquivGroups(A):
	B = set()
	for w in list(A):
		even = ''.join(sorted(w[0::2]))
		odd = ''.join(sorted(w[1::2]))
		B.add((even,odd))
	return len(B)

# 8, Longest Uncommon Subsequence
# For strings A, B, when len(A) > len(B), the longest possible subsequence 
# of either A or B is A, and no subsequence of B can be equal to A. Answer: len(A).
# When len(A) == len(B), the only subsequence of B equal to A is B; 
# so as long as A != B, the answer remains len(A).
# When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.

def findLUSlength(A,B)
	return -1 if A==B else max(len(A),len(B))

# 9, Reverse Vowels of a String
def reverseVowels(s):
	vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	s = list(s)
	l = 0
	r = len(s)-1
	while l < r:
		# using while loop to find vowels 
		# time complexity is O(n), since only go through the string once 
		while l < r and s[l] not in vowels:
			l += 1
		while r > l and s[r] not in vowels:
			r -= 1
		s[l], s[r] = s[r], s[l]
		l += 1
		r -= 1
	return ''.join(s)

# 10, Count and Say
def countAndSay(n):
	if n == 1:
		return "1"
	else:
		s = self.countAndSay(n - 1)
        if len(s) > 0:
            current = s[0]
            count = 0
            r = ""
            for i in range(len(s)):
                if s[i] == current:
                    count += 1
                else:
                    r = r + str(count) + current
                    current = s[i]
                    count = 1
            r = r + str(count) + current 
            return r 

# 11, Valid Parentheses
def isValid(s):
	stack = []
	dict = {"]":"[", "}":"{", ")":"("}
	for char in s:
		if char in dict.values():
			stack.append(char)
		elif char in dict.keys():
			if stack == [] or dict[char] != stack.pop():
				return False
		else:
			return False
	if stack == []:
		return True
	else:
		return False

# 12, Length of the Last Word
def lengthOfLastWord(s):
	arr = s.strip(' ').split(' ')
	lword = arr[-1]
	return len(lword)

# 13, Longest Common Prefix
def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	else:
		s1 = min(strs)
		s2 = max(strs)
		for i, c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]
		return s1

# 14, Robot Return to Origin
def judgeCircle(moves):
	if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
		return True
	else:
		return False


if __name__ == '__main__':

	# print strStr("hello", "ll")
	# print uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
	# print reverseWords("asdasa")
	# print reverseStr("asdf",2)
	# print numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
	# print reverseVowels("hello")
	# print isValid("((")
	# print lengthOfLastWord('a ')
	# print judgeCircle("U")





