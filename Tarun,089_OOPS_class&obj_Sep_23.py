#Tarun Banala     23-09-2025    HOME WORRK
#1
 # Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:
        #pass       #Empty statement causes an eroor we have Pass the statement



#2
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()                   #object is created with refrence a
print(id(a))               #provide the address
print(type(a))             #<class'__main__.c1'>
print(a . __dict__)        #{}
print(a)                   #<__main__.c1 object at 0x7fb2844c4a90>
del  a                     #Delete the reference/object address
print(a)                   #Error


#3
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
a . m1()         #3rd  method
m1()             #Function




#4
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
a . m1(10 , 20)             # Two  argument  method : 10,20
a . m1(30)                  #Error
a . m1()                    #Error


#5
 #  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()                       #creates an object with a refrence a
a . m1(10 , 20)                #Two  argument  method :10 20
a . m1(30)                     #Two  argument  method :30 2
a . m1()                       #Two  argument  method : 1 2


#6
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
a . m1()        #Method  of  third  c1  class


#7
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
a . m1()      #Error m1 method is not defined 


#8
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)    #{} 
a . x = 10
print(a . __dict__)    #{'x':10}
a . y = 20
print(a . __dict__)    #{'x':10,'y':20}
a . x = 30
print(a . __dict__)    #{'x':30,'z':30}
a . y = 40
print(a . __dict__)    #{'x':30,'y':40}
del  a . x
print(a . __dict__)     #{'y':40}
del  a . y
print(a . __dict__)      #{}
del   a
print(a . __dict__)      #object a  is deleted



#9 '''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import math

class Triangle:
    def get(self):
        # read 3 sides into the object (self.a, self.b, self.c)
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # check triangle validity (sum of any two sides > third side)
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print("Not a triangle")
            return False   # stop further execution if invalid

    def area(self):
        # Heron's formula: sqrt(s * (s - a) * (s - b) * (s - c))
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        # perimeter = a + b + c
        return self.a + self.b + self.c

# ---- Main Program ----
t = Triangle()        # create triangle object
t.get()               # read inputs

if t.test():          # validate triangle
    print("Area :", t.area())
    print("Perimeter :", t.peri())
