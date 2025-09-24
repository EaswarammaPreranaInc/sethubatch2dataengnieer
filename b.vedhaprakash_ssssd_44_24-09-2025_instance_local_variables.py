# home work on 24/09/2025 module 4 class 2 
---------------------------------------------------------------------------------------

'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a = float(input("Enter side a : "))  #How  to  read  three  sides  into  object  self
		self.b = float(input("Enter side b : ")) #How  to  read  three  sides  into  object  self
		self.c = float(input("Enter side c : ")) #How  to  read  three  sides  into  object  self
	def  test(self):
		if  self.a + self.b >= self.c and self.b + self.c >= self.a and self.c + self.a >= self.b: #  sum  of  every  2  sides  >=  3rd  side:
				pass #Do  nothing
		 else:
				print('Not  a  triangle')
				exit() #How  to  stop  execution
	def  area(self):
			s = (self.a + self.b + self.c) / 2
			return   math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) # area  of  triangle
	def  peri(self):
			return self.a + self.b + self.c #  perimeter  of  triangle
# End of the class
t=trianlge # How  to  create  triangle  class  object
t.get() #How  to  read  inputs  into  object
t.test() # How  to  test  whether  inputs  are  valid
print('Area : ',  t.area())
print('Perimeter : ', t.peri())

------------------------------------- use the above program to solve these below ---------------------------------------------------
'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Reuse  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
t = triangle() # How  to  create  triangle  object
triangle.get(t)  #How  to  call  get()  method  in  another  way
t.test () #How  to  call  test()  method  in  another  way
print('Area : ',  triangle.area(t) #How  to  call  area()  method  in  another  way)
print('Perimeter: ', triangle.peri(t) #How  to  call  peri()  method  in  another  way)

------------------------------------------------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10 # it is local variable 
		self . x = 20 #instance variable 
		print(x) # 10 is printed 
		print(self . x) # here 20 is printed and local variable 
		x += 5 # 15 and here local variable dies once m1 ends 
		self . x += 7 # 27 it is instance variable and updated to 20+7
	def   m2(self):
		print(x) # x is not defined and code stops here
		print(self . x) # nothing
		self . x += 6 # nothing
# End  of  the  class
a = c1() # empty object a is created
a . m1() # 
a . m2() # 
print(a . x) #
print(self . x) # 
print(x) 

# outputs are 10 and 20 

---------------------------------------------------------------------------------------------------------------------------------------
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  --->  x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x = float(input("Enter side x : "))  #How  to  read  inputs  into  variables  x , y  and  z  of  object  self
		 self.y = float(input("Enter side y : ")) 
		 self.z = float(input("Enter side z : "))   
	def   add(self , m , n):
		 self.x = m.x + n.x
        	 self.y = m.y + n.y
        	 self.z = m.z + n.z   #How  to  add  objects  m  and  n  and  store  results  in  object  self
			
	def  disp(self):
		 print(self.x) #How  to  print  object  self
		 print(self.y) 
		 print(self.z) 
# End  of  the  class
a = Test()
b = Test()
c = Test() # How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() #How  to  read  inputs  into  object  'b'
print("Addition Results")
c.add(a+b) # How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.disp() #How  to  print  object  'c'

-----------------------------------------------------------------------------------------------------------------------------------------
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date() # here class date empty object is created 
a . dd = 15 # dd is added to the object a
a . mm = 8 # mm is added to the object a
a . yy = 1947 # yy is added to the object a
print(a) # it wont print these ('15-8-1947') because we have not defined the __str__ 

-------------------------------------------------------------------------------
#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25' #'25' 
class   c2:
	def  __str__(self):
			return   35 # error because __str__ allow str not int
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()  # c1() empty object a created 
b = c2()
c = c3()
d = c4()
print(a) # '25'
print(b) # error because __str__ allow str not int
print(c) # print Hyd  inside the string i.e is __str__ , and python returns value none
print(d) # x is not defined eror 
print(b . __str__()) # error
print(c . __str__()) # hyd none
print(d . __str__(50)) # 50 is printed
