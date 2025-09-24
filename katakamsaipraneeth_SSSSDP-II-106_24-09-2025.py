'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
a = triangle() # How  to  create  triangle  object
triangle.get(a) # How  to  call  get()  method  in  another  way
triangle.test(a) # How  to  call  test()  method  in  another  way
print('Area : ', triangle.area(a)) #  How  to  call  area()  method  in  another  way
print('Perimeter: ', triangle.peri(a)) # How  to  call  peri()  method  in  another  way



#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10 # Lv
		self . x = 20 # int obj
		print(x) # 10
		print(self . x) # 20
		x += 5 # 15
		self . x += 7 # 27
	def   m2(self):
		print(x) # error
		print(self . x) # 27
		self . x += 6 # 33
# End  of  the  class
a = c1() # c1 object
a . m1() # 10  20
a . m2() # 27
print(a . x) # 33
print(self . x) # error
print(x) # error



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x = int(input("x:")) 
		self.y = int(input("Y:"))
		self.z = int(input("Z:")) # How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def   add(self , m , n):
		self.x = m.x + n.x
		self.y = m.y + n.y
		self.z = m.z + n.z
		# How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print('X:', self.x)
		print('Y:', self.y)
		print('Z:', self.z)   # How  to  print  object  self
# End  of  the  class
# How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()
c = Test()
print('First  Object')
a.get() # How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() # How  to  read  inputs  into  object  'b'
c.add(a, b) # How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() # How  to  print  object  'c'


#  Find  outputs (Home  work)
class  Date: # empty class
	pass
# End of the class
a =  Date() # date obj
a . dd = 15 # add dd to obj
a . mm = 8 # add mm to obj
a . yy = 1947 # add yy to obj
print(a) # type and address



#  Find  outputs (Home  work)
class   c1:
	def  _str_(self): # dunder str fun
			return  '25' # string
class   c2:
	def  _str_(self):
			return   35 # int
class   c3:
	def  _str_(self):
			print('Hyd') # None
class   c4:
	def  _str_(self , x):
			return   F'{x}' # int
#end of the class
a = c1() # c1 object
b = c2() # c2 object
c = c3() # c3 object
d = c4() # c4 object
print(a) # 25
print(b) # error
print(c) # None
print(d) # error
print(b . _str_()) # 35
print(c . _str_()) # Hyd  None
print(d . _str_(50)) # 50



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		# How  to  read  roll  number  into  object  self
		self.roll = int(input("Enter Roll Number: "))
		# How  to  read  student  name  into  object  self
		self.name = input("Enter Student Name: ")
		# How  to  read  gender  into  object  self
		self.gender = input("Enter Gender: ")
		# How  to  read  marks  of  3  subjects
		self.marks = []
		for i in range(3):
			mark = float(input(f"Enter Marks for Subject {i+1}: "))
			self.marks.append(mark)
	def   compute(self):
		# How  to  calculate  total  marks
		self.total = sum(self.marks)
		# How  to  calculate  average  marks
		self.average = self.total / 3
		if  self.marks[0] < 40 or self.marks[1] < 40 or self.marks[2] < 40: # At  least one subject is below 40
				# How  to  initilaize  grade  to  'Fail'
				self.grade = 'Fail'
		elif  self.average >= 70:
				# How  to  initilaize  grade  to  'Distinction'
				self.grade = 'Distinction'
		elif  self.average >= 60:
				# How  to  initilaize  grade  to  'First  class'
				self.grade = 'First  class'
		elif  self.average >= 50:
				# How  to  initilaize  grade  to  'Second  class'
				self.grade = 'Second  class'
		else:
				# How  to  initilaize  grade  to  'Third  class'
				self.grade = 'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.roll)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f"Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, Total Marks: {self.total}, Average: {self.average}, Grade: {self.grade}"
#End  of  the  class
# How  to  create  Student  class  object
student = Student()
# How  to  read  inputs  into  object
student.get()
# How  to  store  results  in  object
student.compute()
# How  to  print  object  with  disp()  method
student.disp()
# How  to  print  object  with  __str__()  method
print(student)
print(student.__str__())



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
		#How  to  read  numerator  into  object  self
		self.num = int(input("Enter Numerator: "))
		#How  to  read  denominator  into  object  self
		self.den = int(input("Enter Denominator: "))
		#How  to  call  test()  method
		self.test()
	def  test(self):
		while self.den == 0: # Ask  user  to  reenter  denom  when  denom  is  zero
			print('Denominator  can  not  be  zero')
			self.den = int(input("Enter Denominator: "))
	def __str__(self):
		return f"{self.num} / {self.den}" # values  of  object  in  the  form  of  rational  number  such   as  '2 / 3'

	def add(self , a , b):
		#How  to  add  objects  'a'  and  'b' and  store  results  in  object  self
		self.num = a.num * b.den + b.num * a.den
		self.den = a.den * b.den
		#How  to  simplify  object  self
		self.simplify()
		
	def   sub(self , a , b):
		#How  to  subtract  objects  'a'  and  'b' and  store  results  in  object  self
		self.num = a.num * b.den - b.num * a.den # How  to  simplify  object  self
		self.den = a.den * b.den
		self.simplify()
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		#How  to  multiply  objects  'a'  and  'b' and  store  results  in  object  self
		self.num = a.num * b.num
		self.den = a.den * b.den
		#How  to  simplify  object  self
		self.simplify()
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		#How  to  divide  objects  'a'  and  'b' and  store  results  in  object  self
		self.num = a.num * b.den
		self.den = a.den * b.num
		#How  to  simplify  object  self
		self.simplify()
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
			#How  to  find  gcd  of  numerator  and   denominator
			gcd = math.gcd(self.num, self.den)
			#How  to  simplify  rational  number  in  object  self  i.e.  12 / 15  should  be  simplified  to  4 / 5
			self.num //= gcd
			self.den //= gcd
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
#How  to  create  6  objects  a , b , c , d , e , f
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()
#How  to  read  rational  number  into  object  'a'
a.get()
#How to  read  rational  number  into  object  'b'
b.get()
#How  to  add  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'c'
c.add(a, b)
#How  to  subtract  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'd'
d.sub(a, b)
#How  to multiply  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'e'
e.mul(a, b)
#How  to  divide  rational  numbers  in  objects  a  and  b  and  store  results  in  object  'f'
f.div(a, b)
#How  to  print  object   'c'
print(c)
#How  to  print  object   'd'
print(d)
#How  to  print  object   'e'
print(e)
if f.den != 0:
	print(f)
	#How  to  print  object  'f'
else:
	print('Division  is  not  permitted')