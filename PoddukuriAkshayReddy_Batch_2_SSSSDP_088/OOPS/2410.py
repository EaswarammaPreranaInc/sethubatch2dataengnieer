#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self.number = int(input("Enter number :"))  # How  to   read  number
		self.name = input("Enter name: ") # How  to   read  name
		self.age = int(input("Enter the age: ")) # How  to   read   age
		self.gender = input("Enyter the gender: ")  # How  to   read   gender
	def   disp(self):
		print(self.number,self.name,self.age,self.gender,sep='\t') # How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def compute(self):
            pass
class  student(person):
	def  get(self):
		super().get() # How  to  read   number , name , age , gender
		self.m = [] # How  to  read  marks  of  3  subjects  into  a  list
        for i in range(3):
            mark = float(input(f'Enter marks for subject {i+1}: '))
            self.m.append(mark)
            
            
	def  compute(self):
		self.total = sum(self.m) # How  to  calculate  total  marks
		self.avg = self.total/3 #How  to  calculate  average  marks
  
  
	def  disp(self):
		super().get() # How  to  print  number , name , age , gender
		print(self.total,self.avg,sep='\t') # How  to  print  total  and  average  in  same  line separated  by  tab
  
  
class  teacher(person):
	def   get(self):
		super().get() # How  to  read  number , name , age  and  gender
		self.sub = input('Enter the subject : ') # How  to  read   subject
		self.sal = float(input("Enter the salary : ")) # How  to  read   salary
		self.city = input("Enter the city : ") # How  to  read   city
  
  
	def compute(self):
        if self.city == 'hyd':
            cca = 1000 
        else:
            cca = 800
        # cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
        
        da = self.sal * 0.5 # 50%  of  salary
		hra = self.sal * 0.2 # 20%  of  salary

        self.gp = self.sal + da + hra + cca  # How  to  calculate  grosspay  i.e. salary + da + hra + cca
	
		# How  to  calculate  grosspay  i.e. salary + da + hra + cca
        pf = self.gp * 0.08
        
        if pf > 400:
            pf = 400
        
		# pf = 8%  of  grosspay  but  a  max  of  400
        if self.gp < 10000:
            tax =  self.gp * 0.1
        else:
            tax = self.gp * 0.1 + (self.gp-10000)* 0.15
                        
		# tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		# How  to  calculate  netpay  i.e. grosspay - pf - tax
  
        np = self.gp - pf - tax  # How  to  calculate  netpay  i.e. grosspay - pf - tax
        
	def disp(self):
		super().disp() # How  to  print  number , name , age , gender
		print(self.sub, self.sal, gp, np, sep='\t') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
  
  
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
 

# End  of  the  function
a = []
while  True:
	menu()
	ch = eval(input('Enter choice : '))
	if ch == 1:
		a.append(teacher) # How  to  append  teacher  object  to  list  'a'
	elif ch == 2:
		a.append(student) # How  to  append  student  object  to  list  'a'
	else:
		break # 	How  to  stop  execution
    a[-1].get() # How  to  read  inputs  into  object
	a[-1].compute() # How  to  store   results  in  object
	# How  to  move  to  next  index
	# menu()
	# ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
for x in a:
    if isinstance(x, teacher):
        x.disp()  #
# How  to  print  all  teacher  objects
print()
print('Students')
for x in a:
    if isinstance(x, student):
        x.disp()  #
# How  to  print  all  student  objects
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
			self.x = input("Enter the number: ") # How  to  read  number  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = m.x + m.n  # How  to  add  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Sum  of  the  numbers  :  ' , self.x )  # How  to  print  sum  result)
   
class   string(datatype):
	def  get(self):
			self.x = input("Enter the number: ") # How  to  read  string  into  variable  'x' of  object  self
	def  add(self , m , n):
			self.x = (m.x +n.x ) # How  to  join  objects  m  and  n  and  store  result  in  object  self
	def  display(self):
			print('Join  of  the  two  strings :  ' , self.x) #  How  to  print  the   join  result)
   
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function

if  __name__ == '__main__':
	while  True:
			menu()
			ch =  eval(input('Enter choice : '))
			if ch == 1:
				a = [number(), number(), number()] # How  to  create  list  of  3  number  class  objects
			elif ch == 2:
				a = [string(), string(), string()] # How  to  create  list  of  3  string  class  objects
			else:
				break     # How  to  stop  execution
			a[0].get() # How  to  read  input  into  first  object
			a[1].get() # How  to  read  input  into  2nd  object
			a[2].add(a[0]+a[1]) # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
			a[2].display() # How  to  print  3rd  object
	# end of  while  loop
	print('Good  Bye')
 
 