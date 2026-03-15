#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)                                                                 (10,20,15,18)
                                                                                      <class 'tuple'>
                                                                                      4
f1()                                                                                  ()
                                                                                      <class 'tuple'>
                                                                                      0
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})                                  ([10,20],(30,40,50),{80,90,60,70})
                                                                                      <class 'tuple'>
                                                                                      3
f1('Hyd')                                                                             ('Hyd',)
                                                                                      <class 'tuple'>
                                                                                      1
tpl = (100 , 200 , 150)                                                               ((100,200,150),)
                                                                                      <class 'tuple'>
                                                                                       1
f1(tpl)
f1(t = (10 , 20 , 30))                                                                Error

#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)                   return sum(a) / len(a) if a else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18))                                                                                          15.75
print(avg(25 , 10.8 , True))                                                                                           12.933
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))                                                                            14.26
print(avg())                                                                                                           0
print(avg(25))                                                                                                         25.0
print(avg(3 + 4j , 5 + 6j))                                                                                            (4+5j)
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))                                                                                                        15.75

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)                  return ''.join(map(str, a))
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))                                                                             SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))                                                                           HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))                                                               PythonIsAGreatLanguage
print(concat())                                                                                                       ''
print(concat('Python'))                                                                                               Python
print(concat(1, 2, 3))                                                                                                123

#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)                                      a:10 b:(20,30,40)
f1(50 , 60)                                                a:50 b:(60,)
f1(70)                                                     a:70 b:()
f1(a = 80)                                                 a:80 b:()
f1(b = (10 , 20 , 30) , a = 40)                            Error
f1()                                                       a:25 b:()
f1(a = 10 , (20 , 30 , 40))                                Error
f1(25 , b = (10 , 20 , 30))                                Error
f1(25 , a = (10 , 20 , 30))                                Error
f1((10 , 20 , 30) , 10 , 20 , 30)                          a:(10,20,30) b:(10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)                      Error

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)                                a:(10,20,30) b:40
f1(50 , b = 60)                                          a:(50,) b:60
f1(b = 70)                                               a:() b:70
f1(b = 10 , a = (20 , 30 , 40))                          Error
f1(b = 10 , (20 , 30 , 40))                              Error
f1()                                                     Error
f1(10 , 20 , 30 , (10 , 20 , 30))                        Error
f1(10 , 20 , 30 , 40)                                    Error
f1(25)                                                   Error
f1(10 , 20 , 30 , b = (10 , 20 , 30))                    a:(10,20,30) b:(10,20,30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)                                  a:10 b:(20,30,40) c:50
f1(60 , 70 , c = 80)                                            a:60 b:(70,) c:80
f1(90 , c = 100)                                                a:90 b:() c:100
f1(a = 1 , 2 , c = 3)                                           Error
f1(1 , 2 , 3)                                                   Error
f1(a = 1 , b = 2 , c = 3)                                       Error
f1(a = 25 , 100 , 200 , 300 , c = 35)                           Error

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass
def  f2(*a , b):
        pass
def  f3(a , *b):
        pass
def  f4(a , b):
        pass
def    f5(a , *b , c):
        pass
def   f6( * , a , *b , c):
       pass
def   f7(a , *b , c ,  /):
       pass

valid:f2,f3,f4,f5
Invalid:f1,f6,f7

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)                                     ([10,20],{40,30},(50,60))
	print(type(a))                               <class 'tuple'>
	for  x  in  a:
		print(x)                                  [10,20]
		print(type(x))                            <class 'list'>
# End  of  the  function                      {30,40}
                                              <class 'set'>
                                              (50,60)
                                              <class 'tuple'>
f1([10 , 20] , {30 , 40} , (50 , 60))

# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama  Rao'}

disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

disp()
Results
<class 'dict'>
{}

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')        Results
                                                                                Empno ... 25
                                                                                Empname ... Rama  Rao
                                                                                Salary ... 10000.0
                                                                                Gender ... m
f1()                                                                            Results

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)                                             <class 'tuple'>
                                                                         (25, 10.8, 'Hyd', True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)                   <class 'dict'>
                                                                         {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)                                Emp Number:25 Emp Name:Sita Salary:10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)                             Error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)                                {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)                             {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}

# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)                                                                                         25
print()
f1('Hyd' , 10 , 20 , 30)                                                                       Hyd
                                                                                               (10,20,30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)           10.8
                                                                                               (25, 'Hyd', True)
                                                                                               {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}

Write  a  program  to  evaluate  expression  like  calculator
expr = input("Enter expression (end with '='): ")
for op in "+-*/=":
    expr = expr.replace(op, f" {op} ")
tokens = expr.split()
i = 0
a = float(tokens[i])   
i += 1
while i < len(tokens) - 1:   
    op = tokens[i]       
    b = float(tokens[i+1])   
    if op == '+':
        a = a + b
    elif op == '-':
        a = a - b
    elif op == '*':
        a = a * b
    elif op == '/':
        a = a / b
    i += 2   
print("Result =", a)

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
num=int(input("Enter a number:"))
roman=""
val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
s = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
for i in range(len(val)):
    count = num // val[i]       
    roman += s[i] * count    
    num = num % val[i]
print(roman)

Write  a  program  to  print  each  digit  of  the  number  in  words
n=input("Enter a number:")
a=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
s=''
for ch in n:
    s=s+a[int(ch)]+' '
print(s)

Write  a  program  to  print  all  the  rotations  of  the  string
word=input("Enter a String:")
n=len(word)
for i in range(n):
    rotate=word[i:]+word[:i]
    print(rotate)

Write  a  program  to  print  mathematical  table  of  a  number
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')

Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
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
print('a : ' , a)                   a:10
print('b : ' , b)                   b:20
print('c : ' , c)                   c:30
print()
a +=  1
b +=  1
c +=  1
f1()                               a:11
                                   b:40
                                   c:31
a +=  1
b +=  1
c +=  1
f2()                               a:50
                                   b:22
                                   c:32
print('Bye')                       Bye


# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a)                        10
a += 1
f1()                            20
print(a)                        11
