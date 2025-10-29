
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: # Error A class should not be empty it should contain atleast one statement like (pass)

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))    # Address of the class object
print(type(a))  # <class '__main__.c1>'
print(a . _dict_)   # {}
print(a)    # type and address of the class object
del  a  
print(a)    # Error a is not defined

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
a . m1()    # 3rd method
m1()    # Function



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
a . m1(10 , 20) # Two argument method : 10 20
a . m1(30)  # Error missing 1 required positional argument
a . m1()    # Error missing 2 required positional argument

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
a . m1(10 , 20) # Two  argument  method : 10 20
a . m1(30)  # Two  argument  method : 30 2
a . m1()    # Two  argument  method : 1 2

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
a . m1()    # Method of third c1 class

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
a . m1()    # Error class c1 has no attribute 'm1'

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a .__dict__) # {} 
a . x = 10
print(a .__dict__)   #{'x':10}
a . y = 20
print(a .__dict__)   # {'x':10,'y':20}
a . x = 30
print(a .__dict__)   # {'x':30,'y':20,}
a . y = 40
print(a .__dict__)   #  {'x':10,'y':40}
del  a . x
print(a .__dict__)   # {'y':40}
del  a . y
print(a .__dict__)  # {}
del   a
print(a .__dict__)  # Error a is not defined

(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c

import math
class triangle:
    def get(self):
        self.a=float(input('Enter 1st input : '))
        self.b=float(input('Enter 2nd input : '))
        self.c=float(input('Enter 3rd input : '))
    def test(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            pass
        else:
            print('Not a Triangle')
            exit()
    def area(self):
        s=(self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def peri(self):
        return self.a + self.b + self.c
t=triangle() #How  to  create  triangle  class  object
t.get()
t.test()# How  to  test  whether  inputs  are  valid
print('Area : ',t.area())
print('Perimeter : ',t.peri())

output:-
Enter 1st input : 10
Enter 2nd input : 15
Enter 3rd input : 20
Area :  72.61843774138907
Perimeter :  45.0