#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.num=int(input('enter a num: '))			# How  to   read  number
		self.name=int(input('enter a name: '))			# How  to   read  name
		self.age=int(input('enter a age: '))			# How  to   read   age
		self.gender=int(input('enter a genter: '))			# How  to   read   gender
	def   disp(self):
		print(f"name: {self.name} \t age: {self.age} \t gender: {self.gender}",end='\t')		# How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get()						# How  to  read   number , name , age , gender
		self.marks=[]						# How  to  read  marks  of  3  subjects  into  a  list
	        for i in range(3):
			m=float(input(f"enter marks for subject{i+1}: "))
			self.marks.append(m)
	def  compute(self):
		self.total=sum(self.marks)					# How  to  calculate  total  marks
		self.avg=self.total/3						# How  to  calculate  average  marks
	def  disp(self):
		super.disp()							# How  to  print  number , name , age , gender
		print(f"total: {self.total} \t average: {self.avg:2f}")		#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get()						# How  to  read  number , name , age  and  gender
		self.subject=input('enter subject: '))			# How  to  read   subject
		self.salay=float(input('enter salary: '))		# How  to  read   salary
		self.city=input('enter city: '))			# How  to  read   city
	def   compute(self):
		da = 50% * self.salary					# da = 50%of  salary
		hra = 20%  self.salary					# of  salary
		cca = 1000  	
		if self.city.lower()=='hyd' else 800			# if  employee  lives  in  'Hyd'  and  800  otherwise
		self.grosspay= self.salay + da + hra + cca		# How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf=0.8*self.grosspay					# pf = 8%  of  grosspay  but  a  max  of  400
		if self.grosspay < 10000:				# tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
			tax = 0.1*self.grosspay	
		else:
 			tax=0.15 * self.grosspay			
		self.netpay = self.grosspay - pf - tax                  # How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().disp()						# How  to  print  number , name , age , gender
		print(f"{self.subject} \t salary: {self.salary} \t gross: {self.grosspay: .2f} \t net: {self.netpay:.2f} " )	# How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
		obj=teacher()							# How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
		obj =student()							# How  to  append  student  object  to  list  'a'
	elif ch == 3:
		break
	else:
		print("invalid choice")						# How  to  stop  execution

	obj.get()								# How  to  read  inputs  into  object
	obj.compute()								# How  to  store   results  in  object
	obj.append(obj)								# How  to  move  to  next  index
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
for i in a:									# How  to  print  all  teacher  objects
	if type(i) == teacher:
		i.disp()
print()
print('Students')
										# How  to  print  all  student  objects
for i in a:
	if type(i)==student:
		i.disp()
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
		self.x=int(input('enter x value : ')					# How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.x=m.x + n.x							# How  to  add  objects  m  and  n  and  store  result  in  object  self
	
	def  display(self):
			print('Sum  of  the  numbers  :  ' ,self.x) 			# How  to  print  sum  result)
class   string(datatype):
	def  get(self):
		self.x=input('enter a string: ')					# How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
		super().x = m.x + n.x							# How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' ,self.x) 		# How  to  print  the   join  result)
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
				obj= [number(), number(), number()]			# How  to  create  list  of  3  number  class  objects

			elif  ch  == 2:
				obj=[string(), string(), string()]			# How  to  create  list  of  3  string  class  objects
			else:
				print("invalid choice")					# How  to  stop  execution
			
			obj[0].get()							# How  to  read  input  into  first  object
			obj[1].get()							# How  to  read  input  into  2nd  object
			obj[2].add(obj[0],obj[1])					# How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			obj[2].display()						# How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')