: #  Multilevel  inheritance  demo  program
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
        # How to call m1() of class C?
        C.m1(self)

        # Another way to call m1() of class C without creating an object
        super(D, self).m1()   # or simply super().m1() when inside D

        # How to call m1() of class B?
        B.m1(self)

        # How to call m1() of class A?
        A.m1(self)

#####################
class D method
class C method
class C method
class B method
class A method



: # Find  outputs  (Home  work)
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

#############################
Child Qualification
Mother Color
Father Height
AttributeError: 'child' object has no attribute 'm1'



: #  Find  outputs
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
###############
Child Method




: # Find  outputs
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
####################
Father Method



: # Find  outputs
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
##################
Mother Method




: # Find  outputs
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
#######################
Uncle Method



: # Find  outputs
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
####################
AttributeError: 'child' object has no attribute 'm1'



: # Find  outputs
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
		How  to  call  m1()  method  of  father  class
		How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  mother  class   without  creating  an  object
		How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1()
# End of the class
print(child . _mro_)
How  to  call  m1()  method  of  child  class
print('Bye')
########################
(<class '__main__.child'>, <class '__main__.father'>, <class '__main__.mother'>, <class '__main__.uncle'>, <class 'object'>)

m1 method of child class
m1 method of Father class
m1 method of Father class
m1 method of Mother class
m1 method of Uncle class




: # Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')

##################
parent constructor
child constructor
Bye
child destructor
parent destructor



: # Find  outputs  (Home  work)
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
####################
child constructor
Bye
child destructor



: # Find  outputs  (Home  work)
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
##################
parent constructor
Bye
parent destructor




: # Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

'''
Object  'x'  :10 20 30 40

Object  'y'  :0   0  0  0
'''




: # Find outputs  (Home  work)

class parent:
    x = 100  # static variable

    def __init__(self):
        self.x = 10  # instance variable

class child(parent):
    def __init__(self):
        super().__init__()
        self.y = 20

    def disp(self):
        # How to print static variable 'x'
        print(parent.x)

        # How to print static variable 'x' in another way
        print(self.__class__.x)

        # How to print static variable 'x' in one more way
        print(child.x)

        # How to print variable 'x' of object 'c'
        print(self.x)

        # How to print variable 'y' of object 'c'
        print(self.y)

# End of the class

# How to call disp() method of child class
c = child()
c.disp()

##############################
100
100
100
10
20







: # Find  outputs
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
static   variable  ---> 10

Object  'c'  --->20  30
''
##################
30
20
10



# Find outputs
class    parent:
	How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,  How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,  How  to  print  static  variable  'a'  in  another  way)
		print(self . a)
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  How  to  print  static  variable  'a')
	def   _del_(self):
		print('parent  destructor  :  ' ,  How  to  print  variable  'x')
