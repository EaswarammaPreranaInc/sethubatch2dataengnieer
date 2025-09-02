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
f1(t = (10 , 20 , 30)) # Error: f1() got an unexpected keyword argument 't'
'''
(10, 20, 15, 18)
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
        return sum(a)/len(a) if len(a)>0 else 0
    except:
        return 'All arguments must be numbers' # Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End of the function
print(avg(10 , 20 , 15 , 18)) # 15.75
print(avg(25 , 10.8 , True)) # 12.933333333333334
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.659999999999998
print(avg()) # 0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # All arguments must be numbers

def concat(*a):
    try: return ' '.join(a)
    except: return 'All arguments must be strings'  # Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End of the function
print(concat('Sankar', 'Dayal', 'Sarma')) # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) # '' (empty string)
print(concat('Python')) # Python
print(concat(1, 2, 3)) # All arguments must be strings

def f1(a = 25 , *b):
    print(f'a : {a}  \t   b  :  {b} ')
# End of the function
f1(10 , 20 , 30 , 40) # a : 10 	   b  : (20, 30, 40)
f1(50 , 60)           # a : 50 	   b  : (60,)
f1(70)                # a : 70 	   b  : ()
f1(a = 80)            # a : 80 	   b  : ()
f1(b = (10 , 20 , 30) , a = 40) # Error: f1() got unexpected keyword argument 'b' 
f1()                  # a : 25 	   b  : ()
f1(a = 10 , (20 , 30 , 40))     # Error: positional argument follows keyword argument
f1(25 , b = (10 , 20 , 30))     # Error: f1() got unexpected keyword argument 'b'
f1(25 , a = (10 , 20 , 30))     # Error: f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10, 20, 30) 	   b  : (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # # Error: positional argument follows keyword argument

def f1(*a , b):
    print(F'a  :  {a}   \t   b  :  {b}')
f1(10 , 20 , 30 , b = 40) # a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60) # a  :  (50,)   	   b  :  60
f1(b = 70) # a  :  ()   	   b  :  70
f1(b = 10 , a = (20 , 30 , 40)) # Error: unexpected keyword argument 'a'
f1(b = 10 , (20 , 30 , 40)) # Error: positional argument follows keyword argument
f1() # Error: missing required argument 'b'
f1(10 , 20 , 30 , (10 , 20 , 30)) # Error: missing required argument 'b'
f1(10 , 20 , 30 , 40) # Error: missing required argument 'b'

f1(25)# Error: missing required argument 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  :  (10, 20, 30)   	   b  :  (10, 20, 30)

def f1(a , *b , c):
    print(f'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End of the function
f1(10 , 20 , 30 , 40 , c = 50) # a  :  10  	b  :  (20, 30, 40)  	c  :  50  
f1(60 , 70 , c = 80) # a  :  60  	b  :  (70,)  	c  :  80  
f1(90 , c = 100) # a  :  90  	b  :  ()  	c  :  100  
f1(a = 1 , 2 , c = 3) # Error: positional argument follows keyword argument  
f1(1 , 2 , 3)  # Error: missing required keyword-only argument 'c'  
f1(a = 1 , b = 2 , c = 3) # Error: 'b' is not a keyword argument, only *b accepts multiple values  
f1(a = 25 , 100 , 200 , 300 , c = 35) # Error: positional argument follows keyword argument  

def f1(*a, *b):
    pass #  Error: Two *args not allowed
def f2(*a, b):
    pass #  Valid: *a collects extra args, b must be passed as keyword
def f3(a, *b):
    pass # Valid: a is positional, *b collects extra args
def f4(a, b):
    pass #  Valid: two normal positional params
def f5(a, *b, c):
    pass # Valid: a positional, *b collects, c must be keyword-only
def f6(*, a, *b, c):
    pass # Error: two * not allowed (* already used for keyword-only, *b invalid)
def f7(a, *b, c, /):
    pass # Error: / (positional-only) cannot appear after *args or keyword-only

def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
# End of the function
f1([10, 20], {30, 40}, (50, 60))
output:
([10, 20], {30, 40}, (50, 60))   # a is a tuple of all arguments
<class 'tuple'>                   # type of a is tuple
[10, 20]                          # first element is a list
<class 'list'>
{30, 40}                          # second element is a set
<class 'set'>
(50, 60)                          # third element is a tuple
<class 'tuple'>

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
'''
Results
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

