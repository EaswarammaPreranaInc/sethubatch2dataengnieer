#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()#How  to  call  function  m1()
		self . m1()# recursion
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p = parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c = child()
c.m1()#How  to  call  m1()  method  of  child  class







# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()#Error
		m1()#Error
		print('child  Method')
# End  of  the  class
p = parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c = child()
c.m2()#How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()#Error
self . m1()#Error







# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()#Recursion error
		self . m1()#Error
		m1()
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class







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
		super() . m1()#Error
		super(child).m1()#Error
		self . m1()#Error
		cls . m1()#Error
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child . m1()






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
		super() . m1()#Error
		self . m1()#Error
		cls . m1()#Error
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class







# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)#Error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x)#How  to  print  variable  'x'
		print(child.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(self.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y)#How  to  print  variable  'y'
		print(self.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)#Error
		print(y)#Error
# End  of child  class
p = parent()
p.m1()#How  to  call   m1()  method  of  parent  class
c= child()
c.m2()#How  to  call   m2()  method  of  child  class







# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'  of  parent  class
		print(self.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'  of  parent  class
		print(super().x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x'  of  child  class
		print(self.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent()
p.m1()#How  to  call  m1()  method  of  parent  class
c = child()
c.m1()#How  to  call  m1()  method  of  child  class







#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a=int(input('enter Number:')) #How  to   read  inputs  into   variables  a  and  b  of  object
		self.b=int(input('enter Number:')) #How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(f"{self.a}\t{self.b}") #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		self.a=int(input('enter Number:')) #
		self.b=int(input('enter Number:'))  #How  to   read  inputs  into   variables  a  and  b  of  object
		self.c=int(input('enter Number:')) 
		self.d=int(input('enter Number:')) #How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(f"{self.a}\t{self.b}") #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(f"{self.c}\t{self.d}") #How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a + self.b + self.c + self.d #return   sum  of  values  in  object  self
# End of child class
print('parent  object')
p = parent()
p.get() #How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c = child()
c.get() #How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp() #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c.total()) #  How  to  obtain  sum of  values  of  object  'c')







'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''

#Program:
import math
class circle:
    def get(self):
        self.r = float(input("Enter radius of circle: "))
    def area(self):
        return 3.14159 * (self.r ** 2)
    def cir(self):
        return 2 * 3.14159 * self.r
class cylinder(circle):
    def get(self):
        self.r = float(input("Enter radius of cylinder: "))
        self.h = float(input("Enter height of cylinder: "))
    def area(self):
        return 2 * 3.14159 * (self.r ** 2) + 2 * 3.14159 * self.r * self.h
    def volume(self):
        return 3.14159 * (self.r ** 2) * self.h
def menu():
    print("\n1. Circle")
    print("2. Cylinder")
    print("3. Exit")
while True:
    menu()
    ch = eval(input("Enter choice: "))
    match ch:
        case 1:
            c = circle()
            c.get()
            print("Area           :", c.area())
            print("Circumference  :", c.cir())

        case 2:
            cyl = cylinder()
            cyl.get()
            print("Surface Area :", cyl.area())
            print("Volume       :", cyl.volume())

        case 3:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice! Please try again.")






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

#Program:
class   square:
	def   get(self):
		self.a=int(input('Enter side of suqare:')) #How  to  read  side  of  square
	def   area(self):
		return self.a**2 #   area  of  square
	def   peri(self):
		return 4*self.a #perimeter  of  square
class   rectangle(square):
	def   get(self):
		self.l=int(input('Enter length of rectangle:')) #How  to  read  length  of  rectangle
		self.b=int(input('Enter breadth of rectangle:')) #How  to  read  breadth  of  rectangle
	def   area(self):
		 return self.l*self.b # area  of  rectangle
	def   peri(self):
		return 2 * (self.l + self.b) #perimeter  of   rectangle
class   cube(square):
	def   get(self):
		self.a=int(input('Enter side of cube:')) #How  to  read  side  of  cube
	def   area(self):
		return  6 * (self.a**2) #  area  of  cube
	def   volume(self):
		return self.a**3 #  volume  of  cube
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
			s.get() #How  to  read  side  into   square  object  's'
			print('Area of sqare  :  ' , s.area())
			print('Perimeter  :  ' , s.peri())
		case   2:
			r=rectangle() 
			r.get() #How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area of rectangle :  ' , r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c=cube() 
			c.get() #How  to  read  side  into  cube  object  'c'
			print('Area of cube :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			break #How  to  stop  execution






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
		c1().m1()#How  to  call  m1()  method  of  class  c1
		c5().m1()#How  to  call  m1()  method  of  class  c5
		m1()#How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c = c5()
c.m2()#How  to  call  m2()  method  of  class  c5


12.# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))#True
print(issubclass(int , float))#False
print(issubclass(str , object))#True
print(issubclass(c1 , object))#True
print(issubclass(c2 , object))#True
a = c1()
b = c2()
print(issubclass(b , a))#Error 
print(issubclass(c2 , a))#Error


13.# Find outputs
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
print(issubclass(c4 , (int , float , str , bool)))#false
print(issubclass(c4 , (int , float , c1 , str , bool)))#True
print(issubclass(c4 , [int , float , c1 , str , bool]))#Error






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
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))#Error