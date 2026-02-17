# Find  outputs (Home work)

class  Person:
	def  __init__(self):
		self . name  =  ''  	# adding name to object p with empty string as object is created setter is executed
	@property
	def   name(self):
		print('getter  method') #prints getter method
		return  self . _name    # returns backup variable with empty string,vamsi to p.name
	@name . setter
	def   name(self , value):
		print('Setter  Method') #prints setter method
		self . _name = value    # a backup variable is created with empty string,'vamsi'
	@name . deleter
	def  name(self):
		print('Deleter  method ')   #   prints deleter method
		del  self .  _name  	# back up variable is deleted
#end  of  the  class
p = Person()    				# creating person class object and  calling constructor
print(p . name) 				# printing p.name so getter nethod is executed andd empty string is printed
p . name = 'Vamsi'  			# again we are modifying varaible so setter method is executed again
print(p . name) 				# prints vamsi
del   p . name  				# deletes instance variable p.name so deleter  methos is executed
print(p . name)    				# error as no p.name
del   p 						# object p is deleted





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

class Employee:
    def __init__(self):
        self.eno =int(input("Enter employee number: "))
        self.ename = input("Enter employee name: ")
        self.sal = float(input("Enter salary: "))

    @property
    def eno(self):
        return self._eno

    @eno.setter
    def eno(self, value):
        if value < 0:
            raise ValueError("Employee number cannot be negative.")
        self._eno = value

    @property
    def ename(self):
        return self._ename

    @ename.setter
    def ename(self, value):
        if not value.strip():
            raise ValueError("Employee name cannot be empty.")
        self._ename = value

    @property
    def sal(self):
        return self._sal

    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._sal = value

try:
    emp = Employee()   
    print(f"Employee No: {emp.eno} \nEmployee Name: {emp.ename} \nSalary: {emp.sal}")

except ValueError as msg:
    print(f"{msg}")

'''
output:
Enter employee number: 25
Enter employee name: mahesh
Enter salary: 10000.0
Employee No: 25
Employee Name: mahesh
Salary: 10000.0	
'''
	
