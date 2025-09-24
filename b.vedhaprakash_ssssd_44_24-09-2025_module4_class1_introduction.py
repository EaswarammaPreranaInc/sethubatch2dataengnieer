# homework on 23/09/2025 module 4 class 1 
-----------------------------------------------
# Identify  error  (Home work)
class   c1:
	def  m1(self):
		pass
class   c2:
        pass
class   c3: # ERROR NO M1 METHOD AND NO PRINT STATEMENTS 

---------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	pass
# End  of  the  class
a = c1() # C1 CLASS CREATED AND A REFERENCE TO THAT 
print(id(a)) # ID OF THE ADDRESS  
print(type(a)) # CLASS'__MAIN__.C1' 
print(a . __dict__) # EMPTY DICTIONARY THAT IS {}
print(a) # TYPE AND ADDRESS OF THE A 
del  a # DELETES OBJECT A 
print(a) # NOTHING AND NO OBJECT A EXISTS

------------------------------------------------------

#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method') # M1 HAS SAME NAME NOT PRINTED 
	def   m1(self):
		print('2nd  method') # SAME 
	def   m1(self):
		print('3rd  method') # EXECUTED 3RD METHOD 
# End  of  class  c1
a = c1() # C1() IS CREATED 
a . m1() # EXECUTED 3RD METHOD
m1() # FUNCTION M1 


----------------------------------------------------------
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method') # NOT PRINTED BECAUSE WE HAVE ANOTHER ONE WITH SAME NAME 
	def   m1(self , x):
		print('Single  argument  method : ' , x) # SAAME 
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y) # PRINTED two arguments method : <space>10<space>20 
# End  of  class  c1
a = c1() # c1() class is created 
a . m1(10 , 20) # prints 3rd method 
a . m1(30) # error insufficient arguments 
a . m1() # error no argumnets or insufficient arguments 

------------------------------------------------------------

#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1() # c1() class is created 
a . m1(10 , 20) # 3rd arguments is executed and it prints Two argument method : 10 20 
a . m1(30) # 3rd arguments is executed and it prints Two argument method : 1 30 
a . m1() # 3rd arguments is executed and it prints Two argument method : 1 2

---------------------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class') # same name 
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class') # not printed because it has same name 
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class') # executed 
a = c1() # c1() class created 
a . m1() # 3rd method executed 

--------------------------------------------------------------
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class') # not executed
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class') # not executed 
class   c1:
	pass # nothing executed 
a = c1() # c1() class created 
a . m1() # error no m1 class in the 3rd or last or latest method of c1() class

---------------------------------------------------------------
#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1() # c1() class  created empty object
print(a . __dict__)  # prints the dict a
a . x = 10
print(a . __dict__) # 10 is added to the empty dictionary 
a . y = 20
print(a . __dict__) # 20 is added to the empty dictionary 
a . x = 30
print(a . __dict__) # x is 10 modified to 30 
a . y = 40
print(a . __dict__) # y is 20 modified to 40
del  a . x
print(a . __dict__) # deletes the x in the dictionary 
del  a . y
print(a . __dict__) # deletes the y in the dictionary 
del   a # deletes the dictionary 
print(a . __dict__) # nothing is printed an it is an empty dictionary 

------------------------------------------------------------------
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
t=trianlgeHow  to  create  triangle  class  object
t.get() #How  to  read  inputs  into  object
t.test # How  to  test  whether  inputs  are  valid
print('Area : ',  t.area())
print('Perimeter : ', t.peri())

------------------------------------------------------------------------------------------
