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
o = outer()
o . m1() # How  to  call  m1()  method  of  outer  class
outer() . inner() . m1() # How  to  call  m1()  method  of  inner  class
o . inner() . m1() # How  to  call  m1()  method  of  inner  class  in  another  way
i = outer() . inner() # How  to  call  m1()  method  of  inner  class  in  one  more  way
i . m1()
i = inner() # Error as there is no inner class in current module

'''
Outer  class  constructor
Outer  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method
'''


# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self . empno = int(input('Enter Employee Number : '))
		self . ename = input('Enter Employee Name : ')
		self . sal = float(input('Enter Salary : '))
		self . date() # How  to  create  date  class  object
	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print(f'Employee Number : {self . empno}')
		print(f'Employee Name : {self . ename}')
		print(f'Salary : {self . sal}')
		self . date().disp() # How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self . dd = 15
			self . mm = 8
			self . yy = 1947
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print(f'Date : {self . dd}')
			print(f'Month : {self . mm}')
			print(f'Year : {self . yy}')
# End of the class
# How to call disp() method of emp class
e = emp()
e . disp()



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self . x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self . inner1() # How  to  create  inner1  class  object
		self . inner2() # How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
# How to call disp() method of outer class
o = outer()
o . disp()
o . inner1() . disp() # How to call disp() method of inner1 class
o . inner2() . disp() # How to call disp() method of inner2 class

'''
25
1st  inner  class  method
2nd  inner  class  method
'''


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
# How  to  create  c1  class  object
c = c1()
c . c2() # How  to  create  inner  c2  class  object
c2 = c2() # How  to  create  outer  c2  class  object

'''
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor
'''


