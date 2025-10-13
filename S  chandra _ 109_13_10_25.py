: #  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
How  to  call  m1()  method  of  parent  class
How  to  call  m1()  method  of  child  class

##########################################
# Parent and Child classes have the same instance method
class Parent:
    def m1(self):
        print('Parent Method')

class Child(Parent):
    def m1(self):
        # Call parent class m1() without creating a new object
        super().m1()   # This calls Parent's m1()
        print('Child Method')

# Standalone function
def m1():
    print('m1 function')


# --- Calling the methods ---

# 1. Call Child class m1() method
c = Child()
c.m1()
# Output:
# Parent Method
# Child Method

# 2. Call Parent class m1() method
p = Parent()
p.m1()
# Output:
# Parent Method

# 3. Call the standalone function m1()
m1()
# Output:
# m1 function




: # parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
How  to  call  m1()  method  of  parent  class
How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()
self . m1()
######################################
# Parent and Child classes have different class methods
class Parent:
    @classmethod
    def m1(cls):
        print('Parent Method')

class Child(Parent):
    @classmethod
    def m2(cls):
        # --- Call Parent's class method in multiple ways ---
        
        # 1. Using the parent class name directly
        Parent.m1()
        
        # 2. Using super() in the classmethod context
        super(Child, cls).m1()
        
        # 3. Using cls (Child) to call parent method (works because inheritance)
        cls.m1()
        
        # 4. Using super() with current class reference
        super().m1()
        
        print('Child Method')

# --- Calling the methods ---

# Call Parent's class method
Parent.m1()
# Output: Parent Method

# Call Child's class method
Child.m2()
# Output:
# Parent Method
# Parent Method
# Parent Method
# Parent Method
# Child Method

# Other examples
Child.m1()  # Calls inherited Parent.m1() via Child







: # parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
How  to  call  m1()  method  of  parent  class
How  to  call  m1()  method  of  child  class
###################################
# Parent and Child classes with the same class method
class Parent:
    @classmethod
    def m1(cls):
        print('Parent Method')

class Child(Parent):
    @classmethod
    def m1(cls):
        # --- Call Parent's class method from Child ---
        
        # 1. Using parent class name directly
        Parent.m1()
        
        # 2. Using super() with cls
        super(Child, cls).m1()
        
        # 3. Using super() without arguments (Python 3)
        super().m1()
        
        print('Child Method')

# --- Calling the methods ---

# Call Parent's class method directly
Parent.m1()
# Output: Parent Method

# Call Child's class method
Child.m1()
# Output:
# Parent Method
# Parent Method
# Parent Method
# Child Method






: # Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1()
		super(child).m1()
		self . m1()
		cls . m1()
		print('child  method')
#end of the class
How  to  call  m1()  method  of  parent  class
How  to  call  m2()  method  of  child  class
child . m1()
#############################

# Parent and Child classes with different static methods
class Parent:
    @staticmethod
    def m1():
        print('Parent Method')

class Child(Parent):
    @staticmethod
    def m2():
        # --- Call Parent's static method in multiple ways ---

        # 1. Using Parent class name directly
        Parent.m1()

        # 2. Using Child class name (inherited from Parent)
        Child.m1()

        # 3. Using super() in Child class (works with static methods in Python 3)
        super(Child, Child).m1()  

        print('Child Method')


# --- Calling the methods ---

# Call Parent's static method
Parent.m1()
# Output: Parent Method

# Call Child's static method
Child.m2()
# Output:
# Parent Method
# Parent Method
# Parent Method
# Child Method

# Call inherited Parent's static method using Child
Child.m1()
# Output: Parent Method







: # Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()
		self . m1()
		cls . m1()
		print('child  method')
# End  of  the  class
How  to  call  m1()  method  of  parent  class
How  to  call  m1()  method  of  child  class

#################################
# Parent and Child classes with the same static method
class Parent:
    @staticmethod
    def m1():
        print('Parent Method')

