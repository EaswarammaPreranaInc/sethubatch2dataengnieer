# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o=outer() #How  to  call  m1()  method  of  outer  class
o.m1()
i=o.inner()#How  to  call  m1()  method  of  inner  class
i.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
i2=outer.inner() 
i2.m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()#error

# Find  outputs  (Home  work)
class   emp:
	def __init__(self,eno,ename,empsal):
		self.empno=eno 
                self.name=ename
                self.sal=empsal   #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d=emp.date() #How  to  create  date  class  object
	def   disp(self):
		print(f"{self.empno} {self.name} {self.sal} ")How  to  print  empno , ename , sal  of  object  self
		self.d.disp() #How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd = 15
                        self.mm = 8
                        self.yy = 1947  #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(f"{self.dd} {self.mm} {self.yy} ") #How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
a=emp(25,'rama rao',10000.0)
a.disp()#How  to  call  disp()  method  of  emp  class

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		How  to  initialize  variable  'x'  of  object  self  to  25
		How  to  create  inner1  class  object
		How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a=outer()
a.disp() #How  to  call   disp()  method  of outer  class
i=a.disp()
i.inner1() #How  to  call   disp()  method  of inner1  class
i2=a.disp() 
i2.disp() #How  to  call   disp()  method  of inner2  class

# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a=c1() #How  to  create  c1  class  object
i2=a.c1()How  to  create  inner  c2  class  object
b=c2() #How  to  create  outer  c2  class  object

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
o=c2() #How  to  create  outer  c2  class  object
i1=0.c2() #How  to  create  inner  c2  class  object
i2=c2.c2() #How  to  create  inner  c2  class  object  in  another  way

# Find  outputs (Home  work)
class c1:
    x = 10
    def __init__(self):
	    self . y = 20
a = c1()
b = c1()
a . x += 1
b . y += 1
print(a . x)#11
print(a . y)#11
print(b . x)#10
print(b . y)#21
print(c1 . x)#10
print(a . __dict__)#{y:20,x:10}
print(b . __dict__)#{y:20 x:10}
print(c1 . __dict__)#{x:10}



# Find  outputs (Home  work)
class  c1:
	x = 10
	def  m1(self):
		self . x = 20
a = c1()
a . m1()
print(c1 . x)#10
print(a . x)#10




# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#30,40
print(cls . x , cls . y)#error
print(self . x , self . y)#10,20


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
none
a = c1()#
a . m1()#error
none
a . m1(35)#35
none

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25)#static  method/instance method
25
none
a = c1()
a . m1()#static  method/nstance  method'
none

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)#error
	@classmethod
	def   m2(cls):
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x)#error
	@staticmethod
	def   m3():
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls . x)#error
		print(self . x)#error
# End  of  the  class
print(c1.x) #How  to  print  static  variable  'x'
by creating object #How  to  print  static  variable  'x'  in  another  way
print(x)#error
print(self . x)#25
print(cls . x)#25
a=c1() #How  to  call  method  m1()
a.m1()
c1.m2() #How  to  call  method  m2()
c1.m3()How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30  #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25#error
	def   m1(self):
		c1.d=40  #How  to  add  static  variable  'd'  with  value  40
		self.e=50  #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60 #How  to  add  static  variable  'f'  with  value  60
		cls.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25#error
	@staticmethod
	def   m3():
		How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . __dict__)#
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)
print()
print()
How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
How  to  add  static  variable  'i'  with  value  90
How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)

Begin
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None}

After constructor (__init__)
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None, 'b': 20}
Object x: {'c': 30}

After instance method m1()
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None, 'b': 20, 'd': 40}
Object x: {'c': 30, 'e': 50}

After class method m2()
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70}

After static method m3()
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70,
 'h': 80}

After adding variables outside the class
{'__module__': '__main__', 'a': 10, '__init__': <function ...>, 'm1': <function ...>,
 'm2': <classmethod ...>, 'm3': <staticmethod ...>, '__dict__': <attribute ...>,
 '__weakref__': <attribute ...>, '__doc__': None, 'b': 20, 'd': 40, 'f': 60, 'g': 70,
 'h': 80, 'i': 90}
Object x: {'c': 30, 'e': 50, 'j': 100}



# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
c1.a #How  to  print  variable  'a'
c1.b #How  to  print  variable  'b'
c1.c #How  to  print  variable  'c'













