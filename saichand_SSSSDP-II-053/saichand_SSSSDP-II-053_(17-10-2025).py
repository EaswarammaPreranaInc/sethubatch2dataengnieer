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
                super().m1()
		c.m1(self)#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  an  object
		B.m1(self)#How  to  call  method  m1()  of  class  B
		A.m1(self)#How  to  call  method  m1()  of  class  A
		super(A , self) . m1()
		super(C) . m1()
# End  of  the  class
D().m1()#How  to  call  method  m1()  of  class  D







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

#Output:
Child Qualification
Mother  Color
Father  Height
Error







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

#Output:
Child  Method








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

#Output:
Father  Method








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

#Output:
Mother  Method







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

#Output:
Uncle  Method








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

#Output:
Error







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
		father.m1(self)#How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(mother,self).m1()#How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super.(uncle,self).m1()#How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()
# End of the class
print(child . __mro__)
#How  to  call  m1()  method  of  child  class
c = child()
c.m1()
print('Bye')








# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		#How  to  call  parent  class  constructor
		#cannot call parent constructor
		print('child   constructor')
	def   __del__(self):
		#How  to  call  parent  class  destructor
		#cannot call parent destructor
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

#Output:
child constructor
Bye
child destructor

 






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

#Output:
parent  constructor
Bye
parent  destructor








# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		#How  to  call  parent  class  constructor  with  a2 , b2
		super() . _init_(a2 , b2)
		self . c = c2
		self . d = d2
	def  disp(self):
		#How  to  call  parent  class  disp()  method
		super().disp()
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()








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
		print(child.x)#How  to  print  static  variable  'x'   in  another  way
		print(super().x)#How  to  print  static  variable  'x'   in  one  more  way
		print(self.x)#How  to  print  variable  'x'  of  object  'c'
		print(self.y)#How  to  print  variable  'y'  of  object  'c'
#end of the class
#How  to  call  disp()  method  of   child  class
c = child()
c.disp()

#Output:
100
100
100
10
20







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

#Output:
30
10







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
#Output:
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

#Output:
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>,
 <class '__main__.B'>, <class '__main__.Y'>, <class '__main__.C'>,
 <class '__main__.D'>, <class 'object'>]
class D method
class C method
class Y method
class B method
class A method
class X method
class P method
Bye








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
print(A . mro())
obj = A()
print('Bye')

#Output:
Error becauseCannot create a consistent method resolution
order (MRO) for bases D, E, F








# Identify  Error
class  c1(c1):	#name c1 is not defined
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
a . m1()

#Output:
Parent  Method
Child  Method







# Identify  Error
class   c1(c2):
	pass
class  c2(c1):	#Name c2 is not defined
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

#Output:
Parent Method
Child Method
Grand Child Method




#DATA STRUCTURES:
'''
1.Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
from prog2 import *
class  sll(linked_list):
    def  concat(a , b):
        if  a.isempty():
            a.first=b.first     # 2nd  linked  list  is  the   result
        else:
            last=a.first
            while last.link!=None:
                last=last.link
            last.link=b.first   # How  to  attach  last  node  of  1st  LL  with  first  node  of  2nd  LL
#  End  of  the  class
a=sll()
a.create()  # How  to  create  1st  LL
b=sll()
b.create()  # How  to  create  2nd  LL
a.concat(b) # How  to  concatenate  the  2  LL's
print('Linked  List  :  ' , end = '')
a.disp()    # How  to  print  final  linked  list








#  Write  a  method  to  copy  a  linked  list

class  sll(linked_list):
    def  copy(a):
            b=sll() # How  to  create  a  local  object  for  2nd  linked  list
            p=a.first
            while p!=None:
                new=node(p.data)
                b.append(new)
                p=p.link  # How  to  copy  each  node  of  1st  LL  to  2nd  LL  until   LL  is  exhausted
            return b  # How  to   return  2nd  linked  list
#  End  of  the  clas
a=sll()
a.create()  # How  to  create  1st  linked  list
b=a.copy()  # How  to  copy  1st  linked  list  to  2nd  linked  list
print('Original  linked   list  :  ' , end = '')
a.disp()  # How  to  print  1st  linked  list
print('Copied  linked   list  :  ' , end = '')
b.disp()  # How  to  print  2nd  linked  list







#  Write  destructor  to  delete  whole  linked  list

class  sll(linked_list):
    def __del__(a):
        while not a.isempty():
            temp=a.first
            a.first=a.first.link
            del temp # How  to  remove  each  node  of  LL  until  LL  is  empty
        print('Linked  list  is  empty')
#  End  of  the  clas
a=sll()
a.create()
a.disp()
del a # How  to  create  linked  list







'''
Write  a  method  to  reverse  linked  list

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
        prev=None
        cur=a.first
        while cur!=None:
            next=cur.link
            cur.link=prev
            prev=cur
            cur=next  # How  to  reverse  each  node  of  linked  list
        a.first=prev  # How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
a=sll()
a.create()  # How  to  create  linked  list
print('Input  Linked  List: ',a.disp())  # How  to  print  linked  list
a.reverse()  # How  to  reverse  linked  list
print('Reverse  Linked  List: ',a.disp())  # How  to  print  reverse  linked  list
