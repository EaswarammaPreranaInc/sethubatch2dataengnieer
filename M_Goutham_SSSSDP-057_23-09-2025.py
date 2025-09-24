# Identify  error  (Home work)
class   c1: 
	def  m1(self):
		pass
class   c2:
        pass
class   c3: #Here for every class we should define methods or else we should give pass
	


# Find  outputs  (Home  work)
class c1: #Here class is defined
	pass
# End  of  the  class
a = c1() #An empty object is created for c1 class 
print(id(a)) #Prints the address of the c1 class object
print(type(a)) #Prints the type of a i.e <class '__main__.c1'>
print(a . _dict_) #Empty dict {} as there are no instance variables for the c1 class object
print(a) #Prints the type and address
del  a #C1 class object is deleted
print(a) #Error #there is no obj a 




#  Find  outputs  (Home  work)
def   m1(): #Here regular function is defined with name m1
		print('Function')
class   c1: #Here we have defined class with name c1
	def   m1(self): #Here a method is defined inside the c1 class
		print('1st  method')
	def   m1(self): #Here a method is defined inside the c1 class
		print('2nd  method')
	def   m1(self): #Here a method is defined inside the c1 class and above all are discarded 3rd method is recognized
		print('3rd  method')
# End  of  class  c1
a = c1() #Here an empty object is created for c1 class
a . m1() #Here we are calling the m1 method with obj a i.e '3rd method' is printed
m1() #Here we are calling the regular m1 function i.e 'Function'



#  Find  outputs  (Home  work)
class   c1: #Here we are defined the class c1
	def   m1(self): #Here we are defining the m1 method 
		print('No  argument  method')
	def   m1(self , x): #Here we are defining the m1 method with 1 positional argument
		print('Single  argument  method : ' , x)
	def   m1(self , x , y): #Here we are defining the m1 method with 2 positional argument
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() #Here we are creating the obj for c1 class
a . m1(10 , 20) #Here we are calling the m1 method with obj a i.e 10 20 #output: Two argument method : 10 20
a . m1(30) #Error as we know the last one is recognized so error we are not passing the two arguments
a . m1() #Error #same thing with two positional arguments are missing




#  Find  outputs  (Home  work)
class   c1: #Here we are defined the class c1
	def   m1(self): #Here we are defining the m1 method 
		print('No  argument  method')
	def   m1(self , x): #Here we are defining the m1 method with 1 positional argument
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1, y = 2): #Here we are defining the m1 method with 2 default arguments
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() #Here we are creating the obj for c1 class
a . m1(10 , 20) #Here we are calling the m1 method with obj a i.e 10 20 #output: Two argument method : 10 20
a . m1(30) #here output will be #output: Two argument method : 30 2
a . m1() #Here output will be #output: Two argument method : 1 2





# Find  outputs  (Home  work)
class   c1: #Here we have created a class with name c1
	def   m1(self): #Here we have defined the method in c1 class
		print('Method  of  first  c1  class')
class   c1: #Here we have created a class with name c1
	def   m1(self): #Here we have defined the method in c1 class
		print('Method  of  second  c1  class')
class   c1: #Here we have created a class with name c1
	def   m1(self): #Here we have defined the method in c1 class
		print('Method  of  third  c1  class')
a = c1() #Here we have created empty object for c1 class 
a . m1() #Here we are calling the m1 method with obj a i.e 'Method of third c1 class' as we know last created is recognized




# Find  outputs  (Home  work)
class   c1: #Here we have created a class with name c1
	def   m1(self): #Here we have defined the method in c1 class
		print('Method  of  first  c1  class')
class   c1: #Here we have created a class with name c1
	def   m1(self): #Here we have defined the method in c1 class
		print('Method  of  second  c1  class')
class   c1: #Here we have created a class with name c1
	pass #We are not defining any method in c1 class 
a = c1() #Here an empty object is created for c1 class
a . m1() #Error #As there is no m1 method in last c1 class



#  Find  outputs (Home  work)
class  c1: #Here we have created a class with name c1
        pass #We are not defining any method in c1 class 
# End  of  class
a = c1() #Here we are creating the empty obj for c1 class
print(a . _dict_) #Here we are printing the instance variables of obj a and prints empty dict { }
a . x = 10 #Here we are adding the instance varible x with value 10 to obj a 
print(a . _dict_) #Here we are printing the instance variables of obj a and prints {'x':10}
a . y = 20 #Here we are adding the instance varible y with value 20 to obj a 
print(a . _dict_) #Here we are printing the instance variables of obj a and prints {'x':10 , 'y':20}
a . x = 30 #Here we are modifying the the value of x from 10 to 30 
print(a . _dict_) #Here we are printing the obj a i.e {'x':30 , 'y':20}
a . y = 40 #Here we are modifying the value of y from 20 to 40 
print(a . _dict_) #Here we are printing the obj a i.e {'x':30 , 'y':40}
del  a . x #Here we are deleting the variable x 
print(a . _dict_) #Here we are printing the obj a i.e {'y': 40}
del  a . y #Here we are deleting the variable y
print(a . _dict_) #Here we are printing the obj a i.e {}
del   a #Error #As we already deleted a 
print(a . _dict_) #Error #There is no obj a as we have already deleted



'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import math
class Triangle:
    def get(self):
        # Reading sides of the triangle
        self.a = float(input("Enter the first side: "))
        self.b = float(input("Enter the second side: "))
        self.c = float(input("Enter the third side: "))

    def test(self):
        # Checking if it's a valid triangle using the triangle inequality theorem
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            print('Not a valid triangle')
            return False

    def area(self):
        # Using Heron's formula to calculate area
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def peri(self):
        # Perimeter is the sum of all sides
        return self.a + self.b + self.c

# Creating the Triangle object and using the methods
triangle = Triangle()

# Reading the sides of the triangle
triangle.get()

# Testing if the triangle is valid
if triangle.test():
    # If valid, calculating area and perimeter
    print('Area: ', triangle.area())
    print('Perimeter: ', triangle.peri())
