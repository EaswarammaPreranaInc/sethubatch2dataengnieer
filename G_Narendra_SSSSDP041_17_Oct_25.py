# Multilevel inheritance demo program
class A:
    def m1(self):
        print('class A method')
class B(A):
    def m1(self):
        print('class B method')
class C(B):
    def m1(self):
        print('class C method')
class D(C):
    def m1(self):
        print('class D method')
        # How to call method m1() of class C
        super().m1() 
        C.m1(self)
        
        # How to call method m1() of class C in another way without creating an object
        C.m1(self)
        
        # How to call method m1() of class B
        super(C, self).m1() 
        B.m1(self)
        
        # How to call method m1() of class A
        super(B, self).m1() 
        A.m1(self)
        
        super(A, self).m1() 
        C.m1(self) 
        super(C).m1()  # Incorrect usage, needs an instance as second argument
# End of the class

# How to call method m1() of class D
d = D()
d.m1()
# OR D().m1()
# OR D.m1(d) 
# Outputs when calling m1() on an instance of D:
# class D method

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
c . qualification()
c . color()
c . height()
c . m1()
'''
outputs  :
Child  Qualification
Mother  Color
Father  Height
Error
'''


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
c . m1()
'''
outputs  :
Child  Method
'''


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
c . m1()
'''
outputs  :
Father  Method
'''

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
c . m1()
'''
outputs  :
Mother  Method
'''
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
c . m1()
'''
outputs  :
Uncle  Method
'''


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
c . m1()
'''
outputs  :
Error
'''


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
		#How  to  call  m1()  method  of  father  class
		super() . m1()
		#How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		father . m1(self)
		#How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother , self) . m1()
        #How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()
# End of the class
print(child . _mro_)
#How  to  call  m1()  method  of  child  class
c = child()
c . m1()
print('Bye')


 # Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		#How  to  call  parent  class  constructor
		#can not call parent constructor
		print('child   constructor')
	def   _del_(self):
		#How  to  call  parent  class  destructor
		'''can not call parent destructor'''
		print('child   destructor')
# End of the class
c = child()
print('Bye')


# Find  outputs  (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		print('child   constructor')
	def   _del_(self):
		print('child  destructor')
# End of the class
c = child()
print('Bye')


# Find  outputs  (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')
'''
outputs  :
parent  constructor
Bye 
parent  destructor
'''


 # Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		#How  to  call  parent  class  constructor  with  a2 , b2
		super() . _init_(a2 , b2)
		self . c = c2
		self . d = d2
	def  disp(self):
		#How  to  call  parent  class  disp()  method
		super() . disp()
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  'x'  :  10	20	30	40
Object  'y'  :  0	0	0	0
'''


# Find outputs  (Home  work)
class  parent:
	x = 100
	def   _init_(self):
		self . x = 10
class   child(parent):
	def   _init_(self):
		super() . _init_()
		self . y = 20
	def disp(self):
		#How  to  print  static  variable  'x'
		print(parent . x)
        #How  to  print  static  variable  'x'   in  another  way
		print(self . __class__ . x)
        #How  to  print  static  variable  'x'   in  one  more  way
		print(super() . x)
		#How  to  print  variable  'x'  of  object  'c'
		print(self . x)
		#How  to  print  variable  'y'  of  object  'c'
		print(self . y)
#end of the class
#How  to  call  disp()  method  of   child  class
c = child()
c . disp()
'''
100
100
100
10
20  
'''

# Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x)
		super() . _init_()
	def  disp(self):
		print(self . x)
		print(super() . x)
# End of the class
c = child()
c . disp()
'''
30
10
'''

'''
static   variable  ---> 

