# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass                               Error Extra indentation
class   c3:

# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))                          140621852444624
print(type(a))                        <class '__main__.c1'>
print(a . _dict_)                     Error
print(a)                              <__main__.c1 object at 0x7feec8f34f10>
del  a
print(a)                              Error

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
a . m1()                          3rd method
m1()                              Function

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
a . m1(10 , 20)                                       Two argument method: 10 20
a . m1(30)                                            Error
a . m1()                                              Error

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
a . m1(10 , 20)                                   Two argument method: 10 20
a . m1(30)                                        Two argument method: 30 2
a . m1()                                          Two argument method: 1 2

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
a . m1()                                           Method of third c1 class

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
a . m1()                                          Error

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_)                              {}
a . x = 10
print(a . _dict_)                              {'x':10}
a . y = 20
print(a . _dict_)                              {'x':10,'y':20}
a . x = 30
print(a . _dict_)                              {'x':30,'y':20}
a . y = 40
print(a . _dict_)                              {'x':30,'y':40}
del  a . x
print(a . _dict_)                              {'y':40}
del  a . y
print(a . _dict_)                              {}
del   a
print(a . _dict_)                              Error

Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
import math
class Triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print("Not a triangle")
            return False   
    def area(self):
        s = (self.a + self.b + self.c) / 2   
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = Triangle()
t.get()
if t.test(): 
    print("Area : ", t.area())
    print("Perimeter : ", t.peri())
