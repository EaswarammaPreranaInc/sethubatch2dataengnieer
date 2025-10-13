#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()    #How  to  call  function  m1()
		self . m1() # m1 method of child class calling m1 inside m1 recursion
		print('child  Method')  #prints child method
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1()  #How  to  call  m1()  method  of  parent  class
c=child()
c.m1()  #How  to  call  m1()  method  of  child  class

# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1()  #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1()    #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()    #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()  #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # error as there is no self in m2 method
		m1()    # error as there is m1 function 
		print('child  Method')
# End  of  the  class
parent.m1()  #How  to  call  m1()  method  of  parent  class
child.m2()  #How  to  call  m2()  method  of  child  class
child . m1()    # 1st it searches for m1 in child class if not m1 in parent class
super() . m1()  # error as super cannot be accesed outside class
self . m1()  # error as self cannot be accesed outside class


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1() # m1 method of child class is executed and hence recursion
		self . m1()  # error as there is no self in m2 method
		m1()    # error as there is m1 function 
		print('child  Method')
# End  of  the  class
parent . m1()  #How  to  call  m1()  method  of  parent  class
child.m1()  #How  to  call  m1()  method  of  child  class

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() # parent cls m1() method is executed
		super(child).m1()   # parent.m1() is executed
		self . m1() # error as there is no self
		cls . m1() # error as there is no cls
		print('child  method')
#end of the class
parent.m1()  #How  to  call  m1()  method  of  parent  class
child.m2()  #How  to  call  m2()  method  of  child  class
child . m1()    # as there is m1 method in child class m1 method in parent class is executed

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()
		self . m1() # error
		cls . m1()  # error
		print('child  method')
# End  of  the  class
parent.m1   #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(p.x)    #How  to  print  variable  'x'
		print(parent.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)    # error as no local variable x
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(p.x) #How  to  print  variable  'x'
		print(parent.x)   #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(super().x) #to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(child.x)  #How  to  print  variable  'x' in  last  way  without  creating  an  object
		child.y #How  to  print  variable  'y'
		self.y  #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)  # error as there is no y in parent class
		print(y) # error as no local variable  y
# End  of child  class
p=parent()
p.m1()  #How  to  call   m1()  method  of  parent  class
c=child()
c.m2()  #How  to  call   m2()  method  of  child  class

# Parent  and  Child  classes  have  static  variables  with  same  name
class parent:
	x = 10
	def m1(self):
		# How  to  print  variable  'x'  of  parent  class
		print(self.x)
		# How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(parent.x)

class child(parent):
	x = 20
	def m1(self):
		# How  to  print  variable  'x'  of  parent  class
		print(super().x)
		# How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(parent.x)
		# How  to  print  variable  'x'  of  child  class
		print(self.x)
		# How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
		print(child.x)
# End  of  the  class

# How  to  call  m1()  method  of  parent  class
parent().m1()

# How  to  call  m1()  method  of  child  class
child().m1()

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input())
		self.b=int(input()) #How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b,sep='\t') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input())
		self.b=int(input())     #How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input())
		self.d=int(input())     #How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(self.a,self.b,sep='\t',end='\t') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d,sep='\t') #How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		    return self.a+self.b+self.c+self.d     #return   sum  of  values  in  object  self
# End of child class
print('parent  object')
p=parent() 
p.get() #How  to read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()   
c.get() #How  to read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp()    #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()    #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total())    #How  to  obtain  sum of  values  of  object  'c')



