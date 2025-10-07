#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5#15
		self . x += 7#27
	def   m2(self):
		#print(x)#Error
		print(self . x)#27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)#33
print(self . x)#Error
print(x)#Error

#Repeat  prog5a  such  that  methods  are  called  in  another  way

#1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

from Triangle import triangle
# create triangle object
t = triangle()

# call get() method in another way
triangle.get(t)

# call test() method in another way
triangle.test(t)

# call area() method in another way
print('Area : ', triangle.area(t))

# call peri() method in another way
print('Perimeter : ', triangle.peri(t))

class Test:
    def get(self):
        # read inputs into variables x, y, z of object self
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # add objects m and n, store results in object self
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # print object self
        print("x =", self.x, ", y =", self.y, ", z =", self.z)


# --- Main Program ---
# create three Test class objects
a = Test()
b = Test()
c = Test()

print("First Object")
# read inputs into object 'a'
a.get()

print("Second Object")
# read inputs into object 'b'
b.get()

# add objects a and b and store results in object 'c'
c.add(a, b)

print("Addition results")
# print object 'c'
c.disp()
#output:
First Object
Enter x: 4
Enter y: 5
Enter z: 6
Second Object
Enter x: 3
Enter y: 4
Enter z: 7
Addition results
x = 7 , y = 9 , z = 13

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#type and address of class Date


#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)#Type and address of a
print(b)#Error
print(c)#Error
print(d)#Error
print(b . _str_())#35
print(c . _str_())#Hyd
print(d . _str_(50))#50

'''(Home  work) Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90'''

class  Test:
	def   get(self):
		self.x = int(input("Enter x value: "))
		self.y = int(input("Enter y value: "))  
		self.z = int(input("Enter z value: "))#How  to  read  inputs  into  variables  x , y  and  z  of  object  self
	def  add(self , m , n):
		self.x = m.x+n.x
		self.y = m.y+n.y
		self.z = m.z+n.z #How  to  add  objects  m  and  n  and  store  results  in  object  self
	def  disp(self):
		print("x =", self.x)
		print("y =", self.y)
		print("z =", self.z)  #How  to  print  object  self
