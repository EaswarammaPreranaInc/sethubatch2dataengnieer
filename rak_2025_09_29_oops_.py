# # Find  outputs
# class  Rat:
# 	def   __init__(self , nr1 = 22, dr1 = 7):
# 		self . nr = nr1
# 		self . dr = dr1
# 	def   __str__(self):
# 		return  F'{self . nr}  /  {self . dr}'
# #end  of  the  class
# a = Rat()
# b = Rat(9)
# c = Rat(5,  8)
# d = Rat(dr1 = 9)
# e = Rat(dr1 = 3 , nr1 = 2)
# x = eval(input('Enter numerator  :  '))       #11
# y = eval(input('Enter Denominator  :  '))     #15
# f = Rat(x , y)
# print('a  :  ' , a)     #22 / 7
# print('b  :  ' , b)     #9 / 7
# print('c  :  ' , c)     #5 / 8
# print('d  :  ' , d)     #22 / 9
# print('e  :  ' , e)     #2 / 3
# print('f  :  ' , f)     #11 / 15
# c . __init__()
# print('c  :  ' , c)        #22 / 7
# a . __init__(3.8  , 4.6)   
# print('a  :  ' , a)        #3.8 / 4.6
# # g = Rat(nr1 = 9 , 5)             #error, positional arg cannot be after keyword arg
# # h = Rat(nr = 9 , dr = 5)           #error, keyword name is nr1 not nr and dr1 not dr
# '''
# Object  'a'   --->  nr = 22 , dr = 7

# Object  'b'   --->  nr = 9 , dr = 7
# '''



# # Find  outputs (Home  work)
# class  Date:
#     def   __init__(self , dd1 , mm1  , yy1):
#         self . dd = dd1
#         self . mm = mm1
#         self . yy = yy1
# # End  of  the  class
# a = Date(15 , 8 , 1947)
# b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
# c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
# print('a  :  ' , a . __dict__)                 #a : {'dd': 15, 'mm': 8, 'yy': 1947}
# print('b  :  ' , b . __dict__)                 #b : {'dd': 26, 'mm': 1, 'yy': 1950}
# print('c  :  ' , c . __dict__)                 #c : {'dd': 19, 'mm': 7, 'yy': 1985}
# # d = Date()                                   #error, 3 args are missing
# # e = Date(dd = 30 , mm = 4 , yy = 2022)       #error, keyword arg names are not matching
# # f = Date(dd1 = 26 , mm1 = 8 , 2023)          #positional arg can't be after keyword arg
		 



# # Find  outputs (Home  work)
# class  c1:
# 	def  __init__(self):
# 		print('c1  class constructor')
# 		return  25
# class  c2:
# 	def  __init__(self):
# 		print('c2  class  constructor')
# 		return  None
# class  c3:
# 	def  __init__(self):
# 		print('c3  class  constructor')
# # End  of  class
# # a = c1()                #cannot create obj if constructor returning other than None
# b = c2()                  #c2 class constructor (None is ignored and will not be returned)
# print(b)                  #type and address
# print(b . __init__())     #c2 class constructor \n None
# c = c3()                  #c3 class constructor
# print(c . __init__())     #c3 class constructor \n None
	  


# # Find  outputs (Home  work)
# class  c1:
# 	def  __init__(self):    
# 		print('Constructor') 
# 		b = c1()                 #this is a recursive call since its calling this same constructor, this creates infinite recursion
# # End  of  class
# a = c1()   



# #  Difference  between  init()    and  __init__()   methods (Home  work)
# class c1:
#     def  __init__(self):
#         print('Constructor')
#         self . x = 10
#         self . y = 20
# class c2:
#     def  init(self):
#         print('Method')
#         self . x = 30
#         self . y = 40
# a = c1()                            #Constructor
# print(a . __dict__)                 #{'x': 10, 'y' : 20}
# b = c2()                         
# print(b . __dict__)                 #{}
# b . init()                          #Method
# print(b . __dict__)                 #{'x': 30, 'y': 40}
	  



# # Find  outputs (Home  work)
# class   c1:
#         def   __init__(self):
#                 self . a = 10
#         def   m1(self):
#                 self . b = 20
# #End  of  class  c1
# class   c2:
#         def  m3(self):
#                 x . e = 50
# # End  of  class  c2
# def   f1():
#         x . c = 30
# #  End  of  function  f1
# x = c1()
# print(x . __dict__)                #{'a': 10}
# x . m1()
# print(x . __dict__)                #{'a': 10, 'b': 20}
# f1()
# print(x . __dict__)                #{'a': 10, 'b':20, 'c':30}
# x . d = 40 
# print(x . __dict__)                #{'a': 10, 'b':20, 'c':30, 'd': 40}
# y = c2()
# y . m3()                           
# print(x . __dict__)                #{'a': 10, 'b':20, 'c':30, 'd': 40, 'e': 50}
# z = c1()
# print(z . __dict__)                #{'a': 10}




