# Find  outputs  (Home  work)
class   outer: #This is the outer class
	def  __init__(self): #This is constructor
		print('Outer  class  constructor')
	def  m1(self): #This is method of outer class
		print('Outer  class  method')
	class   inner: #This is the inner class of outer class
		def __init__(self): #Constructor of inner class
			print('Inner  class  constructor')
		def m1(self): #This is the method of inner class
			print('Inner  class  method')
#end of the class
a = outer()
a.m1() #How  to  call  m1()  method  of  outer  class
b = a.inner()
b.m1() #How  to  call  m1()  method  of  inner  class
i = outer.inner()
i.m1()  #How  to  call  m1()  method  of  inner  class  in  another  way
i1 = outer().inner()
i1.m1() #How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = inner() #Error #as there is no class defined with name inner() #inner class is defined inside outer class
'''output:
Outer  class  constructor
Outer  class  method
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
'''



# Find  outputs  (Home  work)
class emp:
    def __init__(self):
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0  # How to initialize empno , ename , sal of object self to 25 , 'Rama Rao' , 10000.0
        self.dob = emp.date()  # How to create date class object

    def disp(self):
        print(self.empno)  # How to print empno , ename , sal of object self
        print(self.ename)  # How to print empno , ename , sal of object self
        print(self.sal)  # How to print empno , ename , sal of object self
        self.dob.disp()  # How to call disp() method of date class

    class date:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947  # How to initialize dd , mm , yy of object self to 15 , 8 , 1947

        def disp(self):
            print(f"Date of birth : {self.dd}-{self.mm}-{self.yy}")  # How to print dd , mm , yy of object self

# End of the class
a = emp()
a.disp()  # How to call disp() method of emp class
'''outputs:
25
Rama Rao
10000.0
Date of birth: 2025-10-08'''
	



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 #How  to  initialize  variable  'x'  of  object  self  to  25
		self.inc1 = outer.inner1() #How  to  create  inner1  class  object
		self.inc2 = outer.inner2() #How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a = outer()
a.disp() #How  to  call   disp()  method  of outer  class
a.inc1.disp()#How  to  call   disp()  method  of inner1  class
a.inc2.disp()#How  to  call   disp()  method  of inner2  class
'''outputs:
25
1st inner class method
2nd inner class method
'''





# Find  outputs  (Home  work)
class   c1: #it is the outer class c1
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2: #it is the inner class c2 of outer class c1
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2: #it is the outer class c2
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a = c1()    #How  to  create  c1  class  object
b = a.c2()  #How  to  create  inner  c2  class  object
c = c2()    #How  to  create  outer  c2  class  object
'''outputs:
outer class c1 constructor
inner class c2 constructor
outer class c2 constructor'''




# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2()    #How  to  create  outer  c2  class  object
b = a.c2()    #How  to  create  inner  c2  class  object
c = c2.c2()    #How  to  create  inner  c2  class  object  in  another  way
'''outputs:
outer class constructor
inner class constructor
inner class constructor'''



# Find  outputs (Home  work)
class c1: 
    x = 10 #It is a static variable x with value 10 and it can be accessble to all the objects of the class
    def __init__(self): #It is the constructor of c1 class
	    self . y = 20 #Variable y is added to obj self with value 20
a = c1() #Here c1 class object is created and constructor is executed
b = c1() #Here another c1 class object is created and constructor is executed
a . x += 1 #Here value of static variable x is modified i.e 10 to 11
b . y += 1 #Here value of instance variable y is modified i.e 20 to 21
print(a . x) #11
print(a . y) #20
print(b . x) #10
print(b . y) #21
print(c1 . x) #10
print(a . ___dict___) # { 'y' : 20,'x' : 11 }
print(b . ___dict___) # { 'y' : 11 }
print(c1 . ___dict___) # { 'X' : 10 }



'''
static   variable  ---> 'X'

Object  'a'  ---> 

Object  'b'  --->
'''


# Find  outputs (Home  work)
class  c1: #Here c1 class is created
	x = 10 #static variable x is defined with value 10
	def  m1(self): #m1 method of c1 class
		self . x = 20 #instance variable x is added to obj self with value 20
a = c1() #c1 class object is created
a . m1() #m1 method is called
print(c1 . x) #Here prints static variable x i.e 10
print(a . x) #Prints the instance variable i.e 20


'''
static   variable   ---> 'x'

object  'a'   --->
'''



