'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''
class Number:
	def __init__(self,value):
		self.value=value
	def ___add__(self,other):
		return Number(self.value + other.value)
	def __str__(self):
		return String(self.value)
class String:
	def __init__(self,text):
		self.text=text
	def __add__(self,other):
		return String(self.text+other.text)
	def __str__(self):
		return self.text

from program7b import Number, String

x=input('enter first input: ')
y=input('enter second input: ')

if x.isdigit() and y.isdigit():
	n1=Number(int(x))
	n2=Number(int(y))
	result = n1 + n2
else:
	s1= String(x)
	s2= String(y)
	result= s1 + s2
	print('joined string: ',result)


