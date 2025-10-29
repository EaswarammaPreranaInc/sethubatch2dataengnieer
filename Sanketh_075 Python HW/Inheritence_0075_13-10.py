#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()#How  to  call  function  m1()
		#self . m1() error because it causes recursion
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p = parent() #How  to  call  m1()  method  of  parent  class
p.m1()
c = child()#How  to  call  m1()  method  of  child  class
c.m1()



# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1() 
		#m1() error no m1() function
		print('child  Method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child.m1()
#super() . m1() #error can't use super outside the class
#self . m1() #error can't use self outside the class


# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		#cls . m1()#error
		#self . m1() #error
		#m1() #error
		print('child  Method')
# End  of  the  class  
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class


 # Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1()#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super(child.child).m1()#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super().m1() #Error static method cannot use super 
		super(child).m1() #Valid 
		#self . m1()
		#cls . m1()
		print('child  method')
#end of the class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m2()#How  to  call  m2()  method  of  child  class
child.m1()


# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		parent.m1()#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		super(child.child).m1()#How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1()
		#self . m1()
		#cls . m1()
		print('child  method')
# End  of  the  class
parent.m1()#How  to  call  m1()  method  of  parent  class
child.m1()#How  to  call  m1()  method  of  child  class


# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(self.x)#How  to  print  variable  'x'
		print(parent.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		#print(x) #error
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(parent.x)#How  to  print  variable  'x'
		print(self.x)#How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(super.x)#How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) #How  to  print  variable  'y'
		print(child.y)#How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super().y)
		#print(y)
# End  of child  class
p = parent()#How  to  call   m1()  method  of  parent  class
p.m1()#
c=child()#How  to  call   m2()  method  of  child  class
c.m1()


# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x)#How  to  print  variable  'x'  of  parent  class
		print(self.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class child(parent):
	x = 20
	def  m1(self):
		print(super().x)#How  to  print  variable  'x'  of  parent  class
		print(parent.x)#How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(child.x)#How  to  print  variable  'x'  of  child  class
		print(self.x)#How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
#How  to  call  m1()  method  of  parent  class
#How  to  call  m1()  method  of  child  class



#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class parent:
	def  get(self):
		self.a = int(input("Enter any number"))
		self.a = int(input("Enter any number"))#How  to   read  inputs  into   variables  a  and  b  of  object
	def  disp(self):
		print(self.a,self.b,sep='\t')#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class child(parent):
	def  get(self):
		super().get()#How  to   read  inputs  into   variables  a  and  b  of  object
		self.c = int(input("Enter any number:"))
		self.d = int(input("Enter any number:"))#How  to   read  inputs  into   variables  c  and  d  of  object
	def disp(self):
		super.disp()#How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		print(self.c,self.d,sep='\t')#How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def total(self):
		return   self.a + self.b + self.c + self.d#sum  of  values  in  object  self
# End of child class
print('parent  object')
p = parent()
p.get()#How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c = child()
c.get()#How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
p.disp()#How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
c.disp()#How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' , c.total())



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
	def  get(self):
	    #How  to  read  radius  into  object
    def  area(self):
		#return  area  of  circle
	def   cir(self):
		#return  circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		#How  to  read  radius  into  object  self
		#How  to  read  height  into  object  self
	def  area(self):
		return   #area  of  cylinder
	def  volume(self):
		return   #volume  of  cylinder
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
				#How  to  read  raidus  into  circle  object
				print('Area  :  ' ,  ???)
				print('Circumference :  ' ,  ???)
		case  2:
				#How  to  read  raidus  and  height  into  cylinder  object
				print('Area : ' ,  ???)
				print('Volume :  ' ,  ???)
		case  3:
				#How  to  stop  execution
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
		How  to  read  side  of  square
	def   area(self):
		return   area  of  square
	def   peri(self):
		return   perimeter  of  square
class   rectangle(square):
	def   get(self):
		How  to  read  length  of  rectangle
		How  to  read  breadth  of  rectangle
	def   area(self):
		 return   area  of  rectangle
	def   peri(self):
		return  perimeter  of   rectangle
class   cube(square):
	def   get(self):
		 How  to  read  side  of  cube
	def   area(self):
		return  area  of  cube
	def   volume(self):
		return  volume  of  cube
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
			How  to  read  side  into   square  object  's'
			print('Area   :  ' ,  ???)
			print('Perimeter  :  ' ,  ???)
		case   2:
			How  to  read  length  and  breadth  into   rectangle  object  'r'
			print('Area  :  ' ,  ??)
			print('Perimeter  :  ' ,  ???)
		case   3:
			How  to  read  side  into  cube  object  'c'
			print('Area  :   ' ,  ???)
			print('Volume  :  ' ,  ???)
		case  4:
			exit()


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
		How  to  call  m1()  method  of  class  c3
		How  to  call  m1()  method  of  class  c4
		How  to  call  m1()  method  of  class  c2
		How  to  call  m1()  method  of  class  c1
		How  to  call  m1()  method  of  class  c5
		How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
How  to  call  m2()  method  of  class  c5


# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))
print(issubclass(int , float))
print(issubclass(str , object))
print(issubclass(c1 , object))
print(issubclass(c2 , object))
a = c1()
b = c2()
print(issubclass(b , a))
print(issubclass(c2 , a))


 # Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))
print(issubclass(c4 , c2))
print(issubclass(c4 , c1))
print(issubclass(c4 , object))
print(issubclass(c4 , (int , float , str , bool)))
print(issubclass(c4 , (int , float , c1 , str , bool)))
print(issubclass(c4 , [int , float , c1 , str , bool]))



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
print(isinstance(25 , int))
print(isinstance(10.8 , float))
print(isinstance('Hyd' , str))
print(isinstance(3 + 4j , complex))
print(isinstance(True , bool))
print(isinstance(True , int))
print(isinstance('True' , str))
print(isinstance(True , str))
print()
a = c3()
print(isinstance(a , c3))
print(isinstance(a , c2))
print(isinstance(a , c1))
print(isinstance(a , object))
print(isinstance(a , c4))
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))