# Identify  error  (Home work)
'''
class   c1:
	def  m1(self):
		pass
class   c2:
        pass           #error
class   c3: 
                       #error
  '''


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()                
print(id(a))                     #adress of object c1
print(type(a))                   # <class '__main__.c1'>
print(a . _dict_)                #error
print(a)                         <__main__.c1 object at address of c1>
del  a
print(a)                         #error because a is delete in above



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
a . m1()                                #3rd function
m1()                                    #function



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
a . m1(10 , 20)                                      #Two  argument  method :  10 20
a . m1(30)                                           #single argument : 30
a . m1()                                             #no argument method




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
a . m1(10 , 20)                                   #Two  argument  method :  10 20
a . m1(30)                                        #Two  argument  method :  30 2
a . m1()                                          #Two  argument  method :  1 2




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
a . m1()                                             #Method  of  third  c1  class
                 


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
a . m1()                                             #error                         




 #  Find  outputs (Home  work)
class c1:
    pass
# End of class

a = c1()
print(a.__dict__)     # {}

a.x = 10
print(a.__dict__)     # {'x': 10}

a.y = 20
print(a.__dict__)     # {'x': 10, 'y': 20}

a.x = 30
print(a.__dict__)     # {'x': 30, 'y': 20}

a.y = 40
print(a.__dict__)     # {'x': 30, 'y': 40}

del a.x
print(a.__dict__)     # {'y': 40}

del a.y
print(a.__dict__)     # {}

del a
print(a.__dict__)     #error



 '''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import math
class triangle:
    def get(self):
        # How to read three sides into object self
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # if sum of every 2 sides >= 3rd side:
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            # Do nothing
            pass
        else:
            print("Not a triangle")
            # How to stop execution
            exit()

    def area(self):
        # return area of triangle
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        # return perimeter of triangle
        return self.a + self.b + self.c

# End of the class

# How to create triangle class object
t = triangle()

# How to read inputs into object
t.get()

# How to test whether inputs are valid
t.test()

print("Area : ", t.area())
print("Perimeter : ", t.peri())
