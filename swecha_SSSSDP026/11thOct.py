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
p = Person()#setter method
print(p . name)#accessing getter method and empty string
p . name = 'Vamsi'#intializing obj-setter method
print(p . name)# accessing-- getter method and Vamsi
del   p . name## deleter method
#print(p . name)## error bcz var is deleted
del   p# deletes the obj

''''
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
		self.empno = empno
		self.ename = ename
		self.sal = sal
	@property
	def empno(self):
			print('getter method')
			return self._empno
	@property
	def ename(self):
			print('getter method')
			return self._ename
	@property
	def sal(self):
			print('getter method')
			return self._sal
	@empno.setter
	def empno(self,value):
			print('setter method')
			if value < 0:
				raise ValueError('empno can not be -ve')
			self._empno = value
	@ename.setter
	def ename(self,value):
			print('setter method')
			if value == '':
				raise ValueError('ename can not be empty string')
			self._ename = value
	@sal.setter
	def sal(self,value):
			print('setter method')
			if value < 0:
				raise ValueError('sal can not be -ve')
			self._sal = value
while True:
			try:
				empno =int(input("enter empno:"))
				ename = input("enter ename:")
				sal = float(input("enter sal:"))
				e =Emp(empno,ename,sal)
				break
			except ValueError as err:
				print(err)
print("empno:",e.empno)	
print("ename:",e.ename)
print("sal:",e.sal)		