class Child(Parent):
    @staticmethod
    def m1():
        # --- Call Parent's static method ---

        # 1. Using parent class name directly
        Parent.m1()

        # 2. Using super() (works in Python 3 inside class definition)
        super(Child, Child).m1()

        print('Child Method')


# --- Calling the methods ---

# Call Parent's static method
Parent.m1()
# Output: Parent Method

# Call Child's static method
Child.m1()
# Output:
# Parent Method
# Parent Method
# Child Method

# Call inherited Parent's static method via Child (if not overridden)
# (Here Child has overridden it, so this calls Child's method)
# Child.m1() -> Calls Child's static method




: # Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		How  to  print  variable  'x'
		How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		How  to  print  variable  'x'
		How  to  print  variable  'x'  in  another  way  without  creating  an  object
		How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		How  to  print  variable  'x' in  last  way  without  creating  an  object
		How  to  print  variable  'y'
		How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)
		print(y)
# End  of child  class
How  to  call   m1()  method  of  parent  class
How  to  call   m2()  method  of  child  class

#############################
# Parent class with static variable
class Parent:
    x = 10  # static variable

    def m1(self):
        # --- Access Parent's static variable ---

        # 1. Using self
        print(self.x)

        # 2. Using class name
        print(Parent.x)

        # 3. Using super() if called from child (inside child)
        # print(super().x)  # works only if inside child method


# Child class with its own static variable
class Child(Parent):
    y = 20  # static variable

    def m2(self):
        # --- Access Parent's static variable ---
        print(self.x)       # via instance (inherited)
        print(Parent.x)     # via class name
        print(super().x)    # via super()

        # --- Access Child's static variable ---
        print(self.y)       # via instance
        print(Child.y)      # via class name


# --- Calling the methods ---

# Call Parent's method
p = Parent()
p.m1()
# Output:
# 10
# 10

# Call Child's method
c = Child()
c.m2()
# Output:
# 10   (Parent's x via self)
# 10   (Parent's x via Parent class)
# 10   (Parent's x via super())
# 20   (Child's y via self)
# 20   (Child's y via Child class)





: # Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		How  to  print  variable  'x'  of  parent  class
		How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		How  to  print  variable  'x'  of  parent  class
		How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		How  to  print  variable  'x'  of  child  class
		How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
How  to  call  m1()  method  of  parent  class
How  to  call  m1()  method  of  child  class
##############################
 
# Parent class with static variable
class Parent:
    x = 10  # static variable

    def m1(self):
        # --- Access Parent's static variable ---

        # 1. Using self
        print(self.x)

        # 2. Using class name
        print(Parent.x)


# Child class with its own static variable
class Child(Parent):
    y = 20  # static variable

    def m2(self):
        # --- Access Parent's static variable ---
        print(self.x)       # via instance (inherited)
        print(Parent.x)     # via class name
        print(super().x)    # via super() in child method

        # --- Access Child's static variable ---
        print(self.y)       # via instance
        print(Child.y)      # via class name


# --- Calling the methods ---

# Call Parent's method
p = Parent()
p.m1()
# Output:
# 10
# 10

# Call Child's method
c = Child()
c.m2()
# Output:
# 10   (Parent's x via self)
# 10   (Parent's x via Parent class)
# 10   (Parent's x via super())
# 20   (Child's y via self)
# 20   (Child's y via Child class)





: #  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		How  to   read  inputs  into   variables  a  and  b  of  object
		How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return   sum  of  values  in  object  self
# End of child class
print('parent  object')
How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  How  to  obtain  sum of  values  of  object  'c')

################################

# Parent class
class Parent:
    def get(self):
        # Read inputs into variables a and b of object
        self.a = int(input("Enter a: "))
        self.b = int(input("Enter b: "))

    def disp(self):
        # Print variables a and b in same line separated by tab
        print(self.a, self.b, sep='\t')


