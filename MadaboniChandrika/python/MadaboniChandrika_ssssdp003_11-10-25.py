#1st program
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
print(p . name)#getter method /n ""
p . name = 'Vamsi'#setter method
print(p . name)#getter method /n "Vamsi"
del   p . name #deleter method
#print(p . name)
del   p #object  is  deleted

#obj  p---> name="" 


#2nd program
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
        self.Empno=int (input("Enter Employee Number: "))
        self.Empname=input("Enter Employee Name: ")
        self.Salary=float(input("Enter Employee Salary: "))
    @property
    def Empno(self):
        return self.t1
    @property
    def Empname(self):
        return self.t2
    @property
    def Salary(self):
        return self.t3
    @Empno.setter
    def Empno(self,value):
        if value<0:
            raise ValueError("Employee no. cannot be negative")
        else:
            self.t1=value
    @Empname.setter
    def Empname(self,name):
        if name=='':
            raise ValueError("Employee name cannot be empty")
        else:
            self.t2=name
    @Salary.setter
    def Salary(self,sal):
        if sal<0:
            raise ValueError("Salary cannot be negative")
        else:
            self.t3=sal
e=Employee()
print("Employee Number: ",e.Empno)
print("Employee Name: ",e.Empname)
print("Employee Salary: ",e.Salary)


