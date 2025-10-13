#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1()  #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1()    #How  to  call  function  m1()
		self . m1()                 #This causes infinite recursion
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p = parent()    #How  to  call  m1()  method  of  parent  class
p.m1()
c = child() #How  to  call  m1()  method  of  child  class
c.m1()






# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		cls.m1()   #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1()  #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		#self . m1()    #throws error as there is no self
		m1()		#there is no function m1 in the program
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m2()  #How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()              #super can't be used outside the class
self . m1()                 #There is no self in the program






# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()    #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()    #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()          #Recursion
		self . m1()         #There is no self in m1
		m1()       #There is no function m1 in  the program
		print('child  Method')
# End  of  the  class
parent.m1()    #How  to  call  m1()  method  of  parent  class
child.m1()      #How  to  call  m1()  method  of  child  class






# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		parent.m1()     #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		child.m1()      #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		super() . m1()
		super(child).m1()
		self . m1()        #Error as there is no cls
		cls . m1()         #Error as there is no self
		print('child  method')
#end of the class
parent.m1()     #How  to  call  m1()  method  of  parent  class
child.m2()      #How  to  call  m2()  method  of  child  class
child . m1()






# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(p.x)     #How  to  print  variable  'x'
		print(parent.x)     #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x)        #Error as there is no local x       
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(c.x)     #How  to  print  variable  'x'
		print(child.x)     #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(parent.x)     #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(c.y)     #How  to  print  variable  'y'
		print(child.y)     #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y)      #Parent doesn't have variable y
		print(y)            #Error as there is no local y
# End  of child  class
p = parent()
p.m1()        #How  to  call   m1()  method  of  parent  class
c = child()
c.m2()      #How  to  call   m2()  method  of  child  class






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
	    self.r = float(input('Enter the radius of the circle : '))#How  to  read  radius  into  object
	def   area(self):
		return  math.pi*self.r**2
	def   cir(self):
		return  2*math.pi*self.r
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		self.r = float(input('Enter the radius of the cylinder : '))#How  to  read  radius  into  object  self
		self.h = float(input('Enter the height of the cylinder : '))#How  to  read  height  into  object  self
	def  area(self):
		return   2*super().area() + 2*super().cir()*self.h
	def  volume(self):
		return   super().area()*self.h
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
				c = circle()
				c.get()
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				#How  to  read  raidus  and  height  into  cylinder  object
				cy = cylinder()
				cy.get()
				print('Area : ' ,  cy.area())
				print('Volume :  ' ,  cy.volume())
		case  3:
				#How  to  stop  execution
				exit()
	# End  of  match






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
		c3.m1()     #How  to  call  m1()  method  of  class  c3
		c4.m1()     #How  to  call  m1()  method  of  class  c4
		c = c2()        
		c.m1()      #How  to  call  m1()  method  of  class  c2
		super().m1()      #How  to  call  m1()  method  of  class  c1
		self.m1()   #How  to  call  m1()  method  of  class  c5
		m1()    #How  to  call  m1()  function
# End  of  class  c5
def  m1():
	print('m1 function')
# End  of  the  function
c = c5()        
c.m2()      #How  to  call  m2()  method  of  class  c5






# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))              #True
print(issubclass(int , float))          #False
print(issubclass(str , object))         #True
print(issubclass(c1 , object))          #True
print(issubclass(c2 , object))          #True
a = c1()
b = c2()
print(issubclass(b , a))                #Error as issubclass requires its argument to be classes
print(issubclass(c2 , a))               #Same issue as the above






# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))              #True
print(issubclass(c4 , c2))              #True
print(issubclass(c4 , c1))              #True
print(issubclass(c4 , object))          #True
print(issubclass(c4 , (int , float , str , bool)))      #False
print(issubclass(c4 , (int , float , c1 , str , bool)))     #True
print(issubclass(c4 , [int , float , c1 , str , bool]))     #Error as 2nd argument can't be a list






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
print(isinstance(25 , int))                 #True
print(isinstance(10.8 , float))             #True
print(isinstance('Hyd' , str))              #True
print(isinstance(3 + 4j , complex))         #True
print(isinstance(True , bool))              #True
print(isinstance(True , int))               #True
print(isinstance('True' , str))             #True
print(isinstance(True , str))               #False
print()
a = c3()
print(isinstance(a , c3))                   #True
print(isinstance(a , c2))                   #True
print(isinstance(a , c1))                   #Ture
print(isinstance(a , object))               #True
print(isinstance(a , c4))                   #False
print(isinstance(a, (int, float, str, bool)))           #False
print(isinstance(a, (int, float, c3, str, bool)))       #True
print(isinstance(a, (int, float, c1, str, bool)))       #True
#print(isinstance(a, [int, float, c3, str, bool]))       #Error as 2nd argument can't be a list