# Child class
class Child(Parent):
    def get(self):
        # Read inputs into variables a and b (from parent)
        super().get()  # reuse Parent get method
        # Read inputs into variables c and d of object
        self.c = int(input("Enter c: "))
        self.d = int(input("Enter d: "))

    def disp(self):
        # Print variables a and b
        print(self.a, self.b, sep='\t')
        # Print variables c and d
        print(self.c, self.d, sep='\t')

    def total(self):
        # Return sum of values in object
        return self.a + self.b + self.c + self.d


# --- Main Program ---

# Parent object
print('Parent object')
p = Parent()
p.get()   # Read inputs for parent
print('Parent object :', end='\t')
p.disp()  # Display parent values

# Child object
print('Child object')
c = Child()
c.get()   # Read inputs for child
print('Child object :', end='\t')
c.disp()  # Display child values

# Sum of values in child object
print('Sum of the values in child object :', c.total())





: '''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import  math
class   circle:
	def   get(self):
	    How  to  read  radius  into  object
	def   area(self):
		return  area  of  circle
	def   cir(self):
		return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		How  to  read  radius  into  object  self
		How  to  read  height  into  object  self
	def  area(self):
		return   area  of  cylinder
	def  volume(self):
		return   volume  of  cylinder
# End of cylinder class
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
while  True:
	menu()
	ch = eval(input('Enter choice : '))
	match  ch:
		case  1:
				How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  ???)
				print('Circumference :  ' ,  ???)
		case  2:
				How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  ???)
				print('Volume :  ' ,  ???)
		case  3:
				How  to  stop  execution
	# End  of  match

###########################

import math

# Parent class: Circle
class Circle:
    def get(self):
        # Read radius into object
        self.r = float(input("Enter radius of circle: "))

    def area(self):
        # Area of circle = pi * r^2
        return 3.14159 * self.r ** 2

    def cir(self):
        # Circumference of circle = 2 * pi * r
        return 2 * 3.14159 * self.r


# Child class: Cylinder (inherits from Circle)
class Cylinder(Circle):
    def get(self):
        # Read radius (reuse parent get)
        super().get()
        # Read height into object
        self.h = float(input("Enter height of cylinder: "))

    def area(self):
        # Surface area of cylinder = 2*pi*r^2 + 2*pi*r*h
        return 2 * 3.14159 * self.r ** 2 + 2 * 3.14159 * self.r * self.h

    def volume(self):
        # Volume of cylinder = pi * r^2 * h
        return 3.14159 * self.r ** 2 * self.h


# Menu function
def menu():
    print("1. Circle")
    print("2. Cylinder")
    print("3. Exit")


# Main loop
while True:
    menu()
    ch = int(input("Enter choice: "))
    match ch:
        case 1:
            c = Circle()
            c.get()  # Read radius
            print("Area:", c.area())
            print("Circumference:", c.cir())
        case 2:
            cyl = Cylinder()
            cyl.get()  # Read radius and height
            print("Area:", cyl.area())
            print("Volume:", cyl.volume())
        case 3:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice, try again.")







: '''
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
		How  to  read  side  of  square
	def   area(self):
		return   area  of  square
	def   peri(self):
		return   perimeter  of  square
class   rectangle(square):
	def   get(self):
		How  to  read  length  of  rectangle
		How  to  read  breadth  of  rectangle
	def   area(self):
		 return   area  of  rectangle
	def   peri(self):
		return  perimeter  of   rectangle
class   cube(square):
	def   get(self):
		 How  to  read  side  of  cube
	def   area(self):
		return  area  of  cube
	def   volume(self):
		return  volume  of  cube
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
			How  to  read  side  into   square  object  's'
			print('Area   :  ' ,  ???)
			print('Perimeter  :  ' ,  ???)
		case   2:
			How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  ??)
			print('Perimeter  :  ' ,  ???)
		case   3:
			How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  ???)
			print('Volume  :  ' ,  ???)
		case  4:
			How  to  stop  execution

######################################
# Parent class: Square
class Square:
    def get(self):
        # Read side of square
        self.a = float(input("Enter side of square: "))

    def area(self):
        # Area of square = a^2
        return self.a ** 2

    def peri(self):
        # Perimeter of square = 4 * a
        return 4 * self.a


