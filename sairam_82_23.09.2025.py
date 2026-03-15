#1 Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3:	# class must have either methods or pass

#2 Find  outputs  (Home  work)
class c1:	# define the class
	 pass
# End  of  the  class
a = c1()	# create the class object and ref a points to the class object 
print(id(a))	#address of class object
print(type(a))	#<class '__main__.c1'>
print(a . _dict_)	# {}
print(a)		# returns the type and address
del  a		# deletes the dict a
print(a)		# Error due to a is already deleted

#3  Find  outputs  (Home  work)
def   m1():		# m1 function define
		print('Function')		# Function
class   c1:	# 	# define the class c1 
	def   m1(self):	# method m1 
		print('1st  method')
	def   m1(self):	# method m1
		print('2nd  method')
	def   m1(self):	# method m1
		print('3rd  method')		#3rd  method  due to multiple methods with same name last method is recognized remainig are discarded
# End  of  class  c1
a = c1()	#class object is created and ref a points to the class object
a . m1()	# call the m1 method throgh object a
m1()	# call the m1 function

#4  Find  outputs  (Home  work)
class   c1:		# define the class c1
	def   m1(self):	# method m1 
		print('No  argument  method')
	def   m1(self , x):	# method m1 
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):	# method m1 
		print('Two  argument  method : ' , x , y)		#Two  argument  method :  10 20
# End  of  class  c1
a = c1()	# class object is created c1 and ref a points to the c1 object 
a . m1(10 , 20)	# call the m1 method that to latest method of same name of methods 
a . m1(30)		# error due one arg is missing 
a . m1()		# error due two arg 's  are  missing

#5 Find  outputs  (Home  work)
class   c1: 		# define the  class c1 
	def   m1(self):	# define the method m1
		print('No  argument  method')
	def   m1(self , x):	# define the method with same name m1
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):	## define the method  with same name m1 	# default x=1  y=2
		print('Two  argument  method : ' , x , y)	#Two  argument  method : 10 20
# End  of  class  c1
a = c1()	# create the class object  and ref a points the class object
a . m1(10 , 20)	# call the method m1 here latest mathod is excuted due when the multiple methods are define with same name then latest method only recognized 
a . m1(30) 	# error due we have to pass the two args one is missing
a . m1()		# error due we have to pass the two args 

#6 Find  outputs  (Home  work)
class   c1:		# define the class c1
	def   m1(self):	# define the method m1
		print('Method  of  first  c1  class')
class   c1:		# define the class with same name c1
	def   m1(self):	# define the method m1
		print('Method  of  second  c1  class')
class   c1:		# define the class with same name c1
	def   m1(self):	# define the method m1
		print('Method  of  third  c1  class')	#	Method  of  third  c1  class
a = c1()	# creates the class object c1 and a points the that class object
a . m1()	# call the m1 method 	#here latest method of latest class only recognized when multiple classes are present with same name of class

#7 Find  outputs  (Home  work)
class   c1:		# define the class c1
	def   m1(self):	# define the method m1
		print('Method  of  first  c1  class')
class   c1:	# again define the class with same name c1
	def   m1(self):	# define the method with same name m1
		print('Method  of  second  c1  class')
class   c1:	# again define the class with same name c1
	pass	
a = c1()	#create the class object and ref a points the classs object
a . m1()	# Error  due here call the method of latest class of lastest method 	but in latest class c1 dont have method m1	

#8  Find  outputs (Home  work)
class  c1:	# define the class c1
        pass
# End  of  class
a = c1()	#     create class object  and a ref points to the class object  
print(a . _dict_)  	#{}
a . x = 10	# instance variable x=10
print(a . _dict_)	#{'x':10}
a . y = 20	#instance variable y=20 
print(a . _dict_)	#{'x':10,'y':20}
a . x = 30		#x modifies to 30
print(a . _dict_)	#{'x':30,'y':20}
a . y = 40		#y modifies to 40
print(a . _dict_)	#{'x':30 , 'y': 40}
del  a . x		# del the x from dictionary
print(a . _dict_)	#{'y':40}
del  a . y		# del the y from dict a 
print(a . _dict_)	# {}
del   a		# delete the dict a
print(a . _dict_)	# error

#9 program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
import math

class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def get(self):
        # Read three sides into the object
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Check triangle inequality rule
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print("Not a valid triangle")
            return False   # stops further execution

    def area(self):
        s = (self.a + self.b + self.c) / 2  # semi-perimeter
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# --- Main Program ---
t = Triangle()    # create object
t.get()           # read sides

if t.test():      # check validity
    print("Perimeter:", t.peri())
    print("Area:", t.area())
