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

class emp:
    def _init_(self):
        self.empno=int(input("Enter Employee Number : "))
        self.ename=input("Enter Employee Name : ")
        self.sal=float(input("Enter Employee Salary : "))
    @property
    def empno(self):
        return self._empno
    @empno.setter
    def empno(self,x):
        if x<0:
            raise ValueError("Employee Number cannot be negative")
        self._empno=x
    @property
    def ename(self):
        return self._ename
    @ename.setter
    def ename(self,x):
        if x=='':
            raise ValueError("Employee Name cannot be Empty")
        self._ename=x
    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self,x):
        if x<0:
            raise ValueError("Salary cannot be negative")
        self._sal=x
try:
    e=emp()
    print("Employee Number : ",e.empno)
    print("Employee Name : ",e.ename)
    print("Employee Salary : ",e.sal)
except ValueError as message:
    print(message)