#  Find  outputs  (Home  work)
class  parent: #Here parent class is created 
	def  m1(self): #Here m1 method is defined
		print('Overridden  Method')
class  child(parent): #Here Child class is inheriting the parent class
	def  m1(self): #Here m2 is defined
		print('Overriding  Method')
#end of the class
x = parent() #Here parent class object is created
x . m1() #Here m1 method of parent class is called
x = child() #Here child class object is created
x . m1() #Here child class m1 method is created
'''output:
Overridden Method
Overriding Method'''



# Find  outputs   (Home  work)
class   parent: #Here parent class is created
	def  m1(self): #Here m1 method is defined
		print('m1  method  of  parent  class')
	def  m2(self): #Here m2 method id defined
		print('m2  method  of  parent class')
class  child(parent): #Here child class is inheriting the parent class
	def  m1(self): #Here m1 method is defined 
		print('m1  method  of  child  class')
	def  m3(self): #Here m2 method is defined
		print('m3  method  of  child  class')
#end of the class
x = parent() #Here parent class object is created
x . m1() #Here m1 method of parent class is called
x . m2() #Here m2 method of parent class is called
#x . m3() #Error #there is no m3 method in parent class
x = child() #Here child class obj is created
x . m1()  #Here m1 method of child class is called
x . m2() #Here m2 method is searched in child class if not there then parent class m2 method is called
x . m3() #Here child class m3 method is called
'''output:
m1  method  of  parent  class
m2  method  of  parent  class
m1  method  of  parent  class
m2  method  of  parent  class
m3  method  of  parent  class
'''


# Find  outputs  (Home  work)
class  parent: #Here parent class is created
	def  marriage(self): #Here marriage method is defined
		print('Arranged Marriage')
	def  property(self): #Here property method is defined
		print('One  Crore')
	def  study(self): #Here study method is defined
		print('Studies only' , end = '\t')
class  child(parent): #Here child class is inheriting the parent class
	def  marriage(self): #Here marriage method is defined 
		print('Love Marriage')
	def  study(self): #Here study method is defined
		super() . study() #Here study method of parent class is called
		print(' + Entertainment')
#end of the class
c = child() #Here child class object is created
c . marriage() #Here marriage method of child class is called
c . property() #Here property method is searched in child class but not there so parent class property method is called
c . study() #Here study method of child class is called
'''output:
Love Marriage
One crore
Studies only 	+ Entertainment'''



# Find  outputs  (Home  work)
class  parent: #Here parent class is created
	def  add(self , x , y): #Here add method is defined with 2 arguments
		return  x + y #add method returns the addition of 2 argument values
class  child(parent): #Here child class is inherited by child class
	def   add(self , x , y , z): #Here add method is defined with 3 arguments
		return   x + y + z #add method returns the addition of 3 argument values
# End of the class
c = child() #Here child class object is created
print(c . add(10 , 20 , 30)) #Here add method of child class is called with arguments 10 20 30
#print(c . add(10 , 20)) #Error #in child class add method is expecting 3 arguments but 2 given
print(super(child , c) . add(40,50)) #Here add method of parent class is called
'''outputs:
60
90
'''



 # Find  outputs  (Home  work)
class  parent: #Here parent class is created
	def  add(self , x , y): #Here add method is defined with 2 arguments
		print('parent  method')
		return  x + y #add method is returning the addition of 2 arguments values
class  child(parent): #Here child class is inheriting the parent class
	def   add(self , x , y , z = 3): #Here add method is defined with 3 arguments and for one argument default value is given 
		print('child  method')
		return  x + y + z #Here add method returns the addition of 3 argument values
#End  of  the  class
c = child() #Here child class object is created
print(c . add(10 , 20 , 30)) #Here add method of child class is called with 3 values 10 20 30 
print(c . add(10 , 20)) #Here add method of child class is called with 2 values 10 20 and another argument default value is taken
'''output:
Child method
60
Child method
33
'''



#Find  outputs  (Home  work)
class  parent: #Here parent class is created
	def   m1(self , a , b , /): #Here m1 method is defined with 2 arguments they are only positional arguments
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent): #Here child class is inheriting the parent class
	def   m1(self , x , y): #Here m1 method is defined with 2 arguments
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child() #Here child class object is created
c . m1(x = 10 , y = 20) #Here m1 method of child class is called with keyword arguments
c . m1(30 , 40) #Here m1 method of child class is called with positional arguments
'''outputs:
Child method ---> x : 10	y : 20
Child method ---> x : 30	y : 40
'''




 # Find  outputs (Home  work)
