# Find  outputs (Home work)
class  Person:
	def  __init__(self):
		self.name  =  ''
	@property
	def   name(self):
		print('getter  method')
		return  self._name
	@name.setter
	def   name(self , value):
		print('Setter  Method')
		self._name = value
	@name.deleter
	def  name(self):
		print('Deleter  method ')
		del  self._name
#end  of  the  class
p = Person()
print(p . name)
p.name = 'Vamsi'
print(p.name)
del   p.name
#print(p . name) #Error there is no value in name method
#del   p #Error there no p defined in program



'''
Output:
Setter Method
getter Method

Setter Method
getter Method
Vamsi
Deleter method
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
    def __init__(self, empno, ename, sal):
        self.empno = empno
        self.ename = ename
        self.sal = sal
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
    def empno(self, value):
        if value <= 0:
            raise ValueError(" Emp number cannot be negative")
        self._empno = value

    @ename.setter
    def ename(self, value):
        if value.strip() == "":
            raise ValueError("Emp name cannot be empty")
        self._ename = value

    @sal.setter
    def sal(self, value):
        if value <= 0:
            raise ValueError("Salary cannot be negative")
        self._sal = value

#End of the class
while True:
    try:
        empno = int(input("Enter employee number : "))
        ename = input("Enter employee name : ")
        sal = float(input("Enter salary : "))

        e = Emp(empno, ename, sal)

        print("Employee number :", e.empno)
        print("Employee name :", e.ename)
        print("Employee salary :", e.sal)
        break  # exit loop if everything is valid

    except ValueError as err:
        print(err)
        print()  # just for spacing before retrying

    

# Enter  employee  number :  -25
#Empno cannot be negative

# Enter  employee  number :  25
#Enter  employee  name :
#Emp  name cannot be empty  string

#Enter  employee  number :  25
#Enter  employee  name :  Vamsi
#Enter  salary :  -20
#Salary cannot be negative

#Enter  employee  number :  25
#Enter  employee  name :  Vamsi
#Enter  salary :  10000.0
#Employee number  :  25
#Employee name  :  Vamsi
#Employee salary :   10000.0


