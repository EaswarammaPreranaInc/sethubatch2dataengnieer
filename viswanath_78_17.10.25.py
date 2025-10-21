#  Multilevel  inheritance  demo  program
class  A:
	def m1(self):
	    print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		super().m1 # print('class   D   method')
		super(D,self).m1  # How  to  call  method  m1()  of  class  C
		C.m1(D()) # How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		super(C,self)  # How  to  call  method  m1()  of  class  B
		 super(B,self) # How  to  call  method  m1()  of  class  A
	    	super(A,self).m1() # error
		super(C) . m1() # error
# End  of  the  class
d = D()
d.m1() # How  to  call  method  m1()  of  class  D

class father:
    def height(self):
        print('Father Height')
class mother:
    def color(self):
        print('Mother Color')
class child(mother, father):
    def qualification(self):
        print('Child Qualification')
# End of the class
c = child()
c.qualification()  # Child Qualification
c.color()  # Mother Color
c.height()  # Father Height
c.m1()  # Error: method m1() is not defined in any class

class uncle:
    def m1(self):
        print('Uncle Method')
class mother:
    def m1(self):
        print('Mother Method')
class father:
    def m1(self):
        print('Father Method')
class child(father, mother, uncle):
    def m1(self):
        print('Child Method')
# end of the class
c = child()
c.m1()  # Child Method

class uncle:
    def m1(self):
        print('Uncle Method')
class mother:
    def m1(self):
        print('Mother Method')
class father:
    def m1(self):
        print('Father Method')
class child(father, mother, uncle):
    pass
# end of the class
c = child()
c.m1()  # Father Method

class uncle:
    def m1(self):
        print('Uncle Method')
class mother:
    def m1(self):
        print('Mother Method')
class father:
    pass
class child(father, mother, uncle):
    pass
# end of the class
c = child()
c.m1()  # Mother Method

class uncle:
    def m1(self):
        print('Uncle Method')
class mother:
    pass
class father:
    pass
class child(father, mother, uncle):
    pass
# end of the class
c = child()
c.m1()  # Uncle Method

class uncle:
    pass
class mother:
    pass
class father:
    pass
class child(father, mother, uncle):
    pass
# end of the class
c = child()
c.m1()  # Error: method m1() not found in child or any parent class

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
		super(child , self).m1() # How  to  call  m1()  method  of  father  class
		super().m1() # How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father , self).m1() # How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother , self) . m1() # How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() # error : 'super' object has no attribute 'm1'
# End of the class
print(child . __mro__)  #(child,father,mother,uncle,object)
c = child() 
c.m1() # How  to  call  m1()  method  of  child  class
print('Bye')
# Output sequence:
# m1 method of child class
# m1 method of Father class
# m1 method of Father class
# m1 method of Mother class
# m1 method of Uncle class
# Bye

class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super().__init__() # How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super().__del__() # How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')

class parent:
    def __init__(self):
        print('parent constructor')
    def __del__(self):
        print('parent destructor')
class child(parent):
    def __init__(self):
        print('child constructor')
    def __del__(self):
        print('child destructor')
# End of the class
c = child()  # child constructor
print('Bye')  # Bye
       # child  destructor
 

class parent:
    def __init__(self):
        print('parent constructor')
    def __del__(self):
        print('parent destructor')
class child(parent):
    pass
# End of the class
c = child()  # parent constructor 
print('Bye')  # Bye
  	       # parent  destructor 

class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2,b2) #How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() # How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x') # Object  x
x . disp() # 10   20   30   40
print('Object  y') # Object  y
y . disp() # 0     0     0      0

class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super().__init__()
		self . y = 20
	def disp(self):
		print(child.x) # How  to  print  static  variable  'x' #100
		print(parent.x) # How  to  print  static  variable  'x'   in  another  way # 100 
		print(super().x) # How  to  print  static  variable  'x'   in  one  more  way # 100
		print(self . x) # How  to  print  variable  'x'  of  object  'c' # 10
		print(self . y) # How  to  print  variable  'y'  of  object  'c' # 20
#end of the class'''
c = child()
c.disp() # How  to  call  disp()  method  of   child  class

class parent:
    x = 10
    def __init__(self):
        self.x = 20
class child(parent):
    def __init__(self):
        self.x = 30
        print(self.x)      # 30
        super().__init__() # call parent constructor, sets self.x = 20
    def disp(self):
        print(self.x)      # 20 (instance variable after parent constructor)
        print(super().x)   # 10 (static variable from parent class)
# End of the class
c = child()  
c.disp()  

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
print(P . mro()) # [P,X,A,Y,B,C,D,obj]
obj = P()
obj . m1()
Print('Bye')
Outputs :
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye

class D:
    def __init__(self):
        super().__init__()
        print('class D constructor')
class E:
    def __init__(self):
        super().__init__()     
        print('class E constructor')
class F:
    def __init__(self):
        super().__init__()
        print('class F constructor')
class B(D, E):
    def __init__(self):
        super().__init__()
        print('class B constructor')
class C(D, E, F):
    def __init__(self):
        super().__init__()
        print('class C constructor')
class A(B, C):
    def __init__(self):
        super().__init__()
        print('class A constructor')
print(A.mro())    
obj = A()
print('Bye')
Outputs :
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye

class c1(c1):
    pass  # Error: parent 'c1' is not defined

class c1:
    def m1(self):
        print('Parent Method')
class c1(c1):
    def m1(self):
        super().m1()
        print('Child Method')
a = c1()
a.m1()
Outputs :
Parent Method
Child Method

class c1(c2):
    pass
class c2(c1):
    pass  # Error: parent 'c2' is not defined

class c2:
    def m1(self):
        print('Parent Method')

class c1(c2):
    def m1(self):
        super().m1()
        print('Child Method')
class c2(c1):
    def m1(self):
        super().m1()
        print('Grand Child Method')
a = c2()
a.m1()
Outputs :
Parent Method
Child Method
Grand Child Method


