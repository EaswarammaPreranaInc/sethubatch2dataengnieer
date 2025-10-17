#  parent  and  child  classes  have  same  Instance  method
class parent:
	def m1(self):
		print('parent  Method')
class child(parent):
	def m1(self):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() # How  to  call  function  m1()
		self . m1()
		print('child  Method')
# End  of  the  class
def m1():
	print('m1  function')
# End of  the  function
p = parent() 
p.m1() # How  to  call  m1()  method  of  parent  class
c = child() 
c.m1() # How  to  call  m1()  method  of  child  class
'''
Outputs
parent Method
parent Method
m1 function
parent Method
m1 function
parent Method
m1 function infinite times, recursion error
'''









# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def m1(cls):
		print('parent  Method')
class child(parent):
	@classmethod
	def m2(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # Error Cannot use self in class method
		m1() # Error, there is no m1() function 
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1() # Error, cannot use child outside the class
super() . m1() # Error, cannot use super outside the class
self . m1() # Error, cannot use self outside the class
'''
Outputs
parent Method
parent Method
parent Method
parent Method
parent Method
child Method
'''









# parent  and  Child  classes  have  same  class   method
class parent:
	@classmethod
	def m1(cls):
		print('parent  Method')
class child(parent):
	@classmethod
	def m1(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1()
		m1()
		print('child  Method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class
'''
Outputs
parent  Method
parent  Method
parent  Method
parent  Method 
parent  Method
parent  Method
parent  Method infinite times 
recursion error
'''









# Parent  and  Child  classes  have  different  static  methods
class parent:
	@staticmethod
	def m1():
	    print('parent  method')
class child(parent):
	@staticmethod
	def m2():
		parent.m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super(child, child).m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super().m1() # Error, cannot use super() function in static method
		super(child).m1() # Error, cannot pass single argument to super function
		self . m1() # Error cannot use self in static method
		cls . m1() # Error cannot use cls in static method
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child.m1()
'''
Outputs
parent  method
parent  method
parent  method
parent  method
child method
parent method
'''









# Parent  and  Child  classes  have  same  static  method
class parent:
	@staticmethod
	def m1():
		print('parent  method')
class child(parent):
	@staticmethod
	def m1():
		parent(m1) # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child, child).m1() # How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super().m1() # Error, cannot use super() function without passing 2 argument to super() function
		self . m1() # Error, cannot use self in static method
		cls . m1() # Error, cannot use cls in static method
		print('child  method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class
'''
Outputs
parent method
parent method
parent method
child method
'''









# Parent  and  child  classes  have   static  variables  with  different  names
class parent:
	x = 10
	def m1(self):
		print(parent.x) # How  to  print  variable  'x'
		print(self.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x) # Error, there is no variable 'x' in method m1
# End  of  parent  class
class child(parent):
	y = 20
	def m2(self):
		print(parent.x) # How  to  print  variable  'x'
		print(child.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(super().x) # How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(self.x) # How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) # How  to  print  variable  'y'
		print(child.y) # How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # Error cannot use super for class method for accessing variable
		print(y) # Error, cannot access variable y without classname
# End  of child  class
p = parent()
p.m1() # How  to  call   m1()  method  of  parent  class
c = child() 
c.m2() # How  to  call   m2()  method  of  child  class
'''
Outputs
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
class parent:
	x = 10
	def m1(self):
		print(self.x) # How  to  print  variable  'x'  of  parent  class
		print(parent.x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class  child(parent):
	x = 20
	def m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(super().x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) # How  to  print  variable  'x'  of  child  class
		print(self.x) # How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent() 
p.m1() # How  to  call  m1()  method  of  parent  class
c = child()
c.m1() # How  to  call  m1()  method  of  child  class
'''
Outputs
10
10
10
10
20
20
'''









# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class parent:
	def get(self):
		self.a = int(input("Enter 1st input:")) 
		self.b = int(input("Enter 2nd input:")) # How  to   read  inputs  into   variables  a  and  b  of  object
	def disp(self):
		print(F'{self.a} \t {self.b}') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End of Parent class
class child(parent):
	def get(self):
		super().get() # How  to   read  inputs  into   variables  a  and  b  of  object
		self.c = int(input("Enter 1st input:")) 
		self.d = int(input("Enter 2nd input:")) # How  to   read  inputs  into   variables  c  and  d  of  object
	def disp(self):
		super().disp() # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(F'{self.c} \t {self.d}') # How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def total(self):
		return self.a + self.b + self.c + self.d # return sum  of  values  in  object  self
# End of child class
print('parent  object')
p = parent() 
p.get() # How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c = child() 
c.get() # How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp() # How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp() # How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,  c.total()) # How  to  obtain  sum of  values  of  object  'c'









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
		self. r = float(input("Enter radius:")) # How  to  read  radius  into  object
	def area(self):
		return math.pi * self.r ** 2 # return  area  of  circle
	def cir(self):
		return 2 * math.pi * self.r # return  circumference  of  circle
# End of circle class
class cylinder(circle):
	def get(self):
		super().get() # How  to  read  radius  into  object  self
		self.h = float(input("Enter height:")) # How  to  read  height  into  object  self
	def area(self):
		return 2 * super().area() + super().cir() * self.h # return   area  of  cylinder
	def volume(self):
		return super().area() * self.h # return   volume  of  cylinder
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
			c.get() # How  to  read  raidus  into  circle  object
			print('Area  : ' , c.area())
			print('Circumference : ' ,c.cir())
		case 2:
			c = cylinder() 
			c.get() # How  to  read  raidus  and  height  into  cylinder  object
			print('Area : ' , c.area())
			print('Volume :  ' , c.volume())
		case 3:
			exit() # How  to  stop  execution
	# End of match
'''
Outputs
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 1
Enter radius:5
Area  :  78.53981633974483
Circumference :  31.41592653589793
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 2
Enter radius:4
Enter height:6
Area :  251.32741228718345
Volume :   301.59289474462014
1 . Circle
2 . Cylinder
3 . Exit
Enter choice : 3
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
class square:
	def get(self):
		self.a = float(input("Enter side of square:")) # How  to  read  side  of  square
	def area(self):
		return self.a ** 2 # return   area  of  square
	def peri(self):
		return 4 * self.a # return   perimeter  of  square
class rectangle(square):
	def get(self):
		super().get() # How  to  read  length  of  rectangle
		self.b = float(input("Enter breadth of rectangle:")) # How  to  read  breadth  of  rectangle
	def area(self):
		return self.a * self.b # return   area  of  rectangle
	def peri(self):
		return 2 * (self.a + self.b) # return  perimeter  of   rectangle
class cube(square):
	def get(self):
		super().get() # How  to  read  side  of  cube
	def area(self):
		return 6 * super().area() # return  area  of  cube
	def volume(self):
		return super().area() * self.a # return  volume  of  cube
def menu():
	print('1 . Square')
	print('2 . Rectangle')
	print('3 . Cube')
	print('4 . Exit')
# End  of  the  function
while True:
	menu()
	ch = int(input('Enter  choice : '))
	match ch:
		case 1:
			s = square() 
			s.get() # How  to  read  side  into   square  object  's'
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' , s.peri())
		case 2:
			r = rectangle() 
			r.get() # How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' ,  r.peri())
		case 3:
			c = cube() 
			c.get() # How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  c.area())
			print('Volume  :  ' ,  c.volume())
		case 4:
			exit() # How  to  stop  execution
'''
Outputs
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 1
Enter side of square:5
Area   :   25.0
Perimeter  :   20.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 2
Enter length of rectangle:4
Enter breadth of rectangle:6
Area  :   24.0
Perimeter  :   20.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 3
Enter side of cube:6
Area  :    216.0
Volume  :   216.0
1 . Square
2 . Rectangle
3 . Cube
4 . Exit
Enter  choice : 4
'''









# Find  outputs
class c1:
	def m1(self):
		print('m1  method  of  class  c1')
class c2:
	def m1(self):
		print('m1 method of class c2')
class c3:
	@classmethod
	def m1(cls):
		print('m1 method of  class c3')
class c4:
	@staticmethod
	def m1():
		print('m1 method of  class c4')
class c5(c1):
	def m1(self):
		print('m1 method of class c5')
	def m2(self):
		c3.m1() # How  to  call  m1()  method  of  class  c3
		c4.m1() # How  to  call  m1()  method  of  class  c4
		a = c2() 
		a.m1() # How  to  call  m1()  method  of  class  c2
		b = c1() 
		b.m1() # How  to  call  m1()  method  of  class  c1
		c = c5() 
		c.m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def m1():
	print('m1 function')
# End  of  the  function
d = c5() 
d.m2() # How  to  call  m2()  method  of  class  c5
'''
Outputs
m1 method of  class c3
m1 method of  class c4
m1 method of class c2
m1  method  of  class  c1
m1 method of class c5
m1 function
'''









# Find  outputs
class c1:
    pass
class c2(c1):
    pass
# End of the class
print(issubclass(c2 , c1))
print(issubclass(int , float))
print(issubclass(str , object))
print(issubclass(c1 , object))
print(issubclass(c2 , object))
a = c1()
b = c2()
print(issubclass(b , a)) # Error, first argument must be class
print(issubclass(c2 , a)) # Error second argument must be class
'''
Outputs
True
False
True
True
True
'''
				 








# Find outputs
class c1:
    pass
class c2(c1):
    pass
class c3(c2):
    pass
class c4(c3):
    pass
print(issubclass(c4 , c3))
print(issubclass(c4 , c2))
print(issubclass(c4 , c1))
print(issubclass(c4 , object))
print(issubclass(c4 , (int , float , str , bool)))
print(issubclass(c4 , (int , float , c1 , str , bool)))
print(issubclass(c4 , [int , float , c1,str,bool])) # Error,second argument must be a tuple of classes
'''
Outputs
True
True
True
True
False
True
'''









#  Find  outputs
class c1:
    pass
class c2(c1):
    pass
class c3(c2):
    pass
class c4:
    pass
#  End  of  the  class
print(isinstance(25 , int))
print(isinstance(10.8 , float))
print(isinstance('Hyd' , str))
print(isinstance(3 + 4j , complex))
print(isinstance(True , bool))
print(isinstance(True , int))
print(isinstance('True' , str))
print(isinstance(True , str)) # Error True is instance of bool and int
print()
a = c3()
print(isinstance(a , c3))
print(isinstance(a , c2))
print(isinstance(a , c1))
print(isinstance(a , object))
print(isinstance(a , c4))
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) # Error, a is not object of int, float, str or bool
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))
print(isinstance(a , [int  ,  float  ,  c3 ,str , bool])) # Error, second argument must be tuple of classes
'''
Outputs
True
True
True
True
True
True
True
False

True
True
True
True
False
False
True
True
'''









# Write  a  program   to  determine  length  of  linked  list
from prog2 import *
class sll(linked_list):
	def length(a):
		ctr = 0
		p = a.first
		while p != None:
			ctr += 1
			p = p.link
		return ctr # return  number  of  nodes  in  the  linked  list
# End  of  the  class
if  __name__  ==  '__main__':
	l = sll() 
	l.create() # How  to  create  linked  list
	print('Number of nodes :',l.length())   
'''
Outputs
10
20
30
40
^Z
Number of nodes : 4
'''









'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''
from prog2a import *
class linkedlist(sll):
	def find(a , i):
		p = a.first
		ctr = 1
		while p != None:
			if ctr == i:
			    return p.data # return  data  of  ith  node
			else:
				p = p.link
				ctr += 1
		return None # return  None  when  ith  node  does  not  exist
# End  of  the  class
l = linkedlist() 
l.create() # How  to  create  linked  list
while True:
	i = int(input("Enter  value  of  'i':  "))
	data = l.find(i) # How  to   obtain  data  of  ith  node
	if data is None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {data}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good Bye')
'''
Outputs
Enter  values  terminated  by  ctrl+z
25
10.8
'Hyd'
True
3+4j
^Z
Enter  value  of  'i':  1
Data   of  node  1  is  :  25
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  2
Data   of  node  2  is  :  10.8
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  3
Data   of  node  3  is  :  Hyd
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  4
Data   of  node  4  is  :  True
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  5
Data   of  node  5  is  :  (3+4j)
Do  you  wish  to  continue (y / n) :  y
Enter  value  of  'i':  6
Node  6  does  not  exist
Do  you  wish  to  continue (y / n) :  n
Good Bye
'''









'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''
from prog2a import *
class sll(linked_list):
	def search(a , x):
		p = a.first
		while p != None:
			if p.data == x:
				break
			else:
				p=p.link
		if p == None:
			return None
		else:
			return p # return  address  of  that  node  where  'x'  is  found  and  None  otherwise
# End  of  the  class
s = sll() # How  to  create  linked  list
s.create() 
while True:
	x = eval(input("Enter  value  to  be  searched :  "))
	s.search(x) # How  to  call  search()  method
	if s.search(x) is None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  {s.search(x)}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good Bye')
'''
Outputs
Enter  values  terminated  by  ctrl+z
25
10.8
'Hyd'
True
3+4j
^Z
Enter  value  to  be  searched :  True
Found  at  address  :  <prog2.node object at 0x0000021B3F7C9E00>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  3+4j
Found  at  address  :  <prog2.node object at 0x0000021B3F7CB820>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  'Hyd'
Found  at  address  :  <prog2.node object at 0x0000021B3F9E8E10>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  25
Found  at  address  :  <prog2.node object at 0x0000021B3F7574D0>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  10.8
Found  at  address  :  <prog2.node object at 0x0000021B3F9E8CD0>
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  10
10  is  not  found
Do  you  wish  to  continue (y / n) :  y
Enter  value  to  be  searched :  15
15  is  not  found
Do  you  wish  to  continue (y / n) :  n
Good Bye
'''









'''
Write  a  method  to  insert  a  node  in  the  linked  list
1) How  many  links  have  to  be  modified  for  insertion ?  --->  Two  links

2) How  to  insert  a  node  at  the  begining  of  linked list ?  --->  Modify  new  node  link  to  1st  node
																														and
																										modify  the  reference  a . first  to  new  node

3) How  to  insert  a  node  at  the  end  of  linked list ?  --->  Modify  new  node  link  to  None
																												and
																								modify  last  node  link  to  new  node

4) How  to  insert  a  node  after  ith  node ?  --->  Modify  new  node  link  to  (i + 1)th  node  and
																		        modify  ith  node  link   to  new  node

5) In  which  order  can  links  be  modified ?  --->  Modify  new  node  link  first  and  then  existing  node  link

6) Is  logic  same  for  middle  insertion  and  insertion  at  the  end  ? --->  Yes

7) What  is  the  difference  between  insertion  at  the  begining  and  insertion  anywhere  else ?  --->
															a . first  is  modified  when  node  is   inserted  at  the  begining  and
															a . first  reference  remains  unchanged  when  node  is   inserted  anywhere  else
'''
from prog2a import *
class linkedlist(sll):
	def insert(a , i , x):
		if i <= 0: # if  'i'  is  an  invalid  node  number:
			print(F'Node  {i}  does  not  exist')
			return
		new = node(x)
		if i == 1: # elif  insertion  at  the  begining  of  LL:
			new.link = a.first # How  to  create  a  new  node
			a.first = new # How  to  insert  new  node  at  the  begining  of  LL
		else:
			p = a.first # How  to  create  a  new  node
			for _ in range(i - 1):
				if p is None:
					print(F'Node {i} does not exist')
					return
				p = p.link # How  to  insert  new  node  after  ith  node  of  LL
			if p is None:
				print(F'Node {i} does not exist')
				return
			new.link = p.link
			p.link = new
# End  of  the  class
l = linkedlist() # How  to  create  a  linked  list
l.create()
while True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	l.insert(i, x) # How  to  insert   new  node  after   ith  node
	print('Linked  List  :  ' , end = '')
	l.disp() # How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
'''
Outputs
Enter  values  terminated  by  ctrl+z
25
10.8
'Hyd'
True
3+4j
^Z
Enter  value  of  'i' :  2
Enter  value  to  be  inserted  :  False
Linked  List  :  25     10.8    False   Hyd     True    (3+4j)
Would  you  like  to  insert  another  node (Y  or   N) ?  :  y
Enter  value  of  'i' :  5
Enter  value  to  be  inserted  :  15
Linked  List  :  25     10.8    False   Hyd     True    15      (3+4j)
Would  you  like  to  insert  another  node (Y  or   N) ?  :  n
'''









'''
Write  a method  to  delete  ith  node  of  linked  list

1) How  many  links  have  to  be  modifed  for  deletion ?  --->  Single  link

2) How  to  remove  ith  node  of  linked list ?  --->  Modify  (i - 1)th  node  link  to  (i + 1)th  node

3) How  to  remove  first  node  of  linked list ?  --->  Move  a . first  to  2nd  node

4) How  to  remove  last  node  of  linked list ?  --->  Modify  last  but  one  node  link  to  None

5) How  to  remove  the  node  when  there  is  a  single  node  in  linked  list  ?  --->  Reinitialize  a . first  to  None

6) Logic  for  middle  node  and  last  node  deletion  is  same

7) Similarly  logic  for  first  node  and  single  node  deletion  is  same
'''
from prog2a import *
class linkedlist(sll):
	def delete(a , i):
		if i <= 0 or a.first is None: # if  'i'  is  an  invalid  node  number:
			return None
		elif i == 1: #deletion of  1st  node:
			deleted_data = a.first # How  to  delete  first  node  logically
			a.first = a.first.link #How  to  delete  first  node  physically
			return deleted_data.data  # How  to  return  data  of  the  deleted  node
		else:
			p = a.first
			for _ in range(i - 2):
				if p is None:
					return None
				p = p.link
			if p is None or p.link is None:
				return None
			deleted_data = p.link
			p.link = deleted_data.link
			return deleted_data.data
# End  of  the  class
l = linkedlist() 
l.create() # How  to  create  linked  list
while True:
	i = int(input('Enter  value  of  i  :  '))
	deleted_data = l.delete(i) # How  to  delete  ith  node
	if deleted_data is None:
		print(F'Node  {i}  does  not  exist')
	else:
		print('Data  of  deleted  node  is  ' ,  deleted_data)
	print('Linked  List  :  ' , end = '')
	l.disp() # How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break
'''
Outputs
Enter  values  terminated  by  ctrl+z
10
20
30
40
^Z
Enter  value  of  i  :  2
Data  of  deleted  node  is   20
Linked  List  :  10     30      40
Would  you  like  to  delete  another  node (Y  or   N) ?  :  y
Enter  value  of  i  :  5
Node  5  does  not  exist
Linked  List  :  10     30      40
Would  you  like  to  delete  another  node (Y  or   N) ?  :  y
Enter  value  of  i  :  3
Data  of  deleted  node  is   40
Linked  List  :  10     30
Would  you  like  to  delete  another  node (Y  or   N) ?  :  n
'''