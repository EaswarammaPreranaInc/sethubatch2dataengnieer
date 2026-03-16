#  parent  and  child  classes  have  same  Instance  method
class  parent: #Here we have created the parent class
	def   m1(self): #Defined the method m1
		print('parent  Method')
class   child(parent): #Here we are inheriting the parent class into the child class
	def   m1(self): #Method m1 of child class
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() #How  to  call  function  m1()
		#self . m1() #Here we are calling the method m1 of child class so recursion
		print('child  Method')
# End  of  the  class
def  m1(): #it is the function m1() which is outside the class
	print('m1  function')
# End of  the  function
p = parent()
p.m1() #How  to  call  m1()  method  of  parent  class
c = child()
c.m1()
'''outputs:
parent method
parent method
m1 function
child method'''
	



# parent  and  child  classes  have  different  class  methods
class  parent: 
	@classmethod
	def   m1(cls): #It is a class method 
		print('parent  Method')
class  child(parent): #Here we are inheriting the parent class into the child class
	@classmethod
	def   m2(cls): #It is also class method 
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()    #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()    #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()    #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1() #Error #we cannot use self for class methods and there is no self in current method m2
		#m1() #Error #No function m1 is in the current program
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1() #executes the method of parent class
super() . m1() #Error #super cannot be used outside the class
#self . m1() #Error #self cannot be used outside the class
'''outputs:
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
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1() #here we are calling the m1 method of current class which leads recursion
		#self . m1() #Error #We cannot use self as owner object is class method
		m1() #Error #there is no m1 function in current program
		print('child  Method') 
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class
'''outputs:
parent method
parent method
parent method
child method'''


# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super(child,child).m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() #Error #super(no=-args) cannot be used for static methods
		super(child).m1() #Error #one argument is not perimitted
		#self . m1() #Error #There cannot be self as ower object in static method 
		#cls . m1() #Error #No cls in current method
		print('child  method')
#end of the class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1() #Executes the method of parent class as there is no m1 method in child class
'''outputs:
parent method
parent method
parent method
parent method
child method
parent method'''




# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1() #Error #super with no args is not valid for static methods
		#self . m1() #Error #we cannot use self as owner object for static method
		#cls . m1() #Error #there is no cls in current method
		print('child  method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class
'''outputs:
parent method
parent method
parent method
child method
'''


# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'
		print(self.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x) #Error #there is no local x 
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x) #How  to  print  variable  'x'
		print(super().x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(self.x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y) #How  to  print  variable  'y'
		print(self.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) #Error #there is no y in m1 method and also in the parent class
		#print(y) #Error #There is no local y
# End  of child  class
a = parent()
a.m1() #How  to  call   m1()  method  of  parent  class
b = child()
b.m2() #How  to  call   m2()  method  of  child  class
'''outputs:
10
10
10
10
10
10
20
20'''


# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(self.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(super().x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) #How  to  print  variable  'x'  of  child  class
		print(self.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
a = parent() 
a.m1() #How  to  call  m1()  method  of  parent  class
b = child()
b.m1() #How  to  call  m1()  method  of  child  class
'''outputs:
10
10
10
10
20
20'''
	



#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a = int(input("Enter the value of a: "))
		self.b = int(input("Enter the value of b: ")) #How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b,sep='\t')#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get() #How  to   read  inputs  into   variables  a  and  b  of  object
		self.c = int(input("Enter the value of c: "))
		self.d = int(input("Enter the value of d: ")) #How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		super().disp() #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d,sep='\t')#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a + self.b + self.c + self.d  #sum  of  values  in  object  self
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
print('Sum of  the  values  in  child  object :  ' , c.total()) # How  to  obtain  sum of  values  of  object  'c'
'''outputs:
parent  object
Enter the value of a: 10
Enter the value of b: 20
child  object
Enter the value of a: 30
Enter the value of b: 40
Enter the value of c: 50
Enter the value of d: 60
parent  object  :       10      20

