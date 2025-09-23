# Identify  error  (Home work)

class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3:

'''
Error class c3 is should have atleast 1 method or pass so both are not present it throws error
'''

# Find  outputs  (Home  work)

class c1:
    pass
# End of the class
a = c1()
print(id(a))          # Print address of a
print(type(a))        # Prints <class '__main__.c1'>
print(a . _dict_)     # 'c1' object doesn't have '_dict_'
print(a)              # prints type and address
del a                 # removes a
print(a)              # 'a' is removed


#  Find  outputs  (Home  work)

def   m1():
		print('Function')
class   c1:
	def   m1(self):                      # Ignored, there is a another method m1 is declared
		print('1st  method')
	def   m1(self):                      # Ignored, there is a another method m1 is declared
		print('2nd  method')
	def   m1(self):
		print('3rd  method')
# End  of  class  c1
a = c1()
a.m1()
m1()

'''
Outputs:

3rd  method
Function
'''


#  Find  outputs  (Home  work)

class   c1:
	def   m1(self):                                     # Ignored, there is a another method m1 is declared
		print('No  argument  method')               
	def   m1(self , x):                                 # Ignored, there is a another method m1 is declared
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a .m1(30)           # c1.m1() missing 1 required positional argument 'y'
a.m1()              # c1.m1() missing 2 required positional arguments 'x' and 'y'


'''
Outputs:

Two  argument  method :  10 20
'''


#  Find  outputs  (Home  work)

class   c1:
	def   m1(self):
		print('No  argument  method')                   # Ignored, there is a another method m1 is declared
	def   m1(self , x):
		print('Single  argument  method : ' , x)        # Ignored, there is a another method m1 is declared
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a .m1(30)
a.m1()

'''
Outputs:

Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2
'''


# Find  outputs  (Home  work)

class   c1:                                         # Ignored, there is a another class C1 is declared
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:                                         # Ignored, there is a another class C1 is declared
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a=c1()
a.m1()

'''
Outputs:

Method  of  third  c1  class
'''


# Find  outputs  (Home  work)

class   c1:                                         # Ignored, there is a another class C1 is declared
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:                                         # Ignored, there is a another class C1 is declared
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a=c1()
a.m1()    # Error, because m1 doesn't exist in the class c1.


#  Find  outputs (Home  work)

class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)       # {}
a . x = 10
print(a . _dict_)       # {'x': 10}
a . y = 20
print(a . _dict_)       # {'x': 10, 'y': 20}
a . x = 30
print(a . _dict_)       # {'x': 30, 'y': 20}
a . y = 40
print(a . _dict_)       # {'x': 30, 'y': 40}
del  a . x
print(a . _dict_)       # {'y': 40}
del  a . y
print(a . _dict_)       # {}
del   a
print(a._dict_)         # Object a is deleted it throws error


'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import  math
class  triangle:
	def  get(self):
		How  to  read  three  sides  into  object  self
	def  test(self):
		if  sum  of  every  2  sides  >=  3rd  side:
				Do  nothing
		 else:
				print('Not  a  triangle')
				How  to  stop  execution
	def  area(self):
			return   area  of  triangle
	def  peri(self):
			return  perimeter  of  triangle
# End of the class
How  to  create  triangle  class  object
How  to  read  inputs  into  object
How  to  test  whether  inputs  are  valid
print('Area : ',   ???)
print('Perimeter : ', ???)
'''

import math

class Triangle:
    # Method to read sides into the object
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    # Method to test if sides form a valid triangle
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # Valid triangle
        else:
            print("Not a triangle")
            exit()  # Stop execution

    # Method to calculate area using Heron's formula
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    # Method to calculate perimeter
    def peri(self):
        return self.a + self.b + self.c

# How  to  create  triangle  class  object
t = Triangle()

# How  to  read  inputs  into  object
t.get()

# How  to  test  whether  inputs  are  valid
t.test()

# Print area and perimeter
print("Area:", t.area())
print("Perimeter:", t.peri())