from  abc  import  * #Here from abc we are importing all the members 
class  c1(ABC): #Here is a abstract base class is inherited by c1 class so it is an abstract class
	@abstractmethod
	def  m1(self): #Here m1 abstract method is defined
		pass
	def  __init__(slef):#Here constructor is defined
		print('c1  class  constructor')

class  c2(ABC): #Here is a abstract base class ABC is inherited by c2 class so it is an abstract class
	def  m1(self): #Here m1 concrete method is defined
		pass
	def  __init__(slef): #Here constructor of class c2 is defined
		print('c2  class  constructor')

class  c3: #Here class c3 is created which is concrete class
	@abstractmethod
	def  m1(self): #Here abstract method m1 is defined 
		pass
	def  __init__(slef): #Here constructor is defined in c3 class
		print('c3  class  constructor')

class  c4(c1): #Here class c4 is inheriting the c1 class
	def  m1(self): #Here m1 method id defined
		pass
	def  __init__(slef): #Here constructor is defined for c4 class
		print('c4  class  constructor')

class  c5(c1): #Here c5 class is inheriting the c1 class
	def  __init__(slef): #Here constructor of c5 class is defined
		print('c1  class  constructor')
		
# End  of  the  class
#c1() #Error #as c1 class is abstract class and it has abstract method 
c2() #Here c2 class constructor is executed
c3() #Here constructor of c3 class is executed 
c4() #Here c4 class constructor is executed
#c5() #Error #we cannot create oject as this class is inheriting the c1 class which is abstarct class
'''output:
c2 class constructor
c3 class constructor
c4 class constructor'''



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
		self.a = float(input()) #How  to  read  value  of  'a'
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
		super().get()
		self.b = float(input())
		self.c = float(input()) #How  to  read  the  3  sides  of  triangle
	def   area(self):
		s = ( self.a + self.b + self.c ) / 2
		return math.sqrt(s * (s - self.a) *  (s - self.b) * (s - self.c)) #area  of  triangle
	def   peri(self):
		return self.a + self.b + self.c  #perimeter  of  triangle
	def   test(self):
		if self.a+self.b > self.c and self.b+self.c > self.a and self.c+self.a > self.b:#sum  of  every  2  sides  should  be  >   3rd   side
			pass #do  nothing
		else:
			print('Not a triangle')
			exit() #How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super().get() #How  to  read  radius
	def   area(self):
		return 3.14159 * self.a ** 2  #area  of  circle
	def   peri(self):
		return 2 * 3.14159 * self.a  #circumference  of circle
	def  test(self):
		if self.a < 0: #side  is  -ve
			print('Radius  can  not  be  -ve')
			exit()#How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super().get()
		self.b = float(input()) #How  to  read  length  and  breadt
	def   area(self):
		return self.a * self.b #area  of  rectangle
	def   peri(self):
		return 2 * (self.a+self.b) #perimeter  of  triangle
	def  test(self):
		if self.a == self.b: #length  and   breadth  same
			print('Not  a rectangle')
			exit() #How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super().get() #How  to  read  the  side
	def   area(self):
		return self.a ** 2 #area  of  square
	def   peri(self):
		return 4*self.a #perimeter  of  square
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
	print('Area  :  ' ,s.area())
	print('Perimeter  :  ' ,s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				operation(triangle()) #How  to  call  operation()  function
		case  2:
				operation(circle()) #How  to  call  operation()  function
		case  3:
				operation(rectangle()) #How  to  call  operation()  function
		case  4:
				operation(square()) #How  to  call  operation()  function
		case  5:
				exit() #How  to  stop  execution
	# End  of  match
# End of while  loop




# Find  outputs (Home  work)
from   abc    import    * #Here from abc module we are importing all the members using *
class   parent(ABC): #here parent class is inheriting the abstarct class from abstract base class ABC i.e parent is the child class of ABC
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):			#Here in the parent class we have all the abstractmethods so it is an interface
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent): #Here child class is inheriting the parent class
	def  m1(self): #Here we are implementing the m1 method of parent class
		print('m1  method  of  child  class')
class  gc(child): #Here gc is inheriting the child class
	def  m2(self): #Here m2 method of parent class is implementing in gc class 
		print('m2  method  of    gc  class')
class  ggc(gc): #ggc is inheriting the gc class
	def  m3(self): #M3 method of parent class is implementing 
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc() #Here ggc class object is created
a . m1() #here m1 method of child class is called
a . m2() #Here m2 method of gc class is called
a . m3() #Here m3 method of ggc class is called
#parent() #Error #we cannot create object for parent class as it is abstract class
#child() #Error #same thing here
#gc() #Error #same thing here
'''outputs:
m1  method  of  child  class
m2  method  of    gc  class
m3  method  of  ggc  class'''