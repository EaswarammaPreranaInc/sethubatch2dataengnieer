class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() #How  to  call  function  m1()
		self . m1()	# recursion
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent()
p.m1() #How  to  call  m1()  method of  parent  class
c=child() 
c.m1() #How  to  call  m1()  method of  child  class

class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # error
		m1() # error
		print('child  Method')
# End  of  the  class
p=parent() 
p.m1() #How  to  call  m1()  method  of  parent  class
c=child() 
c.m2() #How  to  call  m2()  method  of  child  class
child . m1()
super() . m1() # error
self . m1() # error

class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1()	# recursion error
		#self . m1() # error
		m1()
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class

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
		#super() . m1()	# error
		#super(child).m1()	# error
		#self . m1() # Error
		#cls . m1() # Error
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2() #How  to  call  m2()  method  of  child  class
child . m1()

class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child,child).m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		#super() . m1()	# error
		#self . m1()	# error
		#cls . m1()	# error
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class

class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'
		print(self.x) # How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x) # error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x) #How  to  print  variable  'x'
		print(child.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(self.x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(super().x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(child.y) #How  to  print  variable  'y'
		print(self.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		#print(super() . y) # error
		#print(y) # error
# End  of child  class
p=parent()
p.m1() #How  to  call   m1()  method  of  parent  class
c=child()
c.m2() #How  to  call   m2()  method  of  child  class

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
p=parent()
p.m1() #How  to  call  m1()  method  of  parent  class
c=child()
c.m1() #How  to  call  m1()  method  of  child  class

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

Q) Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder
Ans) import  math
class   circle:
	def   get(self):
	    self.r=int(input('enter radius:')) #How  to  read  radius  into  object 
	def area(self):	
		return  3.14159 * (self.r ** 2) #area  of  circle
	def   cir(self):
		return  2 * 3.14159 * self.r #circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r=int(input('enter radius:')) #How  to  read  radius  into  object  self
		self.h=int(input('enter height:')) #How  to  read  height  into  object  self
	def  area(self):
		return 2 * 3.14159 * (self.r ** 2) + 2 * 3.14159 * self.r * self.h  #area  of  cylinder
	def  volume(self):
		return  3.14159 * (self.r ** 2) *  self.h #  volume  of  cylinder
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
				c.get() #How  to  read  raidus  into  circle  object
				print('Area  :  ' , c.area())
				print('Circumference :  ' , c.cir())
		case  2:
				c=cylinder() 
				c.get() #How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  c.area())
				print('Volume :  ' , c.volume())
		case  3:
				break #How  to  stop  execution
	# End  of  match

Q) Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube
Ans) class   square:
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
		c3.m1() #How  to  call  m1()  method  of  class  c3
		c4.m1() #How  to  call  m1()  method  of  class  c4
		c2().m1() #How  to  call  m1()  method  of  class  c2
		c1().m1() #How  to  call  m1()  method  of  class  c1
		c5().m1() #How  to  call  m1()  method  of  class  c5
		m1() #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c=c5()
c.m2() #How  to  call  m2()  method  of  class  c5

class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1)) # True
print(issubclass(int , float))  # False
print(issubclass(str , object)) # True
print(issubclass(c1 , object))  # True
print(issubclass(c2 , object))  # True
a = c1()
b = c2()
print(issubclass(b , a))        #error bcz arg1  should be class
print(issubclass(c2 , a))       # error bcz arg 2 should class or tuple of classes

class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))      # true
print(issubclass(c4 , c2))      # True
print(issubclass(c4 , c1))      # true
print(issubclass(c4 , object))  # true
print(issubclass(c4 , (int , float , str , bool)))      # false
print(issubclass(c4 , (int , float , c1 , str , bool))) # True
print(issubclass(c4 , [int , float , c1 , str , bool])) # error it should be the class or tuple of classes

