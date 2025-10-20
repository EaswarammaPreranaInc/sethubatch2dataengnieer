#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() # How  to  call  function  m1()
		#self . m1()
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
a = parent() 
a.m1() # How  to  call  m1()  method  of  parent  class
b = child() 
b.m1() # How  to  call  m1()  method  of  child  class

'''
parent  Method
parent  Method
m1  function
child  Method
'''



# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1() # error
		#m1() # error 
		print('child  Method')
# End  of  the  class
a = parent() 
a.m1() # How  to  call  m1()  method  of  parent  class
b = child() 
b.m2() # How  to  call  m2()  method  of  child  class
child . m1()
#super() . m1()
#self . m1()



# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1()
		#self . m1()
		#m1()
		print('child  Method')
# End  of  the  class
a = parent() 
a.m1() # How  to  call  m1()  method  of  parent  class
b = child() 
b.m1() # How  to  call  m1()  method  of  child  class

'''
parent  Method
parent  Method
parent  Method
child  Method
'''


# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super(child,child).m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() # How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() # How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		#super() . m1() # error
		#super(child).m1() # error
		#self . m1() # error 
		#cls . m1() # error
		print('child  method')
#end of the class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m2() # How  to  call  m2()  method  of  child  class
child . m1()

'''
parent  method
parent  method
parent  method
parent  method
child  method
parent  method
'''


# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() # How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1() # How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		#super() . m1()
		#self . m1()
		#cls . m1()
		print('child  method')
# End  of  the  class
parent.m1() # How  to  call  m1()  method  of  parent  class
child.m1() # How  to  call  m1()  method  of  child  class

'''
parent  method
parent  method
parent  method
child  method
'''


# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'
		print(self.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x) # error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x) # How  to  print  variable  'x'
		print(child.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(self.x) # How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x) # How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y) # How  to  print  variable  'y'
		print(self.y) # How  to  print  variable  'y'  in  another  way  without  creating  an  object
		#print(super() . y) # error
		#print(y) # error
# End  of child  class
a = parent()
a.m1() # How  to  call   m1()  method  of  parent  class
b = child() 
b.m2() # How  to  call   m2()  method  of  child  class


# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(self.x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(parent.x) # How  to  print  variable  'x'  of  parent  class
		print(super().x) # How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x) # How  to  print  variable  'x'  of  child  class
		print(self.x) # How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
p = parent() 
p.m1() # How  to  call  m1()  method  of  parent  class
c = child() 
c.m1() # How  to  call  m1()  method  of  child  class



#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		self.a = int(input('enter any number:')) 
		self.b = int(input('enter any number:'))# How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(self.a,self.b,sep = '\t', end = '\t') # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		super().get() # How  to   read  inputs  into   variables  a  and  b  of  object
		self.c = int(input('enter any number:')) 
		self.d = int(input('enter any number:'))# How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		super().disp() # How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d,sep = '\t') # How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		return self.a + self.b + self.c + self.d # sum  of  values  in  object  self
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
print('Sum of  the  values  in  child  object :  ' ,  c.total()) # How  to  obtain  sum of  values  of  object  'c'



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
	    self.r = int(input('Enter radius:')) # How  to  read  radius  into  object
	def   area(self):
		return 3.14159 * math.pow(self.r, 2) # return  area  of  circle
	def   cir(self):
		return 2 * 3.14159 * self.r # return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r = int(input('Enter radius:')) # How  to  read  radius  into  object  self
		self.h = int(input('Enter height:')) # How  to  read  height  into  object  self
	def  area(self):
		return (2 * super().area()) + (super().cir() * self.h) # return   area  of  cylinder
	def  volume(self):
		return   (super().area() * self.h) # volume  of  cylinder
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
				a = circle() 
				a.get() # How  to  read  raidus  into  circle  object
				print('Area  :  ' , a.area())
				print('Circumference :  ' , a.cir())
		case  2:
				b = cylinder() 
				b.get() # How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  b.area())
				print('Volume :  ' , b.volume())
		case  3:
				exit() # How  to  stop  execution
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
		self.s = int(input('Enter side:')) # How  to  read  side  of  square
	def   area(self):
		return self.s ** 2 # return   area  of  square
	def   peri(self):
		return self.s * 4 # return   perimeter  of  square
class   rectangle(square):
	def   get(self):
		self.l = int(input('Enter length:')) # How  to  read  length  of  rectangle
		self.b = int(input('Enter breadth:')) # How  to  read  breadth  of  rectangle
	def   area(self):
		 return self.l * self.b # return   area  of  rectangle
	def   peri(self):
		return 2 * (self.l + self.b) # return  perimeter  of   rectangle
class   cube(square):
	def   get(self):
		 self.s = int(input('Enter side:')) # How  to  read  side  of  cube
	def   area(self):
		return 6 * self.s ** 2 # return  area  of  cube
	def   volume(self):
		return self.s ** 3 # return  volume  of  cube
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
			s = square() 
			s.get() # How  to  read  side  into   square  object  's'
			print('Area   :  ' , s.area())
			print('Perimeter  :  ' ,  s.peri())
		case   2:
			r = rectangle() 
			r.get() # How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' , r.peri())
		case   3:
			c = cude() # How  to  read  side  into  cube  object  'c'
			print('Area  :   ' , c.area())
			print('Volume  :  ' , c.volume())
		case  4:
			exit() # How  to  stop  execution





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
		c3.m1() # How  to  call  m1()  method  of  class  c3
		c4.m1() # How  to  call  m1()  method  of  class  c4
		c = c2()
		c.m1() # How  to  call  m1()  method  of  class  c2
		super().m1() # How  to  call  m1()  method  of  class  c1
		self.m1() # How  to  call  m1()  method  of  class  c5
		m1() # How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
a = c5()
a.m2() # How  to  call  m2()  method  of  class  c5


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
#print(issubclass(b , a)) # error
#print(issubclass(c2 , a)) # error


# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) # true
print(issubclass(c4 , c2)) # true
print(issubclass(c4 , c1)) # true
print(issubclass(c4 , object)) # true
print(issubclass(c4 , (int , float , str , bool))) # false
print(issubclass(c4 , (int , float , c1 , str , bool))) # true
print(issubclass(c4 , [int , float , c1 , str , bool])) # error



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
print(isinstance(25 , int)) # true
print(isinstance(10.8 , float)) # true
print(isinstance('Hyd' , str)) # true 
print(isinstance(3 + 4j , complex)) # true
print(isinstance(True , bool)) # true
print(isinstance(True , int)) # true
print(isinstance('True' , str)) # true
print(isinstance(True , str)) # false
print()
a = c3()
print(isinstance(a , c3)) # true
print(isinstance(a , c2)) # true
print(isinstance(a , c1)) # true
print(isinstance(a , object)) # true
print(isinstance(a , c4)) # false
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) # false
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool))) # true
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) # true
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) # false



#  Write  a  program   to  determine  length  of  linked  list

from linked_list import *

class  sll(linked_list):
	def  length(a):
		p = a.first
		ctr = 0
		while p != None:
			ctr+=1
			p = p.link
		return ctr # return  number  of  nodes  in  the  linked  list
# End  of  the  class


if  __name__  ==  '__main__':
	a = sll()
	a.create() # How  to  create  linked  list
	print('Number  of  nodes : ' , a.length())



'''
Write  a  progam  to  determine  data  of  ith  node

1) What  does  method  do  when  ith  node  exists ?  --->  Return  data  of  ith  node

2) What  does  method  do  when  ith  node  does  not  exist ?  --->  Return  None
'''

from prog1a import *

class   linkedlist(sll):
	def  find(a , i):
		if i<1 or i>a.length():
			return None
		p = a.first
		for j in range(i-1):
			p = p.link
		return p.data # return  data  of  ith  node and  return  None  when  ith  node  does  not  exist
		
