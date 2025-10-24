# Program 
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input("Enter your Number :"))  # How  to   read  number
		self.name=input("Enter your Name :") # How  to   read  name
		self.age=int(input("Enter your Age :"))  # How  to   read   age
		self.gender=input("Enter your Gender (M/F) :")  # How  to   read   gender
	def   disp(self):
		print("Number :",self.number) # How  to  print  number , name , age , gender  in  same  line  separated  by  tab
		print("Name :",self.name)
		print("Age :",self.age)
		print("Gneder :",self.gender)
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()  #How  to  read   number , name , age , gender
		self.marks=[]  #How  to  read  marks  of  3  subjects  into  a  list
		for i in range(3):
			m=int(input(F"Enter marks of M{i+1}:"))
			self.marks.append(m)
	def  compute(self):
		self.total=sum(self.marks)  # How  to  calculate  total  marks
		self.avg=self.total/len(self.marks)  #How  to  calculate  average  marks
	def  disp(self):
		super().disp()  # How  to  print  number , name , age , gender
		print("Total Marks :",self.total)  #How  to  print  total  and  average  in  same  line separated  by  tab
		print("Average",self.avg)
class  teacher(person):
	def   get(self):
		super().get() #How  to  read  number , name , age  and  gender
		self.sub=input("Enter Your Subject Teach :")  # How  to  read   subject
		self.sal=int(input("Enter Your Salary :")) # How  to  read   salary
		self.city=input("Enter Your City :") # How  to  read   city
	def   compute(self):
		self.da =self.sal * 50/100
		self.hra =self.sal * 20/100
		if self.city =="Hyd"or "hyd":
			self.cca=1000
		else:
			self.cca=500
		self.gross_pay=self.sal+self.da+self.hra+self.cca
		self.pf=8/100 * self.gross_pay
		if self.pf > 400:
			self.pf=400
		if self.gross_pay>10000:
			self.tax=10/100 * self.gross_pay
		else:
			self.tax=15/100 * self.gross_pay
		self.net_pay=self.gross_pay-self.pf-self.tax
	def   disp(self):
		super().disp()  # How  to  print  number , name , age , gender
		print("Salary :",self.sal)  # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
		print("Gross Salary :",self.gross_pay)
		print("Net Salary :",self.net_pay)
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
			t=teacher()  # How  to  append  teacher  object  to  list  'a'
			t.get()
			t.compute()
			a.append(t)
	elif  ch == 2:
			s=student()  # How  to  append  student  object  to  list  'a'
			s.get()
			s.compute()
			a.append(s)
	elif ch==3:
		break  # How  to  stop  execution
	else:
		print("Invalid Number")
#end of loop
print('Teachers')
for obj in a :  # How  to  print  all  teacher  objects
	if isinstance(obj,teacher):
		obj.disp()
print()
print('Students')
for obj in a: # How  to  print  all  student  objects
	if isinstance(obj,student):
		obj.disp()
print('Good  Bye')

# Program
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
			self.x=int(input("Enter Any Number :"))  # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.sum=m.x+n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' ,self.sum)
class   string(datatype):
	def  get(self):
			self.x=input("Enter any String :") # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.sum=m.x+n.x  # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.sum)
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
					a=number()  #How  to  create  list  of  3  number  class  objects
					b=number()
					c=number()
			elif  ch  == 2:
					a=string()  # How  to  create  list  of  3  string  class  objects
					b=string()
					c=string()
			else:
					break # How  to  stop  execution
			a.get()  # How  to  read  input  into  first  object
			b.get() # How  to  read  input  into  2nd  object
			c.add(a,b)  # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			c.display()  # How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')
