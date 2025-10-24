#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		#How  to   read  number
	    self.number = eval(input('Enter number : '))
		#How  to   read  name
        self.name = input('Enter name : ')
		#How  to   read   age
        self.age = eval(input('Enter age : '))
        #How  to   read   gender
        self.gender = input('Enter gender : ')
	def   disp(self):
		#How  to  print  number , name , age , gender  in  same  line  separated  by  tab
		print(self.number, self.name, self.age, self.gender, sep='\t')
	@abstractmethod
	def   compute(self):
                pass
class  student(person):
	def  get(self):
		#How  to  read   number , name , age , gender
		super().get()
        #How  to  read  marks  of  3  subjects  into  a  list
		self.marks = []
        for i in range(3):
            mark = float(input(f'Enter marks for subject {i+1}: '))
            self.marks.append(mark)
	def  compute(self):
		#How  to  calculate  total  marks
		self.total = sum(self.marks)
        #How  to  calculate  average  marks
		self.average = self.total / len(self.marks)
	def  disp(self):
		#How  to  print  number , name , age , gender
		super().disp()
        #How  to  print  total  and  average  in  same  line separated  by  tab
		print(self.total, self.average, sep='\t')
class  teacher(person):
	def   get(self):
		#How  to  read  number , name , age  and  gender
		super().get()
        #   How  to  read   subject
        self.subject = input('Enter subject : ')
        #How  to  read   salary
        self.salary = float(input('Enter salary : '))
        #How  to  read   city
        self.city = input('Enter city : ')
	def   compute(self):
		#da = 50%  of  salary
		da = 0.5 * self.salary
        #hra = 20%  of  salary
		hra = 0.2 * self.salary
        #cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
		if self.city.lower() == 'hyd':
            cca = 1000
        else:
            cca = 800   
        #How  to  calculate  grosspay  i.e. salary + da + hra + cca
		self.grosspay = self.salary + da + hra + cca
        #pf = 8%  of  grosspay  but  a  max  of  400
		pf = 0.08 * self.grosspay
        if pf > 400:
            pf = 400
        #tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		if self.grosspay < 10000:
            tax = 0.1 * self.grosspay
        else:
            tax = 0.15 * self.grosspay  
		#How  to  calculate  netpay  i.e. grosspay - pf - tax
		self.netpay = self.grosspay - pf - tax
	def   disp(self):
		#How  to  print  number , name , age , gender
		super().disp()
        #How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
		print(self.subject, self.salary, self.grosspay, self.netpay, sep='\t')
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
			#How  to  append  teacher  object  to  list  'a'
        t = teacher()   
	elif  ch == 2:
			#How  to  append  student  object  to  list  'a'
        s = student()
	else:
		#How  to  stop  execution
		break
	    #How  to  read  inputs  into  object
        obj.get()
        #How  to  compute  values  in  object
	    #How  to  store   results  in  object
        obj.compute()
        a.append(obj)
	    #How  to  move  to  next  index
#end of loop
print('Students')
	menu()
	ch = eval(input('Enter choice : '))
#end of loop
print('Teachers')
#How  to  print  all  teacher  objects
for obj in a:
    if isinstance(obj, teacher):
        obj.disp()
print()
print('Students')
#How  to  print  all  student  objects
for obj in a:
    if isinstance(obj, student):
        obj.disp()
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
			#How  to  read  number  into  variable  'x' of  object  self
            self.x = eval(input('Enter number : '))
	def  add(self , m , n):
			#How  to  add  objects  m  and  n  and  store  result  in  object  self
            self.sum = m.x + n.x
	def  display(self):
			#print('Sum  of  the  numbers  :  ' , How  to  print  sum  result)
            print('Sum of the numbers : ', self.sum)
class   string(datatype):
	def  get(self):
			#How  to  read  string  into  variable  'x' of  object  self    
            self.x = input('Enter string : ')
	def  add(self , m , n):
			#How  to  join  objects  m  and  n  and  store  result  in  object  self
            self.join = m.x + n.x
	def  display(self):
			#print('Join  of  the  two  strings :  ' , How  to  print  the   join  result)
            print('Join of the two strings : ', self.join)
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
				    #How  to  create  list  of  3  number  class  objects
                    m = number()
                    n = number()
                    r = number()
			elif  ch  == 2:
					#How  to  create  list  of  3  string  class  objects
                    m = string()
                    n = string()
                    r = string()
			else:
				#How  to  stop  execution   
                break
                #How  to  read  input  into  first  object
                m.get()
                #How  to  read  input  into  2nd  object
                n.get()
                #How  to  add  (or)  join  the  two  objects
                r.add(m , n)
                #How  to  print  3rd  object
                r.display()
	# end of  while  loop
	print('Good  Bye')