# End  of  the  class
a=Test() 
b=Test()
c=Test() #How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
c.add(a, b)#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() #How  to  print  object  'c

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   student:
	def   get(self):  #  self  is  object  's'
		self . rno = int(input('Enter  roll  number : ')) #  Adds  variable  rno  to  object  's'  with  user  input
		self . sname = input('Enter  student  name :  ')  #  Adds  variable  sname  to  object  's'  with  user  input
		self . gender = input(('Enter  gender (m/f) : '))   #  Adds  variable  gender  to  object  's'  with  user  input
		self . m = []  #  Adds  empty  list   'm'   to  object  's'
		for  i  in  range(3):  #  Marks  of  3  subjects
			marks = int(input(F'Enter  marks  of  subject  {i + 1}  :  '))  #  Reads  input  to  local  variable
			self . m . append(marks)  #  Appends   value  of  Lv  to  list  s . m
	def   compute(self):  #  self  is  object  's'
		self . tot = sum(self . m)  #  Adds  variable  tot  to  object  's'  with  sum  of  marks
		self . avg = self . tot / 3  #  Adds  variable  avg  to  object  's'  with  average  marks
		if  min(self . m) < 40:   #  At  least  one  subject  is  below  40  marks
				self . grade = 'Fail'  #  Adds  variable  grade  to  object  's'  with  'Fail'
		elif  self . avg >= 70:
				self . grade = 'Distinction'  #  Adds  variable  grade  to  object  's'  with  'Distinction'
		elif  self . avg >= 60:
				self . grade = 'First  class'  #  Adds  variable  grade  to  object  's'  with  'First  class'
		elif  self . avg  >= 50:
				self . grade = 'Second  class'   #  Adds  variable  grade  to  object  's'  with  'Second  class'
		else:
				self . grade = 'Third  class'   #  Adds  variable  grade  to  object  's'  with  'Third  class'
	def  disp(self):  #  self  is  object  's'
		print('Roll  Number  :  ' ,  self . rno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' ,  self . gender)
		print('Total  Marks  :  ' , self . tot)
		print(F'Average  :  {self . avg:.2f}')
		print('Grade  :  ' , self . grade)
	def   _str_(self):
		return  F'{self . rno}  \t {self . sname}  \t  {self . gender}  \t  {self . tot}  \t  {self . avg:.2f}  \t  {self . grade}'  #  Concatenates  all  the  value  of  object  self  to  form  a  string
#End  of  the  class
if  _name_ == '_main_':  #  True when  prog9a  is  executed  and  False  when  prog9a  is  imported
	s = student() #  Creates  an  empty  student class object
	s . get() #   Reads  inputs  to  object  's'
	s . compute()  #  Stores  results  in  object  's'
	s . disp()  #  Prints  values  of  object  's'
	print(s)  #  Executes  _str_()  method  of  student  class  which  returns  all  the  values  of  object  's'  in  the  form  of  string




#  Object  's'  --->  rno = 25 , sname = 'Rama Rao' , gender = 'm' , m = [52,48,55] , total = 155 , average = 51.66 , grade = '2nd  class'


'''
Can  Fail  be  handled  at  the  end ?  --->  No  and  it  should  be  handled  only  at  the  begining
'''

'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 =  (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 = (18 - 15) / 27 = 	3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =	10 / 27  = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division  and   return  True

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 = (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =	0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->   2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted  and  return  False

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero

4) What  does  div()  method  return ?  ---> True  when  division  is  succesful  and  False  otherwise
'''
import  math
class  rat:
	def  get(self):
		self . nr = int(input('Enter  numerator :  '))  # Adds  variable  nr  to  object  self  with  user  input
		self . dr = int(input('Enter  denominator :  '))  # Adds  variable  dr  to  object  self  with  user  input
		self . test()  #  Is  denom  of  object  self  zero
	def  test(self):
		while  self . dr == 0:  #  Repeat  until  dr  is  non-zero
			self . dr = int(input('Denom  can  not  be  zero , reenter :  '))  #  Reads  non-zero  denominator  to  object  self
	def    _str_(self):
			 return  F'{self . nr} / {self . dr}'  #   Concatenates  values  of  self  to  form  a  string  with  '/'
	def   add(self , a , b):
		self . nr = a . nr * b . dr + a . dr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr  # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()  #  Simplifies  values  of  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self . nr = a . nr * b . dr - a . dr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr   # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()   #  Simplifies  values  of  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self . nr = a . nr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr   # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()   #  Simplifies  values  of  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self . nr = a . nr * b . dr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . nr  # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()  #  Simplifies  values  of  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if  self . nr != 0:
			ans = math . gcd(self . nr , self . dr)  #  gcd  of  values  of  self
			self . nr = self . nr // ans  #  Simplifies  nr  of  object  self
			self . dr = self . dr // ans   #  Simplifies  dr  of  object  self
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
if  _name_ == '_main_': #  True  when  prog10a  is  executed  and  False  when  prog10a  is  imported
	a = rat() #  Creates  6  empty  rat  class  objects
	b = rat()
	c = rat()
	d = rat()
	e = rat()
	f = rat()
	a . get()  #  Reads  inputs  to  object  'a'
	b . get()  #  Reads  inputs  to  object  'b'
	c . add(a , b)  #  Adds  objects  'a'  and  'b'  and  stores  results  in  object  'c'
	d . sub(a , b)  #  Subtracts  objects  'a'  and  'b'  and  stores  results  in  object  'd'
	e . mul(a , b)  #  Multipliees  objects  'a'  and  'b'  and  stores  results  in  object  'd'
	f . div(a , b)  #  Divides  objects  'a'  and  'b'  and  stores  results  in  object  'f'
	print('Sum : ' , c)  #   _str_()  method  of  rat  class  returns   values  of  object  'c'  in  the  form  of  string
	print('Difference : ' , d)  #   _str_()  method  of  rat  class  returns   values  of  object  'd'  in  the  form  of  string
	print('Product : ' , e)  #   _str_()  method  of  rat  class  returns   values  of  object  'e'  in  the  form  of  string
	if  b . nr != 0:
		print('Division : ' , f)  #   _str_()  method  of  rat  class  returns   values  of  object  'f'  in  the  form  of  string
	else:
		print('Division  is  not  permitted')


'''
1) Can  a  method  call  another  method  of  same  class ?  ---> Yes  with  self . method()

2) get()  calls  which  method  ?  --->  Method  test()  of  the  same  class

3) If  get()  method  is  called  wrt  obj  'a' ,
    test()  method  is  called  wrt  which  object ?  ---> Same  object  'a'  due  to  self . test()

4) add()  calls  which  method  ?  ---> Method  simplify()  of  the  same  class

5) If  add()  method  is  called  wrt  object  'c',
    simplify()  method  is  called  wrt  which  object ?  ---> Same  object  'c'  due  to  self . simplify()

6) In  which  order  can  methods  of  the  class  be  defined ?  ---> Any  order

7) Can  a  method  be  called  before  it  is  defined ?  ---> Yes
    Can  a  function  be  called  before  it  is  defined ?  ---> No
'''










































