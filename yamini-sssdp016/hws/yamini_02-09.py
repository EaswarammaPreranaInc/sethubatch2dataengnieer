#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()    # empty tuple is sent to the function
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})    #  ([10,20],(30,40,50),{70,80,90,60})
f1('Hyd') # ('Hyd',)
tpl = (100 , 200 , 150) 
f1(tpl)     #  ((100,200,150),)
f1(t = (10 , 20 , 30)) #error as for variable args we cannot use keyword arguments

'''
(10,20,15,18)
<class 'tuple'>
4
'''

#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)

def  avg(*a):
    try:
	    return  sum(a) / len(a) 
    except :
            print('Give valid  input')
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))


#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    try:
	     return  ' '.join(a)
    except :
            return  'Only  strings  are  allowed'
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) #a : 25  \t   b  :  (10 , 20 , 30 , 40)
f1(50 , 60) #a : 25  \t   b  :  (50 , 60)
f1(70)  #a : 25  \t   b  :  (70,)
f1(a = 80) #a : 80  \t   b  :  ()
f1(b = (10 , 20 , 30) , a = 40) # var arg function  cannot have   keyword  argument
f1()    #a : 25  \t   b  :  ()
f1(a = 10 , (20 , 30 , 40)) #Error: positional argument follows keyword argument
f1(25 , b = (10 , 20 , 30))     #var arg function  cannot have   keyword  argument
f1(25 , a = (10 , 20 , 30)) # a should be single element as there is no * for a in header
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10, 20, 30)           b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # error as positional argument follows keyword argument

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)   # a  :  (10 , 20 , 30 )  \t   b  :  40
f1(50 , b = 60)  # a  :  (50 , )  \t   b  :  60
f1(b = 70) # a  :  ()  \t   b  :  70
f1(b = 10 , a = (20 , 30 , 40)) # error as a should not be keyword argument
f1(b = 10 , (20 , 30 , 40)) # error as positional argument follows keyword argument
f1() # error as b is missing
f1(10 , 20 , 30 , (10 , 20 , 30)) # error as b is missing
f1(10 , 20 , 30 , 40) # error as b is missing
f1(25) # error as b is missing
f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  :  (10 , 20 , 30 )  \t   b  :  (10 , 20 , 30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a:10 b:(20,30,40) c:50
f1(60 , 70 , c = 80)    # a:60 b:(70,) c:80
f1(90 , c = 100)    # a:90 b:() c:100
f1(a = 1 , 2 , c = 3)   # error as positional argument follows keyword argument
f1(1 , 2 , 3) # error as c is missing
f1(a = 1 , b = 2 , c = 3) # error as b is not a keyword argument
f1(a = 25 , 100 , 200 , 300 , c = 35) # a:25 b:(100,200,300) c:35

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
       # pass # error as only one *args is allowed
def  f2(*a , b):
        pass # valid as b is keyword only argument
def  f3(a , *b):
        pass # valid as a is positional argument and b is *args
def  f4(a , b):
        pass # valid as both are positional arguments
def    f5(a , *b , c):
        pass # valid as a is positional, b is *args and c is keyword only argument
def   f6( * , a , *b , c):
       #pass  #error as only one *args is allowed
def   f7(a , *b , c ,  /):
       pass # / must be ahead of *

# Find  outputs  (Home  work)
def   f1(*a):
	print(a) # ([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a)) # <class 'tuple'>
	for  x  in  a:
		print(x) # [10, 20]  {30, 40}  (50, 60)
		print(type(x))  # <class 'list'>  <class 'set'>  <class 'tuple'>
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

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

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
<class  'dict'>
{'EmpNo' : 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}
<class  'dict'>
{'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , 'Gender' : 'm'}
<class  'dict'>
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
Results
Empno... 25
Empname... Rama  Rao
Salary... 10000.0
Gender... m
Results

'''

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a)) # class tuple
	print(a) # (25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a)) # class <dict>
	print(a) # {'EmpNum': 25 , 'EmpName':  'Sita' , 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)

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

'''
Emp  Number  :  25  	  Emp  Name  :  Sita   	  Salary  :	10000.0
error as there are no parameters with these names eno and empname
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
'''

# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)  # 25
print() # prints nothimg goes to next line
f1('Hyd' , 10 , 20 , 30) # Hyd (10, 20, 30)
print() # prints nothimg goes to next line
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) # 10.8 (25, 'Hyd', True) {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5
'''

n = input()
result = int(n[0])  
for i in range(1, len(n), 2):  
    op = n[i]                 
    num = int(n[i+1])          
    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        result = result / num
print(result)

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
    roman = ""

    if num >= 1000:
        q = num // 1000
        roman += "M" * q
        num = num % 1000

    if num >= 900:
        q = num // 900
        roman += "CM" * q
        num = num % 900

    if num >= 500:
        q = num // 500
        roman += "D" * q
        num = num % 500

    if num >= 400:
        q = num // 400
        roman += "CD" * q
        num = num % 400

    if num >= 100:
        q = num // 100
        roman += "C" * q
        num = num % 100

    if num >= 90:
        q = num // 90
        roman += "XC" * q
        num = num % 90

    if num >= 50:
        q = num // 50
        roman += "L" * q
        num = num % 50

    if num >= 40:
        q = num // 40
        roman += "XL" * q
        num = num % 40

    if num >= 10:
        q = num // 10
        roman += "X" * q
        num = num % 10

    if num >= 9:
        q = num // 9
        roman += "IX" * q
        num = num % 9

    if num >= 5:
        q = num // 5
        roman += "V" * q
        num = num % 5

    if num >= 4:
        q = num // 4
        roman += "IV" * q
        num = num % 4

    if num >= 1:
        q = num // 1
        roman += "I" * q
        num = num % 1

    return roman

n=int(input())
# Example
print( int_to_roman(n))

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


n=input()
s=''
a=['zero','one','two','three','four','five','six','seven','eight','nine']
for i in n:
    s+=a[int(i)]+' '
print(s)





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

n=input()
for i in range(len(n)):
    s=''
    s+=n[i:]+n[:i]
    print(s)


'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''
n= int(input())
for i in range(11):
    print(f'{n}*{i}={n*i}')
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

x=int(input())
p=ord('A')
for i in range(x):
    print(' '*(x-i-1),end='')
    s=''
    for j in range(p,p+i+1):
        s+=chr(j)+' '
    print(s)


#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) # a : 10
	print('b : ' , b)   # b: 20
	print('c : ' , c) # c:30
	print() # prints nothing and goes to next line
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) # a : 11
	print('b : ' , b) # b : 40
	print('c : ' , c) # c : 31
	print()
# End  of  f2()  function
c = 30
print('a : ' , a) # a : 50
print('b : ' , b) # b : 22
print('c : ' , c) # c : 32
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye')    # bye

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # prints 20
	a += 1
#End  of  the  function
a = 10
print(a)    # 10
a += 1# a=11
f1() # function call
print(a) # prints 11
