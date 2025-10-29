# # Find  outputs (Home work)
# class  Person:
# 	def  _init_(self):
# 		self . name  =  ''
# 	@property
# 	def   name(self):
# 		print('getter  method')
# 		return  self . _name
# 	@name . setter
# 	def   name(self , value):
# 		print('Setter  Method')
# 		self . _name = value
# 	@name . deleter
# 	def  name(self):
# 		print('Deleter  method ')
# 		del  self .  _name
# #end  of  the  class
# p = Person()
# print(p . name)
# p . name = 'Vamsi'
# print(p . name)
# del   p . name
# #print(p . name)
# del   p

    
    
    
    
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
    def __init__(self):
        self.empno = 0
        self.empname = ''
        self.salary = 0.0

    @property
    def empno(self):
        return self.empno
    
    @property
    def empname(self):
        return self.empname
    
    @property
    def salary(self):
        return self.salary
    
    @empno.setter
    def empno(self,x):
        if x < 0 :
            raise ValueError("Emp No cannot be Less than one")
        self.empno = x
        
    @empname.setter    
    def empname(self,x):
        if len(x) == 0:
            raise ValueError("Emp Name cannot be Empty String")
        self.empname = x
        
    @salary.setter
    def salary(self,x):
        if x < 0:
            raise ValueError('Salary cannot be less Than Zero')  
        self.salary = x

a = Emp()
while True:
    try:
        a.empno = int(input("Enter the Emp No: "))
        a.empname = input("Enter the Emp Name: ")
        a.salary = float(input("Enter the Salary: "))
        print('Employee Details:')
        print("Employee number  : ", a.empno)
        print("Employee name  : ", a.empname)
        print("Employee salary  : ", a.salary)
        break
    except ValueError as ve:
        print(ve)
        

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