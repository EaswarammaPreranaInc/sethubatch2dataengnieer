# Identify  error 
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # error : no method or pass in class



# Find  outputs  
class   c1:
	pass
# End  of  the  class
a = c1() # create c1 class object
print(id(a)) # Address of c1
print(type(a)) # <class '__main__.c1'>
print(a . __dict__) # {} : converts to object to dictionary
print(a) # type and address of c1
del  a # deletes class c1
#print(a) # error : name 'a' is not defined



#  Find  outputs 
def   m1():
		print('Function')
class   c1:
	def   m1(self): # discarded
		print('1st  method')
	def   m1(self): # discarded
		print('2nd  method')
	def   m1(self): # recognised
		print('3rd  method')
# End  of  class  c1
a = c1()
a . m1() # calling method m1
m1() # calling function m1 
'''
o/p:
3rd method
Function
'''



#  Find  outputs  
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # Two argument method : 10 20
#a . m1(30) 
#a . m1()



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
a . m1(10 , 20) # Two argument method : 10 20
a . m1(30) # Two argument method : 30 2
a . m1() # Two argument method : 1 2



# Find  outputs  
class   c1: # discarded
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1: # discarded
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1: # recognised
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1()
a . m1() # Method of third c1 class



# Find  outputs 
class   c1: # Discarded
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1: # discarded
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1: # recognised
	pass
a = c1()
#a . m1() # no method m1



#  Find  outputs
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  # {}
a . x = 10
print(a . __dict__) # {'x':10}
a . y = 20
print(a . __dict__) # {'x':10, 'y':20}
a . x = 30
print(a . __dict__) # {'x':30, 'y':20}
a . y = 40
print(a . __dict__) # {'x':30, 'y':40}
del  a . x
print(a . __dict__) # {'y':40}
del  a . y
print(a . __dict__) # {}
del   a
#print(a . __dict__) # error: 'a' is not defined



''' 
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=float(input('Enter side a: '))
		self.b=float(input('Enter side b: '))
		self.c=float(input('Enter side c: ')) # How  to  read  three  sides  into  object  self
	def  test(self):
		if (self.a+self.b>self.c) and (self.b+self.c>self.a) and (self.c+self.a>self.b):# sum  of  every  2  sides  >=  3rd  side:
			return True
		else:
			print('Not  a  triangle')
			return False
			# stop  execution
	def  area(self):
			s=(self.a+self.b+self.c)/2
			return   math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)) # area  of  triangle
	def  peri(self):
			return  self.a+self.b+self.c # perimeter  of  triangle
# End of the class
t=triangle()  #   create  triangle  class  object
t.get() #  read  inputs  into  object
if t.test(): # How  to  test  whether  inputs  are  valid
	print('Area : ',t.area())
	print('Perimeter : ',t.peri())
	