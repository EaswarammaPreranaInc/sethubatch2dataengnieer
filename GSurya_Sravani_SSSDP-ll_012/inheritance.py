#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() #How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c=child() #How  to  call  m1()  method  of  child  class
c.m1()


# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		How  to  call  m1()  method  of  parent  class  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
p=parent() #How  to  call  m1()  method  of  parent  class
p.m1()
c=child() #How  to  call  m2()  method  of  child  class
c.m2()
child . m1()#error
super() . m1()#error
self . m1()#error


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1()How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()#recursion
		self . m1()#error
		m1()#error
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class


# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1()#'parent method'
		super(child).m1()#'parent method'
		self . m1()#error
		cls . m1()#error
		print('child  method')
#end of the class
parent.m1() #How  to  call  m1()  method  of  parent  class
chid.m2() #How  to  call  m2()  method  of  child  class
child . m1()#error

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()ow  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()'parent method'
		self . m1()#'parent method
		cls . m1()#error
		print('child  method')
# End  of  the  class
p=parent() #How  to  call  m1()  method  of  parent  class
p.m1()#'parent method
c=child() #How  to  call  m1()  method  of  child  class
c.m1()



# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x) #How  to  print  variable  'x'
		print(parent.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)#error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x) #How  to  print  variable  'x'
		print(parent.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) #How  to  print  variable  'y'
		print(child.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)#error
		print(y)
# End  of child  class
p=parent() #How  to  call   m1()  method  of  parent  class
p.m1()
c=child() #How  to  call   m2()  method  of  child  class
c.m2()


# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x) #How  to  print  variable  'x'  of  parent  class
		print(parent.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super().x) #How  to  print  variable  'x'  of  parent  class
		print(child.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)How  to  print  variable  'x'  of  child  class
		print(child.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent() #How  to  call  m1()  method  of  parent  class
p.m1()
c=child() #How  to  call  m1()  method  of  child  class
c.m1()


#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=input("enter num: ") #How  to   read  inputs  into   variables  a  and  b  of  object
                self.b=input("enter num: ")
	def    disp(self):
		print(f" {self.a} {self.b}", sep='\t')How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		print(super().a)#How  to   read  inputs  into   variables  a  and  b  of  object
                print(super().b)
                self.c=input("enter num: ") #How  to   read  inputs  into   variables  a  and  b  of  object
                self.d=input("enter num: ")
		How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(f"{self.a} {self.b}",sep="\t") #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(f" {self.c} {self.d} ",sep="\t")How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return   sum  (self.a,self.b,self.c,self.d)
# End of child class
print('parent  object')
p=parent() #How  to  read  inputs  into  parent  class  object  'p'
p.get()
print('child  object')
c=child() #How  to  read  inputs  into  child  class  object  'c'
c.get()
print('parent  object  :  ' , end = '\t')
How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  How  to  obtain  sum of  values  of  object  'c')


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
		super(c4,self) #How  to  call  m1()  method  of  class  c3
		c4.m1()  #How  to  call  m1()  method  of  class  c4
		super(c3,self) #How  to  call  m1()  method  of  class  c2
		super(c2,self) #How  to  call  m1()  method  of  class  c1
		self.m1() #How  to  call  m1()  method  of  class  c5
		m1() #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
cl1=c5() #How  to  call  m2()  method  of  class  c5
cl1.m2()


# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))#true
print(issubclass(int , float))#false
print(issubclass(str , object))#true
print(issubclass(c1 , object))#true
print(issubclass(c2 , object))#true
a = c1()
b = c2()
print(issubclass(b , a))#false
print(issubclass(c2 , a))#false

# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))#true
print(issubclass(c4 , c2))#false
print(issubclass(c4 , c1))#false
print(issubclass(c4 , object))#true
print(issubclass(c4 , (int , float , str , bool)))#True
print(issubclass(c4 , (int , float , c1 , str , bool)))##true
print(issubclass(c4 , [int , float , c1 , str , bool]))#error



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
print(isinstance(25 , int))#true
print(isinstance(10.8 , float))#true
print(isinstance('Hyd' , str))#truetrue#
print(isinstance(3 + 4j , complex))#true
print(isinstance(True , bool))#true
print(isinstance(True , int))#false
print(isinstance('True' , str))#true
print(isinstance(True , str))#false
print()
a = c3()
print(isinstance(a , c3))#true
print(isinstance(a , c2))#true
print(isinstance(a , c1))#true
print(isinstance(a , object))#true
print(isinstance(a , c4))#false
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))#true
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))#true
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))#false
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))#error