class  child(parent):
	How  to  add  static  variable  'b'  with  value  20
	def   _init_(self):
		How  to  call  parent  class  constructor
		print('Child  constructor')
		How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method')
		print(How  to  print  variable  'y')
	@classmethod
	def   m2(cls):
		How  to  call  m2()  method  of  parent  class
		How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m2()
		self . m2()
		print('Child  class  "class"  method')
		print(How  to  print  static  variable  'a')
		print(How  to  print  static  variable  'a'  in  another  way)
		print(How  to  print  static  variable  'a'  in  one  more  way)
		print(How  to  print  static  variable  'a'  in  last  way)
		print(How  to  print  static  variable  'b')
		print(How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		How  to  call  m3()  method  of  parent  class
		How  to  call  m3()  method  of  parent  class  in   another  way
		self . m3()
		cls . m3()
		print('child  class  static  method' , How  to  print  static  variable  'a')
		print(How  to  print  static  variable  'a'  in  another  way)
		print(How  to  print  static  variable  'b'
	def _del_(self):
		How  to  call  destructor  of  parent  class
		print('child  destructor' ,  How  to  print  variable  'y')
#end of the class
How  to  call  m2()  method  of  child  class
How  to  call  m3()  method  of  child  class
How  to  call  m1()  method  of  child  class

$$$$$$$$$$$$$$$$$$
'''
Static   variables  --->

object   'c'  --->

class parent:
    a = 10  # static variable 'a'

    def __init__(self):
        print('Parent constructor')
        self.x = 30  # instance variable 'x'

    def m1(self):
        print('Parent class instance method :', self.x)

    @classmethod
    def m2(cls):
        print('Parent class "class" method :', cls.a)
        print('Parent class "class" method :', parent.a)
        # print(self.a)  invalid in classmethod (no self)

    @staticmethod
    def m3():
        print('Parent class static method :', parent.a)

    def __del__(self):
        print('Parent destructor :', self.x)


class child(parent):
    b = 20  # static variable 'b'

    def __init__(self):
        super().__init__()  # call parent constructor
        print('Child constructor')
        self.y = 40  # instance variable 'y'

    def m1(self):
        super().m1()  # call parent m1()
        print('Child class instance method')
        print(self.y)

    @classmethod
    def m2(cls):
        super(child, cls).m2()  # call parent class method (one way)
        parent.m2()             # another way without object
        print('Child class "class" method')
        print(parent.a)
        print(cls.a)
        print(child.a)
        print(super(child, cls).a)
        print(cls.b)
        print(child.b)

    @staticmethod
    def m3():
        parent.m3()  # call parent static method (one way)
        child.m3()   # would recurse infinitely if not careful
        # So we must be careful; instead call parent.m3() twice
        print('Child class static method :', parent.a)
        print(parent.a)
        print(child.b)

    def __del__(self):
        super().__del__()  # call parent destructor
        print('Child destructor :', self.y)


# --- How to call methods ---
c = child()        # calls constructors
c.m1()             # instance method
child.m2()         # class method
child.m3()         # static method


 
#################################
Parent constructor
Child constructor
Parent class instance method : 30
Child class instance method
40
Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Child class "class" method
10
10
10
10
20
20
Parent class static method : 10
Parent class static method : 10
Child class static method : 10
10
20
Child destructor : 40
Parent destructor : 30





: '''
Write  a  funciton  to  concatenate  two  linked  lists

How  to  concatenate  two  linked list's ?  ---> Modify  last  node  link  of  1st  linked list  to  first  node  of  2nd  linked list
'''
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

#################################
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Class for operations on SLL
class sll(LinkedList):
    def concat(self, other):
        # if first list is empty
        if self.head is None:
            self.head = other.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            # attach last node of first LL with head of 2nd LL
            temp.next = other.head

# ---- Main section ----
# create 1st linked list
a = sll()
a.insert_last(10)
a.insert_last(20)
a.insert_last(30)

# create 2nd linked list
b = sll()
b.insert_last(40)
b.insert_last(50)

# concatenate
a.concat(b)

print('Linked List : ', end='')
a.display()
#######################
Linked List : 10 20 30 40 50





: #  Write  a  method  to  copy  a  linked  list
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
############################
class sll(LinkedList):
    def copy(self):
        newlist = sll()  # create 2nd linked list
        temp = self.head
        while temp:
            newlist.insert_last(temp.data)
            temp = temp.next
        return newlist

# ---- Main section ----
# create 1st linked list
a = sll()
a.insert_last(11)
a.insert_last(22)
a.insert_last(33)

# copy 1st linked list to 2nd
b = a.copy()

print('Original linked list : ', end='')
a.display()

print('Copied linked list   : ', end='')
b.display()
####################
Original linked list : 11 22 33
Copied linked list   : 11 22 33







: #  Write  destructor  to  delete  whole  linked  list
class  sll(linked_list):
	def    _del_(a):
			How  to  remove  each  node  of  LL  until  LL  is  empty
			print('Linked  list  is  empty')
#  End  of  the  clas
How  to  create  linked  list
###############################
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Base LinkedList class
class linked_list:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Derived class with destructor
class sll(linked_list):
    def __del__(self):
        temp = self.head
        while temp:
            prev = temp
            temp = temp.next
            del prev   # delete node
        print("Linked list is empty")

# ---- Main section ----
a = sll()
a.insert_last(10)
a.insert_last(20)
a.insert_last(30)

print("Linked List before deletion: ", end='')
a.display()

# delete the linked list object
del a

###############################
Linked List before deletion: 10 20 30
Linked list is empty




: '''
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
				How  to  reverse  each  node  of  linked  list
				How  to  modify  ref  a . frist   to   last  node  of  linked  list
# End  of  the  class
How  to  create  linked  list
print('Input  Linked  List')
How  to  print  linked  list
How  to  reverse  linked  list
print('Reverse  Linked  List')
How  to  print  reverse  linked  list

#####################################

class sll(linked_list):
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev   # modify first to point to last node

# ---- Main section ----
a = sll()
a.insert_last(11)
a.insert_last(22)
a.insert_last(33)
a.insert_last(44)

print('Input Linked List: ', end='')
a.display()

# reverse linked list
a.reverse()

print('Reversed Linked List: ', end='')
a.display()
######################

Input Linked List: 11 22 33 44
Reversed Linked List: 44 33 22 11







: # Find outputs  (Home  work)
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

#############################

[P, X, A, Y, B, C, D, <class 'object'>]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye





: # Find  outputs  (Home  work)
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
#############################
[A, B, C, D, E, F, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye




: # Identify  Error
class  c1(c1):
	pass
###########################
NameError: name 'c1' is not defined




: # Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()
#################
Parent Method
Child Method




: # Identify  Error
class   c1(c2):
	pass
class  c2(c1):
	pass
#############################
NameError: name 'c2' is not defined





: # Find  outputs
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

##########################
Parent Method
Child Method
Grand Child Method
