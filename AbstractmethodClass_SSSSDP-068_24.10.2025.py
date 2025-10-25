#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
    def   get(self):
        self.a=int(input("Enter Number : "))  #  How  to   read  number
        self.name=input("Enter name : ")  #  How  to   read  name
        self.age=int(input("Enter age : "))  #  How  to   read   age
        self.g=input("Enter Gender(Male/Female) : ")  #  How  to   read   gender
    def   disp(self):
        # Note: Added end='\t' to keep printing on the same line
        print(self.a, self.name, self.age, self.g, sep='\t', end='\t')   # How  to  print  number , name , age , gender  in  same  line  separated  by  tab
    @abstractmethod
    def   compute(self):
          pass
class  student(person):
    def  get(self):
        super().get()  #  How  to  read   number , name , age , gender
        self.s1=int(input("Enter maths marks : "))
        self.s2=int(input("Enter Physics marks : ")) 
        self.s3=int(input("Enter Computers marks : ")) #  How  to  read  marks  of  3  subjects
    def  compute(self):
        self.total=self.s1+self.s2+self.s3  #  How  to  calculate  total  marks
        self.avg=self.total/3  #  How  to  calculate  average  marks
    def  disp(self):
        super().disp()  #  How  to  print  number , name , age , gender
        print(self.total, self.avg, sep='\t')  # How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
    def   get(self):
        super().get()  #  How  to  read  number , name , age  and  gender
        self.sub=input("Enter subject : ")  #  How  to  read   subject
        self.sal=float(input("Enter salary : "))  #  How  to  read   salary
        self.city=input("Enter city : ")  #  How  to  read   city
    def   compute(self):
        self.da=self.sal/2  #  da = 50%  of  salary
        self.hra=self.sal/5  #  hra = 20%  of  salary
        # Make the city check case-insensitive
        self.cca=1000 if self.city.lower() == 'hyd' else 800  #  cca = 1000  if  employee  lives  in  'Hyd'  and  800  otherwise
        self.grosspay=self.sal+self.da+self.hra+self.cca  #  How  to  calculate  grosspay  i.e. salary + da + hra + cca
        self.pf = min(self.grosspay * 0.08, 400)  #  pf = 8%  of  grosspay  but  a  max  of  400
        self.tax=self.grosspay*0.1 if self.grosspay<10000 else self.grosspay*0.15   #tax = 10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
        self.netpay=self.grosspay-self.pf-self.tax  #  How  to  calculate  netpay  i.e. grosspay - pf - tax
    def   disp(self):
        super().disp()  #  How  to  print  number , name , age , gender
        print(self.sub, self.sal, self.grosspay, self.netpay, sep='\t')  #  How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
def  menu():
    print('\n1. Teacher')
    print('2. Student')
    print('3. Exit')
# End  of  the  function
a = []
while  True:
    menu()
    
    # Use int() instead of eval() for safety
    try:
        ch = int(input('Enter choice : '))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        continue

    if   ch == 1:
        print("\n--- Enter Teacher Details ---")
        # How  to  read  inputs  into  object and store results
        obj = teacher()
        obj.get()
        obj.compute()
        a.append(obj)  #  How  to  append  teacher  object  to  list  'a'
        print("Teacher added.")
        
    elif  ch == 2:
        print("\n--- Enter Student Details ---")
        # How  to  read  inputs  into  object and store results
        obj = student()
        obj.get()
        obj.compute()
        a.append(obj)  #  How  to  append  student  object  to  list  'a'
        print("Student added.")
    elif ch == 3:
        break  #  How  to  stop  execution
    else:
        print("Invalid choice, please enter 1, 2, or 3.")
    # The redundant code that was here is removed.
    # The loop repeats, which is "How  to  move  to  next  index"
#end of loop
print('\n--- All Teacher Records ---')
print("Num\tName\tAge\tGender\tSubject\tSalary\tGrossPay\tNetPay")
print("-" * 70)
# How  to  print  all  teacher  objects
for obj in a:
    if isinstance(obj, teacher): # Check if the object is a teacher
        obj.disp() # Call its display method
print() 
print('\n--- All Student Records ---')
print("Num\tName\tAge\tGender\tTotal\tAverage")
print("-" * 60)
# How  to  print  all  student  objects
for obj in a:
    if isinstance(obj, student): # Check if the object is a student
        obj.disp() # Call its display method
print('\nGood  Bye')



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
        self.x=int(input("Enter x value : "))  #  How  to  read  number  into  variable  'x' of  object  self
    def  add(self , m , n):
        self.s=m.x+n.x  #  How  to  add  objects  m  and  n  and  store  result  in  object  self
    def  display(self):
        print('Sum  of  the  numbers  :  ' , self.s)  #    How  to  print  sum  result)
class   string(datatype):
    def  get(self):
        self.x=input("Enter string : ")  #  How  to  read  string  into  variable  'x' of  object  self
    def  add(self , m , n):
        self.x=m.x+n.x  #  How  to  join  objects  m  and  n  and  store  result  in  object  self
    def  display(self):
        print('Join  of  the  two  strings :  ' ,self.x)  #   How  to  print  the   join  result)
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
            list=[number(),number(),number()]   #  How  to  create  list  of  3  number  class  objects
        elif  ch  == 2:
            list=[string(),string(),string()]  #  How  to  create  list  of  3  string  class  objects
        else:
            exit() #  How  to  stop  execution
        list[0].get()  
        list[1].get()  
        list[2].add(list[0] , list[1])
        list[2].display()
        #  How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
        # How  to  read  input  into  first  object
        # How  to  read  input  into  2nd  object
        # How  to  add  (or)  join  the  two  objects  and  store  the  result  in  3rd  object
        #   How  to  print  3rd  object
    # end of  while  loop
    print('Good  Bye')
