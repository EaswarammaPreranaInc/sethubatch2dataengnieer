#  Multilevel  inheritance  demo  program
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
		a=C() 
        a.m1()#How  to  call  method  m1()  of  class  C
		super().m1() #How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		super(C,self).m1() #How  to  call  method  m1()  of  class  B
		super(B,self).m1()#How  to  call  method  m1()  of  class  A
		super(A , self) . m1() #Error
		super(C) . m1() #Error
# End  of  the  class
d=D()
d.m1() #How  to  call  method  m1()  of  class  D

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
c . qualification() #Child Qualification
c . color() #Mother  Color
c . height() #Father  Height
c.m1() #Error


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
c.m1() #Child  Method

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
c.m1() #Father  Method

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
c.m1() #Mother  Method

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
c.m1() #Uncle  Method

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
c.m1() #Error


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
		f=father() 
        f.m1() #How  to  call  m1()  method  of  father  class
		super().m1() #How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father,self).m1() #How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother,self).m1() #How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() #Error
# End of the class
print(child . _mro_) #[child,father,mother,uncle,object]
c=child()
c.m1() #How  to  call  m1()  method  of  child  class
print('Bye')

# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		super()._init_ #How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		super()._del_ #How  to  call  parent  class  destructor
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
c = child() #child   constructor #parent  constructor
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
c = child() #parent  constructor
print('Bye')

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super()._init_(a2,b2) #How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() #How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  'x'  : a:10,b:20,c:30,d:40

Object 'y' : a:0,b:0,c:0,d:0

Object  x
10  20  30  40
Object  x
0   0   0   0
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
		print(parent.x) #How  to  print  static  variable  'x'
		print(super().x) #How  to  print  static  variable  'x'   in  another  way
		print(child.x) #How  to  print  static  variable  'x'   in  one  more  way
		print(self.x)#How  to  print  variable  'x'  of  object  'c'
		print(self.y) #How  to  print  variable  'y'  of  object  'c'
#end of the class
c=child()
c.disp() #How  to  call  disp()  method  of child class

# Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x) #30
		super() . _init_()
	def  disp(self):
		print(self . x) #20
		print(super() . x) #10
# End of the class
c = child()
c . disp()


'''
static   variable  --->x:10

Object  'c'  --->x:20
'''

# Find outputs
class    parent:
	a=10 #How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		self.x=30 #How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)#How  to  print  variable  'x'
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,  parent.a)#How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,  cls.a) #How  to  print  static  variable  'a'  in  another  way)
		print(self . a) #Error
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a) #How  to  print  static  variable  'a')
	def   _del_(self):
		print('parent  destructor  :  ' ,  self.x)#How  to  print  variable  'x')
class  child(parent):
	b=20 #How  to  add  static  variable  'b'  with  value  20
	def   _init_(self):
		super()._init_()#How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40 #How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(self.y) #How  to  print  variable  'y')
	@classmethod
	def   m2(cls):
		parent.m2()#How  to  call  m2()  method  of  parent  class
		super().m2() #How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m2() #Infinite Recursion
		self . m2() #Error
		print('Child  class  "class"  method')
		print(parent.a) #How  to  print  static  variable  'a')
		print(super().a)#How  to  print  static  variable  'a'  in  another  way)
		print(cls.a)#How  to  print  static  variable  'a'  in  one  more  way)
		print(child.a) #How  to  print  static  variable  'a'  in  last  way)
		print(child.b) #How  to  print  static  variable  'b')
		print(cls.b) #How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		parent.m3() #How  to  call  m3()  method  of  parent  class
		child.m3() #How  to  call  m3()  method  of  parent  class  in   another  way
		self . m3() #Error
		cls . m3() #Error
		print('child  class  static  method' , parent.a)#How  to  print  static  variable  'a')
		print(child.a) #How  to  print  static  variable  'a'  in  another  way)
		print(child.b) #How  to  print  static  variable  'b'
	def _del_(self):
		super()._del_() #How  to  call  destructor  of  parent  class
		print('child  destructor' ,  self.y) #How  to  print  variable  'y')
#end of the class
child.m2() #How  to  call  m2()  method  of  child  class
child.m3() #How  to  call  m3()  method  of  child  class
c=child()
c.m1() #How  to  call  m1()  method  of  child  class


'''
Static   variables  --->a:10,b:20

object   'c'  --->x:30,y:40
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
print(P . mro()) #[P,X,A,Y,B,C,D,Object]
obj = P()
obj . m1()
print('Bye')
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
print(A . mro()) #[A,B,C,D,E,F,Object]
obj = A() 
print('Bye')
'''
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye
'''

# Identify  Error
class  c1(c1): #there is no another c1 class to inherit
	pass

# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1() 
a . m1() #Parent  Method #Child  Method

# Identify  Error
class   c1(c2): #Error due to c2 is not defined yet
	pass
class  c2(c1):
	pass

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
'''
Parent  Method
Child  Method
Grand  Child  Method
'''