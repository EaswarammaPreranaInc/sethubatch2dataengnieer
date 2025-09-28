
# 1) Identify  error  (Home work)

class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:     # Error as class c3 is empty class it should have atleast 1 method or pass statement





# 2) Find  outputs  (Home  work)

class c1:
    pass
# End of the class
a = c1()
print(id(a))          # Print address of a
print(type(a))        # Prints <class '__main__.c1'>
print(a . _dict_)     # 'c1' object doesn't have '_dict_'
print(a)              # prints type and address
del a                 # deletes 'a'
print(a)              # Error as 'a' is not defined as it is deleted





# 3) Find  outputs  (Home  work)

def   m1():
		print('Function')
class   c1:
	def   m1(self):                      # Ignored as there is a another method with same name m1 is defined 
		print('1st  method')
	def   m1(self):                      # Ignored as there is a another method with same name m1 is defined
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





# 4) Find  outputs  (Home  work)

class   c1:
	def   m1(self):                                     # Ignored as there is a another method with same name m1 is defined
		print('No  argument  method')               
	def   m1(self , x):                                 # Ignored as there is a another method with same name m1 is defined
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20)
a .m1(30)           # Error as c1.m1() missing 1 required positional argument 'y'
a.m1()              # Error as c1.m1() missing 2 required positional arguments 'x' and 'y'

'''
Outputs:
Two  argument  method :  10 20
'''




# 5) Find  outputs  (Home  work)

class   c1:
	def   m1(self):
		print('No  argument  method')                   # Ignored as there is a another method with same name m1 is defined
	def   m1(self , x):
		print('Single  argument  method : ' , x)        # Ignored as there is a another method with same name m1 is defined
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





# 6) Find  outputs  (Home  work)

class   c1:                                         # Ignored as there is a another class with same name c1 is defined
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:                                         # Ignored as there is a another class with same name c1 is defined
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





# 7) Find  outputs  (Home  work)

class   c1:                                         # Ignored as there is another class with same name c1 is defined
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:                                         # Ignored as there is another class with same name c1 is defined
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a=c1()
a.m1()    # Error as method m1 doesn't exist in the class c1.





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
print(a._dict_)         # Error as object a is deleted
'''
output:
{}
{'x': 10}
{'x': 10, 'y': 20}
{'x': 30, 'y': 20}
{'x': 30, 'y': 40}
{'y': 40}
{}
'''






''' 8) Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''


import math

class Triangle:
    def get(self):  # How  to  read  three  sides  into  object  self
        self.a = float(input("Enter side of a: "))
        self.b = float(input("Enter side of b: "))
        self.c = float(input("Enter side of c: "))

    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # Valid triangle
        else:
            print("Not a triangle")
            exit()  # Stop execution

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))    # area  of  triangle

    def peri(self):
        return self.a + self.b + self.c     # perimeter  of  triangle
# End of the class
t = Triangle()  # How  to  create  triangle  class  object
t.get()         # How  to  read  inputs  into  object
t.test()        # How  to  test  whether  inputs  are  valid

print("Area:", t.area())
print("Perimeter:", t.peri())
'''
output:
Enter side of a: 3
Enter side of b: 4
Enter side of c: 5
Area: 6.0
Perimeter: 12.0

Enter side of a: 2
Enter side of b: 5
Enter side of c: 8
Not a triangle
'''