# Child class: Rectangle (inherits from Square)
class Rectangle(Square):
    def get(self):
        # Read length and breadth
        self.l = float(input("Enter length of rectangle: "))
        self.b = float(input("Enter breadth of rectangle: "))

    def area(self):
        # Area of rectangle = l * b
        return self.l * self.b

    def peri(self):
        # Perimeter of rectangle = 2 * (l + b)
        return 2 * (self.l + self.b)


# Child class: Cube (inherits from Square)
class Cube(Square):
    def get(self):
        # Read side of cube
        self.a = float(input("Enter side of cube: "))

    def area(self):
        # Surface area of cube = 6 * a^2
        return 6 * self.a ** 2

    def volume(self):
        # Volume of cube = a^3
        return self.a ** 3


# Menu function
def menu():
    print("1. Square")
    print("2. Rectangle")
    print("3. Cube")
    print("4. Exit")


# Main loop
while True:
    menu()
    ch = int(input("Enter choice: "))
    match ch:
        case 1:
            s = Square()
            s.get()  # Read side of square
            print("Area:", s.area())
            print("Perimeter:", s.peri())
        case 2:
            r = Rectangle()
            r.get()  # Read length and breadth
            print("Area:", r.area())
            print("Perimeter:", r.peri())
        case 3:
            c = Cube()
            c.get()  # Read side of cube
            print("Surface Area:", c.area())
            print("Volume:", c.volume())
        case 4:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice, try again.")






: # Find  outputs
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
		How  to  call  m1()  method  of  class  c3
		How  to  call  m1()  method  of  class  c4
		How  to  call  m1()  method  of  class  c2
		How  to  call  m1()  method  of  class  c1
		How  to  call  m1()  method  of  class  c5
		How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
How  to  call  m2()  method  of  class  c5

###################################

class c1:
    def m1(self):
        print('m1 method of class c1')

class c2:
    def m1(self):
        print('m1 method of class c2')

class c3:
    @classmethod
    def m1(cls):
        print('m1 method of class c3')

class c4:
    @staticmethod
    def m1():
        print('m1 method of class c4')

class c5(c1):
    def m1(self):
        print('m1 method of class c5')

    def m2(self):
        # Call classmethod of c3
        c3.m1()               # class method, no object needed
        # Call static method of c4
        c4.m1()               # static method, no object needed
        # Call instance method of c2
        c2().m1()             # need object of c2
        # Call instance method of c1
        c1().m1()             # need object of c1
        # Call instance method of c5 (current)
        self.m1()             # via self
        # Call standalone function
        m1()                  # direct call


# Standalone function
def m1():
    print('m1 function')


# Call c5.m2()
obj = c5()
obj.m2()

$$$$$$$$$$$$$$$$$$$$$$$$$$

m1 method of class c3
m1 method of class c4
m1 method of class c2
m1 method of class c1
m1 method of class c5
m1 function







: # Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))      ### True
print(issubclass(int , float))  ### False
print(issubclass(str , object)) ### Ture
print(issubclass(c1 , object))  ### True
print(issubclass(c2 , object))  ### True
a = c1()
b = c2()
print(issubclass(b , a))  ### Error
print(issubclass(c2 , a)) ### Error 






: # Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))  ### True
print(issubclass(c4 , c2))  ### True
print(issubclass(c4 , c1))  ### True
print(issubclass(c4 , object))  ### True
print(issubclass(c4 , (int , float , str , bool))) ## False
print(issubclass(c4 , (int , float , c1 , str , bool)))  ### True
print(issubclass(c4 , [int , float , c1 , str , bool])) ### Type Error





#######################

class c1: pass
class c2(c1): pass
class c3(c2): pass
class c4: pass

