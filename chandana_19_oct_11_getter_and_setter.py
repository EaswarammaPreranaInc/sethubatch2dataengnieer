# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self . name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self . _name
	@name . setter
	def   name(self , value):
		print('Setter  Method')
		self . _name = value
	@name . deleter
	def  name(self):
		print('Deleter  method ')
		del  self .  _name
#end  of  the  class
p = Person() # constructor is executed
print(p . name) # as instance variable is accessed getter method is executed
p . name = 'Vamsi'
print(p . name)
del   p . name # deleted the instance variable
#print(p . name) # error 
del   p 
'''
o/p:
Setter  Method
getter  method

Setter  Method
getter  method
Vamsi
Deleter  method
'''



'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''


class Emp:
	def __init__(self,empno,ename,sal):
		self.empno=empno
		self.ename=ename
		self.sal=sal
		
	@property
	def empno(self):
		return self._empno
	@empno.setter
	def empno(self,value):
		while empno<0:
			print('Empno cannot be negative ')
			value=int(input('Enter employee number :'))
		self._empno=value
		
	@property
	def ename(self):
		return self._ename
	@ename.setter
	def ename(self,value):
		while value.strip()=='':
			print('Employee name cannot be empty string')
			value=input('Enter employee name :')
		self._ename=value
		
	@property
	def sal(self):
		return self._sal
	@sal.setter
	def sal(self,value):
		while value<0:
			print('salary cannot be negative')
			value=float(input('Enter salary :'))
		self._sal=value
		
empno=int(input('enter employee number :'))
ename=input('enter employee name :')
sal=float(input('enter salary :'))
e=Emp(empno,ename,sal)
print('employee number :',e.empno)
print('employee name :',e.ename)
print('employee salary :',e.sal)


