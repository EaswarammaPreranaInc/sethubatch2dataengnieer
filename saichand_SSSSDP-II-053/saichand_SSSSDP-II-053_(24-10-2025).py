'''
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		How  to   read  number
		How  to   read  name
		How  to   read   age
		How  to   read   gender
	def   disp(self):
		How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		How  to  read   number , name , age , gender
		How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
	def  disp(self):
		How  to  print  number , name , age , gender
		How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		How  to  read  number , name , age  and  gender
		How  to  read   subject
		How  to  read   salary
		How  to  read   city
	def   compute(self):
		da = 50%  of  salary
		hra = 20%  of  salary
		cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 8%  of  grosspay  but  a  max  of  400
		tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		How  to  print  number , name , age , gender
		How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
while  True:
	menu()
	ch = eval(input('Enter choice : '))
	if   ch == 1:
			How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			How  to  append  student  object  to  list  'a'
	else:
			How  to  stop  execution
	How  to  read  inputs  into  object
	How  to  store   results  in  object
	How  to  move  to  next  index
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
How  to  print  all  teacher  objects
print()
print('Students')
How  to  print  all  student  objects
print('Good  Bye')
'''

#Program:
from abc import *
class person(ABC):
	def get(self):
		self.number = int(input("Enter number: "))
		self.name = input("Enter name: ")
		self.age = int(input("Enter age: "))
		self.gender = input("Enter gender: ")
	def disp(self):
		print(self.number, self.name, self.age, self.gender, sep="\t")
	@abstractmethod
	def compute(self):
		pass
class student(person):
	def get(self):
		super().get()
		self.marks = []
		print("Enter marks of 3 subjects:")
		for i in range(3):
			self.marks.append(float(input(f"Mark {i+1}: ")))
	def compute(self):
		self.total = sum(self.marks)
		self.avg = self.total / 3 
	def disp(self):
		super().disp()
		print(self.total, self.avg, sep="\t")
class teacher(person):
	def get(self):
		super().get()
		self.subject = input("Enter subject: ")
		self.salary = float(input("Enter salary: "))
		self.city = input("Enter city: ")
	def compute(self):
		da = 0.5 * self.salary
		hra = 0.2 * self.salary
		cca = 1000 if self.city.lower() == 'hyd' else 800
		self.grosspay = self.salary + da + hra + cca
		pf = 0.08 * self.grosspay 
		if pf > 400:
			pf = 400 
		if self.grosspay < 10000:
			tax = 0.1 * self.grosspay
		else:
			tax = 0.15 * self.grosspay
		self.netpay = self.grosspay - pf - tax
	def disp(self):
		super().disp()
		print(self.subject, self.salary, self.grosspay, self.netpay, sep="\t")
def menu():
	print("\n1. Teacher")
	print("2. Student")
	print("3. Exit")
a = []
while True:
	menu()
	ch = int(input("Enter choice: "))
	if ch == 1:
		obj = teacher()
	elif ch == 2:
		obj = student()
	elif ch == 3:
		break
	else:
		print("Invalid choice!")
		continue
	obj.get()
	obj.compute()
	a.append(obj)
# End of loop
print("\nTeachers")
for i in a:
	if isinstance(i, teacher):
		i.disp()
print("\nStudents")
for i in a:
	if isinstance(i, student):
		i.disp()
print("\nGood Bye")








'''
#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):
	@abstractmethod
	def  get(self):
		 pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
			How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , How  to  print  the   join  result)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if  _name_ == '_main_':
	while  True:
			menu()
			ch =  eval(input('Enter choice : '))
			if   ch == 1:
					How  to  create  list  of  3  number  class  objects
			elif  ch  == 2:
					How  to  create  list  of  3  string  class  objects
			else:
					How  to  stop  execution
			How  to  read  input  into  first  object
			How  to  read  input  into  2nd  object
			How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')
'''

#Program:
from abc import abstractmethod, ABC
class datatype(ABC):
	@abstractmethod
	def get(self):
		pass
	@abstractmethod
	def add(self, m, n):
		pass
	@abstractmethod
	def display(self):
		pass
class number(datatype):
	def get(self):
		self.x = int(input("Enter number: "))
	def add(self, m, n):
		self.x = m.x + n.x
	def display(self):
		print("Sum of the numbers :", self.x)
class string(datatype):
	def get(self):
		self.x = input("Enter string: ")
	def add(self, m, n):
		self.x = m.x + n.x
	def display(self):
		print("Join of the two strings :", self.x)
def menu():
	print("\n1. Add numbers")
	print("2. Join Strings")
	print("3. Exit")
while True:
	menu()
	ch = eval(input("Enter choice : "))
	if ch == 1:
		a = [number(), number(), number()]
	elif ch == 2:
		a = [string(), string(), string()]
	else:
		break
	a[0].get()
	a[1].get()
	a[2].add(a[0], a[1])
	a[2].display()
# end of while loop
print("Good Bye")