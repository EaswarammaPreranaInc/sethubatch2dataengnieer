#  Variable  number  of  arguments  demo  program
def   f1(*t): 
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1() #  Empty  tuple  (or)  no  args  are  passed  to  the  function
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90}) #  Tuple  of  3  elements
f1('Hyd') #  Tuple  of  1  element
tpl = (100 , 200 , 150)
f1(tpl) # Tuple  of  1  element
f1(t = (10 , 20 , 30)) # TypeError:  f1()  got  an  unexpected  keyword  argument  't'

'''
(10,20,15,18)
<class 'tuple'>
4
'''


#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    return sum(a)/len(a) if len(a) != 0 else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # 15.75
print(avg(25 , 10.8 , True)) # 12.933333333333334
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # 0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # (4+5j)
tpl = (10 , 20 , 15 , 18) # tuple
print(avg(tpl)) # TypeError


#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    # Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
    return ' '.join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) # (Empty  string)
print(concat('Python')) # Python
print(concat(1, 2, 3)) # error


#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ') 
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10     b : (20, 30, 40)
f1(50 , 60) # a : 50     b : (60,)
f1(70) # a : 70     b : ()
f1(a = 80) # a : 80     b : ()
f1(b = (10 , 20 , 30) , a = 40) # a : 40     b : ((10, 20, 30),)
f1() # a : 25     b : ()
f1(a = 10 , (20 , 30 , 40)) # SyntaxError: positional argument follows keyword argument
f1(25 , b = (10 , 20 , 30)) # TypeError: f1() got an unexpected keyword argument 'b'
f1(25 , a = (10 , 20 , 30)) # TypeError: f1() got multiple values for argument 'a'
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10, 20, 30)      b : (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # SyntaxError: positional argument follows keyword argument


#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a  :  (10, 20, 30)     b  :  40
f1(50 , b = 60) # a  :  (50,)     b  :  60
f1(b = 70) # a  :  ()     b  :  70
#f1(b = 10 , a = (20 , 30 , 40)) # TypeError: f1() got an unexpected keyword argument 'a'
#f1(b = 10 , (20 , 30 , 40)) # SyntaxError: positional argument follows keyword argument
#f1() # TypeError: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , (10 , 20 , 30)) # a :  (10, 20, 30, (10, 20, 30))     b  :  ??? TypeError: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , 40) # a :  (10, 20, 30, 40)     b  :  ??? TypeError: f1() missing 1 required keyword-only argument: 'b'
#f1(25) # a :  (25,)     b  :  ??? TypeError: f1() missing 1 required keyword-only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a :  (10, 20, 30)     b  :  (10, 20, 30)


#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a : 10    b : (20, 30, 40)    c : 50
f1(60 , 70 , c = 80) # a : 60    b : (70,)    c : 80
f1(90 , c = 100) # a : 90    b : ()    c : 100
f1(a = 1 , 2 , c = 3) # SyntaxError: positional argument follows keyword argument
f1(1 , 2 , 3) # TypeError: f1() missing 1 required keyword-only argument: 'c'
f1(a = 1 , b = 2 , c = 3) # TypeError: f1() got an unexpected keyword argument 'b'
f1(a = 25 , 100 , 200 , 300 , c = 35) # SyntaxError: positional argument follows keyword argument


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b): # not valid
        pass
def  f2(*a , b): # valid
        pass
def  f3(a , *b): # valid
        pass
def  f4(a , b): # valid
        pass
def    f5(a , *b , c): # valid
        pass
def   f6( * , a , *b , c): # not valid
       pass
def   f7(a , *b , c ,  /): # not valid
       pass


# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
output:
([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>

# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) #  Dictionary  is  passed  to  the  function
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm') #  Dictionary  is  passed  to  the  function
disp() #  Empty  dictionary  is  passed  to  the  function

output:
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


# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm') # Dictionary  is  passed  to  the  function
f1() # empty dictionary is passed to the function

output: 
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
Results

# Find  outputs (Home  work)
def   f1(*a): # var arg parameter 
	print(type(a))
	print(a)
def   f2(**a): # var arg keyword parameter
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True) # <class 'tuple'>  ,  (25 , 10.8 , 'Hyd' , True)
print() # next line
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0) #  <class 'dict'> , {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}


#  Find  outputs (Home work)
def   f1(empno , ename , sal): 
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # keyword  arguments
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # invalid  keyword  arguments
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # valid  keyword  arguments
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # valid  keyword  arguments


# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) # a = 25 , b = () , c = {}
print() # next line
f1('Hyd' , 10 , 20 , 30) # a = 'Hyd' , b = (10 , 20 , 30) , c = {}
print() # next line
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # a = 10.8 , b = (25 , 'Hyd' , True) , c = {'EmpNo' : 12 , 'EmpName' : 'Rama  Rao' , 'Salary' : 10000.0}



'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop

Iteration         a          op        b        result
------------------------------------------------------
       1               3          +          4           7   --->  'a'

	   2              7          *          5           35   --->  'a'

	   3             35         -          6           29   --->  'a'

	   4             29         /          2           14.5   --->  'a'

	   5            14.5       =          ---           ----
