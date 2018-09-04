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

# 36, 

if __name__ == '__main__':

	#print reverseVowels("hello")
	#print findComplement(5)
	print subdomainVisits(["900 google.mail.com", "50 mail.com"])


	# a = ["408 zfz.network","1789 zqy.ca","622 cwn.net","6629 vdu.bfo.team","817 htq.co","3496 ytn.com","6122 nqk.srp.org","4296 jre.us","8176 gqs.ca","7292 zbl.ksc.net","4126 lir.ajl.team","84 lmm.network","622 wmt.cwn.net","2572 qay.network","7089 ske.yls.com","2979 bhp.org","2740 xhe.org","4439 gtu.us","1110 kdd.znq.us","3314 hkt.net","5041 cdf.hwu.us","4198 okv.co","6920 tlc.dfa.us","654 yjt.co","5016 zwv.gqi.co","59671 team","5705 mqa.wsv.net","9103 vbo.org","2406 hkb.ocf.co","7292 ksc.net","8928 arz.org","8342 srp.team","2447 ksc.com","32 ulz.com","3855 yjt.network","9530 omu.network","2329 vva.qay.network","2531 ser.com","1781 lbk.ksc.co","7476 cze.yvr.net","1873 gjf.ca","3950 xuf.network","1789 xcf.zqy.ca","3055 jkx.com","81314 network","1137 qzi.co","3262 mor.ixi.us","7344 czb.com","3090 yjt.us","6890 bfo.network","3875 ato.network","68516 net","9374 jep.ato.co","9523 cgl.network","7464 jpd.fff.co","2715 okv.us","3528 arz.us","9374 ato.co","7042 btv.com","64390 org","2862 sci.net","9259 bfo.net","9172 zfz.net","3055 fdy.jkx.com","2160 hsj.epf.org","5907 zfz.us","7392 uyy.net","9897 lra.uyy.org","58413 com","2406 ocf.co","6129 hkt.com","3377 jkx.network","12367 bfo.team","59758 co","36170 ca","2160 epf.org","4602 weq.buf.team","6920 dfa.us","1879 lmm.ca","3314 ytd.hkt.net","2862 coh.sci.net","2913 ret.ych.ca","817 sgp.htq.co","9531 hoh.co","3609 bhp.team","8274 ulz.co","9846 fuw.org","1501 ara.ca","2913 ych.ca","5738 lar.bfo.team","8557 lfn.net","3449 tfm.us","654 yls.yjt.co","1781 ksc.co","3215 hoh.network","2777 mkw.co","9897 uyy.org","767 irh.epf.us","2444 gxz.team","4806 xss.dfa.co","9372 hci.jia.network","9581 gqi.team","5016 gqi.co","4975 okv.com","4296 xtb.jre.us","5705 wsv.net","9372 jia.network","8544 bhp.com","1873 kse.gjf.ca","7464 fff.co","3624 epf.network","9219 tfm.ca","1387 hju.gbq.org","4806 dfa.co","3262 ixi.us","7193 fzx.ca","2965 gxj.org","8557 uai.lfn.net","51516 us","8176 ujm.gqs.ca","4602 buf.team","4126 ajl.team","1110 znq.us","2444 vks.gxz.team","6865 thk.net","1523 suq.bhp.co","3111 gdw.team","4521 weh.bfo.us","7476 yvr.net","8167 jre.team","5041 hwu.us","4521 bfo.us","3322 xhe.team","2777 nak.mkw.co","8263 cwn.org","4681 lwf.ytn.network","654 yaw.lmm.ca","8167 ahm.jre.team","3215 bll.hoh.network","4681 ytn.network","767 epf.us","6122 srp.org","3528 jyx.arz.us","408 tdt.zfz.network","8390 zqk.network","9523 wyv.cgl.network","3624 vmv.epf.network","3090 ycc.yjt.us","8544 xrj.bhp.com","1523 bhp.co","4198 xfs.okv.co","7968 gjf.network","3875 brk.ato.network","1387 gbq.org","2471 czb.us","1627 bhp.ca","1137 ujs.qzi.co","5729 srp.com","7089 yls.com","7193 xth.fzx.ca","2715 ubt.okv.us","2531 mce.ser.com"]
	# b = ["408 zfz.network","1789 zqy.ca","622 cwn.net","6629 vdu.bfo.team","817 htq.co","3496 ytn.com","6122 nqk.srp.org","4296 jre.us","8176 gqs.ca","7292 zbl.ksc.net","4126 lir.ajl.team","84 lmm.network","622 wmt.cwn.net","2572 qay.network","7089 ske.yls.com","2979 bhp.org","2740 xhe.org","4439 gtu.us","1110 kdd.znq.us","3314 hkt.net","5041 cdf.hwu.us","4198 okv.co","6920 tlc.dfa.us","654 yjt.co","5016 zwv.gqi.co","59671 team","5705 mqa.wsv.net","9103 vbo.org","2406 hkb.ocf.co","7292 ksc.net","8928 arz.org","8342 srp.team","2447 ksc.com","32 ulz.com","3855 yjt.network","9530 omu.network","2329 vva.qay.network","2531 ser.com","1781 lbk.ksc.co","7476 cze.yvr.net","1873 gjf.ca","3950 xuf.network","1789 xcf.zqy.ca","3055 jkx.com","81314 network","1137 qzi.co","3262 mor.ixi.us","7344 czb.com","3090 yjt.us","6890 bfo.network","3875 ato.network","68516 net","9374 jep.ato.co","9523 cgl.network","7464 jpd.fff.co","2715 okv.us","3528 arz.us","9374 ato.co","7042 btv.com","64390 org","2862 sci.net","9259 bfo.net","9172 zfz.net","3055 fdy.jkx.com","2160 hsj.epf.org","5907 zfz.us","7392 uyy.net","9897 lra.uyy.org","58413 com","2406 ocf.co","6129 hkt.com","3377 jkx.network","12367 bfo.team","59758 co","36170 ca","2160 epf.org","4602 weq.buf.team","6920 dfa.us","1225 lmm.ca","3314 ytd.hkt.net","2862 coh.sci.net","2913 ret.ych.ca","817 sgp.htq.co","9531 hoh.co","3609 bhp.team","8274 ulz.co","9846 fuw.org","1501 ara.ca","2913 ych.ca","5738 lar.bfo.team","8557 lfn.net","3449 tfm.us","654 yls.yjt.co","1781 ksc.co","3215 hoh.network","2777 mkw.co","9897 uyy.org","767 irh.epf.us","2444 gxz.team","4806 xss.dfa.co","9372 hci.jia.network","9581 gqi.team","5016 gqi.co","4975 okv.com","4296 xtb.jre.us","5705 wsv.net","9372 jia.network","8544 bhp.com","1873 kse.gjf.ca","7464 fff.co","3624 epf.network","9219 tfm.ca","1387 hju.gbq.org","4806 dfa.co","3262 ixi.us","7193 fzx.ca","2965 gxj.org","8557 uai.lfn.net","51516 us","8176 ujm.gqs.ca","4602 buf.team","4126 ajl.team","1110 znq.us","2444 vks.gxz.team","6865 thk.net","1523 suq.bhp.co","3111 gdw.team","4521 weh.bfo.us","7476 yvr.net","8167 jre.team","5041 hwu.us","4521 bfo.us","3322 xhe.team","2777 nak.mkw.co","8263 cwn.org","4681 lwf.ytn.network","654 yaw.lmm.ca","8167 ahm.jre.team","3215 bll.hoh.network","4681 ytn.network","767 epf.us","6122 srp.org","3528 jyx.arz.us","408 tdt.zfz.network","8390 zqk.network","9523 wyv.cgl.network","3624 vmv.epf.network","3090 ycc.yjt.us","8544 xrj.bhp.com","1523 bhp.co","4198 xfs.okv.co","7968 gjf.network","3875 brk.ato.network","1387 gbq.org","2471 czb.us","1627 bhp.ca","1137 ujs.qzi.co","5729 srp.com","7089 yls.com","7193 xth.fzx.ca","2715 ubt.okv.us","2531 mce.ser.com"]
	# c = ["2777 nak.mkw.co","654 yaw.lmm.ca","3528 jyx.arz.us","3215 bll.hoh.network","408 tdt.zfz.network","3322 xhe.team","8342 srp.team","9259 bfo.net","3875 brk.ato.network","2531 mce.ser.com","2471 czb.us","4806 xss.dfa.co","654 yls.yjt.co","767 irh.epf.us","1501 ara.ca","243 qay.network","9103 vbo.org","6890 bfo.network","4296 xtb.jre.us","2329 vva.qay.network","9846 fuw.org","4681 lwf.ytn.network","1781 lbk.ksc.co","7464 jpd.fff.co","2740 xhe.org","4602 weq.buf.team","3055 fdy.jkx.com","5705 mqa.wsv.net","6629 vdu.bfo.team","9897 lra.uyy.org","8167 ahm.jre.team","9374 jep.ato.co","3624 vmv.epf.network","6865 thk.net","6920 tlc.dfa.us","9372 hci.jia.network","7968 gjf.network","7292 zbl.ksc.net","2862 coh.sci.net","3855 yjt.network","1387 hju.gbq.org","817 sgp.htq.co","2406 hkb.ocf.co","622 wmt.cwn.net","9172 zfz.net","1523 suq.bhp.co","9581 gqi.team","2160 hsj.epf.org","32 ulz.com","1225 lmm.ca","1137 ujs.qzi.co","5041 cdf.hwu.us","4126 lir.ajl.team","3111 gdw.team","8928 arz.org","9531 hoh.co","7344 czb.com","2715 ubt.okv.us","1110 kdd.znq.us","5729 srp.com","6122 nqk.srp.org","7193 xth.fzx.ca","3496 ytn.com","3950 xuf.network","4521 weh.bfo.us","3262 mor.ixi.us","4975 okv.com","7089 ske.yls.com","4198 xfs.okv.co","2444 vks.gxz.team","1789 xcf.zqy.ca","7392 uyy.net","3449 tfm.us","5907 zfz.us","9530 omu.network","3314 ytd.hkt.net","9523 wyv.cgl.network","4439 gtu.us","8390 zqk.network","1627 bhp.ca","3609 bhp.team","8557 uai.lfn.net","2913 ret.ych.ca","2447 ksc.com","7476 cze.yvr.net","8544 xrj.bhp.com","6129 hkt.com","8274 ulz.co","9219 tfm.ca","5016 zwv.gqi.co","5738 lar.bfo.team","3377 jkx.network","2979 bhp.org","8176 ujm.gqs.ca","84 lmm.network","3090 ycc.yjt.us","7042 btv.com","2965 gxj.org","8263 cwn.org","1873 kse.gjf.ca"]

	# for i in range(len(c)):

	# 	if "lmm.ca" in c[i]:
	# 		print c[i]





