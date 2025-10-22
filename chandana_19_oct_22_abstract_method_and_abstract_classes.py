# Find  outputs 
from  abc  import  *
class  c1(ABC): # abstract class beacuse it has abstract method
	@abstractmethod
	def  m1(self): 
		pass
	def  __init__(self):
		print('c1  class  constructor')
class  c2(ABC): # c2 inherits from ABC, but m1() is a concrete method
	def  m1(self):
		pass
	def  __init__(self):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(self):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(self):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(self):
		print('c1  class  constructor')
# End  of  the  class
#c1() # cannot create object for c1 class as it is abstract class
c2()
c3()
c4()
#c5() # error


'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  ---> sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  ---> a * b  where  'a'  is  length and  'b'  is  breadth
     What  is  the  perimter  of  rectangle ?  --->2 * (a + b)

5) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square  ?  ---> 4 * a
'''
import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		pass 
	@abstractmethod
	def   area(self):
		pass
	@abstractmethod
	def  peri(self):
		pass
	@abstractmethod
	def  test(self):
		pass
class  triangle(shape):
	def   get(self):
		print('Enter  3  sides  of  triangle')
		self.a=float(input('Enter side a :')) 
		self.b=float(input('Enter side b :'))
		self.c=float(input('Enter side c :')) #   read  the  3  sides  of  triangle
	def   area(self):
		s=(self.a+self.b+self.c)/2
		return   math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)) # area  of  triangle
	def   peri(self):
		return  self.a+self.b+self.c # perimeter  of  triangle
	def   test(self):
		if  (self.a+self.b >self.c) and (self.b+self.c>self.a) and (self.c+self.a>self.b): # sum  of  every  2  sides  should  be  >   3rd   side
			pass 
		else:
			print('Not a triangle')
			exit() #  stop execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		self.a=float(input()) # read  radius
	def   area(self):
		return  3.14159*self.a**2 # area  of  circle
	def   peri(self):
		return  2*3.14159*self.a # circumference  of circle
	def  test(self):
		if  self.a<0:# side  is  -ve
			print('Radius  can  not  be  -ve')
			exit() #  stop execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		self.a=float(input('Enter length :'))
		self.b=float(input('Enter breadth :')) # read length  and  breadt
	def   area(self):
		return  self.a*self.b # area of rectangle
	def   peri(self):
		return  2*(self.a+self.b) # perimeter of triangle
	def  test(self):
		if  self.a==self.b:
			print('Not  a rectangle')
			exit() # stop execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		self.a=float(input()) # read the side
	def   area(self):
		return  self.a**2 # area of square
	def   peri(self):
		return  4*self.a # perimeter  of  square
	def  test(self):
		pass
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	s.get() #   read  inputs  to  object  's'
	s.test() #   test  inputs  are  valid (or) not
	print('Area  :  ' , s.area())
	print('Perimeter  :  ' ,s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
			operation(triangle())
		case  2:
			operation(circle()) 
		case  3:
			operation(rectangle()) 
		case  4:
			operation(square()) 
		case  5:
			break
print('Good  Bye')



# Find  outputs 
from abc import *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m1()
a . m2()
a . m3()
#parent() # error
#child() # error
#gc() # error
'''
o/p:
m1  method  of  child  class
m2  method  of    gc  class
m3  method  of  ggc  class
'''