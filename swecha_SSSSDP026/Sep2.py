 Variable  number  of  arguments  demo  program
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
 
 output:
(10,20,15,18)
<class 'tuple'>
4
()
<class 'tuple'>
0
([10 , 20], (30 , 40 , 50), {80 , 70 , 60 , 90})
<class tuple>
3
('Hyd',)
<class 'tuple'>
1
((100 , 200 , 150),)
<class 'tuple'>
1
error

 Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
# 	# Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

outputs:
def avg(*a):
    return sum(a[0]) / len(a[0])
15.75
12.26
14.26
0
25
4+5j
15.75


 Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

output:
def concat(*a):
    return ''.join(map(str , a))
SankarDayalSarma
HydIsGreenCity
PythonIsAGreatLanguage
''
Python
123

Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10  b : (20 , 30 , 40)
f1(50 , 60)#  a : 50  b :(60,)
f1(70)# a : 70  b : ()
f1(a = 80)# a : 80  b : ()
f1(b = (10 , 20 , 30) , a = 40)# Error
f1()# a : 25  b : ()
# f1(a = 10 , (20 , 30 , 40))# error
f1(25 , b = (10 , 20 , 30))# error
f1(25 , a = (10 , 20 , 30))# error
f1((10 , 20 , 30) , 10 , 20 , 30)# a : (10 , 20 , 30)  b : (10 , 20 , 30)
# f1(a = (10 , 20 , 30) , 10 , 20 , 30)# error

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)# a : (10 , 20 , 30)  b : 40
f1(50 , b = 60)# a : (50,)  b : 60
f1(b = 70)# a :() b : 70
f1(b = 10 , a = (20 , 30 , 40))# a : error b : 10
f1(b = 10 , (20 , 30 , 40))#  a : error b : 10
f1()# error
f1(10 , 20 , 30 , (10 , 20 , 30))#Error
f1(10 , 20 , 30 , 40)# error
f1(25)# a : (25,)  b : error
f1(10 , 20 , 30 , b = (10 , 20 , 30))# a  : (10 , 20 , 30)  b : (10 , 20 , 30)

Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)# a : 10  b : (20 , 30 , 40) c : 50
f1(60 , 70 , c = 80)# a : 60  b : (70,)  c : 80
f1(90 , c = 100)# a : 90  b : () c : 100
f1(a = 1 , 2 , c = 3)# error
f1(1 , 2 , 3)# error
f1(a = 1 , b = 2 , c = 3)#error
f1(a = 25 , 100 , 200 , 300 , c = 35)#error


Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):# error
        pass
def  f2(*a , b):# valid
        pass
def  f3(a , *b):# valid
        pass
def  f4(a , b):# valid
        pass
def    f5(a , *b , c):# valid
        pass
def   f6( * , a , *b , c):#error
       pass
def   f7(a , *b , c ,  /):# error
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
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

Results:
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
<class 'dict'>
{'Empno' : 25 , EmpName : 'Sita' , 'Salary' : 10000.0}
<class 'dict'>
{'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , Gender : 'm'}
,class 'dict'>
{}



# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1()

output:
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m


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
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

outputs:
<class 'tuple'>
(25 , 10.8 . 'Hyd' , True)
<class 'dict'>
{'EmpNum' : 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)

outputs:
Emp Number : 25 Emp Name : 'Sita'  Salary : 10000.0
{'empno' : 25 , 'ename' : 'Sita' , Salary : 10000.0}
error
{'eno : 25 , 'empname' : 'Sita' , 'Salary' : 10000.0}
Emp Number : 25 Emp Name : 'Sita'  Salary  : 10000.0
{empno : 25 , 'ename' : 'Sita' , Salary : 10000.0}
error
{'eno' : 25 , 'empname' : 'Sita' , 'Salary' : 10000.0}

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

outputs:
25

Hyd
(10 , 20 , 30)

10.8
(25 , 'Hyd' , True)
{'EmpNo' : 12 , EmpName : 'Rama Rao' , 'Salary' : 10000.0}

Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)# 10
	print('b : ' , b)#20
	print('c : ' , c)#30
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)#11
	print('b : ' , b)#40
	print('c : ' , c)#31
# End  of  f2()  function
c = 30
print('a : ' , a)#50
print('b : ' , b)#22
print('c : ' , c)#32
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')#Bye

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

output : 
10
20
11

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

n=int(input("enter how many lines:"))
for i in range(1 , n + 1):
    print(' ' * (n - i) , end=" ")
    for ch in range(65 , 65 + i):
        print(chr(ch) , end=" ")
    print()    

	output: enter how many lines:5
     A 
    A B 
   A B C 
  A B C D 
 A B C D E    

'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''

n = int(input("enter which table you want:"))
for i in range(1 , 11):
    print(F'{n} * {i} = {n * i}')
    
	output:enter which table you want:7
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

a = input("enter a string:")
n = len(a)
for i in range(n):
    print(a[i:] + a[:i])
    print("rotation")
    
	output:enter a string:SPACE
SPACE
rotation
PACES
rotation
ACESP
rotation
CESPA
rotation
ESPAC
rotation

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
Enter  any   number :  9247
Nine Two Four Seven

a = ['Zero' , 'One' , 'Two' , 'Three' , 'Four' , 'Five' ,'six' , 'Seven' , 'Eight' , 'Nine']
n = 9247
s = ''
for ch in str(n):
    s += a[int(ch)] + ' '
print(s.strip())

output: Nine Two Four Seven

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
expr = "3 + 4 * 5 - 6 / 2 =".split()

i = 0
a = float(expr[i])   
i += 1

while True:
    op = expr[i]     
    if op == "=":
        break
    i += 1
    b = float(expr[i]) 
    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b

    i += 1

print("Result:", a)

 output:Result: 14.5


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

def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M",  "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    for i in range(len(val)):
        count = num // val[i]          
        roman += syb[i] * count        
        num = num % val[i]             
    return roman
print(int_to_roman(3878))  

output:
MMMDCCCLXXVIII
