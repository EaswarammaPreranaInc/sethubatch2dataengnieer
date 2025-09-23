# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:#class should have at least one statement or pass


#2nd program
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#adress of the object
print(type(a))#<class '__main__.c1'>
print(a . __dict__)#{}
print(a)#<__main__.c1 and adress of the object>
del  a#deleting the object
print(a)#Error 


#3rd  program
#  Find  outputs  (Home  work)
def   m1():
		print('Function')#Function
class   c1:
	def   m1(self):
		print('1st  method')#
	def   m1(self):
		print('2nd  method')
	def   m1(self):
		print('3rd  method')#3rd method
# End  of  class  c1
a = c1()
a . m1()
m1()

#4th program
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)#Two argument method :  10 20
# End  of  class  c1
a = c1()
a . m1(10 , 20)
#a . m1(30)#Error
#a . m1()#Error

#5th  program
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
a . m1()#Method of third c1 class


#6th  program
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
a . m1()#Error 

#7th  program
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) #{} 
a . x = 10
print(a . _dict_)#{'x': 10}
a . y = 20
print(a . _dict_)#{'x': 10, 'y': 20}
a . x = 30
print(a . _dict_)#{'x': 30, 'y': 20}
a . y = 40
print(a . _dict_)#{'x': 30, 'y': 40}
del  a . x
print(a . _dict_)#{'y': 40}
del  a . y
print(a . _dict_)#{}
del   a
print(a . _dict_)#Error

#8th program
import math
class triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # Valid triangle, do nothing
        else:
            print('Not a triangle')
            exit()  # Stop execution
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c

# Create triangle object
t = triangle()
# Read inputs
t.get()
# Test validity
t.test()
# Print area and perimeter
print('Area :', t.area())
print('Perimeter :', t.peri())