#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from abc import  *
class person(ABC):
	def get(self):
		self.number = int(input("Enter number:")) # How  to   read  number
		self.name = input("Enter name:") # How  to   read  name
		self.age = int(input("Enter age:")) # How  to   read   age
		self.gender = input("Enter gender:") # How  to   read   gender
	def disp(self):
		print(self.number, self.name, self.age, self.gender, sep =  '\t', end = '\t') # How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def compute(self):
		pass
class student(person):
	def get(self):
		super().get() # How  to  read   number , name , age , gender
		self.m = []
		for i in range(3):
			marks = float(input(F"Enter marks of {i+1} subject:"))
			self.m.append(marks) # How  to  read  marks  of  3  subjects  into  a  list
	def compute(self):
		self.total = sum(self.m) # How  to  calculate  total  marks
		self.avg = self.total/3 # How  to  calculate  average  marks
	def disp(self):
		super().disp() # How  to  print  number , name , age , gender
		print(self.total, self.avg, sep = '\t') # How  to  print  total  and  average  in  same  line separated  by  tab
class teacher(person):
	def get(self):
		super().get() # How  to  read  number , name , age  and  gender
		self.sub = input("Enter subject:") # How  to  read   subject
		self.sal = float(input("Enter salary:")) # How  to  read   salary
		self.city = input("Enter city:") # How  to  read   city
	def compute(self):
		da = 0.50 *  self.sal # 50%  of  salary
		hra = 0.20 * self.sal # 20%  of  salary
		if self.city == 'Hyd':
			cca = 1000
		else:
			cca = 800 # cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		self.gp = self.sal + da + hra + cca # How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 0.8 * self.gp 
		if self.gp > 400:
			pf = 400 # 8%  of  grosspay  but  a  max  of  400
		if self.gp < 10000:
			tax = 0.10 * self.gp
		else:
			tax = 0.10 * self.gp + (0.15 - 10000) * self.gp  # tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.np = self.gp - pf - tax # How  to  calculate  netpay  i.e. grosspay - pf - tax
	def disp(self):
		super().disp() # How  to  print  number , name , age , gender
		print(self.sub, self.sal, self.city, self.gp, self.np, sep = '\t') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
def menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
while True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		a.append(teacher()) # How  to  append  teacher  object  to  list  'a'
	elif ch == 2:
		a.append(student()) # How  to  append  student  object  to  list  'a'
	else:
		break # How  to  stop  execution
	a[-1].get() # How  to  read  inputs  into  object
	a[-1].compute() # How  to  store   results  in  object
#end of loop
print('Teachers')
for i in a:
	if isinstance(i, teacher):
		i.disp() # How  to  print  all  teacher  objects
print()
print('Students')
for i in a:
	if isinstance(i, student):
		i.disp() # How  to  print  all  student  objects
print('Good Bye')
'''
Outputs
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number:111
Enter name:AAA
Enter age:30
Enter gender:M
Enter subject:python
Enter salary:10000
Enter city:Hyd
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number:222
Enter name:BBB
Enter age:30
Enter gender:F
Enter marks of 1 subject:34
Enter marks of 2 subject:67
Enter marks of 3 subject:76
1. Teacher
2. Student
3. Exit
Enter choice : 1
Enter number:333
Enter name:CCC
Enter age:40
Enter gender:M
Enter subject:Java
Enter salary:20000
Enter city:Warangal
1. Teacher
2. Student
3. Exit
Enter choice : 2
Enter number:444
Enter name:DDD
Enter age:24
Enter gender:M
Enter marks of 1 subject:34
Enter marks of 2 subject:67
Enter marks of 3 subject:76
1. Teacher
2. Student
3. Exit
Enter choice : 3
Teachers
111     AAA     30      M       python  10000.0 Hyd     18000.0 180013100.0
333     CCC     40      M       Java    20000.0 Warangal        34800.0 348025700.0     

Students
222     BBB     30      F       155.0   51.666666666666664
444     DDD     24      M       188.0   62.666666666666664 
Good Bye
'''









#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from abc import abstractmethod , ABC
class  datatype(ABC):
	@abstractmethod
	def get(self):
		pass
	@abstractmethod
	def add(self , m ,  n):
		pass
	@abstractmethod
	def display(self):
		pass
class number(datatype):
	def get(self):
		self.x = float(input("Enter number input:")) # How  to  read  number  into  variable  'x' of  object  self
	def add(self , m , n):
		self.x = m.x + n.x # How  to  add  objects  m  and  n  and  store  result  in  object  self
	def display(self):
		print('Sum  of  the  numbers  :  ' , self.x) # How  to  print  sum  result)
class string(datatype):
	def get(self):
		self.x = input("Enter string input:") #vHow  to  read  string  into  variable  'x' of  object  self
	def add(self , m , n):
		self.x = m.x + n.x # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def display(self):
		print('Join  of  the  two  strings :  ' , self.x) # How  to  print  the   join  result)
def menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if __name__ == '__main__':
	while True:
		menu()
		ch =  eval(input('Enter choice : '))
		if ch == 1:
			a = (number(), number(), number()) # How  to  create  list  of  3  number  class  objects
		elif  ch  == 2:
			a = (string(), string(), string())  # How  to  create  list  of  3  string  class  objects
		else:
			break # How  to  stop  execution
		a[0].get() # How  to  read  input  into  first  object
		a[1].get() # How  to  read  input  into  2nd  object
		a[2].add(a[0], a[1]) # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
		a[2].display() # How  to  print  3rd  object
	# end of  while  loop
	print('Good Bye')
'''
Outputs
1. Add  numbers
2. Join  Strings
3. Exit
Enter choice : 1 
Enter number input:34
Enter number input:54
Sum  of  the  numbers  :   88.0
1. Add  numbers
2. Join  Strings
3. Exit
Enter choice : 2
Enter string input:Hyder
Enter string input:abad
Join  of  the  two  strings :   Hyderabad
1. Add  numbers
2. Join  Strings
3. Exit
Enter choice : 3
Good Bye
'''