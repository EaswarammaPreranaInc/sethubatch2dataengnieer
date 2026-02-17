#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()
x . m1() #overridden method
x = child()
x . m1() #overriding method

# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
#end of the class
c = child()
c . marriage() #Love marriage
c . property() #one crore
c . study()# studies only + Entertainment

# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
#end of the class
x = parent()
x . m1() #m1  method  of  parent  class
x . m2() #m2  method  of  parent  class
x . m3() #error
x = child()
x . m1() #m1  method  of  child  class
x . m2() #m2  method  of  parent  class
x . m3() #m3  method  of  child class

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30)) #60
print(c . add(10 , 20)) #error
print(super(child , c) . add(40,50)) #90

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child()
print(c . add(10 , 20 , 30)) #child method, 60
print(c . add(10 , 20)) #child method, 33

#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20) # child method--> x:10  y:20
c . m1(30 , 40) #child method--> x:30  y:40

# Find  outputs (Home  work)
from  abc  import  *
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
c1() #error
c2()#c2 class constructor 
c3()#error , has a abstract method
c4() #c4 class constructor
c5() #c1 class constructor

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
		#  How  to  read  value  of  'a'
		self.a=int(input("Enter a: "))
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
		# How  to  read  the  3  sides  of  triangle
		super().get()
		self.b=int(input("Enter b: "))
		self.c=int(input("Enter c: "))
	def   area(self):
		s=(self.a+self.b+self.c)/2
		return   math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def   peri(self):
		return  self.a+self.b+self.c #perimeter  of  triangle
	def   test(self):
		if  self.a+self.b> self.c or self.b+self.c>self.a or self.a+self.c>self.b #sum  of  every  2  sides  should  be  >   3rd   side
				pass
		else:
			print('Not    a  triangle')
			exit() #How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super().get() #How  to  read  radius
	def   area(self):
		return  math.pi*self.a*self.a #area  of  circle
	def   peri(self):
		return  2*math.pi*self.a #circumference  of circle
	def  test(self):
		if  self.a  <0:
		    print('Radius  can  not  be  -ve')
		    exit() #How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super().get() 
		self.b=int(input("Enter breadth:")) #How  to  read  length  and  breadt
	def   area(self):
		return  self.a*self.b #area  of  rectangle
	def   peri(self):
		return  2*(self.a+self.b) #perimeter  of  triangle
	def  test(self):
		if  self.a==self.b:
		    print('Not  a rectangle')
		    exit() #How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super().get() #How  to  read  the  side
	def   area(self):
		return  self.a*self.a #area  of  square
	def   peri(self):
		return  4*self.a #perimeter  of  square
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
	s.get() #How  to  read  inputs  to  object  's'
	s.test() #How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' ,  s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				t=triangle() 
				operation(t)
				#How  to  call  operation()  function
		case  2:
				c=circle() #How  to  call  operation()  function
				operation(c)
		case  3:
				r=rectangle() #How  to  call  operation()  function
				operation(r)
		case  4:
				s=square() #How  to  call  operation()  function
				operation(s)
		case  5:
				exit() #How  to  stop  execution
	# End  of  match
# End of while  loop
print('Good  Bye')

# Find  outputs (Home  work)
from   abc    import    *
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
a . m1()#m1  method  of  child  class
a . m2() #m2  method  of  gc class
a . m3() #m3  method  of  gcc  class
parent() #error
child()#error
gc() #error