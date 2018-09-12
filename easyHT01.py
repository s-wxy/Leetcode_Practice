
'''
1, Jeswels and Stones
2, Subdomain Visit Count
3, Keyboard Row 
4, Uncommon Words from Two Sentences
5, Distribute Candies

'''

# 1, Jeswels and Stones
# map() function - applying the given function to each item of a given iterable
def numJewelsInStones(J, S):
	return sum(map(J.count, S))
	# return len([c for c in S if c in J])

# 2, Subdomain Visit Count
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

def subdomainVisits01(cpdomains):
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

def subdomainVisits02(cpdomains):
	# using Counter() to count - wise
	c = collections.Counter()
	for cd in cpdomains:
		n, d = cd.split()
		c[d] += int(n)
		for i in range(len(d)):
			if d[i] == '.': c[d[i + 1:]] += int(n)
	return ["%d %s" % (c[k], k) for k in c]

# 3, Keyboard Row 
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

# 4, Uncommon Words from Two Sentences
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

def uncommonFromSentences01(A, B):
	# should learn how to use one line to get result 
	dic = {}
	for s in A.split():
		dic[s] = dic.get(s, 0) + 1
	for s in B.split():
		dic[s] = dic.get(s, 0) + 1
	return [w for w in dic if dic[w] == 1]

# 5, Distribute Candies
def distributeCandies(candies):
	return min(len(candies)/2, len(set(candies)))




if __name__ == '__main__':

	# print numJewelsInStones("aA","aaaaAAC")
	# print subdomainVisits(["900 google.mail.com", "50 mail.com"])



