                               NAME:M.SAICHARAN                     HOMEWORK
                               DATE:23-09-2025

1.# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:			#Error




2.# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()			#Object c1 is created through reference 'a'
print(id(a))			#Address of object 'a may be 1000
print(type(a))			#<class '__main__.c1'>
print(a . _dict_)		#{}
print(a)			#Type and Address of 'a' 
del  a
print(a)			#Error





3.#  Find  outputs  (Home  work)
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

#Output:
3rd  method
Function



4.#  Find  outputs  (Home  work)
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
a . m1(30)			#Error
a . m1()			#Error

#Output;
Two  argument  method :  10 20



5.#  Find  outputs  (Home  work)
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

#Output:
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2



6.# Find  outputs  (Home  work)
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
a . m1()

#Output:
Method  of  third  c1  class


7.# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a = c1()
a . m1()		#Error





8.#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)  
a . x = 10
print(a . _dict_)
a . y = 20
print(a . _dict_)
a . x = 30
print(a . _dict_)
a . y = 40
print(a . _dict_)
del  a . x
print(a . _dict_)
del  a . y
print(a . _dict_)
del   a
print(a . _dict_)		
#Error

#Output:
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}



'''  (Home  work)
9.Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
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
print('Perimeter : ',  ???)

#Program:
import math
class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def get(self):
        # Read 3 sides into object
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        # Check validity of triangle
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print("Not a valid triangle")
            return False
    def area(self):
        s = (self.a + self.b + self.c) / 2   # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = Triangle()       
t.get()             
if t.test():        
    print("Area      :", t.area())
    print("Perimeter :", t.peri())
