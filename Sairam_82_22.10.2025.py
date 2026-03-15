#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method') # overriden method is printed
class  child(parent):
	def  m1(self):
		print('Overriding  Method') # overriding method is printed
#end of the class
x = parent()    # parent class  object is created
x . m1()    # m1 method of parent class is called
x = child() # child class object is created
x . m1()    # m1 method of child class is called

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
x = parent()    # parent class object creation
x . m1()    # m1 method of parent class called
x . m2()    # m2 method of parent class called
x . m3()    # error as m3 method is not present in parent class
x = child()    # child class object creation
x . m1()    # m1 method of child class called
x . m2()    # m2 method of parent class called
x . m3()    # m3 method of child class called

# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore') # one crore is printed
	def  study(self):
		print('Studies only' , end = '\t')  # studies only is printed
class  child(parent):
	def  marriage(self):
		print('Love Marriage')  # love marraige is printed
	def  study(self):
		super() . study()   # parent class study method will be called
		print(' + Entertainment')
#end of the class
c = child()     # child class object is created
c . marriage()  # child class method will be called
c . property()  # 1st searched in child class, not found so parent class method will be called
c . study()    # child class method will be called

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y   # return 40 + 50 = 90
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z  # return 10+20+30 = 60
# End of the class
c = child() # child class object is created 
print(c . add(10 , 20 , 30))    # child class method will be called with 3 arguments
print(c . add(10 , 20))    # error as child class method needs 3 arguments
print(super(child , c) . add(40,50))    # calling parent class method using super with object c

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):    # always child  method  will  be  called as there is same  method  name
		print('child  method')
		return  x + y + z
#End  of  the  class
c = child() # child class object is created
print(c . add(10 , 20 , 30))    # child  method 60
print(c . add(10 , 20))  # child  method 33

#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')     # prints child methods with x and y values
# End of the class
c = child()     # child class object   is created
c . m1(x = 10 , y = 20)    # child  method  is  called with keyword  arguments 10 and 20
c . m1(30 , 40) # child  method  is  called with positional arguments 30 and 40

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
c1()    # error as c1 is abstract class and has abstract method so object creation not possible
c2()# error as c2 is abstract class and has abstract method so object creation not possible
c3()   # error as c3 is abstract class and has abstract method without implementation so object creation not possible
c4()    # c4 class object is created and c4 class constructor called as m1 method is imple1mented in c4 class
c5()   # error as c5 is abstract class and has abstract method without implementation so object creation not possible


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
		a=int(input())  # How  to  read  value  of  'a'
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
		self.a = float(input()) 
		self.b=float(input()) 
		self.c=float(input())   #How  to  read  the  3  sides  of  triangle
	def   area(self):
		s=(self.a +self. b + self.c) / 2
		return   math.sqrt(s * (s - self.a) *  (s -self. b) * (s - self.c)) #area  of  triangle
	def   peri(self):
		return  self.a + self.b + self.c    #perimeter  of  triangle
	def   test(self):
		if  self.a+self.b >  self.c:
			pass
		else:
			print('Not    a  triangle')
			exit()  #How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		self.a = float(input())    #How  to  read  radius
	def   area(self):
		return math.pi * self.a ** 2  # area  of  circle
	def   peri(self):
		return  2 * math.pi * self.a    #circumference  of circle
	def  test(self):
		if  self.a<0:   #side  is  -ve
			print('Radius  can  not  be  -ve')
			exit()  #How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		self.a = float(input())
		self.b=int(input())   #How  to  read  length  and  breadt
	def   area(self):
		return self.a *self. b  # area  of  rectangle
	def   peri(self):
		return  2*(self.a + self.b)  #perimeter  of  triangle
	def  test(self):
		if  self.a==self.b:  #ength  and   breadth  same
			print('Not  a rectangle')
			exit()  ##How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		self.a = float(input())   #How  to  read  the  side
	def   area(self):
		return  self.a**2    #area  of  square
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
	s.test()    #How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' ,  s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				operation(triangle())   #How  to  call  operation()  function
		case  2:
				operation(circle())   #How  to  call  operation()  function
		case  3:
				operation(rectangle())   #How  to  call  operation()  function
		case  4:
				operation(square())   #How  to  call  operation()  function
		case  5:
				exit()  #How  to  stop  execution
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
a = ggc()   # great grandchild  object
a . m1()    # m1 of child class is inherited and executed
a . m2()    # m2 of gc class is inherited and executed
a . m3()    # m3 of ggc class is executed
parent()    # error object creation not possible as parent class is abstract and has abstract methods
child()   # error object creation not possible as child class is abstract and has abstract methods inherited
gc()  # error object creation not possible as gc class is abstract