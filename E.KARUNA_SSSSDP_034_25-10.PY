# program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number=int(input('enter number :')) # read  number
		self.name=input('enter name :') #  read  name
		self.age=int(input('enter age :')) #   read   age
		self.gender=input('enter gender :') #  read   gender
	def   disp(self):
		print(f'number : {self.number} ,name: {self.name} ,age: {self.age} , gender: {self.gender}') #   print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		super().get() #   read   number , name , age , gender
		self.marks=[]
		for i in range(1,4):
			b=int(input(f'enter {i} subject marks :'))
			self.marks.append(b) #   read  marks  of  3  subjects  into  a  list
	def  compute(self):
		self.total=sum(self.marks) #   calculate  total  marks
		self.avg=self.total/3 #   calculate  average  marks
	def  disp(self):
		super().disp() #   print  number , name , age , gender
		print(f'total marks :{self.total}, average :{self.avg}') #   print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super().get() #   read  number , name , age  and  gender
		self.subject=input('enter subject :') #   read   subject
		self.salary=float(input('enter salary :')) #   read   salary
		self.city=input('enter city :') #   read   city
	def   compute(self):
		da = 0.5*self.salary # 50%  of  salary
		hra = 0.2*self.salary # 20%  of  salary
		cca = 1000 if self.city.lower()=='hyd' else 800 # 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		self.grosspay=self.salary+da+hra+cca #   calculate  grosspay  i.e. salary + da + hra + cca
		pf = 0.08*self.grosspay
		if pf>400:
			pf=400 # 8%  of  grosspay  but  a  max  of  400
		tax = 0.1 * self.grosspay if self.grosspay < 10000 else 0.15 * self.grosspay # 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		self.netpay=self.grosspay-pf-tax #   calculate  netpay  i.e. grosspay - pf - tax
	def   disp(self):
		super().disp() #   print  number , name , age , gender
		print(f'subject :{self.subject}, salary :{self.salary}, grosspay :{self.grosspay}, netpay :{self.netpay}') #   print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
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
			x=teacher() #   append  teacher  object  to  list  'a'
	elif  ch == 2:
			x=student() #   append  student  object  to  list  'a'
	else:
			break #   stop  execution
	x.get() #   read  inputs  into  object
	x.compute() #   store   results  in  object
	a.append(x) #   move  to  next  index
	
#end of loop
print('Teachers')
for i in a:
	if isinstance(i,teacher):
		i.disp()  #   print  all  teacher  objects
print()
print('Students')
for i in a:
	if isinstance(i,student):
		i.disp() #   print  all  student  objects
print('Good  Bye')



# program to  add  num  class  objects  and  join  str  class  objects
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
			self.x=int(input('enter x :')) #  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x #   add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' ,self.x) #    print  sum  result
class   string(datatype):
	def  get(self):
			self.x=input('enter a string :') #   read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x=m.x+n.x #   join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' ,self.x) #   print  the   join  result
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
				a=[number(),number(),number()] #   create  list  of  3  number  class  objects
			elif  ch  == 2:
				a=[string(),string(),string()] #   create  list  of  3  string  class  objects
			else:
				break #   stop  execution
			a[0].get() #   read  input  into  first  object
			a[1].get() #   read  input  into  2nd  object
			a[2].add(a[0],a[1]) #   add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			a[2].display() #   print  3rd  object
	# end of  while  loop
	print('Good  Bye')
	





    
from KARUNA import number,string

while True:
    x=input('Enter number/ string /exit :').lower()
    if x =='number':
        a = [number(), number(), number()]  
    elif x=='string':
        a = [string(), string(), string()] 
    elif x=='exit':
        print('Good Bye')
        break
    a[0].get()
    a[1].get()
    a[2].add(a[0],a[1])
    a[2].display()