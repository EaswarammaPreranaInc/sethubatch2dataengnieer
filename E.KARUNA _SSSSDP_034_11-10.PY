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
p = Person()#object is created and constructo is executed i.e setter method
print(p . name)#getter method is executed i.e getter method
p . name = 'Vamsi'#setter method is executed i.e setter method
print(p . name)#getter method and vamsi
del   p . name#deleter is executed i.e deleter method
#print(p . name)#error _name is not deleted
del   p# object is lost





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
class emp:
	def __init__(self,empno,ename,sal):
		self.empno=empno
		self.ename=ename
		self.sal=sal
		@property
		def empno(self):
			return self._empno
		@empno.setter
		def empno(self,value):
			if value<0:
				raise ValueError("Employee number cannot be negative")
			self._empno=value
		@property
		def ename(self):
			return self._ename
		@ename.setter
		def ename(self,value):
			if not value :
				raise ValueError("emp name can not be empty string")	
			self._ename=value
			@property
			def sal(self):
				return self._sal
		@sal.getter
		def sal(self,value):
			if value<0:
				raise ValueError("salary cannot be negative ")
			self.sal=value
e=emp(25,'ramarao',10000)
print(f'emp numer:{emp.name},emp name:{emp.name},salary:{emp.sal}')			
			
		
			  