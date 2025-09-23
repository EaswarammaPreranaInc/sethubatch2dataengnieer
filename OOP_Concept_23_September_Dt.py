# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: # Error due to every class has atleast one method or pass required


# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1()
print(id(a)) # Address of class object
print(type(a)) # < class '__main__.c1'>
print(a . _dict_) # {}
print(a) # Type and address of a class object
del  a # object 'a' is deleted
print(a) # Error due to 'a' is not defined


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
a . m1() # '3rd method'
m1() # 'Function'


Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()
a . m1(10 , 20) # 'Two  argument  method : ' , 10 20
a . m1(30) # Error
a . m1() # Error

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
a . m1(10 , 20)  # Two  argument  method : 10 20
a . m1(30) # Two  argument  method : 30 2
a . m1() # Two  argument  method : 1 2


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
a . m1() # Method  of  third  c1  class


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
a . m1() # Empty Space will be printed due to no statements or methods are there only pass is there

#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()
print(a . _dict_) # {}
a . x = 10  # added 'x' variable with value 10 parameter
print(a . _dict_) # {'x':10}
a . y = 20  # added 'y'  variable with value 20 parameter
print(a . _dict_) # {'x':10,'y':20}
a . x = 30   # modified 'x'  variable with value 30 parameter
print(a . _dict_) # {'x':30,'y':20}
a . y = 40  # modified 'y'  variable with value 40 parameter
print(a . _dict_) # {'x':30,'y':40}
del  a . x  # deleted 'x' variable
print(a . _dict_) # {'y':40}
del  a . y  # deleted 'y'  variable
print(a . _dict_) # {}
del   a  # deleted 'a' class object
print(a . _dict_) # Error due 'a' not defined


'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self,a,b,c):  # How  to  read  three  sides  into  object  self
    self.a=a
    self.b=b
    self.c=c
		print("Inputs are",'a'=,self.a,'b'=self.b,'c'=self.c)
	def  test(self):
		if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
				print("The Sides To Form a Triangle")
        return True
		 else:
				print('Not  a  triangle')
				return False
	def  area(self):
    d=self.a + self.b + self.c
    s=d/2
    area_of_triangle=math.sqrt(s * (s - a) * (s - b) * (s - c))
    return   area_of_triangle
	def  peri(self):
    perimeter_of_triangle=self.a + self.a + self.c
    return  perimeter_of_triangle
# End of the class
t.triangle()   # How  to  create  triangle  class  object
a=float(input("Enter 1st Input :")   #How  to  read  inputs  into  object
b=float(input("Enter 2nd Input :") 
c=float(input("Enter 3rd Input :") 
t.get(a,b,c)   # How  to  test  whether  inputs  are  valid
if a.test():
        print('Area : ',a.area())
        print('Perimeter : ',a.peri())
