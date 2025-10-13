
# Find  outputs (Home work)
class  Person:
	def  _init_(self):
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
p = Person()           # Constructor is called
print(p.name)          # Calls getter (after constructor sets it)
p.name = 'Vamsi'       # Calls setter
print(p.name)          # Calls getter again
del p.name             # Calls deleter
# print(p.name)        # Uncommenting this will raise an AttributeError
del p                  # Deletes object

'''
Setter  Method
getter  method
getter  method
Setter  Method
getter  method
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
    b) Print  empno , ename and sal
'''

class Emp:
	def __init__(self, empno, ename, sal):
		self.empno = empno
		self.ename = ename
		self.sal = sal

	# Getter and Setter for empno
	@property
	def empno(self):
		return self._empno

	@empno.setter
	def empno(self, value):
		if value < 0:
			raise ValueError("Empno cannot be negative")
		self._empno = value

	# Getter and Setter for ename
	@property
	def ename(self):
		return self._ename

	@ename.setter
	def ename(self, value):
		if value.strip() == '':
			raise ValueError("Emp name cannot be empty string")
		self._ename = value

	# Getter and Setter for sal
	@property
	def sal(self):
		return self._sal

	@sal.setter
	def sal(self, value):
		if value < 0:
			raise ValueError("Salary cannot be negative")
		self._sal = value

while True:
	try:
		empno = int(input("Enter  employee  number : "))
		if empno < 0:
			print("Empno cannot be negative\n")
			continue

		ename = input("Enter  employee  name : ")
		if ename.strip() == '':
			print("Emp  name cannot be empty string\n")
			continue

		sal = float(input("Enter  salary : "))
		if sal < 0:
			print("Salary cannot be negative\n")
			continue

		# If all are valid, create object and print
		e = Emp(empno, ename, sal)
		print("Employee number  : ", e.empno)
		print("Employee name  : ", e.ename)
		print("Employee salary : ", e.sal)
		break

	except ValueError as err:
		print(err)
		print()

'''
Output:

Enter  employee  number :  -25
Empno cannot be negative

Enter  employee  number :  25
Enter  employee  name :
Emp  name cannot be empty string

Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  -20
Salary cannot be negative

Enter  employee  number :  25
Enter  employee  name :  Vamsi
Enter  salary :  10000.0
Employee number  :  25
Employee name  :  Vamsi
Employee salary : 10000.0
'''
