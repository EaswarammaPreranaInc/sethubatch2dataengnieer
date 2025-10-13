# Bathini  Raju
# 13/10/2025

#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() #How  to  call  function  m1()
		#self . m1() #Recursion
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent() 
p.m1() #How  to  call  m1()  method  of  parent  class
c=child() 
c.m1() #How  to  call  m1()  method  of  child  class

'''
parent  Method
parent  Method
m1  function
parent  Method
child Method
Recursion line number 9

'''


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1() #Error
		#m1() #Error
		print('child  Method')
# End  of  the  class
p=parent() 
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1()
#super() . m1() #Error
#self . m1() # Error
'''
parent  Method
parent  Method
parent  Method
parent  Method
parent  Method
child  Method
parent  Method
'''

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()  #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1() #Recursion
		self . m1() #Error because no self
		m1() # Error No m1() Function 
		print('child  Method') 
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class
'''
parent  Method
parent  Method
parent  Method
child  Method
'''

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() 
		super(child).m1() #Error super has argumets 0 or 2
		self . m1() # Error
		cls . m1() #Error
		print('child  method')
#end of the class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1()
'''
parent  method
parent  method
parent  method
parent  method
parent  method
child  method
parent  method
'''


# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()
		self . m1() #Error
		cls . m1() #Error
		print('child  method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class
'''
parent  method
parent  method
parent  method
child method
'''

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x) # error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(super().x) #How  to  print  variable  'x'
		print(parent.x )#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super(child,self).x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y) #How  to  print  variable  'y'
		print(self.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # Error
		print(y) #Error
# End  of child  class
p=parent() 
p.m1() #How  to  call   m1()  method  of  parent  class
c=child() 
c.m1() #How  to  call   m2()  method  of  child  class
'''
10
10
10
10
10
20
20
'''

# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(self.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super().x )#How  to  print  variable  'x'  of  parent  class
		print(super(child,self).x)#  print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x'  of  child  class
		print(self.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent()
p.m1() #How  to  call  m1()  method  of  parent  class
c=child()
c.m1() #How  to  call  m1()  method  of  child  class
'''
10
10
10
10
20
20
'''

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
    def    get(self):
        self.a=int(input("Enter a value :"))
        self.b=int(input("Enter b value :"))
    def    disp(self):
        print(self.a,self.b,sep='\t') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
    def    get(self):
        super().get() 
        self.c=int(input("Enter c value :"))
        self.d=int(input("Enter d value :")) 
    def   disp(self):
        print(self.a,self.b,sep='\t')
        print(self.c,self.d,sep='\t')
    def total(self):
        return   self.a+self.b+self.c+self.d 
# End of child class
print('parent  object') 
p=parent() 
p.get() #How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child() 
c.get()#How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp() #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,c.total())
'''
parent  object
Enter a value :10
Enter b value :20
child  object
Enter a value :30
Enter b value :40
Enter c value :50
Enter d value :60
parent  object  :  	10	20

child  object  :  	30	40
50	60
Sum of  the  values  in  child  object :   180

'''


'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''


import math

class circle:
    def get(self):
        self.r = eval(input("Enter the radius :"))  # How to read radius into object

    def area(self):
        return math.pi * self.r ** 2

    def cir(self):
        return 2 * math.pi * self.r  # circumference of circle
# End of circle class


class cylinder(circle):
    def get(self):
        super().get()  # How to read radius into object self
        self.h = int(input("Enter the height :"))  # How to read height into object self

    def area(self):
        return 2 *super().area()+ 2 * math.pi * self.r * self.h

    def volume(self):
        return math.pi * self.r ** 2 * self.h
# End of cylinder class


def menu():
    print('1 . Circle')
    print('2 . Cylinder')
    print('3 . Exit')
# End of menu function


while True:
    menu()
    ch = eval(input('Enter choice : '))
    match ch:
        case 1:
            c = circle()  # How to read radius into circle object
            c.get()
            print('Area  :  ', c.area())
            print('Circumference :  ', c.cir())

        case 2:
            cy = cylinder()
            cy.get()  # How to read radius and height into cylinder object
            print('Area : ', cy.area())
            print('Volume :  ', cy.volume())

        case 3:
            exit()
    # End of match
'''
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 1
Enter the radius :5
Area  :   78.53981633974483
Circumference :   31.41592653589793
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 2
Enter the radius :5
Enter the height :6
Area :  345.5751918948772
Volume :   471.23889803846896
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 3
'''


'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  ---> a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  --->  a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''
class   square:
	def   get(self):
		self.a = int(input("Enter side of square : "))  # How  to  read  side  of  square
	def   area(self):
		return   self.a ** 2
	def   peri(self):
		return   4 * self.a
class   rectangle(square):
	def   get(self):
		self.a = int(input("Enter length of rectangle : "))  # How  to  read  length  of  rectangle
		self.b = int(input("Enter breadth of rectangle : "))  # How  to  read  breadth  of  rectangle
	def   area(self):
		return   self.a * self.b
	def   peri(self):
		return  2 * (self.a + self.b)
class   cube(square):
	def   get(self):
		self.a = int(input("Enter side of cube : "))  # How  to  read  side  of  cube
	def   area(self):
		return  6 * super().area()
	def   volume(self):
		return  self.a ** 3
def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
while  True:
	menu()
	ch = int(input('Enter  choice : '))
	match   ch:
		case   1:
			s = square()
			s.get()
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' ,  s.peri())
		case   2:
			r = rectangle()
			r.get()
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c = cube()
			c.get()
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit()
'''
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 1
Enter side of square : 4
Area   :   16
Perimeter  :   16
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 2
Enter length of rectangle : 5
Enter breadth of rectangle : 2
Area  :   10
Perimeter  :   14
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 3
Enter side of cube : 5
Area  :    150
Volume  :   125
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 4
'''


# Find  outputs
class  c1:
	def  m1(self):
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self):
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls):
		print('m1 method of  class c3')
