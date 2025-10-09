# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#error because it has no statments or methods or pass
	
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#2774646347088
print(type(a))#<class '_main_.c1'>
print(a . __dict__)#<_main_.c1 object at 0x00000201831F4DD0>
print(a)#{}
del  a#deletes the object a
# print(a)#a is not defined

#  Find  outputs  (Home  work)
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
a . m1()
m1()
'''
3rd  method
Function
'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)#c1.m1() missing 1 required positional argument: 'y'
a . m1()##c1.m1() missing 2 required positional arguments: 'x' and 'y'
'''
Two  argument  
method : 10  20

'''

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a . m1(30)
a . m1()
'''
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2
'''
# Find  outputs  (Home  work)
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
a . m1()#method of third c1 class

# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()#'c1' object has no attribute 'm1'

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  
a . x = 10
print(a . __dict__)
a . y = 20
print(a . __dict__)
a . x = 30
print(a . __dict__)
a . y = 40
print(a . __dict__)
del  a . x
print(a . __dict__)
del  a . y
print(a . __dict__)
del   a
print(a . __dict__)#name 'a' is not defined
'''
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}
'''

'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
'''
import  math
class  triangle:
	def  get(self):
		How  to  read  three  sides  into  object  self
	def  test(self):
# # 		if  sum  of  every  2  sides  >=  3rd  side:
# # 				Do  nothing
# # 		 else:
# # 				print('Not  a  triangle')
# # 				How  to  stop  execution
# # 	def  area(self):
# # 			return   area  of  triangle
# # 	def  peri(self):
# # 			return  perimeter  of  triangle
# # # End of the class
# # How  to  create  triangle  class  object
# # How  to  read  inputs  into  object
# # How  to  test  whether  inputs  are  valid
# # print('Area : ',   ???)
# # print('Perimeter : ',  ???)
	  
# '''  (Home  work)
# Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

# 1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

# 2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

# 3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  self
		self.a=float(input("Enter side a:"))
		self.b=float(input("Enter side b:"))
		self.c=float(input("Enter side c:"))
	def  test(self):
		if (self.a + self.b >= self.c) and (self.b + self.c >= self.a) and (self.a + self.c>= self.a):
				return True
		else:
				print('Not  a  triangle')
				exit()# How  to  stop  execution
	def  area(self):
			s = (self.a + self.b +self.c)/2
			return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def  peri(self):
			
			return (self.a +self. b + self.c) / 2
# End of the class
t=triangle()# How  to  create  triangle  class  object
t.get()# How  to  read  inputs  into  object
t.test()# How  to  test  whether  inputs  are  valid
print('Area : ',  t.area() )
print('Perimeter : ',  t.peri())
'''
Enter side a:3
Enter side b:4
Enter side c:5
Area :  6.0
Perimeter : 6.0
'''