print(isinstance(25 , int))       # True
print(isinstance(10.8 , float))   # True
print(isinstance('Hyd' , str))    # True
print(isinstance(3 + 4j , complex)) # True
print(isinstance(True , bool))     # True
print(isinstance(True , int))      # True (bool is subclass of int)
print(isinstance('True' , str))    # True
print(isinstance(True , str))      # False

a = c3()
print(isinstance(a , c3))          # True
print(isinstance(a , c2))          # True
print(isinstance(a , c1))          # True
print(isinstance(a , object))      # True
print(isinstance(a , c4))          # False
print(isinstance(a , (int, float, str, bool)))  # False
print(isinstance(a , (int, float, c3, str, bool))) # True
print(isinstance(a , (int, float, c1, str, bool))) # True
# isinstance(a, [int, float, c3, str, bool])  TypeError, must be tuple








: #  Write  a  program   to  determine  length  of  linked  list
class  sll(linked_list):
	def  length(a):
			return  number  of  nodes  in  the  linked  list
# End  of  the  class
if  _name_  ==  '_main_':
	How  to  create  linked  list
	print('Number  of  nodes : ' , ???)

###############################
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

# Derived class to compute length
class SLL(LinkedList):
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Utility method to insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

# Main program
if __name__ == "__main__":
    ll = SLL()
    
    # Creating linked list by reading values
    n = int(input("Enter number of nodes to insert: "))
    for i in range(n):
        val = int(input(f"Enter value for node {i+1}: "))
        ll.insert_end(val)

    # Print number of nodes
    print("Number of nodes:", ll.length())







: '''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
class   linkedlist(sll):
	def  find(a , i):
			return  data  of  ith  node
			and  return  None  when  ith  node  does  not  exist
# End  of  the  class
How  to  create  linked  list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	How  to   obtain  data  of  ith  node
	if  ???
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  ???')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

########################

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base linked list class
class SLL:
    def __init__(self):
        self.head = None

    # Insert node at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

# Derived class to find ith node
class LinkedList(SLL):
    def find(self, i):
        temp = self.head
        pos = 1
        while temp:
            if pos == i:
                return temp.data
            temp = temp.next
            pos += 1
        return None

# --- Main Program ---
ll = LinkedList()

# Create linked list by reading values
print("Create linked list (Enter -1 to stop):")
while True:
    val = int(input("Enter value: "))
    if val == -1:
        break
    ll.insert_end(val)

print("\nLinked List created.")

# Find ith node
while True:
    i = int(input("\nEnter value of 'i' to find node (0 to stop): "))
    if i == 0:
        break
    data = ll.find(i)
    if data is None:
        print(f"Node {i} does not exist")
    else:
        print(f"Data of node {i} is: {data}")

    ch = input("Do you wish to continue (y / n) : ")
    if ch.lower() == 'n':
        break

print("Good Bye")







: '''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
class  sll(linked_list):
	def  search(a , x):
			return  address  of  that  node  where  'x'  is  found  and  None  otherwise
# End  of  the  class
How  to  create  linked  list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	How  to  call  search()  method
	if  ???
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  ???')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')

#############################

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Utility method to insert node at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

