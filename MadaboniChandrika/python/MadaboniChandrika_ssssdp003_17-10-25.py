#1st program
#Multilevel  inheritance  demo  program
class  A:
	def    m1(self):
		print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		print('class   D   method')
		C.m1(self)#How  to  call  method  m1()  of  class  C
		super(D,self).m1()#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		B.m1(self)#How  to  call  method  m1()  of  class  B
		A.m1(self)#How  to  call  method  m1()  of  class  A
		#super(A , self) . m1()#error
		#super(C) . m1() #error due to self is misiing
# End  of  the  class
d=D()
d.m1()#How  to  call  method  m1()  of  class  D

'''
class   D   method
class   C    method
class   C    method
class  B   method
class   A  method

'''

#2nd  program
# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')
class  mother:
        def  color(self):
                print('Mother  Color')
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')
# End  of  the  class
c  =  child()
c . qualification()#child qualification
c . color()#There is no color method in child class so mother parent class is executed i.e mother color
c . height()#There is no color method in child class so father parent class is executed i.e father height
#c . m1()# error:There is no m1 method in child class and parent classes 
'''

Child Qualification
Mother  Color
Father  Height

'''

#3rd  program
#  Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
        def  m1(self):
                print('Child  Method')
#end  of  the  class
c = child()
c . m1()#child method


#4th  program
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
	pass
#end  of  the  class
c = child()
c . m1()#There is no m1 method in child class, parent father class m1 method is executed i.e father method


#5th  program
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1()#There is no m1 method in child class so parent mother class m1 method is executed i.e mother method


#6th  program
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
c . m1()#There is no m1 method in child class so parent uncle class m1 method is executed i.e uncle method


#7th  program
# Find  outputs
class  uncle:
        pass
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child()
#c . m1()#error There is no m1() method in child class and parent class


#8th  program
# Find  outputs
class   father:
	def  m1(self):
		print('m1  method  of  Father  class')
class   mother:
	def  m1(self):
		print('m1  method  of  Mother  class')
class   uncle:
	def  m1(self):
		print('m1  method  of  Uncle  class')
class   child(father , mother , uncle):
	def  m1(self):
		print('m1  method  of  child  class')
		super().m1()#How  to  call  m1()  method  of  father  class
		super(father,self).m1()#How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(mother,self).m1()#How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self)#How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		#super(uncle , self) . m1() error
# End of the class
print(child . __mro__)#returns tuple of classes i.e(child,father,mother,uncle,object)
c=child()
c.m1()#How  to  call  m1()  method  of  child  class
print('Bye')#bye
'''
o/p:
m1  method  of  child  class
m1  method  of  Father  class
m1  method  of  Mother  class
m1  method  of  Uncle  class
m1  method  of  Uncle  class

'''


#9th  program
# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		#How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		#How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()#constructor is executed of child class i.e child constructor
print('Bye')#bye
#child destructor


#10th  program
# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()#parent classs constructor is executed bcz there is no constructor in child class i.e parent constructor
print('Bye')#bye
#parent destructor


#11th  program
# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2,b2)#How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp()#How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)#child class constructor is executed i.e a2=10,b2=20,c2=30,d2=40
y = child()#a2=0,b2=0,c2=0,d2=0
print('Object  x')#object x
x . disp()# 10 20 30 40
print('Object  y')#object y
y . disp()#0 0 0 0


'''
o/p:
Object  x
10      20      30      40
Object  y
0       0       0       0
'''

#12th  program
# Find outputs  (Home  work)
class  parent:
	x = 100#sv
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
		print(parent.x)#How  to  print  static  variable  'x'
		print(super().x)#How  to  print  static  variable  'x'   in  another  way
		print(child.x)#How  to  print  static  variable  'x'   in  one  more  way
		print(self.x)#How  to  print  variable  'x'  of  object  'c'
		print(self.y)#How  to  print  variable  'y'  of  object  'c'
#end of the class
c=child()#constructor is executed
c.disp()#How  to  call  disp()  method  of   child  class

'''
o/p:
100
100
100
10
20
'''

#13th  program
# Find outputs
class    parent:
	a=10#How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self.x=30 #How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  : ',self.x)#How  to  print  variable  'x'
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,  cls.a) #How  to  print  static  variable  'a'
		print('Parent  class  "class"  method  :  ' ,  parent.a)#How  to  print  static  variable  'a'  in  another  way
		#print(self . a)#error self not  there
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,parent.a), # How  to  print  static  variable  'a'
	def   __del__(self):
		print('parent  destructor  :  ' ,  self.x)# How  to  print  variable  'x'
