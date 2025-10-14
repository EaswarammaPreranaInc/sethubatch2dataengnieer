#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() # How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
# How to call m1() method of parent class
p = parent()
p.m1()
# How to call m1() method of child class
c = child()
c.m1()

'''
parent method
parent method
m1 function
infinite recursion
'''


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent  . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls .m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # error as there is no self
		m1() # error as there is no f1 function
		print('child  Method')
# End  of  the  class
# How to call m1() method of parent class
p = parent()
p . m1()
# How to call m2() method of child class
c = child()
c . m1()
child . m1() # executes method of parent class
super() . m1() # error as there is no super outside the class
self . m1() # error as there is self outside class

'''
parent method
parent method
parent method
parent method
parent method
child method
parent method
'''


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1() # child class m1 method and infinite recursion
		self . m1() # error as there is no self
		m1() # error as there is no m1 method
		print('child  Method')
# End  of  the  class
# How to call m1() method of parent class
p = parent()
p.m1()
# How to call m1() method of child class
c = child()
c.m1()




# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		# super() . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent . m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child . m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() # error as static method cannot use super
		super(child).m1() # error as super has 1 argument
		self . m1() # error as there is no self
		cls . m1() # error as there is no cls
		print('child  method')
#end of the class
# How to call m1() method of parent class
parent . m1()
# How to call m2() method of child class
child() . m2()
child . m1() # executes parent class m1

'''
parent method
parent method
child method
parent method
'''


# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent . m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child . m1() # How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1() # error as static method cannot use super 
		self . m1() # error as there is no self
		cls . m1() # error as there is no cls
		print('child  method')
# End  of  the  class
# How to call m1() method of parent class
parent() . m1()
# How to call m1() method of child class
child() . m1()


# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self . x) # How  to  print  variable  'x'
		print(parent . x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x) # error as there is no local variable x
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(super() . x) # How  to  print  variable  'x'
		print(parent . x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child . x) # How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(self . x) # How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self . y) # How  to  print  variable  'y'
		print(child . y) # How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # error as there is no y in parent class
		print(y) # error as there is no local variable y
# End  of child  class
# How to call m1() method of parent class
p = parent()
p . m1()
# How to call m2() method of child class
c = child()
c . m2()

'''
10
10
10
10
10
10
20
20
'''


# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self . x) # How  to  print  variable  'x'  of  parent  class
		parent . x # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super() . x) # How  to  print  variable  'x'  of  parent  class
		print(parent . x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self . x) # How  to  print  variable  'x'  of  child  class
		print(child . x) # How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
# How to call m1() method of parent class
p = parent()
p . m1()
# How to call m1() method of child class
c = child()
c . m1()

'''
10
10
10
10
20
20
'''

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		# How  to   read  inputs  into   variables  a  and  b  of  object
		self . a = int(input('Enter a Number : ')) 
		self . b = int(input('Enter a Number : '))
	def    disp(self):
		# How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self . a , self . b , sep = '\t')
# End  of  Parent  class
class    child(parent):
	def    get(self):
		# How  to   read  inputs  into   variables  a  and  b  of  object
		super() . get()
		# How  to   read  inputs  into   variables  c  and  d  of  object
		self . c = int(input('Enter a Number : '))
		self . d = int(input('Enter a Number : '))
	def   disp(self):
		super() . disp() # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self . c , self . d , sep = '\t') # How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return  self . a + self . b + self . c + self . d # sum  of  values  in  object  self
# End of child class
print('parent  object')
# How  to  read  inputs  into  parent  class  object  'p'
p = parent()
p . get()
print('child  object')
# How  to  read  inputs  into  child  class  object  'c'
c = child()
c . get()
print('parent  object  :  ' , end = '\t')
p . disp() # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c . disp() # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c . total()) # How  to  obtain  sum of  values  of  object  'c')


# Find  outputs
class  c1:
	def  m1(self):
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self):
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls):
		print('m1 method of  class c3')
class  c4:
	@staticmethod
	def  m1():
		print('m1 method of  class c4')
class  c5(c1):
	def  m1(self):
		print('m1 method of class c5')
	def  m2(self):
		c3 . m1() # How  to  call  m1()  method  of  class  c3
		c4 . m1() # How  to  call  m1()  method  of  class  c4
		a = c2() # How  to  call  m1()  method  of  class  c2
		a . m1()
		super() . m1() # How  to  call  m1()  method  of  class  c1
		self . m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
# How  to  call  m2()  method  of  class  c5
c = c5()
c . m2()

'''
m1 method of  class c3
m1 method of  class c4
m1 method of class c2
m1  method  of  class  c1
m1 method of class c5
m1 function

'''

# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) # True
print(issubclass(int , float)) # False
print(issubclass(str , object)) # True
print(issubclass(c1 , object)) # True
print(issubclass(c2 , object)) # True
a = c1()
b = c2()
print(issubclass(b , a)) # error as arguments should be class name
print(issubclass(c2 , a)) # error as arguments should be class name


# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) # True
print(issubclass(c4 , c2)) # True
print(issubclass(c4 , c1)) # True
print(issubclass(c4 , object)) # True
print(issubclass(c4 , (int , float , str , bool))) # False
print(issubclass(c4 , (int , float , c1 , str , bool))) # True
print(issubclass(c4 , [int , float , c1 , str , bool])) # Error as there 2nd arg should be tuple not list


#  Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int)) # True
print(isinstance(10.8 , float)) # True
print(isinstance('Hyd' , str)) # True
print(isinstance(3 + 4j , complex)) # True
print(isinstance(True , bool)) # True
print(isinstance(True , int)) # False
print(isinstance('True' , str)) # True
print(isinstance(True , str)) # False
print()
a = c3()
print(isinstance(a , c3)) # True
print(isinstance(a , c2)) # True
print(isinstance(a , c1)) # True
print(isinstance(a , object)) # True
print(isinstance(a , c4)) # False
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) # False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool))) # True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) # True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) # Error