# # Find  outputs  (Home  work)
# class   c1:
# 	def   __init__(self):
# 		self . x = 10
# 		self . y = 20
# 		self . z = 30
# #end  of  the  class
# a = c1()
# b = c1()
# print(a . __dict__)          #{'x': 10, 'y': 20, 'z': 30}
# print(b . __dict__)          #{'x': 10, 'y': 20, 'z': 30}
# del  a . x
# del  b . y
# print(a . __dict__)          #{'y': 20, 'z': 30}
# print(b . __dict__)          #{'x': 10, 'z': 30}
# # print(a . x)                 #error, x is deleted from obj a
# # print(b . y)                 #error, y is deleted from obj b
	  


# #  Find  outputs (Home  work)
# class   c1:
# 	def  __init__(self):
# 		print('1st  constructor')
# 	def  __init__(self):
# 		print('2nd  constructor')
# 	def  __init__(self):
# 		print('3rd  constructor')
# # End  of  the  class
# a = c1()  #3rd constructor




# #  Find  outputs  (Home  work)
# class   c1:
# 	def  __init__(self):
# 		print('No  argument  constructor')
# 	def  __init__(self , x):
# 		print('single  argument  constructor : ' , x)
# 	def  __init__(self , x , y):
# 		print('Two  argument  constructor : ' , x , y)
# # End  of  the  class
# a = c1(10 , 20)          #Two  argument  constructor : 10 20
# # b = c1(30)               #error, one more arg is missing
# # c = c1()                 #error, two args are missing




# #  Find  outputs
# class   c1:
# 	def  __init__(self):
# 		print('No  argument  constructor')
# 	def  __init__(self , x):
# 		print('single  argument  constructor : ' , x)
# 	def  __init__(self , x = 100 , y = 200):
# 		print('Two  argument  constructor : ' , x , y)
# # End  of  the  class
# a = c1(10 , 20)          #Two argument constructor: 10 20
# b = c1(30)               #Two argument constructor: 30 200
# c = c1()                 #Two argument constructor: 100 200



# # What  happens  when  function  and  class  have  same  name ?
# def   f1():
# 	print('Function')
# 	return  25
# class   f1:
# 	def  __init__(self):
# 		print('Constructor')
# #end of the  class
# a = f1()                  #constructor
# print(a)                  #type and address of obj a




# # Find  outputs (Home  work)
# class    c1:
# 	def   __init__(self):
# 		print('Constructor')
# def  c1():
# 	print('Function')
# #end of the  class
# a = c1()                  #Function
# print(a)                  #None



# # Find outputs  (Home  work)
# class    c1:
#         def  __init__(self):
#                 print('Constructor')
# def    c1(x):
#         print('Function : ' , x)
# # End  of  class  c1
# # a = c1()                  #error, missing one pos arg
# b = c1(25)                #Function 25
# print(b)                  #None




# #  Save  the  program  in  prog9a.py  file
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9a')
# # #  Find  outputs (Home  work)
# # from  prog9a  import  c1
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9b')
# a = c1()   #c1 class of prog9b



# #  Save  the  program  in  prog9a.py  file
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9a')
# #  Find  outputs (Home  work)
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9c')
# # from  prog9a  import  c1
# a = c1()  #c1 class of prog9c  




# #  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# # How  to  import  class  c1  from  prog9a
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9d')
# # How  to  create  c1  class  object  of  current  module
# # How  to  create  c1  class  object  of  prog9a




# '''
# How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
# '''
# # How  to  import  prog9a
# class   c1:
# 	def  __init__(self):
# 		print('c1  class  of  prog9e')
# # How  to  create  c1  class  object  of  current  module
# # How  to  create  c1  class  object  of  prog9a









