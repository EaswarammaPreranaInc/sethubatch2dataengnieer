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
		super().m1()  #  How  to  call  method  m1()  of  class  C
		super(D,self).m1()  #How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		super(C,self).m1()  #  How  to  call  method  m1()  of  class  B
		super(B,self).m1()  #  How  to  call  method  m1()  of  class  A
		#super(A , self) . m1()  #  Error due to class a not have parent class
		#super(C) . m1()  #  Error
# End  of  the  class
f=D()
f.m1()  #  How  to  call  method  m1()  of  class  D



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
c . qualification()  #  Child Quyalification
c . color()  #  Mother  Color
c . height()  #  Father  Height
c . m1()  #  Error due to no m1 method in Child class



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
c . m1()  #  Child  Method



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
c . m1()  #  Father  Method



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
c . m1()  #  Error due to m1 method in class child



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
c . m1()  #  Uncle  Method



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
c . m1()  #  Error due to no m1 method in class child



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
		father().m1()  #  How  to  call  m1()  method  of  father  class
		super(child,self)  #  How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		mother.m1(self)  #  How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self)  #  How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		#super(uncle , self) . m1(self)  #  Error Due to uncle not have parent class
# End of the class
print(child . __mro__)
cls=child()
cls.m1()  #  How  to  call  m1()  method  of  child  class
print('Bye')




# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super(child,self).__init__()  #  How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		parent.__del__(self)  #  How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')



# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		print('child   constructor')  #  child  constructor
	def   __del__(self):
		print('child  destructor')  #  child  destructor
# End of the class
c = child()
print('Bye')  #  Bye


# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()  #  parent  constructor
print('Bye')
# destructor is executer




# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		parent().__init__(a2,b2)  #  How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2  #  30
		self . d = d2  # 40
	def  disp(self):
		super().disp(self)  #  How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')  #  Object  x
x . disp()
print('Object  y')  #  Object  y
y . disp()



