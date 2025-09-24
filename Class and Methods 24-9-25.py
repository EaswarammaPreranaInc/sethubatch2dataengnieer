'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from hw9 import *
tri = triangle() # How  to  create  triangle  object
triangle . get(tri) # How  to  call  get()  method  in  another  way
triangle . test(tri) # How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(tri)) # How  to  call  area()  method  in  another  way)
print('Perimeter: ',  triangle.peri(tri))  # How  to  call  peri()  method  in  another  way)

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		print(x) # Error as there is no local variable x
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) 
print(self . x) # Error as there is no object self
print(x) # error as there no global variable x

'''
10
20
27
33
'''


'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self . x = float(input('Enter 1st number : ')) # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		self . y = float(input('Enter 2nd number : '))
		self . z = float(input('Enter 3rd number : '))
	def   add(self , m , n):
		self . x = m . x + n . x # How  to  add  objects  m  and  n  and  store  results  in  object  self
		self . y = m . y + n . y
		self . z = m . z + n . z
	def  disp(self):
		 # How  to  print  object  self
		print(f'New value of x : {self . x}')
		print(f'New value of y : {self . y}')
		print(f'New value of z : {self . z}')
# End  of  the  class
# How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()
c = Test()
print('First  Object')
a . get() # How  to  read  inputs  into  object  'a'
print('Second  Object')
b . get() # How  to  read  inputs  into  object  'b'
c . add(a , b) # How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
# How  to  print  object  'c'
c . disp()




#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # type and address of the object




#  Find  outputs (Home  work)
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
print(a) # string 25
print(b) # error as return type must be string
print(c) # error as return type is none
print(d) # error as there should be no argument for automatic execution
print(b . __str__()) # 35
print(c . __str__()) # Hyd <none> None
print(d . __str__(50)) # string 50




'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self . rollno = int(input('Enter a Roll number of the student : ')) # How  to  read  roll  number  into  object  self
		self . sname = input('Enter Student Name : ') # How  to  read  student  name  into  object  self
		self . g = input('Enter gender M or F : ') # How  to  read  gender  into  object  self
		self . sub = eval(input('Enter a Marks of Students in a List : ')) # How  to  read  marks  of  3  subjects
	def   compute(self):
		self . marks = sum(self . sub) # How  to  calculate  total  marks
		self . avg = self . marks / len(self . sub) # How  to  calculate  average  marks
		if  min(self.sub) < 40 : # At  least  one  subject  is  below  40:
				self . grade = 'Fail' # How  to  initilaize  grade  to  'Fail'
		elif  self . avg >= 70 : # average  is  above  >= 70%:
				self . grade = 'Distinction' # How  to  initilaize  grade  to  'Distinction'
		elif self . avg >= 60: # average  is  above  >= 60%:
				self . grade = 'First class' # How  to  initilaize  grade  to  'First  class'
		elif self . avg >= 50:  # average  is  above  >= 50%:
				self . grade = 'Second class' # How  to  initilaize  grade  to  'Second  class'
		else:
				self . grade = 'Third class' # How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' , self . rollno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' , self . g)
		print('Total  Marks  :  ' , self . marks)
		print('Average  :  ' , self . avg)
		print('Grade  :  ' , self . grade)
	def   __str__(self):
		return f'{self . rollno}\t{self . sname}\t {self . g}\t {self . marks}\t {self.avg} \t {self.grade}' # All  the   values  of  object  self  in  the  form  of  string
#End  of  the  class
s = Student() # How  to  create  Student  class  object
# How  to  read  inputs  into  object
s . get()
s . compute() # How  to  store  results  in  object
s . disp() # How  to  print  object  with  disp()  method
print(s) # How  to  print  object  with  _str_()  method





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
		self . n = int(input('Enter a Numerator Value : ')) # How  to  read  numerator  into  object  self
		self . d = int(input('Enter a Denominator value : ')) # How  to  read  denominator  into  object  self
		self . test() # How  to  call  test()  method
	def  test(self):
		if self . d == 0 : 
			self . d = int(input('Re-Enter a Denominator Value(must not be a Zero) : ')) # Ask  user  to  reenter  denom  when  denom  is  zero
	def    __str__(self):
			 return  f'{self . n} / {self . d}' # values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'
	def   add(self , a , b):
		self . n = a . n * b . d + b . n * a . d # How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self . d = a . d * b . d
		self . simplify() # How  to  simplify  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self . n = a . n * b . d - b . n * a . d
		self . d = a . d * b . d # How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self . simplify() # How  to  simplify  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self . n = a . n * b . n # How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.  d = a . n * b . d
		self . simplify() # How  to  simplify  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		if b.n == 0:
            		print("Division is not permitted (Denominator Rational is 0)")
            		self . n, self . d = 0, 0 # How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		else:
            		self . n = a . n * b . d
            		self . d = a . d * b . n
		self . simplify() # How  to  simplify  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			# How  to  find  gcd  of  numerator  and   denominator
			if self.n != 0: 
					g = math.gcd(self.n, self.d)
					self.n //= g
					self.d //= g # How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
# How  to  create  6  objects  a , b , c , d , e , f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
a . get() # How  to  read  rational  number  into  object  'a'
b . get() # How to  read  rational  number  into  object  'b'
c . add(a , b) # How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
d . sub(a , b) # How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
e . mul(a , b) # How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
f . div(a , b) # How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
print(f'Addition : {c}') # How  to  print  object   'c'
print(f'Substraction : {d}') # How  to  print  object   'd'
print(f'Multiplication : {e}') # How  to  print  object   'e'
if f . d != 0:
	print(f'Division : {f}') # How  to  print  object  'f
else:
	print('Division is not permitted')
