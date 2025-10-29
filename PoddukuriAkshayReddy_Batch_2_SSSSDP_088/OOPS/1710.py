
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
		How  to  call  method  m1()  of  class  C
		How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		How  to  call  method  m1()  of  class  B
		How  to  call  method  m1()  of  class  A
		super(A , self) . m1()
		super(C) . m1()
# End  of  the  class
# How  to  call  method  m1()  of  class  D




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
		super(child,self.m1()) # How  to  call  m1()  method  of  father  class
		super().m1() # How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father,self).m1() # How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother,self).m1() # How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()
# End of the class
print(child . _mro_)
# How  to  call  m1()  method  of  child  class
print('Bye')




# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		super.__init__() # How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		super.__del__() # How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child() # parent constructor and child constructor bye
print('Bye') 
# parent destructor and child destructor



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
c = child()  # child   constructor
print('Bye') # Bye
# child   destructor
    
    
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

    
    
# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2,b2) # How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() # How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  'x'  :

Object  'y'  :
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
		print(parent.x) # How  to  print  static  variable  'x'
		print(super().x) # How  to  print  static  variable  'x'   in  another  way
		print(child.x) # How  to  print  static  variable  'x'   in  one  more  way
		print(self.x) # How  to  print  variable  'x'  of  object  'c'
		print(self.y) #How  to  print  variable  'y'  of  object  'c'
#end of the class
c = child()
c.disp() # How  to  call  disp()  method  of   child  class




# Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20 
class   child(parent):
	def  _init_(self):
		self . x = 30 
		print(self . x) # 30
		super() . _init_()
	def  disp(self):
		print(self . x) # 20
		print(super() . x) # 10
# End of the class
c = child() # 
c . disp()


'''
static   variable  --->

Object  'c'  --->
'''



# Find outputs
class    parent:
	a = 10 # How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		self.x = 30 # How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ', self.x )  #  How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,cls.a) #   How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,parent.a) #  How  to  print  static  variable  'a'  in  another  way)
		print(self . a) # Error : no sdelf
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,parent.a) #   How  to  print  static  variable  'a')
	def   _del_(self):
		print('parent  destructor  :  ' ,self.x) #   How  to  print  variable  'x')
class  child(parent):
	b = 20 # How  to  add  static  variable  'b'  with  value  20
	def   _init_(self):
		super.__init__() # How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y = 40 # How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() # How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(self.y ) # How  to  print  variable  'y')
	@classmethod
	def   m2(cls):
		parent.m2() # How  to  call  m2()  method  of  parent  class
		super().m2() # How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m2()
		self . m2()
		print('Child  class  "class"  method')
		print(parent.a) # How  to  print  static  variable  'a')
		print(super().a) # How  to  print  static  variable  'a'  in  another  way)
		print(child.a) # How  to  print  static  variable  'a'  in  one  more  way)
		print(super(child,child).a) # )How  to  print  static  variable  'a'  in  last  way)
		print(child.b) # How  to  print  static  variable  'b')
		print(cls.b) # How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		parent.m3() # How  to  call  m3()  method  of  parent  class
		super(child,child()).m3()  # How  to  call  m3()  method  of  parent  class  in   another  way
        super().m3() # Error 0-args
		self . m3()
		cls . m3()
		print('child  class  static  method' ,parent.a) # How  to  print  static  variable  'a')
		print(child.a) # How  to  print  static  variable  'a'  in  another  way)
		print(child.b) # How  to  print  static  variable  'b'
	def _del_(self):
		super.__del__() # How  to  call  destructor  of  parent  class
		print('child  destructor' ,self.y ) #   How  to  print  variable  'y')
#end of the class
child.m2() # How  to  call  m2()  method  of  child  class
child.m3() # How  to  call  m3()  method  of  child  class
c = child()
c.m1() # How  to  call  m1()  method  of  child  class
# object is lost just before it destructor is executed


# static method can use super keyword if  it has 2 arguments , cannot with 0 arguments 
'''
Static   variables  --->

object   'c'  --->
'''

# a group of classes starting from same class follwed by parent classess until object class

# Write  a  funciton  to  concatenate  two  linked  lists

# How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list

class  sll(linked_list):
	def  concat(a , b):
		if  first  linked  list  is  empty:
			2nd  linked  list  is  the   result
		else:
			How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
#  End  of  the  class
How  to  create  1st  LL
How  to  create  2nd  LL
How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
How  to  print  final  linked  list




#  Write  a  method  to  copy  a  linked  list
class  sll(linked_list):
	def  copy(a):
			How  to  create  a  local  object  for  2nd  linked  list
			How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
			How  to   return  2nd  linked  list
#  End  of  the  clas
How  to  create  1st  linked  list
How  to  copy  1st  linked  list  to  2nd  linked  list
print('Original  linked   list  :  ' , end = '')
How  to  print  1st  linked  list
print('Copied  linked   list  :  ' , end = '')
How  to  print  2nd  linked  list
[17-10-2025 13:32] SRINIVAS Sir SSSSDP: #  Write  destructor  to  delete  whole  linked  list
class  sll(linked_list):
	def    _del_(a):
			How  to  remove  each  node  of  LL  until  LL  is  empty
			print('Linked  list  is  empty')
#  End  of  the  clas
How  to  create  linked  list



'''
# Write  a  method  to  reverse  linked  list

1) How  to  reverse  the  linked  list ?  ---> Modify  4th  node  link  to  3rd  node,
															        modify  3rd  node  link  to  2nd  node,
															        modify  2nd  node  link  to  1st  node,
															        modify  1st  node  link  to  NULL  and
															        modify  first  pointer  to  last  node

2) How  many  references  are  needed  to  reverse  a  linked  list  ?  ---> Three  i.e.  prev , cur , next

3) Where  does  ref  cur   points  to  (in  general) ?  ---> Current  node  i.e.  ith  node
    Where  does  ref  prev   points  to ?  ---> Previous  node  i.e.  (i - 1)th  node
    Where  does  ref  next  points  to ?  ---> Next  node  i.e.  (i + 1)th  node
'''
class  sll(linked_list):
		def  reverse(a):
				How  to  reverse  each  node  of  linked  list
				How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
How  to  create  linked  list
print('Input  Linked  List')
How  to  print  linked  list
How  to  reverse  linked  list
print('Reverse  Linked  List')
How  to  print  reverse  linked  list




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
		# super() . m1() # Error
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
print(P . mro()) # [P,X,A,Y,B,C,D] 
obj = P()
obj . m1()
print('Bye')





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


# Identify  Error
class  c1(c1):
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
a . m1() # Parent Method and Child Method




# Identify  Error
class   c1(c2):
	pass
class  c2(c1):
	pass # Recursion error


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
a . m1() #  parent Method , Child Method and grand child Method