# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: # Error as class should not be empty


  # Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # address of the c1 class object
print(type(a)) # <class , __main__.c1>
print(a . __dict__) # {}
print(a) # type and address of the object
del a 
print(a) # error as object a is deleted

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
a.m1() # 3rd method
m1() # Function


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
a . m1(10 , 20) # Two argument method : 10 <space> 20
#a . m1(30) # Error as two arguments are required
#a . m1() # Error as two arguments are required


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
a . m1(10 , 20) # Two argument method : 10 <space> 20
a .m1(30) # Two argument method : 30 <space> 2 
a.m1() # Two argument method : 1 <space> 2


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
#a = c1()
#a . m1() # Method of third c1 class



# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
#a = c1()
#a . m1() # error as c1 class has no m1 method



#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__) # {}
a . x = 10
print(a . __dict__) # {x : 10}
a . y = 20
print(a . __dict__) # {x : 10 , y : 20}
a . x = 30
print(a . __dict__) # {x : 30 , y : 20}
a . y = 40
print(a . __dict__) # {x : 30 , y : 40}
del  a . x
print(a . __dict__) # {y : 40}
del  a . y
print(a . __dict__) # {}
del   a
print(a . __dict__) # Error as the dict is deleted


'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''

import  math
class  triangle:
	def  get(self):
		pass
	def  test(self):
		if   (self.a + self.b) >= self.c and (x.a + x.c) >= x.b and (x.b + x.c) >= x.a:
				return True
		else:
				print('Not  a  triangle')
				return False
	def  area(self):
			return   math.sqrt(s * (s - x.a) * (s - x.b) * (s - x.c))

	def  peri(self):
			return  x.a + x.b + x.c
# End of the class
x = triangle() # How  to  create  triangle  class  object
x.a = 2 
x.b = 3
x.c = 4 # How  to  read  inputs  into  object
s = (x.a + x.b + x.c)/2 # How  to  test  whether  inputs  are  valid
print('Area : ',  x.area())
print('Perimeter : ',x.peri())