#  Variable  number  of  arguments  demo  program
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
f1(t = (10 , 20 , 30)) # Error because there no argument t

'''
(10,20,15,18)
<class 'tuple'>
4

()
<class 'tuple'>
0

[10, 20], (30, 40, 50), {60, 70, 80, 90})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1
 
((100, 200, 150),)
<class 'tuple'>
1
'''









#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	return sum(a)/len(a)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) # prints 15.75
print(avg(25 , 10.8 , True)) # 12.266666666666666
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 14.26
print(avg()) # Error because of division by zero ,it needs atleast one argument
print(avg(25)) # prints 25.0
print(avg(3 + 4j , 5 + 6j)) # prints (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl)) # Error because tuple elements cannot be added









#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	return ' '.join(a)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) # prints Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # prints Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # prints Python Is A Great Language
print(concat()) # prints nothing
print(concat('Python')) # prints Python
print(concat(1, 2, 3)) # Error because integers cannot be concatenated
			 








#Find  outputs (Home  work)
def   f1(a = 25  , *b):
    print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # prints a : 10<tab>b : (20, 30, 40)
f1(50 , 60) # prints a : 50<tab>b : (60,)
f1(70) # prints a : 70<tab>b : ()
f1(a = 80) # prints a : 80<tab>b : ()
f1(b = (10 , 20 , 30) , a = 40) # Error because b should be positional argument only
f1() # prints a : 25<tab>b : ()
f1(a = 10 , (20 , 30 , 40)) # Error because positional argument cannot be passed after keyword argument
f1(25 , b = (10 , 20 , 30)) # Error because b should be positional argument only
f1(25 , a = (10 , 20 , 30)) # Error because 'a' requires only one arguments but three are given
f1((10 , 20 , 30) , 10 , 20 , 30) # prints a : (10, 20, 30)<tab>b : (10, 20, 30)
f1(a = (10 , 20 , 30), 10, 20, 30) # Error because positional argument cannot be passed after keyword arguments
   








#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # prints a : (10, 20, 30)<tab>b : 40
f1(50 , b = 60) # prints a : (50,)<tab>b : 60
f1(b = 70) # prints a : ()<tab>b : 70
f1(b = 10 , a = (20 , 30 , 40)) # Error because 'a' should be positional argument only
f1(b = 10 , (20 , 30 , 40)) # Error because positional argument cannot be passed after keyword argument
f1() # Error because requires atleast one argument for b
f1(10 , 20 , 30 , (10 , 20 , 30)) # Error because it requires one keyword only argument
f1(10 , 20 , 30 , 40) # Error because it requires one keyword only argument
f1(25) # # Error because it requires one keyword only argument
f1(10 , 20 , 30 , b =(10, 20, 30)) # prints a: (10, 20, 30)<tab>b : (10, 20, 30)
   








#Find  outputs (Home  work)
def   f1(a , *b , c):
    print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # prints a : 10<tab>b : (20, 30, 40)<tab>c : 50
f1(60 , 70 , c = 80) # prints a : 60<tab>b : (70,)<tab>c : 80
f1(90 , c = 100) # prints a : 90<tab>b : ()<tab>c : 100
f1(a = 1 , 2 , c = 3) # Error because positional argument cannot be passed after keyword argument
f1(1 , 2 , 3) # Error becuase c should be keyword only argument
f1(a = 1 , b = 2 , c = 3) # Error because b should be positional only argument
f1(a = 25 , 100 , 200, 300, c = 35) # Error because positional argument cannot be passde after keyword argument
   








# Which  of  the  following  are  valid  ?  (Home  work)
def f1(*a , *b): # Invalid because only one * can be passed
    #pass
def f2(*a , b): # Valid
    pass
def f3(a , *b): # Valid
    pass
def f4(a , b): # Valid
    pass
def f5(a , *b , c): # Valid
    pass
def f6( * , a , *b , c): # Invalid because only one * can be passed
    #pass
def f7(a , *b , c , /): # Invalid because / should be before *
    #pass 








