#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()  #  How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()  #  How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()  #  
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()
c.m1()  #  How  to  call  m1()  method  of  child  class




# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()  #  How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()  #  How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()  #  How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		p.m1()  #  How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()  #  Error
		m1()  #  Error due to no function m1()
		print('child  Method')
# End  of  the  class
p=parent()  
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()  
c.m2()  #  How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()
self . m1()  #  Error due to self cant use outside the class




# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		cls.m1()  #  How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1()  #  How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1()  #  Error due to self is not defined
		m1()  #  Error due to no function m1()
		print('child  Method')
# End  of  the  class
p=parent()  
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()  
c.m1()  #  How  to  call  m1()  method  of  child  class




# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super().m1()  #  How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()  #  How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		parent.m1(self)  #  How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1()
		child.m1()
		self . m1()  #  ERROR DUE TO SELF IS NOT DEFINED
		cls . m1()  #  Error due to cls is not defined
		print('child  method')
#end of the class
p=parent()
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()
c.m2()  #  How  to  call  m2()  method  of  child  class
child . m1()



# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()  #  How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent().m1()  #  How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()
		self . m1()
		cls . m1()
		print('child  method')
# End  of  the  class
p=parent()
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()
c.m1()  #  How  to  call  m1()  method  of  child  class



# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x)  #  How  to  print  variable  'x'
		print(parent.x)  #  How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)  #  Error due to x is not defined
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x)  #  How  to  print  variable  'x'
		print(child.x)  #  How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(parent.x)  #  How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x)  #  How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y)  #  How  to  print  variable  'y'
		print(self.y)  #  How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)
		print(y)  #  Error due to y is not defined
# End  of child  class
p=parent()
p.m1()  #  How  to  call   m1()  method  of  parent  class
c=child()
c.m2()  #  How  to  call   m2()  method  of  child  class



# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x)  #  How  to  print  variable  'x'  of  parent  class
		print(self.x)  #  How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x)  #  How  to  print  variable  'x'  of  parent  class
		print(super().x)  #  How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)  #  How  to  print  variable  'x'  of  child  class
		print(child.x)  #  How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent()
p.m1()  #  How  to  call  m1()  method  of  parent  class
c=child()
c.m1()  #  How  to  call  m1()  method  of  child  class




#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input("Enter a value : "))
		self.b=int(input("Enter a value : "))#  How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b, sep="\t")  #  How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input("Enter a value : "))
		self.b=int(input("Enter a value : "))  #  How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input("Enter a value : "))
		self.d=int(input("Enter a value : "))  #  How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(self.a,self.b, sep="\t")  #  How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d, sep="\t")   #  How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return   f"Sum = ",self.a+self.b+self.c+self.d
# End of child class
print('parent  object')
p=parent()
p.get()  #  How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()  
c.get()  #  How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
print(p)  #  How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
print(c)  #  How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c.total())



'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import  math
class   circle:
	def   get(self):
	    self.r=float(input("Enter Radius : "))  #  How  to  read  radius  into  object
	def area(self):
		return  f"Area of  circle  :  , { math.pi * self.r * self.r}"
	def   cir(self):
		return  f"Circumference of  circle  :  , {2 * math.pi * self.r}"
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r=float(input("Enter Radius : "))  #  How  to  read  radius  into  object  self
		self.h=float(input("Enter Height : "))  #  How  to  read  height  into  object  self
	def  area(self):
		return   f"Area of Cylinder :, { 2 * math.pi * self.r * self.r + 2 * math.pi * self.r * self.h}"
	def  volume(self):
		return   f"Volume of Cylinder :  ,  {math.pi * self.r * self.r * self.h}"
# End of cylinder class
c=circle()
cy=cylinder()
def    menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
while  True:
	menu()
	ch = eval(input('Enter choice : '))
	match  ch:
		case  1:
				c.get()  #  How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				cy.get()  #  How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  cy.area())
				print('Volume :  ' ,  cy.volume())
		case  3:
				exit()  #  How  to  stop  execution
	# End  of  match




'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  ---> a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  --->  a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''
class   square:
	def   get(self):
		self.s=float(input("enter a side : "))  #  How  to  read  side  of  square
	def   area(self):
		return   f"area  of  square  :  {self.s * self.s}"
	def   peri(self):
		return   f"Perimeter  of  square  :  {4 * self.s}"
class   rectangle(square):
	def   get(self):
		self.l=float(input("enter length : "))  #  How  to  read  length  of  rectangle
		self.b=float(input("Enter Breadth : "))  #  How  to  read  breadth  of  rectangle
	def   area(self):
		 return   f"area  of  rectangle  :  {self.l * self.b}"
	def   peri(self):
		return  f"Perimeter  of  rectangle  :  {2 * (self.l + self.b)}"
class   cube(square):
	def   get(self):
		self.s=float(input("enter side : ")) #  How  to  read  side  of  cube
	def   area(self):
		return  f"Surface  area  of  cube  :  {6 * self.s * self.s}"
	def   volume(self):
		return  f"Volume  of  cube  :  {self.s * self.s * self.s}"

sq=square()
r=rectangle()
c=cube()

def  menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
while  True:
	menu()
	ch = int(input('Enter  choice : '))
	match   ch:
		case   1:
			sq.get()  #  How  to  read  side  into   square  object  's'
			print('Area   :  ' ,  sq.area())
			print('Perimeter  :  ' ,  sq.peri())
		case   2:
			r.get()  #  How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c.get()  #  How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit()  #  How  to  stop  execution



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
		c3.m1()  #  How  to  call  m1()  method  of  class  c3
		c4.m1()  #  How  to  call  m1()  method  of  class  c4
		c2.m1()  #  How  to  call  m1()  method  of  class  c2
		super().m1()  #  How  to  call  m1()  method  of  class  c1
		c5.m1()  #  How  to  call  m1()  method  of  class  c5
		m1()  #  How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c=c5()
c.m2()  #  How  to  call  m2()  method  of  class  c5



# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))  #  True
print(issubclass(int , float))  #  True
print(issubclass(str , object))  #  True
print(issubclass(c1 , object))  #  True
print(issubclass(c2 , object)) #  True
a = c1()
b = c2()
print(issubclass(b , a))  # Error
print(issubclass(c2 , a))  #  True



# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))  #  True
print(issubclass(c4 , c2))  #  True
print(issubclass(c4 , c1))  #  True
print(issubclass(c4 , object))  #  True
print(issubclass(c4 , (int , float , str , bool)))  #  True
print(issubclass(c4 , (int , float , c1 , str , bool)))  #  True
print(issubclass(c4 , [int , float , c1 , str , bool]))  #  Error



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
print(isinstance(25 , int))  #  True
print(isinstance(10.8 , float))  #  True
print(isinstance('Hyd' , str))  #  True
print(isinstance(3 + 4j , complex))  #  True
print(isinstance(True , bool))   # True
print(isinstance(True , int))  #  True
print(isinstance('True' , str))  #  True
print(isinstance(True , str))  #  False
print()
a = c3()
print(isinstance(a , c3))  #  True
print(isinstance(a , c2))  #  True
print(isinstance(a , c1))  #  True
print(isinstance(a , object))  #  True
print(isinstance(a , c4))  #  False
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))  #  False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))  #  True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))  #  True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))  #  Error