# End  of  the  class
a = linkedlist() 
a.create() # How  to  create  linked  list
while  True:
	i = int(input("Enter  value  of  'i':  "))
	x = a.find(i) # How  to   obtain  data  of  ith  node
	if x == None:
		print(F'Node  {i}  does  not  exist')
	else:
		print(F'Data   of  node  {i}  is  :  {x}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')


'''
Write  a  method  to  search  for  a  value  in  the  linked  list.

1) What  action  to  be  made  when  'x'  is  not  in  the  node  of  linked  list ?  --->  Move  reference  to  the  next  node

2) What  action  to  be  made  when  'x'  is  in  the  current  node  ?  --->  Return  address  of  that  node

3) What  action  to  be  made  when  'x'  is  not  found  in  the  linked  list  ?  --->  return  None  outside  the  loop
'''

from linked_list import *
class  sll(linked_list):
	def  search(a , x):
		p = a.first
		while p!= None:
			if p.data == x:
				return p
			else:
				p = p.link
		return None # return  address  of  that  node  where  'x'  is  found  and  None  otherwise
# End  of  the  class
a = sll() # initializes a.first to none
a.create() # How  to  create  linked  list
while  True:
	x = eval(input("Enter  value  to  be  searched :  "))
	p = a.search(x) # How  to  call  search()  method
	if  p == None:
		print(F'{x}  is  not  found')
	else:
		print(F'Found  at  address  :  {pp}')
	ch = input('Do  you  wish  to  continue (y / n) :  ')
	if  ch == 'N'  or  ch == 'n':
			break
# End  of  while  loop
print('Good  Bye')


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
from prog1a import *
class  linkedlist(sll):
	def  insert(a , i , x):
		if  i < 0 or i>a.length(): # 'i'  is  an  invalid  node  number:
				print(F'Node  {i}  does  not  exist')
		elif  i == 0: # insertion  at  the  begining  of  LL:
				new = node(x) # How  to  create  a  new  node
				new.link = a.first # How  to  insert  new  node  at  the  begining  of  LL
				a.first = new
		else:
			new = node(x) # How  to  create  a  new  node
			p = a.first # How  to  insert  new  node  after  ith  node  of  LL
			for j in range(i - 1):
				p = p.link
			new.link = p.link
			p.link = new
# End  of  the  class
a = linkedlist() 
a.create() # How  to  create  a  linked  list
while  True:
	i = int(input("Enter  value  of  'i' :  "))
	x = eval(input('Enter  value  to  be  inserted  :  '))
	a.insert(i,x) # How  to  insert   new  node  after   ith  node
	print('Linked  List  :  ' , end = '')
	a.disp() # How  to  print  linked  list
	ch = input('Would  you  like  to  insert  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break



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
from prog1a import *
class  linkedlist(sll):
	def  delete(a , i):
		if  i < 0 or i>a.length(): # 'i'  is  an  invalid  node  number:
			return  None
		elif  i == 1: # deletion of  1st  node
			p = a.first
			a.first = a.first.link #How  to  delete  first  node  logically
			del p #How  to  delete  first  node  physically
			return p.data # How  to  return  data  of  the  deleted  node
		else:
			 temp = a.first
			 j = 1
			 while j < i - 1:
				 temp = temp.link
				 j += 1
                # temp is (i-1)th node
			 p = temp.link               # ith node
			 temp.link = p.link          # (i-1)th node now points to (i+1)th
			 data = p.data
			 del p
			 return data
			#How  to  modify  (i - 1)th  node  link  to  (i + 1)th node
			#How  to  delete  ith  node
			#How  to  return  data  of  the  deleted  node
# End  of  the  class
c = linkedlist() #How  to  create  linked  list
c.create() 
while  True:
	i = int(input('Enter  value  of  i  :  '))
	d = linkedlist() # How  to  delete  ith  node
	a = d.delete(i)
	if  a:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  c.delete(i))
	print('Linked  List  :  ' , end = '')
	c.disp() # How  to  print  linked  list
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break