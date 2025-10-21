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
		c.m1(self)#How  to  call  method  m1()  of  class  C
		super().m1()#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		B.m1(self)#How  to  call  method  m1()  of  class  B
		A.m1(self)#How  to  call  method  m1()  of  class  A
		super(A , self) . m1()
		super(C) . m1()
# End  of  the  class
d = D()
d.m1()#How  to  call  method  m1()  of  class  D



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
c . qualification()#Child qualification
c . color()#Mother color
c . height()#Father heigth
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
c = child()
c . m1()#Child method


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
c . m1()#Father method



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
c . m1()#Uncle method


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
		father.m1(self)#How  to  call  m1()  method  of  father  class
		super().m1()#How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		mother.m1(self)#How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self)#How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()
# End of the class
print(child . __mro__)
c=child()
c.m1()#How  to  call  m1()  method  of  child  class
print('Bye')


# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super().__init__()#How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super.__del__()#How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
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

# outputs:
# child constructor
# Bye 
# child destructor


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
print('Bye')

# output:
# parent constructor
# Bye 
# parent destructor


# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super.__init__(a2,b2)#How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp()#How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

# '''
# Object  'x'  :10,20,30,40

# Object  'y'  :0,0,0,0
# '''


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
		print(parent.x)#How  to  print  static  variable  'x'
		print(self.__class__.x)#How  to  print  static  variable  'x'   in  another  way
		print(child.x)#How  to  print  static  variable  'x'   in  one  more  way
		print(self.x)#How  to  print  variable  'x'  of  object  'c'
		print(self.y)#How  to  print  variable  'y'  of  object  'c'
#end of the class
c=child()
c.disp()#How  to  call  disp()  method  of   child  class
	

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
c . disp()

# outputs:
# 30
# 20
# 10

'''
static   variable  --->

Object  'c'  --->
'''


# Find outputs
class    parent:
	a=10#How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self.x=30#How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,  cls.a)
		print('Parent  class  "class"  method  :  ' ,  parent.a)
		#print(self . a)#error
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' , parent.a )
	def   __del__(self):
		print('parent  destructor  :  ' ,  self.x)
class  child(parent):
	b=20#How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		super.__init__()#How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40#How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(self.y)
	@classmethod
	def   m2(cls):
		super(child,cls).m2()#How  to  call  m2()  method  of  parent  class
		parent.m2()#How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m2()
		#self . m2()#error
		print('Child  class  "class"  method')
		print(cls.a)
		print(parent.a)
		print(child.a)
		print(cls.__bases__[0].a)
		print(child.b)
		print(cls.b)
	@staticmethod
	def   m3():
		parent.m3()#How  to  call  m3()  method  of  parent  class
		super(child,child).m3()#How  to  call  m3()  method  of  parent  class  in   another  way
		#self . m3()#error
		#cls . m3()#error
		print('child  class  static  method' , parent.a)
		print(child.a)
		print(child.b)
	def __del__(self):
		super().__del__()#How  to  call  destructor  of  parent  class
		print('child  destructor' ,  self.y)
#end of the class
child.m2()#How  to  call  m2()  method  of  child  class
child.m3()#How  to  call  m3()  method  of  child  class
c=child()
c.m1()#How  to  call  m1()  method  of  child  class



