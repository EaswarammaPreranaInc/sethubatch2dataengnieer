#1st program
#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object --->parent method
		m1()#How  to  call  function  m1() ---->m1 function
		#self . m1() #recursion
		print('child  Method')#child Method
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c=child()
c.m1()#How  to  call  m1()  method  of  child  class


#2nd program
# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super().m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1()#error
		#m1()#error
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()#parent method
#super() . m1()#error
#self . m1()#error


#3rd program
# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1()#recursion
		#self . m1()#error
		#m1()#error
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class


#4th program
# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		#super() . m1()#error , there is no argument passed to super()
		#super(child).m1()#error,1 arg is cannot be passed
		#self . m1()#error ,there is no self defined
		#cls . m1()#error ,there is no cls defined
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()#parent class method m1 is executed


#5th program
# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		#super() . m1()#error, there is no argument passed to super()
		#self . m1()#error ,there is no self defined
		#cls . m1()#error ,there is no cls defined
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class


#6th program
# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'
		print(parent.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x)#error , there is no x defined
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x)#How  to  print  variable  'x'
		print(super().x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(parent.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y)#How  to  print  variable  'y'
		print(child.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		#print(super() . y)#error , there is no y defined in parent class
		#print(y)#error , there is no y defined
# End  of child  class
p=parent()
p.m1()#How  to  call   m1()  method  of  parent  class
c=child()
c.m2()#How  to  call   m2()  method  of  child  class


#7th program
# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'  of  parent  class
		print(super().x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)#How  to  print  variable  'x'  of  child  class
		print(child.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent()
p.m1()#How  to  call   m1()  method  of  parent  class
c=child()
c.m1()#How  to  call   m1()  method  of  child  class


#8th program
#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input("Enter any number: "))#How  to   read  inputs  into   variables  a  and  b  of  object
		self.b=int(input("Enter any number: "))
	def    disp(self):
		print(self.a,self.b ,sep="\t")#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get()#How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input("Enter any number: "))
		self.d=int(input("Enter any number: "))#How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		super().disp()#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d ,sep="\t")#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a+self.b+self.c+self.d#return   sum  of  values  in  object  self
# End of child class
print('parent  object')
p=parent()
p.get()#How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()
c.get()#How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp()#How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()#How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total())#How  to  print  sum  of  values  in  object  'c'


#9th program
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
	    self.r=float(input("Enter the radius: "))#How  to  read  radius  into  object
	def  area(self):
		return  math.pi *self.r**2
	def   cir(self):
		return 2 * math.pi * self.r #return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super().get()#How  to  read  radius  into  object  self
		self.h=float(input("Enter the heighth of cylinder: "))#How  to  read  height  into  object  self
	def  area(self):
		return   2*super().area() +super().cir()*self.h #return  area  of  cylinder
	def  volume(self):
		return   super().area()*self.h #return  volume  of  cylinder
# End of cylinder class
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
				c=circle()
				c.get()#How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' , c.cir())
		case  2:
				c=cylinder()
				c.get()#How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  c.area())
				print('Volume :  ' , c.volume())
		case  3:
				exit()#How  to  stop  execution
	# End  of  match

#10th program
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
		self.a=float(input('Enter the side: '))#How  to  read  side  of  square
	def   area(self):
		return  self.a**2
	def   peri(self):
		return  4*self.a
class   rectangle(square):
	def   get(self):
		super().get()#How  to  read  length  of  rectangle
		self.b=float(input("Enter the breadth: "))#How  to  read  breadth  of  rectangle
	def   area(self):
		 return  self.a*self.b
	def   peri(self):
		return  2*(self.a+self.b)
class   cube(square):
	def   get(self):
		 super().get()#How  to  read  side  of  cube
	def   area(self):
		return  6 * (self.a**2)
	def   volume(self):
		return  self.a**3
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
			s=square()
			s.get()#How  to  read  side  into   square  object  's'
			print('Area   :  ' , s.area())
			print('Perimeter  :  ' ,  s.peri())
		case   2:
			r=rectangle()
			r.get()#How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' , r.peri())
		case   3:
			c=cube()
			c.get()#How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit()#How  to  stop  execution
           

#11th program
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
		c3.m1()#How  to  call  m1()  method  of  class  c3
		c4.m1()#How  to  call  m1()  method  of  class  c4
		c=c2()
		c.m1()#How  to  call  m1()  method  of  class  c2
		super().m1()#How  to  call  m1()  method  of  class  c1
		self.m1()#How  to  call  m1()  method  of  class  c5
		m1()#How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c5=c5()
c5.m2()#How  to  call  m2()  method  of  class  c5


#12th program
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
#print(issubclass(b , a))#error, atleast 1 arg should be a class
#print(issubclass(c2 , a))#error,arg 2 must be a class or tuple of classes


#13th program
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
print(issubclass(c4 , c2))#true
print(issubclass(c4 , c1))#true
print(issubclass(c4 , object))#true
print(issubclass(c4 , (int , float , str , bool)))#false
print(issubclass(c4 , (int , float , c1 , str , bool)))#true
#print(issubclass(c4 , [int , float , c1 , str , bool]))#error,arg 2 must be a class or tuple of classes


#14th program
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
print(isinstance('Hyd' , str))#true
print(isinstance(3 + 4j , complex))#true
print(isinstance(True , bool))#true
print(isinstance(True , int))#true
print(isinstance('True' , str))#true
print(isinstance(True , str))#false
print()
a = c3()
print(isinstance(a , c3))#true
print(isinstance(a , c2))#true
print(isinstance(a , c1))#true
print(isinstance(a , object))#true
print(isinstance(a , c4))#false
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))#false
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))#true
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))#true
#print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))#error,arg 2 must be a class or tuple of classes