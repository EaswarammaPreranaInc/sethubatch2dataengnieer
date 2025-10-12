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
o/p:
getter  method
None
Setter  Method
getter  method
Vamsi
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

    @empno.setter
    def empno(self, value):
        if value < 0:
            raise ValueError("Emp number cannot be negative")
        self._empno = value

    @property
    def ename(self):
        return self._ename

    @ename.setter
    def ename(self, value):
        if not value:
            raise ValueError("Emp name cannot be empty")
        self._ename = value

    @property
    def sal(self):
        return self._sal

    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._sal = value
# end of the class 
if __name__ == '__main__':
        
    try:
        emp = Emp(101, "John Doe", 50000)
        print(f"Emp No: {emp.empno}, Emp Name: {emp.ename}, Salary: {emp.sal}") 
    except ValueError as e:
        print(e)    
# o/p: Emp No: 101, Emp Name: John Doe, Salary: 50000

#  Write  functions  to  create  and  print  linked  list
class  node:
		def   _init_(self , x):
				self . data = x
				self . link = None
		#   new  = node(25)
class  linked_list:
		def   _init_(a):
				a . first = None
		#  a = linked_list()
		def  isempty(a):
				return  a . first == None
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p  !=  None:
								print(p . data , end = '\t')
								p = p . link
						print()
		def  append(a , new):
				if   a . isempty():
						a . first = new
				else:
						last = a . first
						while  last . link != None:
								last = last . link
						last . link = new
		def  create(a):
				try:
						a . first = None
						print('Enter  values  terminated  by  ctrl+z')
						while  True:
								x = eval(input())
								new = node(x)
								a . append(new)
				except:
						pass
# End  of  the  class
if  __name__ == '__main__':
	a = linked_list()
	a . create()
	print('Linked  List  :  ' , end = '')
	a . disp()
	
# o/p:
# Enter  values  terminated  by  ctrl+z
# 10
# 20    
# 30
# 40
# ^Z
# Linked  List  :  10	20	30	40