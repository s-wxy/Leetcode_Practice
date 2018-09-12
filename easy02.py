



# 13 Roman to Integer
def romanToInt(s):
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(0, len(s) - 1):
		if roman[s[i]] < roman[s[i+1]]:
			z -= roman[s[i]]
		else:
			z += roman[s[i]]
	return z + roman[s[-1]]

# 14 Jeswels and Stones
# map() function - applying the given function to each item of a given iterable
def numJewelsInStones(J, S):
	return sum(map(J.count, S))
	# return len([c for c in S if c in J])

# 15 To Lower Case
def toLowerCase(str):
	return str.lower()

# 16 Hamming Distance, when x and y have same distance 
def hammingDistance_s(x, y):
	diff  = 0 
	for chx, chy in zip (bin(x),bin(y)):
		if chx != chy:
			diff += 1
	return diff

def hammingDistance(x, y):
	return bin(x^y).count('1')

# x ^ y (bitwise operator, https://wiki.python.org/moin/BitwiseOperators)	
#Does a "bitwise exclusive or". 
#Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, 
#and it's the complement of the bit in x if that bit in y is 1

# 17 Unique Morse Code Words
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



# 19 Judge Route Circle
def judgeCircle(moves):
	if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
		return True
	else:
		return False

# 20 Add Digits 
def addDigits(num):
	while num >= 10:
		temp = 0
		while num >0:
			temp += num%10
			num /= 10
		num = temp 
	return num 


if __name__ == '__main__':

	
	# romanToInt("III")
	# print numJewelsInStones("aA","aaaaAAC")
	# print hammingDistance(1,4)
	# print uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
	# print flipAndInvertImage_l([[1,1,0],[1,0,1],[0,0,0]])
	# print judgeCircle("U")