class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int))     # true
print(isinstance(10.8 , float)) # True
print(isinstance('Hyd' , str))  # True
print(isinstance(3 + 4j , complex))     # True
print(isinstance(True , bool))  # true
print(isinstance(True , int))   # True
print(isinstance('True' , str)) # true
print(isinstance(True , str))   # False
print()
a = c3()
print(isinstance(a , c3))       # true
print(isinstance(a , c2))       # True
print(isinstance(a , c1))       #  True
print(isinstance(a , object))   #  True
print(isinstance(a , c4))       # False
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) # False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))  # True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) # True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) # error

Write  a  program   to  determine  length  of  linked  list
from Linkedlist import *
class  sll(linked_list):
    def  length(self):
        count=0
        p=self.first
        while p:
            count+=1
            p=p.link
        return  count
if  __name__  ==  '__main__':
    a=sll()
    a.create()
    a.disp()
    print('Number  of  nodes : ' , a.length())

Write  a  progam  to  determine  data  of  ith  node
from Lengthoflinkedlist import *
class linkedlist(sll):
    def find(self, i):
        p = self.first
        count = 1
        while p is not None:
            if count == i:
                return p.data
            p = p.link
            count += 1
            return None
if __name__ == '__main__':
    a = linkedlist()
    a.create()
    print('\nLinked List:', end=' ')
    a.disp()
    while True:
        i = int(input("\nEnter value of 'i': "))
        data = a.find(i)
        if data is None:
            print(f'Node {i} does not exist')
        else:
            print(f'Data of node {i} is: {data}')
        ch = input('Do you wish to continue (y / n): ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

Write  a  method  to  search  for  a  value  in  the  linked  list.
from Linkedlist import *
class sll(linked_list):
    def search(self, x):
        p = self.first
        while p is not None:
            if p.data == x:
                return p  
            p = p.link
        return None  
if __name__ == '__main__':
    a = sll()
    a.create()
    print('\nLinked List:', end=' ')
    a.disp()
    while True:
        x = eval(input("\nEnter value to be searched: "))
        p = a.search(x)
        if p is None:
            print(f'{x} is not found')
        else:
            print(f'Found at address: {id(p)}')  
        ch = input('Do you wish to continue (y / n): ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

Write  a  method  to  insert  a  node  in  the  linked  list
from Lengthoflinkedlist import *
from Linkedlist import *
class linkedlist(sll):
    def insert(self, i, x):
        n = self.length()  
        if i < 0 or i > n:
            print(f'Node {i} does not exist')
            return
        new = node(x)
        if i == 0:
            new.link = self.first
            self.first = new
        else:
            p = self.first
            count = 1
            while count < i and p is not None:
                p = p.link
                count += 1
            if p is None:  
                print(f'Node {i} does not exist')
                return
            new.link = p.link
            p.link = new
if __name__ == '__main__':
    a = linkedlist()
    a.create()
    while True:
        i = int(input("\nEnter value of 'i' : "))
        x = eval(input('Enter value to be inserted : '))
        a.insert(i, x)
        print('Linked List : ', end='')
        a.disp()
        ch = input('Would you like to insert another node (Y or N)? : ')
        if ch.lower() == 'n':
            break
    print('Good Bye')

Write  a method  to  delete  ith  node  of  linked  list
from Linkedlist import *
from Lengthoflinkedlist import *
class linkedlist(sll):
    def delete(self, i):
        n = self.length()
        if i <= 0 or i > n:
            return None
        if i == 1:
            deleted_data = self.first.data
            self.first = self.first.link  
            return deleted_data
        p = self.first
        count = 1
        while count < i - 1 and p is not None:
            p = p.link
            count += 1
        if p is None or p.link is None:
            return None  
        deleted_data = p.link.data
        p.link = p.link.link  
        return deleted_data
if __name__ == '__main__':
    a = linkedlist()
    a.create()
    while True:
        i = int(input('\nEnter value of i : '))
        data = a.delete(i)
        if data is None:
            print(f'Node {i} does not exist')
        else:
            print('Data of deleted node is:', data)

        print('Linked List : ', end='')
        a.disp()
        ch = input('Would you like to delete another node (Y or N)? : ')
        if ch.lower() == 'n':
            break
    print('Good Bye')