# # Public  and  Private  members  demo  program
# class  Test:
# 	def  __init__(self):
# 		self.x =10             #How  to  initialize  public  variable  'x'  to  10
# 		self.__y = 20          #How  to  initialize  private  variable  'y'  to  20
# 	def  m1(self):
# 		print('m1  method')
# 		print(self.x)       #How  to  print   variable  'x'
# 		print(self.__y)     #How  to  print  private  variable  'y'
# 		self.__m2()         #How  to  call    private  method   m2()
# 		print('Back to m1 method')
# 	def  __m2(self):
# 		print('__m2  method')
# 		print(self.x)       #How  to  print   variable  'x'
# 		print(self.__y)     #How  to  print  private  variable   'y'
# # End  of  the  class
# t = Test()
# print('Outside')
# print(t.x)            #How  to  print  variable  'x'
# print(t._Test__y)     #How  to  print   variable  'y'
# # print(t . __y)        #error, not visible outside
# print(t . __dict__)   #{'x': 10, '_Test__y': 20}, y is seen as _Test.__y
# t.m1()                #How  to  call  method  m1()
# t._Test__m2()         #How  to  call   method  m2()
# # t . __m2()            #error, cannot access directly outside class methods
# print('End')




# #  Find  outputs
# class  c1:
# 	def __init__(self):
# 		self.x = 10             #How  to  initialize  public  variable  'x'  with  10
# 		self.__x = 20           #How  to  initialize  private  variable  'x'  with  20
# 		self.__x__ = 30         #How  to  initialize  public  dunder  variable  'x'  with  30
# 	def  m1(self):
# 		print('public method')
# 	def  __m1(self):
# 		print('private method')
# 	def  __m1__(self):
# 		print('public Dunder method')
# #  End  of  the  class
# a = c1()
# print(a.x)          #How  to  print   variable  'x'
# print(a.__x__)      #How  to  print  public  dunder  variable  'x'
# print(a._c1__x)     #How  to  print   private  variable  'x'
# # print(a . __x)      #error, private variable not visible outside same class methods
# a.m1()              #How  to  call  public  method  m1()
# a.__m1__()          #How  to  call  public  dunder  method  m1()
# a._c1__m1()          #How  to  call  private  method  m1()
# # a . __m1()          #error, private method not visible outside



# '''
# Tricky  program
# Find  outputs
# Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
# '''
# class   c1:
# 	def   __init__(self):
# 		print('Object  is  created  at  address  :  ' , id(self))
# 	def   ___del___(self):
# 		print(F'Object  at  address  {id(self)}  is  lost')
# # End    of    the    class
# a = c1()         #constructor of c1 executed
# a = None         #destructor of c1 executed
# b = c1()         #constructor of c1 executed
# del    b         #destructor of c1 executed
# c = c1()         #constructor of c1 executed
# c = c1()         #constructor and destructor of c1 executed
# d = c1()         #constructor of c1 executed
# e = c1()         #constructor of c1 executed
#                  #3 times destructor of c1 executed



# # Identify  Error (Home  work)
# class   c1:
# 	def  __del__(self , x):
# 		print('destructor : ' ,  x)
# a = c1()
# a . __del__(25)                #destructor cannot have argument, when called explicitly it executes but when obj is being destroyed by pvm it throws error



# # Find  outputs (Home  work)
# class   c1:
# 	def  __del__(self , x = 35):      #destructor can have default arguments
# 		print('destructor : ' , x)
# a = c1()
# a . __del__(25)                       #2 times destructor is executed          



# # Find  outputs (Home  work)
# class   c1:
# 	def  __del__(self):
# 			print('destructor')
# 			b = c1()           #ref b will be deleted soon after method execution, so it creates a infinite recursion call as it calls this same destructor again and again
# a = c1()                        



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()



# #  Find  outputs( Home  work)
# class   c1:
# 	def  __del__(self):
# 		print('1st  destructor')
# 	def  __del__(self):
# 		print('2nd  destructor')
# 	def  __del__(self):
# 		print('3rd  destructor')
# # End  of  the  class
# a = c1()



# #Find  outputs (Home  work)
# class   c1:
# 	def   __init__(self):
# 		print('Object  is  created  at  address  :  ' , id(self))
# 	def   __del__(self):
# 		print(F'Object  at  address  {id(self)}  is  lost  ')
# #end  of  the  class
# c = b = a = c1()
# del   a
# print('Hello')
# del   b
# print('Hi')
# del   c
# print('Bye')
# d = c1()
# print('End')




# # Find  outputs(Home  work)
# class  c1:
#         def     __init__(self):
#                 print('Object  is  created  at  address  :  ' , id(self))
#         def     __del__(self):
#                 print(F'Object  at  address  {id(self)}  is  lost ')
# #End of the class
# list = [c1() , c1() , c1()]
# del  list



# # Find  outputs  (Home  work)
# class   c1:
# 	def  __del__(self):
# 		print('destructor')
# 		return  25
# a = c1()
# print(a . __del__())
# print('Hello')
# del   a
