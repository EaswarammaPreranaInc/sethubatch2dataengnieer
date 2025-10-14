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
	    self . radius = float(input('Enter Radius : ')) # How  to  read  radius  into  object
	def   area(self):
		return  math.pi * (self . radius ** 2) # area  of  circle
	def   cir(self):
		return  2 * math.pi * self . radius# circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super() . get() # How  to  read  radius  into  object  self
		self . height = float(input('Enter Height : ')) # How  to  read  height  into  object  self
	def  area(self):
		return (super() . area() + super().cir()) * self . height # area  of  cylinder
	def  volume(self):
		return super() . area() * self . height # volume  of  cylinder
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
				r = radius() # How  to  read  raidus  into  circle  object
				r . get()
				print('Area  :  ' ,  r.area())
				print('Circumference :  ' ,  r . cir())
		case  2:
				c = cylinder() # How  to  read  raidus  and  height  into  cylinder  object
				c . get()
				print('Area : ' , c . area())
				print('Volume :  ' , c . volume())
		case  3:
				exit() # How  to  stop  execution
	# End  of  match





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
		self . side = float(input('Enter a Side : ')) # How  to  read  side  of  square
	def   area(self):
		return self . side ** 2 # area  of  square
	def   peri(self):
		return self . side * 4 # perimeter  of  square
class   rectangle(square):
	def   get(self):
		self . length = float(input('Enter Length : ')) # How  to  read  length  of  rectangle
		self . breadth = float(input('Enter breadth')) # How  to  read  breadth  of  rectangle
	def   area(self):
		 return self  . length * self . breadth # area  of  rectangle
	def   peri(self):
		return  2 * (self . length + self . breadth) # perimeter  of   rectangle
class   cube(square):
	def   get(self):
		 super() . get() # How  to  read  side  of  cube
	def   area(self):
		return 6 * super() . area() # area  of  cube
	def   volume(self):
		return super().area()  self . a # volume  of  cube
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
			s = square() # How  to  read  side  into   square  object  's'
			s . get()
			print('Area   :  ' ,  s.area())
			print('Perimeter  :  ' , s.peri())
		case   2:
			r = rectangle() # How  to  read  length  and  breadth  into   rectangle  object  'r'
			r . get()
			print('Area  :  ' ,  r.area())
			print('Perimeter  :  ' , r.peri())
		case   3:
			c = cube() # How  to  read  side  into  cube  object  'c'
			print('Area  :   ' , c . area())
			print('Volume  :  ' , c . volume())
		case  4:
			exit() # How  to  stop  execution
