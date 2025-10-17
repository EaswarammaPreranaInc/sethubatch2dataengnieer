 #Find  outputs (Home work)
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
print(p . name) #
del   p . name
print(p.name)
del p

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
    a) Create Emp class object
    b) Print empno , ename and sal
'''
class Emp:
    def __init__(self,):
        self.empno=int(input('Enter employee no: '))
        self.ename=input('Enter employee name: ')
        self.sal=float(input('Enter employee salary: '))
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
        if x<0:
            raise ValueError('Empno cannot be negative')
        self._empno=x
    @ename.setter
    def ename(self,y):
        if y=='':
            raise ValueError('Ename cannot be empty')
        self._ename=y
    @sal.setter
    def sal(self,z):
        if z<0:
            raise ValueError('Salary cannot be negative')
        self._sal=z
try:
	a=Emp()
	print('Employee number :',a.empno)
	print('Employee name :',a.ename)
	print('Employee salary:',a.sal)
except  ValueError  as  msg:
	print(msg)