# Find  outputs  (Home  work)
class   c1: #Here it is a class method because here we have '@classmethod' decorator
	x = 10 #It is a static variable x with value 10
	def  __init__(self): #Constructor of c1 class
		self . y = 20 #Here variable y is added to obj self with value 20
	@classmethod #decorator of class method
	def   m1(cls): #Here cls is the argument for class method
		cls . x = 30 #class Variable x is modified to 30
		cls . y = 40 #class Variable y is added to cls obj with value 40
# End  of  the  class
a = c1() #Here c1 class object is created and constructor is executed
b = c1() #Here c1 class object is created and constructor is executed
c1 . m1() #Here we are calling m1 method
print(a . x) #30
print(a . y) #20
print(b . x) #30
print(b . y) #20
print(c1 . x , c1 . y) #30 #40
#print(cls . x , cls . y) #Error #we should use cls inside the class method
#print(self . x , self . y) #Error #we should use self inside the method



'''
static   variable   ---> 'x'

object  'a'   ---> x , y

object  'b'   ---> x , y
'''



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #Here we are calling the static method with argument 25 
a = c1() #Here we are creating the object for class c1
a . m1(35) #Here we are calling the instance method with argument 35




#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #We are calling the m1 method with respect to staticmethod where we treat self as just an argument not owner obj
a = c1() #Here we are creating the object for c1 class
a . m1() #Here we are calling the m1 method using obj so in the method it is printing the self which is obj so type and address
a . m1(35) #Error #beacuse we are calling the method with argument 25 but method is not excepting any argument and here we are calling the method with obj



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #Here you are calling the static method with argument 25  #prints the static / instance method
                                                                      #25
a = c1() #Here you are creating the object for class c1               
a . m1() #Here youu are calling the m1 method #Prints the #static / instance method
                                                          #type and address




# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
	def   m1(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		#print(cls . x) #Error #no cls is defined in the instance method
	@classmethod
	def   m2(cls):
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls.x) #How  to  print  static  variable  'x'  in  another  way
		#print(self . x) #Error #'self' is not defined in class method
	@staticmethod
	def   m3():
		print(c1.x) #How  to  print  static  variable  'x'
		#print(cls . x) #Error #there is no cls is defined in the static method
		#print(self . x) #Error #there is no self is defined in the static method
# End  of  the  class 
print(c1.x)#How  to  print  static  variable  'x' 
obj = c1()
print(obj.x) #How  to  print  static  variable  'x'  in  another  way
#print(x) #Error #there is no global x
#print(self . x) #Error #there is no self is defined
#print(cls . x) #Error #there is no cls is defined
a = c1() 
a.m1() #How  to  call  method  m1()
c1.m2() #How  to  call  method  m2()
c1.m3() #How  to  call  method  m3()




# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b = 20 #How  to  add  static  variable  'b'  with  value  20
		self.c = 30 #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 #Error #There is no cls is defined
	def   m1(self):
		c1.d = 40   #How  to  add  static  variable  'd'  with  value  40
		self.e = 50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 #How  to  add  static  variable  'f'  with  value  60
		cls.g = 70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 #Error #there is no self defined and in classmethod we cannot have self only cls
	@staticmethod
	def   m3():
		c1.h = 80 #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 #Error #there are no args like self and cls for staticmethod
		#cls . k = 35 #Error #there are no args like self and cls for staticmethod
#End  of  the  class
print('Begin')
print(c1 . __dict__) #{ 'a' : 10 }
print() #Prints nothing
print() #Prints nothing
x = c1() #Creating the c1 class object and constructor is executed
print('Constructor') #Prints constructor
print(c1 . __dict__) # {'a':10,'b':20}
print() #Prints nothing
print() #Prints nothing
x.m1() #How  to  call  m1()  method
print('Instance  method  m1') #Prints instance method of m1
print(c1 .__dict__) #{'a':10,'b':20,'d':40}
print() #Prints nothing
print() #Prints nothing
c1.m2() #How  to  call  m2()  method
print('class  method   m2') #Prints the class method m2
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70}
print() #Prints nothing
print() #Prints nothing
c1.m3() #How  to  call  m3()  method
print('static   method   m3') #Prints the static method m3
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80}
print() #Prints nothing
print() #Prints nothing
c1.i = 90 #How  to  add  static  variable  'i'  with  value  90
x.j = 100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class') 
print(c1 . __dict__) #{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80,'i':90}
print() #Prints nothing
print() #Prints nothing
print("Object  'x' ")
print(x . __dict__)#{'c':30,'e':50,'j':100}
'''outputs:
Begin
#{ 'a' : 10 } and env variables

Constructor
{'a':10,'b':20} and env variables

Instance method m1
#{'a':10,'b':20,'d':40} and env variables

class method m2
 #{'a':10,'b':20,'d':40,'f':60,'g':70} and env variables

static method m3
#{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80} and env variables

outside the class 
{'a':10,'b':20,'d':40,'f':60,'g':70,'h':80,'i':90} and env variables

object 'x'
{'c': 30, 'e': 50, 'j': 100}
'''


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
a = c1()
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'




