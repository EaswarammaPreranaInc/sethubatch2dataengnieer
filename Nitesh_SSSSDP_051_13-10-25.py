#  parent  and  child  classes  have  same  Instance  method
class  parent:
	def   m1(self):
		print('parent  Method')
class   child(parent):
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		m1() #How  to  call  function  m1()
		self . m1() # leads to recursion 
		print('child  Method')
# End  of  the  class
def  m1():
	print('m1  function')
# End of  the  function
p=parent() 
p.m1() #How  to  call  m1()  method  of  parent  class
c=child() 
c.m1() #How  to  call  m1()  method  of  child  class

# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()
		self . m1() # error there is no self reference here 
		m1() # error there is no function m1 here 
		print('child  Method')
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class

# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		c=child()
		c.m1() #How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1() # error there is no self here 
		m1() # error there is no m1 function here 
		print('child  Method')
# End  of  the  class
p=parent()
p.m1() #How  to  call  m1()  method  of  parent  class
c=child()
c.m1() #How  to  call  m2()  method  of  child  class
child . m1() #parent method 
super() . m1() # error
self . m1() # error there is no self ref here 

# Parent  and  Child  classes  have  different  static  methods
class   parent:
	@staticmethod
	def  m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m2():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		child.m1() #How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		super() . m1() #parent method
		super(child).m1() # parent method
		self . m1() # error there is no self here 
		cls . m1() # there is no cls here 
		print('child  method') # child method 
#end of the class
c=child() 
c.m1() #How  to  call  m1()  method  of  parent  class
c.m2() #How  to  call  m2()  method  of  child  class
child . m1()

# Parent  and  Child  classes  have  same  static  method
class   parent:
	@staticmethod
	def   m1():
		print('parent  method')
class   child(parent):
	@staticmethod
	def   m1():
		super().m1() #How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1() #How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
		super() . m1() # parent method
		self . m1() # error there is no self here 
		cls . m1() # error there is no cls here 
		print('child  method') # child method 
# End  of  the  class
parent.m1() #How  to  call  m1()  method  of  parent  class
child.m1() #How  to  call  m1()  method  of  child  class

# Parent  and  child  classes  have   static  variables  with  different  names
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'
		print(self.x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(x) # error  there is no global or local variable 
# End  of  parent  class
class   child(parent):
	y = 20
	def  m2(self):
		print(self.x) #How  to  print  variable  'x'
		print(super().x) #How  to  print  variable  'x'  in  another  way  without  creating  an  object
		print(super(child,self).x) #How  to  print  variable  'x' in  one  more  way  without  creating  an  object
		print(parent.x) #How  to  print  variable  'x' in  last  way  without  creating  an  object
		print(self.y) #How  to  print  variable  'y'
		print(child.y) #How  to  print  variable  'y'  in  another  way  without  creating  an  object
		print(super() . y) # 20
		print(y) # error there is no local or global variable 
# End  of child  class
c=child() 
c.m1() #How  to  call   m1()  method  of  parent  class
c.m2() #How  to  call   m2()  method  of  child  class

# Parent  and  Child  classes  have  static  variables  with  same  name
class   parent:
	x = 10
	def  m1(self):
		print(parent.x) #How  to  print  variable  'x'  of  parent  class
		print(self.x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
class   child(parent):
	x = 20
	def  m1(self):
		print(self.x) #How  to  print  variable  'x'  of  parent  class
		print(super().x) #How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
		print(super(child,self).x) #How  to  print  variable  'x'  of  child  class
		print(parent.x) #How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# End  of  the  class
c=child()
c.m1() #How  to  call  m1()  method  of  parent  class
c.m2() #How  to  call  m1()  method  of  child  class

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class   parent:
	def    get(self):
		a=int(input("enter value:")) 
		b=int(input("enter value:")) 
		self.a=a 
		self.b=b
		#How  to   read  inputs  into   variables  a  and  b  of  object
	def    disp(self):
		print(f'{self.a}\t{self.b}') #How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# End  of  Parent  class
class    child(parent):
	def    get(self):
		a=int(input("enter value:")) 
		b=int(input("enter value:")) 
		c=int(input("enter value:")) 
		d=int(input("enter value:"))
		self.a=a 
		self.b=b 
		self.c=c 
		self.d=d 
		# How  to   read  inputs  into   variables  a  and  b  of  object
		# How  to   read  inputs  into   variables  c  and  d  of  object
	def   disp(self):
		print(self.a,self.b,sep='\t')
		print(self.c,self.d,sep='\t')
		# How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
		# How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
	def  total(self):
		d=self.__dict__ 
		sum=0
		for x in d:
			sum+=d[x]
		return sum 
		# return   sum  of  values  in  object  self
# End of child class
print('parent  object')
p=parent()
p.get()
# How  to  read  inputs  into  parent  class  object  'p'
print('child  object')
c=child()
c.get()
# How  to  read  inputs  into  child  class  object  'c'
print('parent  object  :  ' , end = '\t')
print(p.disp()) #How  to  print  object  'p'
print()
print('child  object  :  ' , end = '\t')
print(c.disp()) #How  to  print  object  'c'
print('Sum of  the  values  in  child  object :  ' ,c.total())#  How  to  obtain  sum of  values  of  object  'c')


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
	    r=int(input("Enter radius:")) #How  to  read  radius  into  object
		self.r=r
	def   area(self):
		return  3.14*self.r*self.r #area  of  circle
	def   cir(self):
		return  2*3.14*self.r #circumference  of  circle
# End  of  circle  class
class  cylinder(circle):
	def   get(self):
		super().get() #How  to  read  radius  into  object  self
		h=int(input("enter the height :"))
		self.h=h #How  to  read  height  into  object  self
	def  area(self):
		return   2*3.14*(self.r*self.r+self.r*self.h) #area  of  cylinder
	def  volume(self):
		return   3.14*self.r.self.r*self.h #volume  of  cylinder
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
				c=circle() #How  to  read  raidus  into  circle  object
				c.get()
				print('Area  :  ' ,  c.area())
				print('Circumference :  ' ,  c.cir())
		case  2:
				cy=cylinder() #How  to  read  raidus  and  height  into  cylinder  object
				cy.get()
				print('Area : ' ,  cy.area())
				print('Volume :  ' ,  cy.volume())
		case  3:
				# How  to  stop  execution
				exit()
	# End  of  match