# Find  outputs (Home work)
class  Person:
	def  __init__(self): #Here self is obj p
		self . name  =  '' #Here setter method is executed 
	@property
	def   name(self):
		print('getter  method') 
		return  self . _name  #This is the backup variable
	@name . setter #This is setter method 
	def   name(self , value): #Here self is p and value is the value to be assigned to the instance variable 
		print('Setter  Method')
		self . _name = value #adds the backup variable to object p
	@name . deleter
	def  name(self): #Self is obj p
		print('Deleter  method ')
		del  self .  _name #Deletes the backup variable
#end  of  the  class
p = Person() #Here object is created and constructor is executed that means to the obj p instance variable name is added and setter method is executed with backup variable created
print(p . name) #Here getter method returns the ''
p . name = 'Vamsi' #Here setter method modifies the value of name to 'vamsi'
print(p . name) #Here getter method returns the name i.e 'vamsi'
del   p . name #Here deleter method deletes the two variables name and _name variable from the object p
#print(p . name) #Error #Getter method throws error beacause p.name variable does not exits 
del   p #Here distructor is executed before object p is deleted but not getter method
'''output:
setter method
getter method 
empty string
setter method
vamsi
deleter method
Destructor'''


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
	def __init__(self):
		self.empno = int(input("Enter the emp no: "))
		self.ename = input("Enter the emp no: ")
		self.sal = input("Enter the sal: ")
	@property
	def empno(self):
		return self._empno
	@property
	def ename(self):
		return self._ename
	@property
	def sal(self):
		return self._sal
	@empno.setter
	def empno(self,x):
		if x < 0:
			raise ValueError("Empno cannot be Zero")
		self._empno = x
	@ename.setter
	def ename(self,x):
		if x == '':
			raise ValueError("Ename cannot be empty")
		self._ename = x
	@sal.setter
	def sal(self,x):
		if x < 0:
			raise ValueError("sal cannot be zero")
		self._sal = x
try:
	e = emp()
	print("Emp no :",e.empno)
	print("Emp name :",e.ename)
	print("Emp sal :",e.sal)
except ValueError as msg:
	print(msg)
	
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
'''