Object  'c'  --->
'''




 # Find outputs
class    parent:
	#How  to  add  static  variable  'a'  to  parent  class  with  value  10
	a =  10
	def     _init_(self):
		print('Parent  constructor')
		#How  to  add  instance  variable  'x'  with  value  30
		self . x  =  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)#How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		#How  to  print  static  variable  'a'
		print('Parent  class  "class"  method  :  ' ,  parent . a)
		#How  to  print  static  variable  'a'  in  another  way)
		print('Parent  class  "class"  method  :  ' ,  cls . a)
		print(self . a)
	@staticmethod
	def   m3():
		# How  to  print  static  variable  'a')
		print('Parent  class  static  method  :  ' ,  parent . a)
	def   _del_(self):
		# How  to  print  variable  'x')
		print('Parent  destructor  :  ' ,  self . x)
class  child(parent):
	#How  to  add  static  variable  'b'  with  value  20
	b = 20
	def   _init_(self):
		#How  to  call  parent  class  constructor
		super() . _init_()
		print('Child  constructor')
		#How  to  add  instance  variable  'y'  with  value  40
		self . y  =  40
	def   m1(self):
		#How  to  call  m1()  method  of  parent  class
		super() . m1()
		print('Child  class  instance  method')
		#print(How  to  print  variable  'y')
		print('Child  class  instance  method  :  ' ,  self . y)
	@classmethod
	def   m2(cls):
		#How  to  call  m2()  method  of  parent  class
		super() . m2()
		#How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		parent . m2()
		cls . m2()
		self . m2()
		print('Child  class  "class"  method')
		#How  to  print  static  variable  'a')
		print(cls. a)
		#print(How  to  print  static  variable  'a'  in  another  way)
		print(self . a)
        #print(How  to  print  static  variable  'a'  in  one  more  way)
		print(parent . a)
		#print(How  to  print  static  variable  'a'  in  last  way)
		print(self . __class__ . a)
		#print(How  to  print  static  variable  'b')
		print(cls . b)
		#print(How  to  print  static  variable  'b'  in  another  way)
		print(self . b)
	@staticmethod
	def   m3():
		#How  to  call  m3()  method  of  parent  class
		parent . m3()
		#How  to  call  m3()  method  of  parent  class  in   another  way  without  creating  an  object		
		self . m3()
		cls . m3()
		#print('child  class  static  method' , How  to  print  static  variable  'a')
		print('child  class  static  method' , parent . a)
		#print(How  to  print  static  variable  'a'  in  another  way)
		print(self . a)
		#print(How  to  print  static  variable  'b'
		print(self . __class__ . b)
	def _del_(self):
		#How  to  call  destructor  of  parent  class
		super() . _del_()
		print('child  destructor' ,  How  to  print  variable  'y')
#end of the class
#How  to  call  m2()  method  of  child  class
c = child()
c . m2()
#How  to  call  m3()  method  of  child  class
c . m3()
#How  to  call  m1()  method  of  child  class
c . m1()
'''
o/p:
Parent  constructor
Child  constructor
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Child  class  "class"  method
10
10
10
10
20
Parent  class  static  method  :   10
Parent  class  static  method  :   10
child  class  static  method 10
10
20
m1  method  of  Father  class
Parent  class  instance  method  :   20
Child  class  instance  method
Child  class  instance  method  :   40
Parent  destructor  :   20
child  destructor  :   40
'''

# Find outputs  (Home  work)
class  A:
	def  m1(self):
		super() . m1()
		print('class A method')
class  B:
	def m1(self):
		super() . m1()
		print('class B method')
class  C:
	def m1(self):
		super() . m1()
		print('class C method')
class  D:
	def m1(self):
		#super() . m1()
		print('class D method')
class  X(A , B):
        def m1(self):
                super() . m1()
                print('class X method')
class  Y(B , C , D):
        def m1(self):
                super() . m1()
                print('class Y method')
class  P(X , Y , C):
        def m1(self):
                super() . m1()
                print('class P method')
#end of the class
print(P . mro())
obj = P()
obj . m1()
print('Bye')
'''
outputs  :
[class P, class X, class A, class Y, class B, class C, class D, class object]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye
'''


# Find  outputs  (Home  work)
class  D:
        def _init_(self):
                super() . _init_()
                print('class D constructor')
class  E:
        def _init_(self):
                super() . _init_()
                print('class E constructor')
class  F:
        def _init_(self):
                super() . _init_()
                print('class F constructor')
class  B(D , E):
        def _init_(self):
                super() . _init_()
                print('class B constructor')
class  C(D , E , F):
        def _init_(self):
                super() . _init_()
                print('class C constructor')
class  A(B , C):
        def _init_(self):
                super() . _init_()
                print('class A constructor')
#end of the class
print(A . mro())
obj = A()
print('Bye')
'''
outputs  :
[class A, class B, class D, class C, class E, class F, class object]
class D constructor
'''
# Identify  Error
class  c1(c1):
	pass
'''
outputs  :
Error
'''


# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()

'''outputs  :   
Parent  Method
Child  Method
'''


 # Identify  Error
class   c1(c2):
	pass
class  c2(c1):
	pass
'''
outputs  :  Error
'''


 # Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')
class   c1(c2):
	def  m1(self):
			super() . m1()
			print('Child  Method')
class  c2(c1):
	def  m1(self):
			super() . m1()
			print('Grand  Child  Method')
a = c2()
a . m1()

'''outputs  :
Parent  Method
Child  Method
Grand  Child  Method
'''