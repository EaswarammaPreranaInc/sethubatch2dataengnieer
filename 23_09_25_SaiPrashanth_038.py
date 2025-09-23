#!/usr/bin/env python
# coding: utf-8
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: #error # Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) #address of the  object
print(type(a)) #<class '__main__.c1'>
print(a . __dict__) #{}
print(a) #type and  address
del  a #object  is  deleted
print(a)#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1()# 3rd  method
m1() # Function#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) #Two  argument  method :  10 20
#a . m1(30) #error
#a . m1() #error#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) #  Two  argument  method :  10 20
a . m1(30) #  Two  argument  method :  30 2
a . m1() #  Two  argument  method :  1 2# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1()# Method  of  third  c1  class# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1() # Create  object  of  class  c1
a . m1() #error because  class  c1  has  no  method  m1#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)   # {}
a . x = 10
print(a . _dict_) # {'x': 10}
a . y = 20
print(a . _dict_) # {'x': 10, 'y': 20}
a . x = 30
print(a . _dict_) # {'x': 30, 'y': 20}
a . y = 40
print(a . _dict_) # {'x': 30, 'y': 40}
del  a . x
print(a . _dict_) # {'y': 40}
del  a . y
print(a . _dict_)# {}
del   a
print(a . _dict_)# Error
# In[2]:


'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=float(input("enter side of a")) #How  to  read  three  sides  into  object  self
		self.b=float(input("enter side of b"))
		self.c=float(input("enter side of c"))
	def  test(self):    
		if (self.a+self.b)>self.c and (self.b+self.c)>self.a and (self.c+self.a)>self.b:
			pass
		else:
			print("invalid sides")
			exit()
	def  area(self):
			s=(self.a+self.b+self.c)/2
			area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
			return   area 
	def  peri(self):
			p=self.a+self.b+self.c
			return  p 
# End of the class
obj=triangle()#How  to  create  triangle  class  object
obj.get()#How  to  read  inputs  into  object
obj.test()#How  to  test  whether  inputs  are  valid
print('Area : ',  obj.area())#How  to  call  area  method  using  object
print('Perimeter : ',  obj.peri())#How  to  call  perimeter  method  using  object







# %%