# Derived SLL class with search method
class SLL(LinkedList):
    def search(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return temp  # return node address
            temp = temp.next
        return None

# --- Main Program ---
ll = SLL()

# Create linked list by reading values
print("Create linked list (Enter -1 to stop):")
while True:
    val = int(input("Enter value: "))
    if val == -1:
        break
    ll.insert_end(val)

print("\nLinked List created.")

# Search for values in linked list
while True:
    x = int(input("\nEnter value to be searched (0 to stop): "))
    if x == 0:
        break
    node = ll.search(x)
    if node is None:
        print(f"{x} is not found")
    else:
        print(f"Found at address: {node} with data: {node.data}")

    ch = input("Do you wish to continue (y / n) : ")
    if ch.lower() == 'n':
        break

print("Good Bye")







: '''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
																														and
																										modify  the  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None
																												and
																								modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		        modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
class  linkedlist(sll):
	def  insert(a , i , x):
		if  'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  insertion  at  the  begining  of  LL:
				How  to  create  a  new  node
				How  to  insert  new  node  at  the  begining  of  LL
		else:
			How  to  create  a  new  node
			How  to  insert  new  node  after  ith  node  of  LL
# End  of  the  class
How  to  create  a  linked  list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	How  to  insert   new  node  after   ith  node
	print('Linked  List  :  ' , end = '')
	How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break

############################

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base linked list class
class SLL:
    def __init__(self):
        self.head = None

    # Utility method to print linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ' if temp.next else '')
            temp = temp.next
        print()

# Derived class with insertion method
class LinkedList(SLL):
    def insert(self, i, x):
        new_node = Node(x)
        
        # Insert at the beginning
        if i == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        # Insert after ith node
        temp = self.head
        pos = 0
        while temp and pos < i:
            temp = temp.next
            pos += 1
        
        if temp is None:
            print(f"Node {i} does not exist")
        else:
            new_node.next = temp.next
            temp.next = new_node

# --- Main Program ---
ll = LinkedList()

# Create linked list by reading values
print("Create linked list (Enter -1 to stop):")
while True:
    val = int(input("Enter value: "))
    if val == -1:
        break
    ll.insert(i=ll.head and 0 or 0, x=val)  # inserting at beginning initially

print("\nInitial Linked List:")
ll.display()

# Insert nodes at any position
while True:
    i = int(input("\nEnter value of 'i' (position after which to insert, 0 for beginning): "))
    x = int(input("Enter value to be inserted: "))
    ll.insert(i, x)
    print("Linked List : ", end='')
    ll.display()
    
    ch = input("Would you like to insert another node (Y or N)? : ")
    if ch.lower() == 'n':
        break






: '''
Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''
class  linkedlist(sll):
	def  delete(a , i):
		if   'i'  is  an  invalid  node  number:
			return   ???
		elif  deletion of  1st  node:
			How  to  delete  first  node  logically
			How  to  delete  first  node  physically
			How  to  return  data  of  the  deleted  node
		else:
			How  to  modify  (i - 1)th  node  link  to  (i + 1)th node
			How  to  delete  ith  node
			How  to  return  data  of  the  deleted  node
# End  of  the  class
How  to  create  linked  list
while  True:
	i = int(input('Enter  value  of  i  :  '))
	How  to  delete  ith  node
	if  ???:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  ???)
	print('Linked  List  :  ' , end = '')
	How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break


####################################

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base linked list class
class SLL:
    def __init__(self):
        self.head = None

    # Utility method to print linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ' if temp.next else '')
            temp = temp.next
        print()

# Derived class with delete method
class LinkedList(SLL):
    def delete(self, i):
        if self.head is None:
            return None  # List is empty, nothing to delete

        # Delete first node
        if i == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data

        # Delete ith node
        temp = self.head
        pos = 0
        while temp.next and pos < i - 1:
            temp = temp.next
            pos += 1

        # If ith node does not exist
        if temp.next is None:
            return None

        deleted_data = temp.next.data
        temp.next = temp.next.next  # Modify link to skip ith node
        return deleted_data

# --- Main Program ---
ll = LinkedList()

# Create linked list by reading values
print("Create linked list (Enter -1 to stop):")
while True:
    val = int(input("Enter value: "))
    if val == -1:
        break
    # Insert at end
    new_node = Node(val)
    if ll.head is None:
        ll.head = new_node
    else:
        temp = ll.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

print("\nInitial Linked List:")
ll.display()

# Delete nodes by position
while True:
    i = int(input("\nEnter value of 'i' (position to delete, 0-based index): "))
    deleted_data = ll.delete(i)
    if deleted_data is None:
        print(f"Node {i} does not exist")
    else:
        print(f"Data of deleted node is: {deleted_data}")
    
    print("Linked List : ", end='')
    ll.display()
    
    ch = input("Would you like to delete another node (Y or N)? : ")
    if ch.lower() == 'n':
        break