# Find  outputs  (Home  work)
def f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
Outputs:
([10 , 20] , {30 , 40} , (50 , 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{30, 40}
<class 'set'>
(50, 60)
<class 'tuple'>
'''
   








# Variable  number  of  keyword  arguments  demo  program
def disp(**a):
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
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}

Results
<class 'dict'>
{EmpNo : 25, EmpName : 'Sita', Salary : 10000.0}

Results
<class 'dict'>
{AcNo : 30, CustName : 'Kiran', Balance : 20000.0, Gender : 'm'}

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
'''
Outputs

Results
EmpNo...25
EmpName...Rama Rao
Salary...10000.0
Gender...m
Results
'''









# Find  outputs (Home  work)
def f1(*a):
	print(type(a))
	print(a)
def f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
'''
Outputs

<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum' : 25 , 'EmpName' :  'Sita' , 'Salary' : 10000.0}
'''   









#  Find  outputs (Home work)
def  f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def  f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # prints Emp Number : 25, Emp Name : 'Sita', Salary : 10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error because arguments names must be same
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # prints {empno : 25 , ename : 'Sita' , sal : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # prints {eno = 25 , empname = 'Sita' , salary = 10000.0}









# Find  outputs   (Home  work)
def f1(a ,  *b , **c):
	print(a)
	if b:
	    print(b)
	if c:
		print(c)
# End  of  the  function
f1(25) 
print() 
f1('Hyd' , 10 , 20 , 30) 
print() 
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
'''
Outputs:

25

Hyd
(10, 20, 30)

10.8
(25, Hyd, True)
{EmpNo : 12 , EmpName : 'Rama  Rao' , Salary : 10000.0}
'''
   








#Find  outputs (Home  work)
a = 10
def f1():
	b = 40
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def f2():
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

'''
Outputs

a : 10
b : 20
c : 30

a : 11
b : 40
c : 31

a : 50
b : 22
c : 32
'''









# Find  outputs (Home  work)
def f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)
a += 1
f1()
print(a)
'''
Outputs 

10
20
11
'''









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

	   5            14.5       =          ---           ----
Enter  any  expression  terminated  by  =  :  3+4*5-6/2=
Result : 14.5
'''
s = input("Enter any expression:")
a = eval(s[0])
op = s[1]
i = 2
while op != '=':
	b = eval(s[i])
	i += 1
	match op:
		case '+': a += b
		case '-': a -= b
		case '*': a *= b
		case '/': a /= b
	op = s[i]
	i += 1
print('Result :', a)









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
     and so on
Enter  any  number :  3878
Roman  Equivalent :   MMMDCCCLXXVIII
'''
n = int(input("Enter any number:"))
a = {1000 : 'M' , 900 : 'CM' , 500 : 'D' , 400 : 'CD' , 100 : 'C' , 90 : 'XC' , 50 : 'L' , 40 : 'XL' , 10 : 'X' , 9 : 'IX', 5 : 'V' , 4 : 'IV' , 1 : 'I'}
b = ''
for i in a.keys():
	cnt = n // i
	b += a[i] * cnt
	n %= i
print('Roman Equivalent:', b)









'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1        '9'       9               'Nine'          '' + 'Nine' + ' '

	 2        '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3        '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4         '7'       7               'Seven'        'Nine Two Four ' + 'Seven' + ' '
Enter  any   number :  9247
Nine Two Four Seven
'''
a = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n = input("Enter any integer:")
b = ''
for i in n:
	b += a[int(i)] + ' '
print(b)









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

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0  to  i - 1
Enter any string :  SPACE
Rotations
SPACE
PACES
ACESP
CESPA
ESPAC
'''
a = input("Enter any string:")
print("Rotations")
for i in range(len(a)):
	print(a[i:] + a[:i]) 
 









'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 1 = 70
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
n = int(input("Enter any number:"))
for i in range(1, 11):
	print(F'{n} * {i} = {n*i}')









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

	   5         'A' to 'E'
How  many  lines ?  :  7
       A
      A B
     A B C
    A B C D
   A B C D E
  A B C D E F
 A B C D E F G
'''
n = int(input("Enter number of lines:"))
s = n
for i in range(1, n+1):
	print(' ' * s, end = '')
	s = -1
	for j in range(i):
		print(chr(65+j), end = ' ')
	print()