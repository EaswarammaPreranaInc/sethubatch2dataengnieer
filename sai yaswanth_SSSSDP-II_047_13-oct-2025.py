#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()#How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m1()  method  of  child  class
c.m1()
	

# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
p = parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m2()  method  of  child  class
c.m2()
child . m1()
super() . m1()
self . m1()


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
p = parent#How  to  call  m1()  method  of  parent  class
p.m1()
c = child#How  to  call  m1()  method  of  child  class
c.m1()
	

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
p = parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m1()  method  of  child  class
c.m1()


 # Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.c1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super.c1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1()
		super(child).m1()
		self . m1()
		cls . m1()
		print('child  method')
#end of the class
p = parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m2()  method  of  child  class
c.m2()
child . m1()


# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(super.x)#How  to  print  variable  'x'
		print(parent.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(child.x)#How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(parent.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y)#How  to  print  variable  'y'
		print(child.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)
		print(y)
# End  of child  class
p = parent#How  to  call   m1()  method  of  parent  class
p.m1()
c = child()#How  to  call   m2()  method  of  child  class
c.m2()
	

# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super().x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)#How  to  print  variable  'x'  of  child  class
		print(child.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent()#How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m1()  method  of  child  class
c.m1()


#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a,self.b=map(int,input().split())#How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b,sep='\t')#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a,self.b=map(int,input().split())#How  to   read  inputs  into   variables  a  and  b  of  object
		self.c,self.d=map(int,input().split())#How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(self.a,self.b,sep='\t')#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d,sep='\t')#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a + self.b + self.c + self.d
# End of child class
print('parent  object')
p = parent()#How  to  read  inputs  into  parent  class  object  'p'
p.get()
print('child  object')
c = child()#How  to  read  inputs  into  child  class  object  'c'
c.get()
print('parent  object  :  ' , end = '\t')
p.disp()#How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()#How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c.total())


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
class square:
	def get(self):
		self.a = float(input('Enter side of square: '))  # How to read side of square
	def area(self):
		return self.a ** 2
	def peri(self):
		return 4 * self.a

class rectangle(square):
	def get(self):
		self.a = float(input('enter length of rectangle: '))  # How to read length of rectangle
		self.b = float(input('enter breadth of rectangle: '))  # How to read breadth of rectangle
	def area(self):
		return self.a * self.b
	def peri(self):
		return 2 * (self.a + self.b)

class cube(square):
	def get(self):
		self.a = float(input('enter side of cube: '))  # How to read side of cube
	def area(self):
		return 6 * (self.a ** 2)
	def volume(self):
		return self.a ** 3

def menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End of the function

while True:
	menu()
	try:
		ch = int(input('Enter  choice : '))
	except Exception:
		print('Invalid choice')
		continue
	match ch:
		case 1:
			s = square()  # How to read side into square object 's'
			s.get()
			print('Area   :  ', s.area())
			print('Perimeter  :  ', s.peri())
		case 2:
			r = rectangle()  # How to read length and breadth into rectangle object 'r'
			r.get()
			print('Area  :  ', r.area())
			print('Perimeter  :  ', r.peri())
		case 3:
			c = cube()  # How to read side into cube object 'c'
			c.get()
			print('Area  :   ', c.area())
			print('Volume  :  ', c.volume())
		case 4:
			break  # How to stop execution


'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import math
class circle:
	def get(self):
		self.r = int(input('enter radius:'))  # How  to  read  radius  into  object 
	def area(self):
		return 3.14159 * (self.r ** 2)  # area  of  circle
	def cir(self):
		return 2 * 3.14159 * self.r  # circumference  of  circle
# End  of  circle  class
class cylinder(circle):
	def get(self):
		self.r = int(input('enter radius:'))  # How  to  read  radius  into  object  self
		self.h = int(input('enter height:'))  # How  to  read  height  into  object  self
	def area(self):
		return 2 * 3.14159 * (self.r ** 2) + 2 * 3.14159 * self.r * self.h  # area  of  cylinder
	def volume(self):
		return 3.14159 * (self.r ** 2) * self.h  #  volume  of  cylinder
# End of cylinder class
def menu():
	print('1 . Circle')
	print('2 . Cylinder')
	print('3 . Exit')
#end of menu function
while True:
	menu()
	ch = eval(input('Enter choice : '))
	match ch:
		case 1:
			c = circle()
			c.get()  # How  to  read  raidus  into  circle  object
			print('Area  :  ', c.area())
			print('Circumference :  ', c.cir())
		case 2:
			c = cylinder()
			c.get()  # How  to  read  raidus  and  height  into  cylinder  object
			print('Area : ', c.area())
			print('Volume :  ', c.volume())
		case 3:
			break  # How  to  stop  execution
	# End  of  match