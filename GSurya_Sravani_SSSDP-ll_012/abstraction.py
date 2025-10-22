#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
#end of the class
x = parent()#
x . m1()#'Overridden  Method'
x = child()
x . m1()#Overriding  Method



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
x . m1()#m1  method  of  parent  class'
x . m2()#m2  method  of  parent class
x . m3()#error
x = child()
x . m1()#m1  method  of  child  class
x . m2()#m2  method  of  parent class
x . m3()#m3  method  of  child  class



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
c . marriage()#Love Marriage
c . property()#One  Crore
c . study()#Studies only      + Entertainment 


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End of the class
c = child()
print(c . add(10 , 20 , 30))#60
print(c . add(10 , 20))#30
print(super(child , c) . add(40,50))#90



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
print(c . add(10 , 20 , 30))#child  method
60
print(c . add(10 , 20))#parent  method
33



#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)#child  method  --->  x  :  10  \t  y  :  20
c . m1(30 , 40)#parent  method  --->   a  :  30  \t  b  :  40


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
c1()#c1  class  constructor
c2()#c2  class  constructor
c3()#c3  class  constructor
c4()#c4  class  constructor
c5()#c1  class  constructor


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
	def   get(self,a1):
		 self.a=a1 #How  to  read  value  of  'a'
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
		self.a=int(input("enter 1st side: ")
                self.b=int(input("enter 2st side: ")  #How  to  read  the  3  sides  of  triangle
                self.c=int(input("enter 3rd side: ")
	def   area(self):
            self.s=(self.a+self.b+self.c)/2
            #sqrt(s * (s - a) *  (s - b) * (s - c))
		return   math.sqrt(self.s * (self.s - self.a) *  (self.s - self.b) * (self.s - self.c))
	def   peri(self):
		return  self.a+self.b+self.c
	def   test(self):
		if  sum(self.a,self.b)>self.c and  sum(self.c,self.b)>self.a and sum(self.a,self.c)>self.b 
				print("valid triangle")
		else:
			print('Not    a  triangle')
			break
class   circle(shape):
	def   get(self):
		self.r=int(input('Enter  radius  of  circle  : ' ))
		#How  to  read  radius
	def   area(self):
		return  3.14159 * self.r ^ 2 
	def   peri(self):
		return  2 * 3.14159 * self.r

	def  test(self):
		if  self.r <0
		    print('Radius  can  not  be  -ve')
		    break
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		self.l=int(input("enter lenghth of rectangle : ") #How  to  read  length  and  breadt
                self.b=int(input("enter breadth of rectangle : ")
	def   area(self):
		return  self.l*self.b
	def   peri(self):
		return  2*(self.l + self.b)
	def  test(self):
		if  self.l  ==   self.b  
		    print('Not  a rectangle')
		    break
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		self.side=int(input("enter side of the square : ") #How  to  read  the  side
	def   area(self):
		return  self.side^2
	def   peri(self):
		return  4*self.side
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
        s.get()#How  to  read  inputs  to  object  's'
	s.tet()How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' ,  s.peri())
# End  of  the  function
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				t=triangle()
                                operation(t) #How  to  call  operation()  function
		case  2:
				c=circle()
                                operation(c) #How  to  call  operation()  function
		case  3:
				r=rectangle()
                                operation(r) #How  to  call  operation()  function
		case  4:
				sq=square()
                                operation(sq) #How  to  call  operation()  function
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
a = ggc()#
a . m1()#m1  method  of  ggc  class
a . m2()#m2  method  of    gc  class
a . m3()#m3  method  of  ggc  class
# End  of  the  class

parent()#error
child()#error
gc()#error



































