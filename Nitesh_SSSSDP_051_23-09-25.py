# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
    # error: class 3 does not have any method or pass statement
	
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) #address of object a
print(type(a)) #<class '__main__.c1'>
print(a . __dict__) #{}
print(a)# <class '__main__.c1'> address
del  a 
print(a)#error, there is no object 'a'

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
a . m1() #1st method
m1()#error there is not function m1 in the cuurent module

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
a . m1(10 , 20) #Two argument method 10 20
a . m1(30) #error you need to pass one more argument
a . m1() #error you need to pass two arguments

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
a . m1(10 , 20) #Two argument method 10 20 
a . m1(30) #two argument method 30 2
a . m1() #two argument method 1 2

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
a . m1() #Method  of  third  c1  class

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
a . m1() #error there is no method m1 in the class c1

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  #{}
a . x = 10
print(a . __dict__)#{x:10}
a . y = 20
print(a . __dict__)#{x:10,y:20}
a . x = 30
print(a . __dict__)#{x:30,y:20}
a . y = 40
print(a . __dict__)#{x:30,y:40}
del  a . x
print(a . __dict__)#{y:40}
del  a . y
print(a . __dict__)#{}
del   a
print(a . __dict__)#error there is no object a

'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		# How  to  read  three  sides  into  object  self
		self.x=int(input("Enter 1st side: "))
		self.y=int(input("Enter 2nd side: "))
		self.z=int(input("Enter 3rd side: "))
		
	def  test(self):
		if self.x+self.y>=self.z and self.y+self.z>=self.x and self.z+self.x>=self.y:
			pass
		else:
			print("Not a triangle")
			exit()
		# if  sum  of  every  2  sides  >=  3rd  side:
		# 		Do  nothing
		#  else:
		# 		print('Not  a  triangle')
		# 		How  to  stop  execution
	def  area(self):
			s=(self.x+self.y+self.z)/2
			area=math.sqrt(s*(s-self.x)*(s-self.y)*(s-self.z))
			return   area
	def  peri(self):
			return  self.x+self.y+self.z
# End of the class
tri=triangle()#How  to  create  triangle  class  object
tri.get()#How  to  read  inputs  into  object
tri.test()#How  to  test  whether  inputs  are  valid
print('Area : ',   tri.area())
print('Perimeter : ',  tri.peri())