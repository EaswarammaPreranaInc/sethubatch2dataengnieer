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
p = Person()
print(p . name)
p . name = 'Vamsi'
print(p . name)
del   p . name
#print(p . name)
del   p

'''	# output
	setter method
	getter method

	setter method
	getter method
	Vamsi
	Deleted method
'''



 '''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

'''	output
class Emp:
	def __init__(self, empno, ename, sal):
		self.empno = empno
		self.ename= ''
		self.sal =sal

	@property
	def empno(self):
		print('getter method')
		return self._empno
	
	@empno.setter
	def empno(self,value):
		print('setter method')
		if value<0:
			print('empno cannot be negative')
		self._empno=value
			
	@property
	def ename(self):
		print('getter method')
		return self._ename
	
	@name.setter
	def ename(self,x):
		print('setter method')
		
		self._ename=value

	@property
	def sal(self):
		print('getter method')
		return self._sal
	@salary.setter
	def sal(self,value):
		print('setter method')
		if value<0:
			print('salary cannot be negative')
		self._sal = value
e=Emp()
e.empno=101
e.ename='raj'
e.sal=34000
print(e.empno)
print(e.ename)
print(e.sal)
	
	

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''
 Enter  employee  number :  -25
Empno cannot be negative



 Enter  employee  number :  25
Enter  employee  name :
Emp  name cannot be empty  string



 Enter  employee  number :  25
 Enter  employee  name :  Vamsi
 Enter  salary :  -20
 Salary cannot be negative



 Enter  employee  number :  25
 Enter  employee  name :  Vamsi
 Enter  salary :  10000.0
 Employee number  :  25
 Employee name  :  Vamsi
 Employee salary :   10000.0