class  child(parent):
	b=20 #How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		super().__init__()#How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40 #How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(self.y)#How  to  print  variable  'y'
	@classmethod
	def   m2(cls):
		parent.m2()#How  to  call  m2()  method  of  parent  class
		super().m2()#How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m2()#error recursion 
		#self . m2()#self is not there in class method 
		print('Child  class  "class"  method')
		print(cls.a)#How  to  print  static  variable  'a'
		print(child.a)#How  to  print  static  variable  'a'  in  another  way
		print(parent.a)#How  to  print  static  variable  'a'  in  one  more  way
		print(super(child,cls).a)#How  to  print  static  variable  'a'  in  last  way
		print(child.b)#How  to  print  static  variable  'b'
		print(cls.b)#How  to  print  static  variable  'b'  in  another  way
	@staticmethod
	def   m3():
		parent.m3()#How  to  call  m3()  method  of  parent  class
		super(child,child).m3()#How  to  call  m3()  method  of  parent  class  in   another  way
		#self . m3()#error there is no self in static method
		#cls . m3()#error
		print('child  class  static  method' , parent.a)#How  to  print  static  variable  'a'
		print(super(child,child).a)#How  to  print  static  variable  'a'  in  another  way
		print(child.b)#How  to  print  static  variable  'b'
	def __del__(self):
		super().__del__()#How  to  call  destructor  of  parent  class
		print('child  destructor' , self.y) # How  to  print  variable  'y'
#end of the class
c=child()
c.m2()#How  to  call  m2()  method  of  child  class
child.m3()#How  to  call  m3()  method  of  child  class
c.m1()#How  to  call  m1()  method  of  child  class

'''

o/p:
Parent  constructor
Child  constructor
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Child  class  "class"  method
10
10
10
10
20
20
Parent  class  static  method  :   10
Parent  class  static  method  :   10
child  class  static  method 10
10
20
Parent  class  instance  method  :  30
Child  class  instance  method
40
parent  destructor  :   30
child  destructor 40
'''

#14th  program
# Find outputs  (Home  work)
class  A:
	def  m1(self):
		super() . m1() #It goes to y.m1()
		print('class A method')
class  B:
	def m1(self):
		super() . m1()#It goes to c.m1()
		print('class B method')
class  C:
	def m1(self):
		super() . m1()#it goes to d.m1()
		print('class C method')
class  D:
	def m1(self):
		#super() . m1()
		print('class D method')#class D method
class  X(A , B):
        def m1(self):
                super() . m1()#it goes to A.m1()
                print('class X method')
class  Y(B , C , D):
        def m1(self):
                super() . m1()#it goes to B.m1()
                print('class Y method')
class  P(X , Y , C):
        def m1(self):
                super() . m1()#this super().m1() goes to x.m1()
                print('class P method')
#end of the class
print(P . mro())#[P,X,Y,B,C,A,D,object]
obj = P()#object p is created
obj . m1()
print('Bye')#Bye
'''
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye
'''

#15th  program
# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()
                print('class D constructor')
class  E:
        def __init__(self):
                super() . __init__()
                print('class E constructor')
class  F:
        def __init__(self):
                super() . __init__()
                print('class F constructor')
class  B(D , E):
        def __init__(self):
                super() . __init__()
                print('class B constructor')
class  C(D , E , F):
        def __init__(self):
                super() . __init__()
                print('class C constructor')
class  A(B , C):
        def __init__(self):
                super() . __init__()
                print('class A constructor')
#end of the class
print(A . mro())#[A,B,C,D,E,F,object]
obj = A()
print('Bye')
'''
o/p:
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye

'''

#16th  program
# Identify  Error
class  c1(c1):#c1 does not exist
	pass


#17th  program
# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()#parent method
        #child method


#18th  program
# Identify  Error
class   c1(c2):#error c2 is does not exist
	pass
class  c2(c1):
	pass


#19th  program
# Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')#parent method
class   c1(c2):
	def  m1(self):
			super() . m1()
			print('Child  Method')
class  c2(c1):
	def  m1(self):
			super() . m1()#goes to c1
			print('Grand  Child  Method')
a = c2()
a . m1()#calling m1() on grandchild class c2

'''
o/p:
parent method
child method 
Grand child method
'''