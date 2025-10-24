'''#1.  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number = int(input("Enter Id number : ")) # How  to   read  number
		self.name = input("Enter Name : ") # How  to   read  name
		self.age = int(input("Enter age : ")) # How  to   read   age
		self.gender = input("Enter Gender : ") # How  to   read   gender
	def   disp(self):
		print(self.number, self.name, self.age, self.gender, sep = '\t',end = "\t") # How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get() # How  to  read   number , name , age , gender
		self.marks = [] # How  to  read  marks  of  3  subjects  into  a  list
		for i in range(3):
			mark = int(input(f'Enter marks for subject {i+1} : '))
			self.marks.append(mark)
	def  compute(self):
		self.tot = sum(self.marks) # How  to  calculate  total  marks
		self.avg = self.tot/len(self.marks) # How  to  calculate  average  marks
	def  disp(self):
		super().disp() # How  to  print  number , name , age , gender
		print(self.tot, self.avg, sep='\t' ) # How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get() # How  to  read  number , name , age  and  gender
		self.sub = input("Enter subject : ") # How  to  read   subject
		self.sal = int(input("Enter salary : ")) # How  to  read   salary
		self.city = input("Enter city : ") # How  to  read   city
	def   compute(self):
		da = 0.5 * self.sal
		hra = 0.2 * self.sal
		if self.city.lower() == 'hyd':
			cca = 1000
		else:
			cca = 800
		self.grosspay = self.sal + da + hra + cca
		pf = min(0.08 * self.grosspay, 400)
		if self.grosspay < 10000:
			tax = 0.1 * self.grosspay
		else:
			tax = 0.15 * self.grosspay
		self.netpay = self.grosspay - pf - tax 
	def   disp(self):
		super().disp() # How  to  print  number , name , age , gender
		print(self.sub, self.sal, self.grosspay, self.netpay, sep = '\t') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			obj = teacher()
			obj.get()  
			obj.compute()
			a.append(obj)  # How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			obj = student()
			obj.get()
			obj.compute()
			a.append(obj)
			# How  to  append  student  object  to  list  'a'
	else:
			break # How  to  stop  execution  of  loop
	

print('Teachers')
for obj in a:
	if isinstance(obj, teacher):
		obj.disp()  # How  to  print  all  teacher  objects
print()
print('Students')
for obj in a:
	if isinstance(obj, student):
		obj.disp()  # How  to  print  all  student  objects
print('Good  Bye')'''



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
			self.x = int(input("Enter a number : ")) # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + n.x # How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x)
class   string(datatype):
	def  get(self):
			self.x = input("Enter a string : ") # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + n.x # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x)
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if  __name__ == '__main__':
	while  True:
			menu()
			ch =  eval(input('Enter choice : '))
			if   ch == 1:
					m = number() # How  to  create  list  of  3  number  class  objects
					m.get()
					n = number()
					n.get()
					o = number()
					o.add(m , n)
					o.display()
			elif  ch  == 2:
					m = string() # How  to  create  list  of  3  string  class  objects
					m.get()
					n = string()
					n.get()
					o = string()
					o.add(m , n)
					o.display()
			else:
					break # How  to  stop  execution
			
	# end of  while  loop
	print('Good  Bye')