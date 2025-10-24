from  abc  import  *
class  person(ABC):
	def   get(self):
		self.num=int(input('Enter number:'))	#How  to   read  number
		self.name=input('Enter name:')	#How  to   read  name
		self.age=int(input('Enter age'))	#How  to   read   age
		self.gender=input('Enter gender')	#How  to   read   gender
	def   disp(self):
		print('number:', self.num, 'name:', self.name, 'age:',self.age, 'gender:',self.gender, sep='\t',end='\t')	#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get() 	#How  to  read   number , name , age , gender
		self.marks = []                                 # list to store marks
		for i in range(3):
			m = float(input(f'Enter subject {i+1} marks: '))
			self.marks.append(m)	#How  to  read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total = sum(self.marks)	#How  to  calculate  total  marks
		self.avg = self.total / 3	#How  to  calculate  average  marks
	def  disp(self):
		super().disp()	#How  to  print  number , name , age , gender
		print('Total:', self.total, 'Average:', self.avg, sep='\t')	#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get()	#How  to  read  number , name , age  and  gender
		self.subject = input('Enter subject: ')	# How  to  read   subject
		self.salary = float(input('Enter salary: '))	# How  to  read   salary
		self.city = input('Enter city: ')	#How  to  read   city
	def   compute(self):
		da = 0.50*self.salary	#50%  of  salary
		hra = 0.20*self.salary	#20%  of  salary
		if self.city.lower() == 'hyd':
			cca = 1000	#cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		else:
			cca = 800
		self.grosspay = self.salary + da + hra + cca	#How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = 0.08* self.grosspay
		if pf>400:
			pf=400	#8%  of  grosspay  but  a  max  of  400
		if self.grosspay < 10000:
			tax = 0.10 * self.grosspay
		else:
			tax = 0.15 * self.grosspay	#tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.netpay = self.grosspay - pf - tax	#How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().disp()	#How  to  print  number , name , age , gender
		print('Subject:', self.subject, 'Salary:', self.salary,'GrossPay:', self.grosspay, 'NetPay:', self.netpay, sep='\t')	#How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
		a.append(teacher())	#How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
		a.append(student())	#	How  to  append  student  object  to  list  'a'
	else:
		break	#	How  to  stop  execution
	a[-1].get()	#How  to  read  inputs  into  object
	a[-1].compute()	#How  to  store   results  in  object
	#How  to  move  to  next  index
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
for obj in a:                                     
	if isinstance(obj, teacher):
		obj.disp()	#How  to  print  all  teacher  objects
print()
print('Students')
for obj in a:                                     
	if isinstance(obj, student):
		obj.disp()	#How  to  print  all  student  objects
print('Good  Bye')
1. Teacher
2. Student
3. Exit
1. Teacher
2. Student
3. Exit
1. Teacher
2. Student
3. Exit
1. Teacher
2. Student
3. Exit
1. Teacher
2. Student
3. Exit
Teachers
number:	10	name:	Radha	age:	30	gender:	Female	Subject:	Java	Salary:	30000.0	GrossPay:	52000.0	NetPay:	43800.0

Students
number:	1	name:	Krishna	age:	20	gender:	Male	Total:	210.0	Average:	70.0
Good  Bye
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
			self.x=int(input('enter no: ')) #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x  #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x)    #How  to  print  sum  result)
class   string(datatype):
	def  get(self):
			self.x =input('Enter string: ') #How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + n.x  #How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x)   # How  to  print  the   join  result)
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
				ob = [number(), number(), number()]	#How  to  create  list  of  3  number  class  objects
			elif  ch  == 2:
				ob = [string(), string(), string()]	#How  to  create  list  of  3  string  class  objects
			else:
				break  #How  to  stop  execution
			ob[0].get() #How  to  read  input  into  first  object
			ob[1].get() #How  to  read  input  into  2nd  object
			ob[2].add(ob[0], ob[1]) #How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			ob[2].display() #How  to  print  3rd  object
	# end of  while  loop
print('Good  Bye')
	
''' 
1. Add numbers
2. Join Strings
3. Exit
Enter choice : 2
Enter string:20
Enter string:20
Join of the two strings :
2020
1. Add numbers
2. Join Strings
3. Exit
Enter choice : 1
Enter a number:20
Enter a number:20
Sum of the numbers :
40
1. Add numbers
2. Join Strings
3. Exit
Enter choice : 2
Enter string:Hyder
Enter string:abad
Join of the two strings :
Hyderabad
1. Add numbers
2. Join Strings
3. Exit
Enter choice: 3
Good Bye
Press any key to continue'''
1. Add  numbers
2. Join  Strings
3. Exit
Join  of  the  two  strings :   1020
1. Add  numbers
2. Join  Strings
3. Exit
Sum  of  the  numbers  :   30
1. Add  numbers
2. Join  Strings
3. Exit
Good  Bye
