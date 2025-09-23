
#====================================== # Identify  error  (Home work)

class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
#There is no pass or method inside c3 class
#====================================== # Find  outputs  (Home  work)

class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))   #some id
print(type(a))  #<class '__main__.c'1>
print(a . __dict__)  #{}
print(a)  # genrator
del  a
print(a)  #ntg to print becoz a is deleted

#====================================== #  Find  outputs  (Home  work)

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
a . m1()   #3rd method
m1()  #Function

#====================================== #  Find  outputs  (Home  work)

class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)   #Two argu method: 10 ,20
a . m1(30) #  becoz of 'y' is missing and method is same so error is raised
a . m1()   #Error becoz of no argu

#====================================== #  Find  outputs  (Home  work)

class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)   #Two argu methodd+: 10 ,20
a . m1(30)   #Two argu methodd+: 30 ,2
a . m1()#Two argu methodd+: 1 ,2

#====================================== # Find  outputs  (Home  work)

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
a . m1() #method os third c1 class

#====================================== # Find  outputs  (Home  work)

class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()  #Error becoz of no method in 3rd c1()

#====================================== #  Find  outputs (Home  work)

class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)   #{}
a . x = 10
print(a . __dict__)   #{x:10}
a . y = 20
print(a . __dict__)   #{x:10,y:20}
a . x = 30
print(a . __dict__)   #{x:30,y:20}
a . y = 40
print(a . __dict__)   #{x:30,y:40}
del  a . x
print(a . __dict__)   #{y:40}
del  a . y
print(a . __dict__)   #{}
del   a
print(a . __dict__)   #Error there ntg to del

#====================================== '''  (Home  work)
'''
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''

import  math
class  triangle:
	def  get(self,a,b,c):
		self.a=a
		self.b=b
		self.c=c# How  to  read  three  sides  into  object  self
	def  test(self):
		if  (a+b>c and b+c>a and a+c>b):#sum  of  every  2  sides  >=  3rd  side:
			return True# Do  nothing
		else:
			print('Not  a  triangle')
			exit()
				# How  to  stop  execution
	def  area(self):
		s=(a+b+c)/2
		return   math.sqrt(s*(s-a)*(s-b)*(s-c))
	def  peri(self):
		return  a+b+c#perimeter  of  triangle
# End of the class
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
obj=triangle()
obj.get(a,b,c)
obj.test()
print('Area : ', obj.area())
print('Perimeter : ',  obj.peri())
# How  to  create  triangle  class  object
# How  to  read  inputs  into  object
# How  to  test  whether  inputs  are  valid

