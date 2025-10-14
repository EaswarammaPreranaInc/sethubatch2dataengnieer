#parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()#How  to  call  function  m1()
		#self . m1()#recurion 
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c=child()
c.m1()#How  to  call  m1()  method  of  child  class

'''
o/p:
parent method
parent method
m1 function
child method
'''



# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1()#self is not there in m1 method of parent class
		#m1()#function not there
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()#parent class is executed bcz there is no m1() method in child class
#super() . m1()#error super() cannnot use outside class
#self . m1()#error self cannnot use outside class
'''
o/p:
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
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1()# recursion
		#self . m1()#rror self is not there child class
		#m1()#error function not defined
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child .m1()#How  to  call  m1()  method  of  child  class
'''
o/p:
parent method
parent method
parent method
child method
'''



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
		#super() . m1()#error super()method take as two arguments for static method 
		#super(child).m1()#error super () method cannot  take one agrument
		#self . m1()#self is not there in parent class
		#cls . m1()#cls is not defined
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()
'''
o/p:
parent method
parent method
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
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1()#How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		#super() . m1()#error super()method has two arguments for static method
		#self . m1()#error self not defined
		#cls . m1()#cls is not there in child class and parent class
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class

'''
o/p:
parent method
parent method
parent method
child method

'''




# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10#static variable
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x)#error there is no global and loacl x
# End  of  parent  class
class   child(parent):
	y = 20#sv
	def  m2(self):
		print(parent.x)#How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y)#How  to  print  variable  'y'
		print(self.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		#print(super() . y)#error due to 'y' is not in the parent class 
		#print(y)#error there is no local and global y
# End  of child  class
p=parent()
p.m1()#How  to  call   m1()  method  of  parent  class
c=child()
c.m2()#How  to  call   m2()  method  of  child  class


'''
o/p:
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
		print(parent.x)#How  to  print  variable  'x'  of  parent  class
		print(self.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(super().x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(self.x)#How  to  print  variable  'x'  of  child  class
		print(child.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p=parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c=child()
c.m1()#How  to  call  m1()  method  of  child  class


'''
o/p:
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
		self.a=int(input('enter any nmber:'))
		self.b=int(input('enter any number:'))#How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b ,sep='\t')#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get()#How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input('enter any nmber:'))
		self.d=int(input('enter any number:'))#How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		super().disp()#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d ,sep='\t')#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
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
print('Sum of  the  values  in  child  object :  ' , c.total())# How  to  obtain  sum of  values  of  object  'c'



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
		self.r=float(input('enter radius of the circle:')) #How  to  read  radius  into  object
	def   area(self):
		return 3.14159 * self.r **2#return  area  of  circle
	def   cir(self):
		return 2 * 3.14159 * self.r#return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r=float(input('enter radius of the cylinder:'))#How  to  read  radius  into  object  self
		self.h=float(input('enter height of cylinder:'))#How  to  read  height  into  object  self
	def  area(self):
		return 2 * 3.14159 * self.r ** 2 + 2 * 3.14159 * self.r *self.h#return   area  of  cylinder
	def  volume(self):
		return 3.14159 * self.r ** 2 *  self.h#return   volume  of  cylinder
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
				print('Circumference :  ' ,  c.cir())
		case  2:
				cyl=cylinder()#How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  cyl.get())
				print('Volume :  ' , cyl.volume())
		case  3:
				exit()#How  to  stop  execution
	# End  of  match


'''
o/p:
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 1
enter radius of the circle:5.5
Area  :   95.0330975
Circumference :   34.55749
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 2
enter radius of the cylinder:3.3
enter height of cylinder:7
Area :  None
Volume :   239.48340569999993
'''


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
		self.a=float(input('enter side of square:'))#How  to  read  side  of  square
	def   area(self):
		return  self.a**2 #area  of  square
	def   peri(self):
		return  4*self.a #perimeter  of  square
class   rectangle(square):
	def   get(self):
		self.l=float(input('enter length of rectangle:')) #How  to  read  length  of  rectangle
		self.b=float(input('enter breadth of rectangle:')) #How  to  read  breadth  of  rectangle
	def   area(self):
		return  self.l*self.b#area  of  rectangle
	def   peri(self):
		return  2*(self.l+self.b) #perimeter  of   rectangle
class   cube(square):
	def   get(self):
		self.c=float(input('enter side of cube:'))#How  to  read  side  of  cube
	def   area(self):
		return 6*self.c**2 #area  of  cube
	def   volume(self):
		return  self.c**3 #volume  of  cube
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
			print('Area  :  ' , r.area())
			print('Perimeter  :  ' , r.peri())
		case   3:
			c=cube()
			c.get()#How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit()#How  to  stop  execution



'''
o/p:
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 1
enter side of square:4
Area   :   16.0
Perimeter  :   16.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 2
enter length of rectangle:3
enter breadth of rectangle:4
Area  :   12.0
Perimeter  :   14.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 3
enter side of cube:7
Area  :    294.0
Volume  :   343.0

'''


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
		c2().m1()#How  to  call  m1()  method  of  class  c2
		super().m1()#How  to  call  m1()  method  of  class  c1
		self.m1()#How  to  call  m1()  method  of  class  c5
		m1()#How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
#How  to  call  m2()  method  of  class  c5



# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))#True
print(issubclass(int , float))#Flase
print(issubclass(str , object))#True
print(issubclass(c1 , object))#True
print(issubclass(c2 , object))#True
a = c1()
b = c2()
#print(issubclass(b , a))#error
#print(issubclass(c2 , a))#error argument 2 must be a class



# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))#True
print(issubclass(c4 , c2))#True
print(issubclass(c4 , c1))#True
print(issubclass(c4 , object))#True
print(issubclass(c4 , (int , float , str , bool)))#False
print(issubclass(c4 , (int , float , c1 , str , bool)))#True
#print(issubclass(c4 , [int , float , c1 , str , bool]))#error argument must be tuple of classes


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
print(isinstance(25 , int))#True
print(isinstance(10.8 , float))#True
print(isinstance('Hyd' , str))#True
print(isinstance(3 + 4j , complex))#True
print(isinstance(True , bool))#True
print(isinstance(True , int))#True
print(isinstance('True' , str))#True
print(isinstance(True , str))#False
print()
a = c3()
print(isinstance(a , c3))#True
print(isinstance(a , c2))#True
print(isinstance(a , c1))#True
print(isinstance(a , object))#True
print(isinstance(a , c4))#False
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))#False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))#True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))#True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))#error argument 2 must be tuple of classes