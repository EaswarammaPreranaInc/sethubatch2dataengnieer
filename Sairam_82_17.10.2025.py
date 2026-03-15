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
		super().m1()    #How  to  call  method  m1()  of  class  C
		super(D,self).m1()  #How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		super(C,self).m1()  #How  to  call  method  m1()  of  class  B
		super(B,self).m1()  #How  to  call  method  m1()  of  class  A
		super(A , self) . m1()  # error as there is no super class for class A
		super(C) . m1() # error super doesnt take 1 argument
# End  of  the  class
d=D()
d.m1()
#How  to  call  method  m1()  of  class  D

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
c  =  child()   # child class object is created
c . qualification() # calling qualification method of child class
c . color() # calls color method of mother class with child object
c . height()# calls height method of father class with child object
c . m1()    # error as there is no m1 method in any classes

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
                print('Child  Method')  # child method is printed as there is same method 
#end  of  the  class
c = child() # creating child class object
c . m1()    # calling child method

# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method') # as there is no m1 in child class father clss m1 is called
class  child(father , mother , uncle):
	pass
#end  of  the  class
c = child() # child class object is created
c . m1()    # calling child class m1 method



# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method') # as there is no m1 in child class and father clss mother m1 is called
class  father:
        pass
class  child(father , mother , uncle):
        pass
#end  of  the  class
c = child() # child class object is created
c . m1()    # calling child class m1 method


# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')  # as there is no m1 in child class father and  mother clss uncle class m1 is called
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass

#end  of  the  class
c = child() # child class object is created
c . m1()    # calling child class m1 method

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
c = child() # child class object is created
c . m1()    # calling child class m1 method error as there is no m1 in either child class or parent classes

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
		super().m1()    #How  to  call  m1()  method  of  father  class
		super(child,self).m1()  #How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father,self).m1() #How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother,self).m1() #How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()  # error according to mro there is no parent for uncle
# End of the class
print(child . __mro__)    #[child, father , mother , uncle, object]
c=child()
c.m1()  #How  to  call  m1()  method  of  child  class
print('Bye')

# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super().__init__()  #How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super().__del__() #How  to  call  parent  class  destructor
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
c = child() # child class object is created and constructor is executed
print('Bye')    # prints bye
#object is deleted destructor is executed of child class

# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')  #  as there is no constructor in child clss parent class constructor is executed
	def   __del__(self):
		print('parent  destructor') #as there is no destructor in child clss parent class destructor is executed
class  child(parent):
	pass
# End of the class
c = child() # child class object is created and constructor is executed 
print('Bye')    # prints bye
# object os deleted destructor is executed

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2 , b2) ##How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp()  #How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  'x'  :	a2=10     b2= 20      c2=30      d2=40

Object  'y'  :a2=0     b2= 0      c2=0      d2=0

'''

# Find outputs  (Home  work)
class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()  # parent class constructor is executed
		self . y = 20
	def disp(self):
		print(parent.x)    #How  to  print  static  variable  'x'
		print(super().x)     #How  to  print  static  variable  'x'   in  another  way
		print(child.x)     #How  to  print  static  variable  'x'   in  one  more  way
		print(self.x)      #How  to  print  variable  'x'  of  object  'c'
		print(self.y)      #How  to  print  variable  'y'  of  object  'c'
#end of the class
c=child()
c.disp()
##How  to  call  disp()  method  of   child  class

# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20       # variable x is replaced with 20
class   child(parent):
	def  __init__(self):
		self . x = 30   # variable x is added to object c with value 30
		print(self . x) # prints 30
		super() . __init__()  # calling parent clss constructor
	def  disp(self):
		print(self . x) # prints 20
		print(super() . x)  # prints static varible 10
# End of the class
c = child() # child class object is created and constrcutor is executed
c . disp()  # calling disp method of child class


'''
static   variable  ---> x=10

Object  'c'  ---> x=30 replaced with 20
'''

# Find outputs
class    parent:
	a=10    #How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self.x=30    #How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,self.x)  #How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' , parent.a)     #How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,  cls.a)#How  to  print  static  variable  'a'  in  another  way)
		print(self . a) #error as self is not an argument of m2
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a) #How  to  print  static  variable  'a')
	def   __del__(self):
		print('parent  destructor  :  ' ,self.x )#  How  to  print  variable  'x')
class  child(parent):
	b=20    ##How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		super().__init__()    #How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40    #How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1()    #How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(self.y)   #How  to  print  variable  'y')
	@classmethod
	def   m2(cls):
		parent.m2() #How  to  call  m2()  method  of  parent  class
		super().m2()    #How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m2()  # recursion as calling same method inside a method
		self . m2() # error as there is no argument self
		print('Child  class  "class"  method')
		print(parent.a) #How  to  print  static  variable  'a')
		print(super().a )    #(How  to  print  static  variable  'a'  in  another  way)
		print(cls.a)   #How  to  print  static  variable  'a'  in  one  more  way)
		print(child.a)  # (How  to  print  static  variable  'a'  in  last  way)
		print(child.b)  #How  to  print  static  variable  'b')
		print(cls.b)    #How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		super().m3()    #How  to  call  m3()  method  of  parent  class
		parent.m3()    #How  to  call  m3()  method  of  parent  class  in   another  way
		self . m3() # error as m3 doesnt has self argument
		cls . m3()# error as m3 doesnt has cls argument
		print('child  class  static  method' ,parent.a) # How  to  print  static  variable  'a')
		print(super().a)    #How  to  print  static  variable  'a'  in  another  way)
		print(child.b)    #How  to  print  static  variable  'b'
	def __del__(self):
		super().__del__()    #How  to  call  destructor  of  parent  class
		print('child  destructor' , self.y) # How  to  print  variable  'y')
#end of the class
child.m2()  #How  to  call  m2()  method  of  child  class
child.m3()  #How  to  call  m3()  method  of  child  class
c=child()
c.m1()  #How  to  call  m1()  method  of  child  class


'''
Static   variables  ---> a=10,b=20

object   'c'  --->x=30,y=40
'''

