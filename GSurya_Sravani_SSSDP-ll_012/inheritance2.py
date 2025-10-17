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
c  =  child()#
c . qualification()#Child Qualification
c . color()#Mother  Color
c . height()#Father  Height
c . m1()#error


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
c = child()#
c . m1()#Child  Method


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
c . m1()#Father  Method


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
c . m1()#Mother  Method


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
c . m1()#Uncle  Method

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
c . m1()#error


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
		c= child()
Super().m1()#How  to  call  m1()  method  of  father  class
		#super(child,self) #How  to  call  m1()  method  of  father  #class  in  another  way  without  creating  an  object
Super(child ,self)#		How  to  call  m1()  method      of  mother  class   without  creating  an  object
Super(father,self).m1()#		How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(mother , self) . m1()# error
# End of the class
print(child . __mro__)#father,mother,uncle,object
C .m1()How  to  call  m1()  method  of  child  class
print('Bye')


# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		Super.m1() #How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		Super().__del__ #How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
'parent  constructor'
'child   constructor
Parent   destructor
child   destructor
print('Bye')



# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		print('child   constructor')
	def   __del__(self):
		print('child  destructor')
# End of the class
c = child()
print('Bye')

parent  constructor'
'child   constructor
Parent   destructor
child   destructor

# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
parent  constructor'
Parent   destructor
print('Bye')

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
Super().__init__()		How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		Super().disp() #How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)#
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()
10	20	30	40
0	0	0	0

# Find outputs  (Home  work)
class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
		Parent.x #How  to  print  static  variable  'x'
		Super().x #How  to  print  static  variable  'x'   in  another  way
		Self.x #How  to  print  static  variable  'x'   in  one  more  way
	Child.x #	How  to  print  variable  'x'  of  object  'c'
	Self.y #	How  to  print  variable  'y'  of  object  'c'
#end of the class
C= child() #
C disp() #How  to  call  disp()  method  of   child  class


# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20
class   child(parent):
	def  __init__(self):
		self . x = 30
		print(self . x)
		super() . __init__()
	def  disp(self):
		print(self . x)
		print(super() . x)
# End of the class
c = child()
30
30
20
c . disp()



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
print(P . mro())#x,y,c,object
obj = P()#
obj . m1()#
Error
print('Bye')




# Identify  Error
class  c1(c1):
	pass# no class c1


# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()#
Parent method
Child method 


# Identify  Error
class   c1(c2):
	pass# child class can't be inherited 
class  c2(c1):
	pass# valid 


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
a . m1()#parent method
Grand  Child  Method