#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.no=int(input("Enter number:")) #How  to   read  number
		self.name=input("Enter name:") #How  to   read  name
		self.age=int(input("Enter age:")) #How  to   read   age
		self.gender=input("Enter gender M/F?:") #How  to   read   gender
	def   disp(self):
		print(self.no,self.name,self.age,self.gender,sep='\t',end='\t') #How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get() #How  to  read   number , name , age , gender
		self.marks=[]
		for i in range(3):
			self.marks.append(int(input(f'Enter {i+1} subject marks'))) #How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total=0 #How  to  calculate  total  marks
		for x in self.marks:
			self.total+=x
		self.avg=self.total/len(self.marks) #How  to  calculate  average  marks
	def  disp(self):
		super().disp() #How  to  print  number , name , age , gender
		print(self.total,self.age,sep='\t') #How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get() #How  to  read  number , name , age  and  gender
		self.subject =input("Enter subject:") #How  to  read   subject
		self.sal=int(input("Enter salary:")) #How  to  read   salary
		self.city=input("Enter city:") #How  to  read   city
	def   compute(self):
		da = self.sal /2 #50%  of  salary
		hra = (self.sal)/5 #20%  of  salary
		if self.city=='Hyd':
			cca=1000
		else:
			cca=800
		# cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		self.gpay=self.sal+da+hra+cca # How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = min(400,(8*self.gpay)/100) # 8%  of  grosspay  but  a  max  of  400
		tax=0
		if self.gpay<10000:
			tax=self.gpay/10
		else:
			tax=self.gpay*15/100
		# tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		# How  to  calculate  netpay  i.e. grosspay - pf - tax
		self.netpay=self.gpay-pf-tax
	def   disp(self):
		super().disp() #How  to  print  number , name , age , gender
		print(self.subject,self.sal,self.gpay,self.netpay,sep='\t') #How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			a.append(teacher()) #How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
			a.append(student())#How  to  append  student  object  to  list  'a'
	else:
			break #How  to  stop  execution
	a[-1].get() #How  to  read  inputs  into  object
	a[-1].compute() #How  to  store   results  in  object
	# How  to  move  to  next  index
	# menu()
	# ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
for x in a:
	if isinstance(x,teacher):
		x.disp()
# How  to  print  all  teacher  objects
print()
print('Students')
# How  to  print  all  student  objects
for x in a:
	if isinstance(x,student):
		x.disp()
print('Good  Bye')

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
			self.x=int(input("Enter x:")) #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x) #How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			self.x=input("Enter x:") #How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x #How  to  join  objects  m  and  n  and  store  result  in  object  self
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
			l=[]
			if   ch == 1:
					l=[number(),number(),number()] #How  to  create  list  of  3  number  class  objects
			elif  ch  == 2:
					l=[string(),string(),string()] #How  to  create  list  of  3  string  class  objects
			else:
					break #How  to  stop  execution
			l[0].get() #How  to  read  input  into  first  object
			l[1].get() #How  to  read  input  into  2nd  object
			l[2].add(l[0],l[1]) #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			l[2].display() #How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')