'''
############# program #############
expr = input("Enter expression (end with =): ").split() # ['3', '+', '4', '*', '5', '-', '6', '/', '2', '=']

i = 0
a = float(expr[i])   # first number
i += 1

while i < len(expr):
    op = expr[i]     # operator
    if op == "=":    # stop when '=' is reached
        break
    b = float(expr[i+1])  # next number
    
    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b
    
    # move to next operator
    i += 2

print("Result =", a)

Enter  any  expression  terminated  by  =  :  3+4*5-6/2=
Result :  14.5


'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M
900  -  CM
500 -  D
400 - CD
100 -   C
90  -  XC
50  -  L
40  -  XL
10  -  X
9  -  IX
5  -  V
4  -  IV
1  -  I

1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVIII

2) What  is  the  result  of  3878 // 1000 ?  --->  3
    How  many  M's  are  concatenated  to  the  sting ?  --->  Three  becoz  3878 / 1000  is  3
    What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  --->  0
    How  many  CM's  are  concatenated  to  the  string ?  ---> Zero  becoz  878 / 900  is  0
    What  is  the  result  of  878 % 900 ?  --->  878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  ---> One  becoz  878 / 500  is  1
     What  is  the  result  of  878 % 500 ?  ---> 378
      and  so  on
'''
############## program ##########
roman = {1000 : 'M', 900 : 'CM', 500 : 'D', 400 : 'CD', 
         100 : 'C', 90 : 'XC', 50 : 'L', 40 : 'XL', 
         10 : 'X', 9 :'IX', 5 : 'V', 4:'IV', 
         1 :'I'}
a = eval(input("Enter regular number:")) # 3878
b = ''
for i,j in roman.items():
    if a >= i:
        b += (a // i) * j
        a = a % i
print("Roman number:", b)

Enter  any  number :  3878
Roman  Equivalent :   MMMDCCCLXXVIII



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
'''
############ program ##############
a = ['zer0','one','two','three','four','five','six','seven','eight','nine']

num = input("Enter a number:")
word = ''
for i in num:
    word += a[int(i)] + ' '
print("In words:", word)

Enter  any   number :  9247
Nine Two Four Seven


'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                             PACES
				     ACESP
				     CESPA
				     ESPAC

2) What  are  the  indexes  of  SPACE ?  ---> 0  to  4
     What  are  the  indexes  of  PACES ?  ---> 1  to  4 , 0  to  0
     What  are  the  indexes  of  ACESP ?  ---> 2  to  4 , 0  to  1
     What  are  the  indexes  of  CESPA ?  ---> 3  to  4 , 0  to  2
     What  are  the  indexes  of  ESPAC ?  ---> 4  to  4 , 0  to  3

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0  to  i - 1
'''
########### PROGRAM ###########
# Program to print all rotations of a string

s = input("Enter a string: ")

n = len(s)

print("All rotations are:")
for i in range(n):
    rotation = s[i:] + s[:i]   # slice from i to end + start to i
    print(rotation)


Enter any string :  SPACE
Rotations
SPACE
PACES
ACESP
CESPA
ESPAC


'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       		7 * 2 = 14
			  	7 * 3 = 21
				.....
				 7 * 10 = 70
'''
############### PROGRAM ##########
num = int(input("Enter table number: "))

for i in range(1, 11):   # 1 to 10
    print(f"{num} * {i} = {num * i}")


Enter  table  number :  7
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70


'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
           ---------------------
           1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''
############ PROGRAM ##########3
# Program to print alphabet pyramid

n = int(input("How many lines ? : "))

for i in range(1, n+1):
    # print leading spaces
    print(" " * (n - i), end="")

    # print letters from A onwards
    for j in range(i):
        print(chr(65 + j), end=" ")

    print()  # new line


How  many  lines ?  :  7
       A
      A B
     A B C
    A B C D
   A B C D E
  A B C D E F
 A B C D E F G


#Find  outputs (Home  work)
a = 10 # Global  variable
def   f1(): 
	b = 40 # Local  variable
	print('a : ' , a) # a : 10
	print('b : ' , b) # b : 40
	print('c : ' , c) # c : 30
	print()
# End  of  f1()  function
b = 20 # Global  variable
def    f2():
	a = 50 # Local  variable
	print('a : ' , a) # a : 50
	print('b : ' , b) # b : 20
	print('c : ' , c) # c : 30
# End  of  f2()  function
c = 30 # Global  variable
print('a : ' , a) # a : 10
print('b : ' , b) # b : 20
print('c : ' , c) # c : 30
print() # new  line
a +=  1 # increment
b +=  1
c +=  1
f1() # a : 11 b : 40 c : 31
a +=  1
b +=  1
c +=  1
f2() # call
print('Bye') # Bye


# Find  outputs (Home  work)
def   f1():
	a = 20 # Local  variable
	print(a) # 20
	a += 1 # increment
#End  of  the  function
a = 10 # Global  variable
print(a) # 10
a += 1 # increment
f1() # call
print(a) # 11