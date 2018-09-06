# 31, Reverse String
def reverseString(s):
	return s[::-1]

# 32, Reverse Vowels of a String
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

# 33, Number Complement. apply BitwiseOperators
def findComplement(num):
	i = 1
	while i <= num:
		# return i iwht the bits shifted to the left by 1 place, new bits on right are 0
		i = i << 1
		# bitwise exclusive or 
	return (i-1) ^ num 

	# string modify method 
	combin = ''
	for digit in bin(num)[2:]:
		if digit=='0':
			combin += '1'
		else:
			combin += '0'
	return int(combin, 2)

# 34, Majority Element 
def majorityElement(nums):
	return max(set(nums), key=nums.count)

# 35, Subdomain Visit Count
def subdomainVisits(cpdomains):

	sub2count = {}
	sub2count["com"] = 0
	out = []
	for sub in list(cpdomains):
		num = int(sub.split(" ")[0])						
		domain = sub.split(" ")[1]
		sub_domain = ".".join(domain.split(".")[1:])
		# one domain could be a sub_domain of another
		if domain not in sub2count:
			sub2count[domain] = 0
		sub2count[domain] += num 
		if sub_domain not in sub2count:
			sub2count[sub_domain] = 0
		sub2count[sub_domain]+=num
		# one sub_domain could has its own sub_subdomain
		if "." in sub_domain:
			subsub =  ".".join(sub_domain.split(".")[1:])
			if subsub not in sub2count:
				sub2count[subsub] = 0
			sub2count[subsub]+=num
	for [sub_domain, count] in sub2count.items():
		out.append(str(count)+' '+sub_domain)
	return out


	# here is a better way to find sub_domain
	# use rfind() recursive find "." to generate sub_domain
	# s.rfind(str, 0, len(str))
	result_dict = {}
	result = []
	for domain in cpdomains:
		count, domain = domain.split()
		count = int(count)
		index = len(domain)
		while index >= 0:
			# find the "." last index from right to left
			s_index = domain.rfind(".", 0, index)
			subdomain = domain[s_index + 1:]
			result_dict[subdomain] = result_dict.get(subdomain, 0) + count
			index = s_index - 1
        
	for k, v in result_dict.iteritems():
		result.append(str(v) + " " + k)           
	return result


	# using Counter() to count - wise
	c = collections.Counter()
	for cd in cpdomains:
		n, d = cd.split()
		c[d] += int(n)
		for i in range(len(d)):
			if d[i] == '.': c[d[i + 1:]] += int(n)
	return ["%d %s" % (c[k], k) for k in c]

# 36, Keyboard Row 
def findWords(words):
	a = set("qwertyuiop")
	b = set("asdfghjkl")
	c = set("zxcvbnm")
	out = []
	words = list(words)
	for word in words:
		w = set(word.lower())
		if a&w == w:
			out.append(word)
		if b&w == w:
			out.append(word)
		if c&w == w:
			out.append(word)
	return out 

# 37,  Groups of Special-Equivalent Strings
def numSpecialEquivGroups(A):
	B = set()
	for w in list(A):
		even = ''.join(sorted(w[0::2]))
		odd = ''.join(sorted(w[1::2]))
		B.add((even,odd))
	return len(B)

# 38, Shortest Distance to a Character
def shortestToChar(S,C):
	c_index = []
	out = [0]*len(S)
	for i,c in enumerate(S):
		if c == C:
			c_index.append(i)
	for i,c in enumerate(S):
		if c != C:
			out[i] = min(list(map(lambda x: abs(x-i),c_index)))
	return out 

# 39, Uncommon Words from Two Sentences
def uncommonFromSentences(A, B):

	words = {}
	arr = A.split(" ") + B.split(" ")
	out = []
	for i in arr:
		if i not in words:
			words[i] = 0
		words[i] += 1
	for w,i in words.items():
		if i == 1:
			out.append(w)
	return out

	# should learn how to use one line to get result 
	dic = {}
	for s in A.split():
		dic[s] = dic.get(s, 0) + 1
	for s in B.split():
		dic[s] = dic.get(s, 0) + 1
	return [w for w in dic if dic[w] == 1]

# 40, Find the Difference
def findTheDifference(s, t):
	s,t = sorted(s),sorted(t)
	if s == t[:-1]:
		return t[-1]
	else:
		for w in zip(s,t):
			if w[0] != w[1]:
				return w[1]



if __name__ == '__main__':

	#print reverseVowels("hello")
	#print findComplement(5)
	#print subdomainVisits(["900 google.mail.com", "50 mail.com"])
	#print numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
	#print shortestToChar("loveleetcode","e")
	#print uncommonFromSentences("this apple is sweet","this apple is sour")
	print findTheDifference("abcd","abecd")




