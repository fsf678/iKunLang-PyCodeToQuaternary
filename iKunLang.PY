"""
        		  iKunLang
        	    爱坤语言哈哈哈
        	   iKun指定编程语言
        	   (直接基于4进制哈)
        	  By Flysmallfish

	备注：词穷了哈哈，一些变量名用的中文🤣我就是小黑子！！😁
简单修改一下就能把 鸡你太美 变成其他的。

作者Bilibili :   https://space.bilibili.com/1292466375 (嘿嘿投个币吧！)
作者 Q Q  号 :   2040244628 (请勿打扰，拜托😉)
开源    地址 :	 https://github.com/Flysmallfish/iKunLang-PyCodeToQuaternary
"""
import sys

class pytomycode():
	def ascii(t):
		new = []
		for i in t:
			new.append(ord(i))
		return new

	def f(n,x):
		a=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
		b=[]
		while True:
			s=n//x
			y=n%x
			b=b+[y]
			if s==0:break
			n=s

		ret = ''
		for i in b[::-1]:
			ret = ret+str(a[i])
		return ret

	def nbf(asc,x):
		for i in asc:
			asc[asc.index(i)] = int ( pytomycode.f(i,x) )
		return asc

	def re(s):
		n=[]

		for i in s:
			n.append(str(s[ s.index(i) ]) .replace("0","鸡") .replace("1","你") .replace("2","太") .replace("3","美"))

		return n

class mycodetopy():
	def char(t):
		new = []
		for i in t:
			new.append(chr(i))
		return new

	def ftoten(num,n):

		baseStr = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
              "a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19}
		new_num = 0
		nNum = len(num) - 1
		for i in num:
			new_num = new_num  + baseStr[i]*pow(n,nNum)
			nNum = nNum -1
		
		return new_num

	def re(s):
		n=[]

		for i in s:
			n.append(int(str(s[ s.index(i) ]) .replace("鸡","0") .replace("你","1") .replace("太","2") .replace("美","3"),4))

		return n

	def ascii(t):
		new = []
		for i in t:
			new.append(chr(i))
		return new


def compile(原Py):
	#Py编译mylang

	原Py转ascii = pytomycode.ascii (原Py)

	原PyAscii4进制 = pytomycode.nbf (原Py转ascii,4)


	nb = pytomycode.re(原PyAscii4进制)
	转换 = ''
	for i in nb:
		转换 = 转换+i+" "

	return 转换


#mylang编译Py
def explain(mylangcode):

	ls = mylangcode.split()

	asc = mycodetopy.re(ls)

	代码 = mycodetopy.ascii(asc)

	代码 = "".join(代码)

	if 代码 != '':
		print("[Log] 运行代码 (Cpython) - "+代码+"\n")

	exec(代码)

if __name__ == "__main__":

	print('Python 解释器 - '+sys.version+' on PC\nFish   解释器 - 1.0.0 (tags/v1.0.0, June 23 2022, 14:34:06) Type "compile" to get pythonCmdS MyCmd')

	try:
		f=open(sys.argv[1],'r',encoding='utf-8',errors='ignore')
		print("\n\n[Log] 已开始运行文件: "+sys.argv[1]+"  !\n")

		try:
			explain(f.read())
		except Exception as error:
			print(error)	
		f.close()

	except:
		pass

	import pyperclip

	while True:
		i = input(">>> ")
		if i == "compile":
			pc=input("Cin the PyCode>>> ")
			print(pc+"'s mylangcode is "+compile(pc)+"\n(Auto copy | 自动复制哦！)")
			pyperclip.copy(compile(pc))
		else:
			try:
				explain(i)
			except Exception as error:
				print(error)

	import os
	os.system("pause")	