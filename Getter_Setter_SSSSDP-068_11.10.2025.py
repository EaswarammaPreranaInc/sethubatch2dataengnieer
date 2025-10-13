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

'''
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
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    # Setter methods
    def set_empno(self, empno):
        if empno < 0:
            raise ValueError("Empno cannot be negative")
        self.__empno = empno

    def set_ename(self, ename):
        if ename.strip() == "":
            raise ValueError("Emp name cannot be empty string")
        self.__ename = ename

    def set_sal(self, sal):
        if sal < 0:
            raise ValueError("Salary cannot be negative")
        self.__sal = sal

    # Getter methods
    def get_empno(self):
        return self.__empno

    def get_ename(self):
        return self.__ename

    def get_sal(self):
        return self.__sal
while True:
    try:
        empno = int(input("Enter employee number :  "))
        if empno < 0:
            print("Empno cannot be negative")
            continue

        ename = input("Enter employee name :  ")
        if ename.strip() == "":
            print("Emp name cannot be empty string")
            continue

        sal = float(input("Enter salary :  "))
        if sal < 0:
            print("Salary cannot be negative")
            continue
        e = Emp(empno, ename, sal)
        break

    except ValueError as err:
        print(err)
        continue

# Print employee details
print("Employee number  : ", e.get_empno())
print("Employee name  : ", e.get_ename())
print("Employee salary :  ", e.get_sal())