class  c4:
	@staticmethod
	def  m1():
		print('m1 method of  class c4')
class  c5(c1):
	def  m1(self):
		print('m1 method of class c5')
	def  m2(self):
		c3.m1() #How  to  call  m1()  method  of  class  c3
		c4.m1() #How  to  call  m1()  method  of  class  c4
		x=c2()
		x.m1() #How  to  call  m1()  method  of  class  c2
		super().m1() #How  to  call  m1()  method  of  class  c1
		self.m1() #How  to  call  m1()  method  of  class  c5
		m1() #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c=c5() 
c.m2() #How  to  call  m2()  method  of  class  c5


# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) # True
print(issubclass(int , float)) # False
print(issubclass(str , object)) # True
print(issubclass(c1 , object)) # True
print(issubclass(c2 , object)) # True
a = c1()
b = c2()
#print(issubclass(b , a)) # Error
#print(issubclass(c2 , a)) #Error



# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) #True
print(issubclass(c4 , c2)) #True
print(issubclass(c4 , c1)) # #True
print(issubclass(c4 , object)) # True
print(issubclass(c4 , (int , float , str , bool))) #False
print(issubclass(c4 , (int , float , c1 , str , bool))) #True
print(issubclass(c4 , [int , float , c1 , str , bool])) #Error

#  Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int)) # True
print(isinstance(10.8 , float)) # True
print(isinstance('Hyd' , str)) #True
print(isinstance(3 + 4j , complex)) # True
print(isinstance(True , bool)) #True
print(isinstance(True , int)) #True
print(isinstance('True' , str)) #True
print(isinstance(True , str)) #False
print()
a = c3()
print(isinstance(a , c3)) # True
print(isinstance(a , c2)) # True
print(isinstance(a , c1)) #True
print(isinstance(a , object)) #True
print(isinstance(a , c4)) #False
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) #Flase
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool))) #True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) #True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))# Error