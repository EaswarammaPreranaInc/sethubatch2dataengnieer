def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
f1(t = (10 , 20 , 30))      
#output:
'''                                                                                                                                                                                     output                                                                                                                                                                                                        (10, 20, 15, 18)
<class 'tuple'>
4
()
<class 'tuple'>
0
([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3
('Hyd',)
<class 'tuple'>
1
((100, 200, 150),)
<class 'tuple'>
1

'''
def avg(*a):
    try:
        return sum(a) / len(a)
    except ZeroDivisionError:
        return 0

print(avg(10, 20, 15, 18))                  # 15.75
print(avg(25, 10.8, True))                  # 12.933333...
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))     # 14.26
print(avg())                                # 0
print(avg(25))                              # 25.0
print(avg(3 + 4j, 5 + 6j))                  # (4+5j)
tpl = (10, 20, 15, 18)
print(avg(*tpl))                            # 15.75

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
    return ' '.join(str(x) for x in a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))
#output
'''
Sankar Dayal Sarma
Hyd Is Green City
Python Is A Great Language

Python
1 2 3
'''
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10      b  :  (20,30,40)
f1(50 , 60)#a : 50     b : (60,)
f1(70)#a :  70     b :  ()
f1(a = 80)#a : 80     b  : ()
f1(b = (10 , 20 , 30) , a = 40)#a : 40  b  :  (10,20,30)
f1()#a : 25  b : ()
f1(a = 10 , (20 , 30 , 40))#positional argument follows keyword argument
f1(25 , b = (10 , 20 , 30))#f1() got an unexpected keyword argument 'b'
f1(25 , a = (10 , 20 , 30))#f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10,20,30)     b :  (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#positional argument follows keyword argument

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  : (10,20,30)    b  :  40
f1(50 , b = 60)#a  :  (50,)    b  :  60
f1(b = 70)#a   :   ()    b   :  70
f1(b = 10 , a = (20 , 30 , 40))#f1() got an unexpected keyword argument 'a'
f1(b = 10 , (20 , 30 , 40))#positional argument follows keyword argument
f1()#f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , (10 , 20 , 30))#f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , 40)#f1() missing 1 required keyword-only argument: 'b'
f1(25)#f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a    :    (10,20,30)   b  :  (10,20,30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :   10     b   :  (20,30,40)  c  : 50
f1(60 , 70 , c = 80)#a  :  60    b   :  (70,)   c  :  80
f1(90 , c = 100)#a   :   90     b  :  ()     c   :  100
f1(a = 1 , 2 , c = 3)#positional argument follows keyword argument
f1(1 , 2 , 3)#f1() missing 1 required keyword-only argument: 'c'
f1(a = 1 , b = 2 , c = 3)#f1() got an unexpected keyword argument 'b'
f1(a = 25 , 100 , 200 , 300 , c = 35)#f1() got an unexpected keyword argument 'b'

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):# invalid Cannot have more than one * parameter.
        pass
def  f2(*a , b):# valid *a collects extra positional arguments.b becomes a keyword-only parameter.
        pass
def  f3(a , *b):#Valid a is a normal parameter, *b collects extra positional arguments.
        pass
def  f4(a , b):#Valid Standard function with two parameters.
        pass
def    f5(a , *b , c):#Valid c is keyword-only because it appears after *b.
        pass
def   f6( * , a , *b , c):#Invalid Only one * can be used to indicate start of keyword-only arguments.*b after * is not allowed.
       pass
def   f7(a , *b , c ,  /):#Invalid / must appear before * and keyword-only parameters.Syntax is wrong (positional-only indicator / cannot be placed at the end like this).
       pass

def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
#output  
'''                                                                                                                                                                                                     ([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>
'''
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''                                                                                                                                                                                                                  #output                                                                                                                                                                                                            Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()         
#output  
'''                                                                                                                                                                                                                 #output                                                                                                                                                                                                      Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results
'''
# Find  outputs (Home  work)
def   f1(*a):
    print(type(a))
    print(a)
def   f2(**a):
    print(type(a))
    print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)                                                                                                                            #output                                                                                                                                                                                                           <class 'tuple'>
(25, 10.8, 'Hyd', True)
#output
# '''
# <class 'dict'>
# {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# '''
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#f1() got an unexpected keyword argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)#{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)#{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}                                                                                                                                                                                                                                                                                                                                             
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)    
#output                                                                                                                                                                                                             25
'''
Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''
#Write  a  program  to  evaluate  expression  like  calculator
a=input("Enter the string: ")
expr = a.split()
i = 0
a = int(expr[i])   
while True:
    op = expr[i+1]   
    if op == "=":   
        break
    b = int(expr[i+2])   
    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b
    i += 2
print("Result:", a)
'''Enter  any  expression terminated by  = : 3+4*5-6/2=
Result:14.5'''

# Write a program  to  print  roman  equivalent  of  a  number

def to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, symbol in roman_map:
        count = num // value
        result += symbol * count
        num %= value
    return result
number = int(input("Enter a number: "))
print(to_roman(number))     
'''Enter  a  number :  3878
MMMDCCCLXXVIII      '''                                                                                                                                                                       #output                                                                                                                                                                                                               Enter a number: 3878


'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1              '9'       9               'Nine'          '' + 'Nine' + ' '

	 2             '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3             '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4             '7'       7               'Seven'        'Nine Two Four ' + 'Seven' + ' '
'''                                                                                                                                                                                                                           a = ['Zero', 'One', 'Two', 'Three', 'Four', 
     'Five', 'Six', 'Seven', 'Eight', 'Nine']

num = input("Enter a number: ")
s = ""
for ch in num:
    s += a[int(ch)] + " "
print(s.strip())  
#output:                                                                                                                                                                                     Enter a number: 123
'''Enter  a number :  9247
Nine Two Four Seven'''

# Write  a  program  to  print  all  the  rotations  of  the  string
s = input("Enter a string: ")
length = len(s)
for i in range(length):
    shifting = s[i:] + s[:i]
    print(shifting)
#output
'''
Enter a string: space
space
paces
acesp
cespa
espac
'''
#Write  a  program  to  print  mathematical  table  of  a  number

# Let  input  be  7,
# What  is  the  output ?  --->  7 * 1 = 7
#                        						 7 * 2 = 14
# 			  								 7 * 3 = 21
# 												 .....
# 											 7 * 10 = 70
number = int(input("Enter a number"))
for i in range(1,11):
    print(f"{number}*{i}={number * i}")            
'''                                                                                                                                                  #output                                                                                                                                                                                                    Enter a number7
7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63
7*10=70
'''

# Write a  program to print following pyramid
# Input: 5

#              A
#             A B
#            A B C
#           A B C D
#          A B C D E
# 	   i         ch
# ---------------------
#        1         'A'

# 	   2         'A'  to  'B'

# 	   3         'A'  to  'C'

# 	   4         'A'  to  'D'

# 	   5         'A'  to  'E'
                
num = int(input("Enter number of rows: "))
for i in range(1, num + 1):
    print(" " * (num - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye') 
#output      
'''                                 
a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32
Bye
'''
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)                                                      

#output                                                   
# 10
# 20
# 11