def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()
'''
 Results
 Empno ... 25
 Empname ... Rama  Rao
 Salary ... 10000.0
 Gender ... m
 Results
'''

def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''

def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number : 25  Emp  Name : Sita  Salary:10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error: keys must match function parameter names
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)  # {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)  # {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

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
'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''

q) Write  a  program  to  evaluate  expression  like  calculator
Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5
Hint:  Use  while  loop
Ans) expr = input("Enter any expression terminated by = : ")
i = 0
a = ""  # to store the first number
# Read the first number (before any operator)
while expr[i].isdigit():
    a += expr[i]
    i += 1
a = float(a)   
while i < len(expr):
    op = expr[i]   # operator (+, -, *, /, =)
    if op == "=":
        break  # end of expression
    i += 1
    # read next number 'b'
    b = ""
    while expr[i].isdigit():
        b += expr[i]
        i += 1
    b = float(b)
    # perform operation
    if op == "+":
        a = a + b
  elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b
print("Result :", a)
q) Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M  900  -  CM  500 -  D  400 – CD  100 -   C  90  -  XC  50  -  L  40  -  XL  10  -  X  9  -  IX         5  - V  4  -  IV  1  -  I
1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVII
Ans) def to_roman(num):
    values = [1000, 900, 500, 400,
              100, 90, 50, 40,
              10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD",
               "C", "XC", "L", "XL",
               "X", "IX", "V", "IV", "I"]
    roman = ""
    i = 0
    while num > 0:
        q = num // values[i]              
        roman += symbols[i] * q           
        num = num % values[i]            
        i += 1
    return roman
n = int(input("Enter a number : "))
print("Roman Equivalent :", to_roman(n))

q)Write  a  program  to  print  each  digit  of  the  number  in  words
Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven
Ans) n = input("Enter a number: ")
a = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
s = ""  
for ch in n:
    digit = int(ch)          
    word = a[digit]          
    s = s + word + " "       
print("Output:", s.strip())

q) Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                        PACES
				ACESP
				CESPA
				ESPAC

Ans) s = input("Enter a string: ")
for i in range(len(s)):
        print( s[i:] + s[:i])

q) Write  a  program  to  print  mathematical  table  of  a  number
Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       		      7 * 2 = 14
			      7 * 3 = 21
			       .....
			       7 * 10 = 70

Ans) n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f'{n} * {i} = {n * i}')

q) Write a  program to print following pyramid
Input: 5
              A
            A B
           A B C
          A B C D
         A B C D E
Ans) n = int(input("Enter the number: "))  
for i in range(1, n+1):
    print(" " * (n - i), end="")  # spaces
    for ch in range(ord('A'), ord('A') + i):
        print(chr(ch), end=" ")
    print()

a = 10
def f1():
    b = 40
    print('a : ' , a) # a :  11
    print('b : ' , b) # b :  40
    print('c : ' , c) # c :  31
    print() # (blank line)
# End of f1() function
b = 20
def f2():
    a = 50
    print('a : ' , a) # a :  50
    print('b : ' , b) # b :  22
    print('c : ' , c) # c :  32
# End of f2() function
c = 30
print('a : ' , a) # a :  10
print('b : ' , b) # b :  20
print('c : ' , c) # c :  30
print() # (blank line)
a += 1
b += 1
c += 1
f1()
a += 1
b += 1
c += 1
f2()
print('Bye') # Bye

def f1():
    a = 20
    print(a) # 20
    a += 1
# End of the function
a = 10
print(a) # 10
a += 1
f1()
print(a) # 11