child  object  :        30      40
50      60
Sum of  the  values  in  child  object :   180'''




'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r

2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
     What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite\
'''
import  math
class   circle:
	def   get(self):
		self.r = int(input("Enter the radius: ")) #How  to  read  radius  into  object
	def   area(self):
		return math.pi * self.r ** 2 #return  area  of  circle
	def   cir(self):
		return  2 * math.pi* self. r #circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super().get() #How  to  read  radius  into  object  self
		self.h = float(input("Enter the Height: ")) #How  to  read  height  into  object  self
	def  area(self):
		return  2 * super().area() + super().cir() * self.h   #area  of  cylinder
	def  volume(self):
		return super().area() * self.h  #volume  of  cylinder
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
				c = circle() #How  to  read  raidus  into  circle  object
				c.get()
				print('Area  :  ' , c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				b = cylinder() #How  to  read  raidus  and  height  into  cylinder  object
				b.get()
				print('Area : ' ,  b.area())
				print('Volume :  ' ,  b.volume())
		case  3:
				exit() #How  to  stop  execution
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
		self.a = float(input("Enter a side: ")) #How  to  read  side  of  square
	def   area(self):
		return self.a ** 2 #area  of  square
	def   peri(self):
		return 4 ** self.a  #perimeter  of  square
class   rectangle(square):
	def   get(self):
		super().get() #How  to  read  length  of  rectangle
		self.b = float(input("Enter the breadth: ")) #How  to  read  breadth  of  rectangle
	def   area(self):
		return  self.a * self.b #area  of  rectangle
	def   peri(self):
		return  2 * (self.a + self.b) #perimeter  of   rectangle
class   cube(square):
	def   get(self):
		super().get() #How  to  read  side  of  cube
	def   area(self):
		return  6 * super().area() #area  of  cube
	def   volume(self):
		return  super().area() * self.a #volume  of  cube
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
			s = square() #How  to  read  side  into   square  object  's'
			s.get()
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' ,  s.peri())
		case   2:
			r = rectangle() #How  to  read  length  and  breadth  into   rectangle  object  'r'
			r.get()
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case   3:
			c = cube() #How  to  read  side  into  cube  object  'c'
			c.get()
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case  4:
			exit() #How  to  stop  execution





# Find  outputs
class  c1:
	def  m1(self): #Here m1 is method of c1 class
		print('m1  method  of  class  c1')
class  c2:
	def  m1(self): #Here m1 is method of c2 clas
		print('m1 method of class c2')
class  c3:
	@classmethod
	def  m1(cls): #Here it is a classmethod m1 of c3 class
		print('m1 method of  class c3')
class  c4:
	@staticmethod 
	def  m1(): #Here it is a staticmethod of c4 class
		print('m1 method of  class c4')
class  c5(c1): #Here we are inheriting the properities of c1 class to c5 class
	def  m1(self): #Here m1 is method od c5 class
		print('m1 method of class c5')
	def  m2(self):
		c3.m1() #How  to  call  m1()  method  of  class  c3
		c4.m1() #How  to  call  m1()  method  of  class  c4
		a = c2()
		a.m1() #How  to  call  m1()  method  of  class  c2
		super().m1() #How  to  call  m1()  method  of  class  c1
		self.m1() #How  to  call  m1()  method  of  class  c5
		m1() #How  to  call  m1()  function
# End  of  class  c5
def  m1(): #Here it is a regular function m1
	print('m1 function')
# End  of  the  function
a = c5() 
a.m2() #How  to  call  m2()  method  of  class  c5

'''outputs:
m1 method of class c3
m1 method of class c4
m1 method of class c2
m1 method of class c1
m1 method of class c5
m1 function
'''




# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) #True
print(issubclass(int , float)) #False
print(issubclass(str , object)) #True
print(issubclass(c1 , object)) #True
print(issubclass(c2 , object)) #True
a = c1()
b = c2()
#print(issubclass(b , a)) #Error #argument 1 must be a class
#print(issubclass(c2 , a)) #False





# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) #True
print(issubclass(c4 , c2)) #True
print(issubclass(c4 , c1)) #True
print(issubclass(c4 , object)) #True
print(issubclass(c4 , (int , float , str , bool))) #False
print(issubclass(c4 , (int , float , c1 , str , bool))) #True
#print(issubclass(c4 , [int , float , c1 , str , bool])) #Error #Argument 2 must be a tuple not list 





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
print(isinstance(25 , int)) #True
print(isinstance(10.8 , float)) #True
print(isinstance('Hyd' , str)) #True
print(isinstance(3 + 4j , complex)) #True
print(isinstance(True , bool)) #True
print(isinstance(True , int)) #True 
print(isinstance('True' , str)) #True
print(isinstance(True , str)) #False
print()
a = c3()
print(isinstance(a , c3)) #True
print(isinstance(a , c2)) #True
print(isinstance(a , c1)) #True
print(isinstance(a , object)) #True
print(isinstance(a , c4)) #False
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) #False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool))) #True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) #True
# print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) #Error #Argument 2 must be a tuple not list