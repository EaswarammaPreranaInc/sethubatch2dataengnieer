#1st program
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
#class   c3: #error , as there are statements in class c3 
	

#2nd program
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))#some address of empty class object (say 1000)
print(type(a)) #<class'__main__.c1'>
print(a . __dict__)#{}
print(a)#type and address of class object a
del  a #class object a is removed
#print(a) #error a not defined


#3rd program
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
a . m1()#3rd method
m1()#Function


#4th program
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
a . m1(10 , 20)#Two argument method: 10 20
#a . m1(30)#error , 1 positional arg is missing
#a . m1() #error 2 positional arguments are missing


#5th program
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
a . m1(10 , 20) #Two argument method: 10 20
a . m1(30) #Two argument method: 30 2
a . m1() #Two argument method: 1 2


#6th program
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
a . m1() #Method of third c1 class


#7th program
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
a . m1() #error,latest c1 does not have attribute m1()


#8th program
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)  #{}
a . x = 10
print(a . __dict__)#{'x':10}
a . y = 20
print(a . __dict__)#{'x':10,'y':20}
a . x = 30
print(a . __dict__)#{'x':30,'y':20}
a . y = 40
print(a . __dict__)#{'x':30,'y':40}
del  a . x
print(a . __dict__)#{'y':40}
del  a . y
print(a . __dict__)#{}
del   a
#print(a . __dict__)#error ,a not defined


#9th program
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import math
class Triangle:
    def get(self):
        # Read three sides and store them in the object
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True  # Valid triangle
        else:
            print("Not a triangle!")
            return False  # Invalid triangle
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
    def peri(self):
        return self.a + self.b + self.c
t = Triangle()       # Create object of class
t.get()              # Read sides into object
if t.test():         # Check validity before calculation
    print("Area      : ", t.area())
    print("Perimeter : ", t.peri())
