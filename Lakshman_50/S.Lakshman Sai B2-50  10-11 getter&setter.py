
# Write  a  program  to  implement  min  priority  queue  using  list
class  priority_queue:
	def  _init_(pq):
		How  to  create  an  empty  list  in  object  pq
	def  isempty(pq):
		return  True  when  list  held  by  object  pq   is  empty  and  False  otherwise
	def  insert(pq , x):
		 How  to  insert  'x'  into  the  list  held  by  object  pq
		 How  to  sort  the  list  held  by  object  pq
	def  delete(pq):
		How  to  delete  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  deletion  is  not  possible)
	def  highest_priority(pq):
		How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  the  list  is  empty)
	def  smallest_priority(pq):
		How  to  return  the  highest  priority  element  from  the  list  held  by  object  pq
		(return  None  when  the  list  is  empty)
	def  disp(pq):
		How  to  print  the  list  held  by  object  pq
	def   size(pq):
		How  to  return  number   of  elements  in  the  list  held  by  object  pq
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  priority  queue')
        print('4. Highest  priority  element of  priority  queue')
        print('5. Smallest  priority  element of  priority  queue')
        print('6. Number  of  elements  in  the  priority  queue')
        print('7. Exit')
# End of  the  function
if  _name_  ==  '_main_':
	How  to  create  priority_queue  class  object
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
						x = eval(input('Enter  element  to  be  inserted : '))
						How  to  insert  'x'  into  priority  queue
						How  to  print  priority  queue
			case  2:
						How  to  delete  highest  priority  element  from  priority  queue  and  print
						if  ???:
							print('Priority  queue  is  empty  , deletion  is  not  permitted')
						else:
							print('Deleted  element : '  , ???)
						How  to  print  priority  queue
			case  3:
						How  to  print  priority  queue
			case  4:
						How  to  obtain  highest  priority  element
						if  ???
							print('Priority  queue  is  empty')
						else:
							print('Highest  priority  element :  ' ,  ???)
			case  5:
						How  to  obtain  smallest  priority  element
						if  ???
							print('priority  queue  is  empty')
						else:
							print('Smallest  priority  element :  ' ,  ???)
			case  6:
						print('Number  of  elements  :  ' ,  ???)
			case  7:  exit()
		# End  of  match


#===================================================================================

#Object  'pq'   --->  list = []
 Here  is  the  blueprint  of  priority  queue

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


#=================================================================================
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

class  Emp:
	def __init__(self):
		self.empno=0
		self.ename=" "
		self.sal=0.0

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
			raise ValueError("Empno cannot be negative")
		self._empno=x

	@ename.setter
	def ename(self,x):
		if x=="":
			raise ValueError("Emp name cannot be empty string")
		self._ename=x

	@sal.setter
	def sal(self,x):
		if x<0:
			raise ValueError("Salary cannot be negative")
		self._sal=x

#end of the class
e=Emp()
while True:
	try:
		e.empno=int(input("enter the emp id :"))
		e.ename=input("enter the emp name :")
		e.sal=float(input("enter the emp salary : "))
	except ValueError as ve:
		print(ve)
	else:
		break

print("Employee number  : ", e.empno)
print("Employee name  : ", e.ename)
print("Employee salary : ", e.sal)

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


class Emp:
    def __init__(self):
        self.empno = 0
        self.ename = " "
        self.sal = 0.0

    @property
    def empno(self):
        return self._empno

    @empno.setter
    def empno(self, x):
        if x < 0:
            raise ValueError("Empno cannot be negative")
        self._empno = x

    @property
    def ename(self):
        return self._ename

    @ename.setter
    def ename(self, x):
        if x== "":
            raise ValueError("Emp name cannot be empty")
        self._ename = x

    @property
    def sal(self):
        return self.sal

    @sal.setter
    def sal(self, x):
        if x < 0:
            raise ValueError("Salary cannot be negative")
        self._sal = x


# ---- end of class ----

e = Emp()
while True:
   try:
       e.empno = int(input("Enter the emp id: "))
       e.ename = input("Enter the emp name: ")
       e.sal = float(input("Enter the emp salary: "))
   except ValueError as ve:
       print("Error:", ve)
	else:
		break

print("\nEmployee Details:")
print("Employee number :", e.empno)
print("Employee name   :", e.ename)
print("Employee salary :", e.sal)
