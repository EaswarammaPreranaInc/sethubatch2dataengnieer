'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from chandana_19_sep_23_class_and_objects import triangle
b=triangle() # How  to  create  triangle  object
triangle.get(b)# How  to  call  get()  method  in  another  way
triangle.test(b) #How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(b)) #How  to  call  area()  method  in  another  way
print('Perimeter: ',  triangle.peri(b))#How  to  call  peri()  method  in  another  way


#  Find  outputs 
class   c1:
	def  m1(self):
		x = 10
		self . x = 20 # assigns 20 to instance variable a.x
		print(x) # prints local variable 'x'
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		#print(x) # local variable 'x' is not defined and therenis no global 'x'
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
#print(self . x)  # error : self is not a global variable. it exists inside method
#print(x) # error: 'x' is local variable of m1 method

'''
o/p:
10
20
27
33
'''



'''  
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input('Enter X : '))
		self.y=int(input('Enter y : '))
		self.z=int(input('Enter z : ')) # read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z # add  objects  m  and  n  and  store  results  in  object  self		 
	def  disp(self):
		print(f'x= {self.x}, y= {self.y}, z={self.z}') #  print  object  self
# End  of  the  class
a=Test()
b=Test()
c=Test() # create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #  read  inputs  into  object  'a'
print('Second  Object')
b.get() # read  inputs  into  object  'b'
c.add(a,b) # add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() # print  object  'c'
'''
o/p:
First  Object
Enter X : 10
Enter y : 20
Enter z : 30
Second  Object
Enter X : 40
Enter y : 50
Enter z : 60
Addition  results
x= 50, y= 70, z=90
'''


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # prints type and address of class date



#  Find  outputs 
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # type and address of c1
print(b) # type and address of c2
print(c) # type and address of c3
print(d) # type and address of c4
print(b . _str_()) # returns int 35
print(c . _str_()) # prints Hyd and returns None
print(d . _str_(50)) # returns int 50
'''
o/p:
35
Hyd
None
50
'''


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.roll_num=int(input('Enter roll number : ')) #read  roll  number  into  object  self
		self.name=input('Enter student name :') # read  student  name  into  object  self
		self.gender=input('Enter gender:') # read  gender  into  object  self
		self.m1=float(input('Enter marks of 1st subject: '))
		self.m2=float(input('Enter marks of 2nd subject: '))
		self.m3=float(input('Enter marks of 3rd subject: '))
		# How  to  read  marks  of  3  subjects
	def   compute(self):
		self.total=self.m1+self.m2+self.m3 # calculate  total  marks
		self.average=self.total/3 # calculate  average  marks
		if  self.m1<40 or self.m2<40 or self.m3<40 : # At  least  one  subject  is  below  40:
				self.grade='fail' #   initilaize  grade  to  'Fail'
		elif  self.average>=70: # average  is  above  >= 70%:
				self.grade='Distinction' #   initilaize  grade  to  'Distinction'
		elif  self.average>=60: # average  is  above  >= 60%:
				self.grade='First Class' #  initilaize  grade  to  'First  class'
		elif  self.average>=50: #  average  is  above  >= 50%:
				self.grade='Second class' #  initilaize  grade  to  'Second  class'
		else:
				self.grade='third class' #  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' , self.roll_num)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' ,self.total)
		print('Average  :  ' ,self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		        return f"Roll: {self.roll_num}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.average}, Grade: {self.grade}"
                #All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
a=Student() # create  Student  class  object
a.get() # read  inputs  into  object
a.compute() # How  to  store  results  in  object
a.disp() # How  to  print  object  with  disp()  method
print(a) # How  to  print  object  with  _str_()  method



'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  ---> 2 / 3 + 5 / 9 = (18 + 15) / 27 = 33 / 27 = 11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 = 1 / 9
    What  is  the  product  ?  ---> 	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  ---> 	2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  ---> 	2 / 3 * 0 / 9 = 	0 / 27  =  	0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  ---> 	2 / 3 /  0 / 9 = 2 / 3 * 9 / 0 = 	18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		self.num=int(input('Enter numerator: ')) # How  to  read  numerator  into  object  self
		self.den=int(input('Enter denominator: '))#How  to  read  denominator  into  object  self
		self.test() # How  to  call  test()  method
	def  test(self):
		while self.den==0:
			print('denominator cannot be zero')
			self.den=int(input('re enter denominator')) # Ask  user  to  reenter  denom  when  denom  is  zero
	def __str__(self):
		return  f'{self.num}/{self.den}' # values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def add(self,a,b):
		self.num=a.num*b.den+b.num*a.den
		self.den=a.den*b.den # How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def sub(self,a,b):
		self.num=a.num*b.den-b.num*a.den
		self.den=a.den*b.den # How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() #How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self.num=a.num*b.num
		self.den=a.den*b.den # How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.simplify() # How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def div(self , a , b):
		if b.num==0:
			self.num=None
			self.den=None
		else:
			self.num=a.num*b.den
			self.den=a.den*b.num #How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
			self.simplify() # How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			if self.num==0:
				self.den=self.den#How  to  find  gcd  of  numerator  and   denominator
			else:
				g=math.gcd(self.num,self.den)
				self.num//=g
				self.den//=g# How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat() #How  to  create  6  objects  a , b , c , d , e , f
a.get() # How  to  read  rational  number  into  object  'a'
b.get() # How to  read  rational  number  into  object  'b'
c.add(a,b) # How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d.sub(a,b) # How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e.mul(a,b) # How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f.div(a,b) # How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print('sum: ',c) # How  to  print  object   'c'
print('diff: ',d) # How  to  print  object   'd'
print('product: ',e) # How  to  print  object   'e'
if  f.num is not  None:
	print('division= ',f) # How  to  print  object  'f
else:
	print('Division  is  not  permitted')
	
'''
o/p:
Enter numerator: 2
Enter denominator: 3
Enter numerator: 5
Enter denominator: 9
sum:  11/9
diff:  1/9
product:  10/27
division=  6/5
'''