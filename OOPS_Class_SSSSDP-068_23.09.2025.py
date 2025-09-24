# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:  #  Error due to no methods



# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a))  #  address of class
print(type(a))  #  classs name
print(a . __dict__)  #  {}
print(a)  #  class name and address
del  a   #  deletes the a
print(a)  #   Error



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
a . m1()
m1()
'''
3rd  method
function
'''



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
a . m1(10 , 20)  #  Two  argument  method : 10 20
a . m1(30)  #  Error due to m1 want 2 arguments 1 givened
a . m1()  #   #  Error due to m1 want 2 arguments 0 givened



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
a . m1(10 , 20)
a . m1(30)
a . m1()
'''
Two  argument  method : 10 20
Two  argument  method : 30 2
Two  argument  method : 1 2
'''



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
a . m1()  #  method of third c1 class




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
a . m1()  #  Error due to method m1 id not defined in c1



#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . __dict__)    #  {}
a . x = 10
print(a . __dict__)  #  {x:10}
a . y = 20
print(a . __dict__)  #  {x:10,y:20}
a . x = 30
print(a . __dict__)  #  {x:30,y:20}
a . y = 40
print(a . __dict__)  #  {x:30,y:40}
del  a . x
print(a . __dict__)  #  {y:40}
del  a . y
print(a . __dict__)  #  {}
del   a
print(a . __dict__)  # Error due to a is not defined



'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''

import math
class triangle:
    def get(self):
        self.p = int(input("Enter 1st side of Triangle : "))
        self.q = int(input("Enter 2nd side of Triangle : "))
        self.r = int(input("Enter 3rd side of Triangle : "))  # How  to  read  three  sides  into  object  self
    def test(self):
        if self.p + self.q > self.r and self.p + self.r > self.q and self.q + self.r > self.p:
            pass  # Do nothing
        else:
            print('Not a triangle')
            exit()  #  How  to  stop  execution
    def area(self):
        s = (self.p + self.q + self.r) / 2
        return math.sqrt(s * (s - self.p) * (s - self.q) * (s - self.r))
    def peri(self):
        return self.p + self.q + self.r
    
# End of the class
a = triangle()   #  How  to  create  triangle  class  object
a.get()          #  How  to  read  inputs  into  object
a.test()         #  How  to  test  whether  inputs  are  valid
print('Area : ', a.area())
print('Perimeter : ', a.peri())
