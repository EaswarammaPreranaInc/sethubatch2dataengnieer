# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()  # stores object a with values nr1 =22,dr1=7
b = Rat(9)  # stores object b with values nr1 =9,dr1=7
c = Rat(5,  8)  # stores object c with values nr1 =5,dr1=8
d = Rat(dr1 = 9) # stores object d with values nr1 =22,dr1=9
e = Rat(dr1 = 3 , nr1 = 2) # stores object e with values nr1 =2,dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # stores object f with values nr1 =11,dr1=15
print('a  :  ' , a)  #  22/7
print('b  :  ' , b)  #  9/7
print('c  :  ' , c)  #  5/8
print('d  :  ' , d)  #  22/9
print('e  :  ' , e)  #  2/3
print('f  :  ' , f)  #  11/15
c . __init__()  #  # stores object c with values nr1 =22 ,dr1=7
print('c  :  ' , c) #  5/8
a . __init__(3.8  , 4.6)  # stores object a with values nr1 =3.8,dr1=4.6
print('a  :  ' , a)  #  3.8/4.6
g = Rat(nr1 = 9 , 5)  #  Error due to positional argument after keyword argument
h = Rat(nr = 9 , dr = 5)  # Error due to unexpected arguments nr,dr

'''
Object  'a'   --->  nr = 22 , dr = 7

Object  'b'   --->  nr = 9 , dr = 7
'''



# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)  # stores object a with values dd1=15,mm1=8,yy1=1947
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)  # stores object a with values dd1=26,mm1=1,yy1=1950
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)  # stores object a with values dd1=19,mm1=7,yy1=1985
print('a  :  ' , a . __dict__)  # stores object a with values dd1=15,mm1=8,yy1=1947
print('b  :  ' , b . __dict__)  # stores object a with values dd1=26,mm1=1,yy1=1950
print('c  :  ' , c . __dict__)  # stores object a with values dd1=19,mm1=7,yy1=1985
d = Date()  #  Error due to requered 3 arguments
e = Date(dd = 30 , mm = 4 , yy = 2022)  #  Error due tp there sis no dd , mm,yy arguments
f = Date(dd1 = 26 , mm1 = 8 , 2023)  #  Error duee to positional argument after keyword argument



# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')  #  c1 class constructor
		return  25  #  Error due to __init__ should return None only
class  c2:
	def  __init__(self): 
		print('c2  class  constructor')  #  C2 class constructor
		return  None  
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()
b = c2()
print(b)  #  tYPE AND ADDRESS of object
print(b . __init__())  #  C2 class constructor  and returns none
c = c3()  #  c3 class constructor
print(c . __init__())  #  C3 class constructor



# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')  
		b = c1()  #  Error due to Unlimited Recursion 
# End  of  class
a = c1()


#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()  #  Constructor , stores x=10,y=20 in object a
print(a . __dict__)  #  {'x': 10, 'y': 20}
b = c2()  
print(b . __dict__)  # {}
b . init()  #  Method
print(b . __dict__)  #  {'x': 30, 'y': 40}