#  Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls): #Here we have defined the class method
		cls . x = int(input('Enter  any  number    :  ')) #Here we are reading the input to class
	def  get2(self): #Here we have defined the normal method
		self . y = int(input('Enter  any  number  :  ')) 
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
		Test . x += 1 #Here we are modifying the static variable by 1
		self . y  += 1 #here we are modifying the instance variable by 1
		self . z  += 1 #here we are modifying the instance variable by 1
		self . x  += 1 #self.x = self.x + 1 #here right side we are modifying the static variable and left side we are adding the instance variable x to obj
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t') #Prints the static variable x and instance variables y z x with tab seperated 
# End  of  the  class
Test . get1() #Calling the classmethod get 
a = Test() #Creating the object a for Test class 
b = Test() #Creating the object b for Test class
c = Test() #Creating the object c for Test class
a . get2() #calling the get2 method with obj a
b . get2() ##calling the get2 method with obj b
c . get2() ##calling the get2 method with obj c
a . compute() #calling the compute method with obj a
b . compute() #calling the compute method with obj b
c . compute() #calling the compute method with obj c
a . disp() #calling the disp method with obj a
b . disp() #calling the disp method with obj b
c . disp() #calling the disp method with obj c
'''outputs:
13      21      31      12
13      41      51      13
13      61      71      14
'''


'''
static variable x --> 13

object a -->13  21 31 12

object b -->13  41 51 13

object c -->13  61 71 14
'''




'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n = int(input("Enter number of elements: ")) #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a = []  # List to hold vector elements
		print("Enter", vector.n, "elements:")
		for _ in range(vector.n):
			self.a.append(int(input())) #How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.a = []  # Initialize list to hold result
		for i in range(vector.n):
			self.a.append(x.a[i] + y.a[i])  #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object

a = vector.get1()  #How  to  call  get1()  method
a = vector()
a.get2() #How  to  read  the  list  into  1st  object  'a'
b = vector()
b.get2()	#How  to  read  the  list  into  2nd  object  'b'
c = vector()
c.add(a.b) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print("Resultant vector after addition:")
print(c.a)#How  to  print  the  list  of  3rd   object






'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class c1:
    x = 1
    y = 2
    z = 3

# Get the class dictionary
a = c1.__dict__
print(a)
# Filter static variables (exclude special methods/attributes)
b = {}

for i in a:
    # Exclude environment variables (usually start and end with double underscores)
    if not (i.startswith('__') and i.endswith('__')):
        b[i] = a[i]

# Print result
print("Static variables of class c1:", b)



'''
{'_module': 'main', 'firstlineno': 6, 'x': 1, 'y': 2, 'z': 3, 'static_attributes': (), 'dict': <attribute 'dict' of 'c1' objects>, 'weakref': <attribute 'weakref' of 'c1' objects>, 'doc_': None}
static  variables  of  class  c1 :   {'x': 1, 'y': 2, 'z': 3}
'''



# What  are  k , l ,  x , y , z , m , n , p , q , s ?  (Home  work)
class   c1:
	x = 10  #  What  is  variable  'x'  ---> static variable
	def    m1(self):
		self . y = 20   #  What  is  variable  'y'  ---> instance variable
		z = 30   #  What  is  variable   'z'  ---> local variable
		c1 . m = 40   #  What  is  variable   'm'  ---> static variable
#end of the class
def    f1():
	a = c1()
	a . p = 50   #  What  is   variable  'p'  ---> instance variable
	c1 . q = 60   #  What  is  variable   'q'  ---> static variable
	s = 70   #  What  is  variable   's'  ---> local variable
#end of the function
k = 80   #  What  is  variable 'k'  ---> global variable
c1 . l = 90   #  What  is  variable  'l'  ---> static variable
b = c1()
b . n = 100   #  What  is  variable  'n' ---> instance variable