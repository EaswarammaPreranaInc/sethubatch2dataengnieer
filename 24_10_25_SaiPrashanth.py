#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def  get(self):
		self.no=int(input('enter no'))#How  to   read  number
		self.name=input("enter name")#How  to   read  name
		self.age=int(input("enter age"))#How  to   read   age
		self.gender = input("enter gender m/f: ")#How  to   read   gender
	def   disp(self):
		print(f'{self.no}\t{self.name}\t {self.age}\t{self.gender}', end='\t' )#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
		pass
class  student(person):
	def  get(self):
		super().get()#How  to  read   number , name , age , gender
		self.list=[]#How  to  read  marks  of  3  subjects  into  a  list
		for i in range(3):
			marks = int(input(f'Enter marks for subject {i+1}: '))
			self.list.append(marks)
	def  compute(self):
		self.total=sum(self.list)#How  to  calculate  total  marks
		self.avg=self.total/3 #How  to  calculate  average  marks
	def  disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(f'{self.total}\t{self.avg}',end="")#How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get() ##How  to  read  number , name , age  and  gender
		self.sub=input("enter subject name")#How  to  read   subject
		self.sal=float(input("enter salary"))#How  to  read   salary
		self.city=input("enter city")#How  to  read   city
	def   compute(self):
		da = self.sal*0.5#50%  of  salary
		hra = self.sal*0.2#20%  of  salary
		cca = 1000 if (self.city=='Hyd' or self.city=='hyd') else 800 #1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		self.grosspay=self.sal+da+hra+cca #How  to  calculate  grosspay  i.e. salary + da + hra + cca
		pf = min(self.grosspay*0.08,400) #8%  of  grosspay  but  a  max  of  400
		tax = self.grosspay*0.1 if self.grosspay < 10000 else self.grosspay*0.15 #10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.netpay=self.grosspay-pf-tax #How  to  calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().disp()#How  to  print  number , name , age , gender
		print(f'{self.sub}\t{self.sal}\t {self.grosspay}\t {self.netpay}')#How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
		t=[teacher()]
			#How  to  append  teacher  object  to  list  'a'
	elif  ch == 2:
		t=[student()]
	else:
		break #How  to  stop  execution
	t[0].get()
	t[0].compute()
	a.append(t[0])
	'''How  to  read  inputs  into  object
	How  to  store   results  in  object
	How  to  move  to  next  index'''

#end of loop
print('Teachers')
for i in a:
	if isinstance(i,teacher):
		i.disp()
	 #How  to  print  all  teacher  objects
print()
print('Students')
for i in a:
    if isinstance(i,student):
        i.disp()
#How  to  print  all  student  objects
print('Good  Bye')
"""
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
		self.x=int(input("enter no")) #How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.obj=m.x+n.x #How  to  add  objects  m  and  n  and  store  result  in  object  self
	def display(self):
		print('Sum  of  the  numbers  :  ' ,self.obj) #How  to  print  the   sum  result
class   string(datatype):
	def  get(self):
		self.x=input("enter string")#How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
		self.obj=m.x+n.x 
		#How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.obj)#How  to  print  the   join  result)
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
				a=[number(),number(),number()]#How  to  create  list  of  3  number  class  objects
			elif  ch  == 2:
				a=[string(),string(),string()]
            #How  to  create  list  of  3  string  class  objects
			else:
				break #How  to  stop  execution
			a[0].get()
			a[1].get()
			a[2].add(a[0],a[1])
			a[2].display()
			
			'''How  to  read  input  into  first  object
			How  to  r ead  input  into  2nd  object
			How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			How  to  print  3rd  object'''
	# end of  while  loop
	print('Good  Bye')"""