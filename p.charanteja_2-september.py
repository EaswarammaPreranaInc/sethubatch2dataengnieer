#  Variable  number  of  arguments  demo  program

def f1(*t):
    print(t)
    print(type(t))
    print(len(t))
    print()
# End  of  the  function
f1(10, 20, 15, 18)  # Tuple of 4 elements
f1()
f1([10, 20], (30, 40, 50), {60, 70, 80, 90})
f1('Hyd')
tpl = (100, 200, 150)
f1(tpl)
f1(t=(10, 20, 30))  # This will put the named argument in a tuple with empty *t

output:
(10, 20, 15, 18)
<class 'tuple'>
4

()
<class 'tuple'>
0

([10, 20], (30, 40, 50), {80, 90, 70, 60})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100, 200, 150),)
<class 'tuple'>
1

()
<class 'tuple'>
0









#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  
def avg(*a):
    return sum(a)/len(a) if a else None  # Returns None for no args
print(avg(10, 20, 15, 18))                   # 15.75
print(avg(25, 10.8, True))                   # 12.933... (True is 1)
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))      # 14.26
print(avg())                                 # None
print(avg(25))                               # 25.0
print(avg(3+4j, 5+6j))                       # (4+5j)
tpl = (10, 20, 15, 18)
print(avg(*tpl))                             # 15.75
output:
15.75
12.933333333333334
14.26
None
25.0
(4+5j)
15.75






#  Write  a  function  to  concatenate  strings  passed  to  the  function  
def concat(*a):
    return ''.join(str(x) for x in a)
print(concat('Sankar', 'Dayal', 'Sarma'))           # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))         # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # PythonIsAGreatLanguage
print(concat())                                     # ''
print(concat('Python'))                             # Python
print(concat(1, 2, 3))                              # '123'

output:
SankarDayalSarma
HydIsGreenCity
PythonIsAGreatLanguage

Python
123








#Find  outputs 
def f1(a=25, *b):
    print(f'a : {a} \t   b  :  {b}')
f1(10, 20, 30, 40)                  # a=10, b=(20,30,40)
f1(50, 60)                          # a=50, b=(60,)
f1(70)                              # a=70, b=()
f1(a=80)                            # a=80, b=()
f1(b=(10, 20, 30), a=40)            # a=40, b=( (10, 20, 30), )
f1()                                # a=25, b=()
# f1(a=10, (20, 30, 40))  # SyntaxError: positional argument follows keyword argument
# f1(25, b=(10, 20, 30))  # TypeError: got multiple values for argument 'b'
# f1(25, a=(10, 20, 30))  # TypeError: got multiple values for argument 'a'
f1((10, 20, 30), 10, 20, 30)        # a=(10,20,30), b=(10,20,30)
# f1(a=(10, 20, 30), 10, 20, 30)    # SyntaxError: positional argument follows keyword argument

output:
a : 10 	   b  :  (20, 30, 40)
a : 50 	   b  :  (60,)
a : 70 	   b  :  ()
a : 80 	   b  :  ()
a : 40 	   b  :  ((10, 20, 30),)
a : 25 	   b  :  ()
a : (10, 20, 30) 	   b  :  (10, 20, 30)








#Find  outputs 
def f1(*a, b):
    print(f'a  :  {a}   \t   b  :  {b}')
f1(10, 20, 30, b=40)            # a=(10,20,30); b=40
f1(50, b=60)                    # a=(50,); b=60
f1(b=70)                        # a=(); b=70
# f1(b=10, a=(20, 30, 40))     # TypeError: f1() got an unexpected keyword argument 'a'
# f1(b=10, (20, 30, 40))      # SyntaxError
f1()                            # TypeError: missing required keyword argument 'b'
f1(10, 20, 30, (10, 20, 30))   # TypeError: missing required keyword argument 'b'
f1(10, 20, 30, 40)              # TypeError: missing required keyword argument 'b'
f1(25)                          # TypeError: missing required keyword argument 'b'
f1(10, 20, 30, b=(10, 20, 30)) # a=(10,20,30), b=(10,20,30)

output:
a  :  (10, 20, 30)   	   b  :  40
a  :  (50,)   	   b  :  60
a  :  ()   	   b  :  70
a  :  (10, 20, 30)   	   b  :  (10, 20, 30)







#Find outputs
def f1(a, *b, c):
    print(f'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
f1(10, 20, 30, 40, c=50)      # a=10, b=(20,30,40), c=50
f1(60, 70, c=80)              # a=60, b=(70,), c=80
f1(90, c=100)                 # a=90, b=(), c=100
# f1(a=1, 2, c=3)             # SyntaxError
f1(1, 2, 3, c=4)              # a=1, b=(2,3), c=4
# f1(1, 2, 3)                 # TypeError: missing required argument 'c'
# f1(a=1, b=2, c=3)           # TypeError: unexpected keyword arguments
f1(25, 100, 200, 300, c=35)   # a=25, b=(100,200,300), c=35

output:
a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
a  :  60  	  b  :  (70,)  	  c  :  80
a  :  90  	  b  :  ()  	  c  :  100
a  :  1  	  b  :  (2, 3)  	  c  :  4
a  :  25  	  b  :  (100, 200, 300)  	  c  :  35








# Which  of  the  following  are  valid  ?

# def f1(*a, *b): pass # invalid - multiple *args not allowed
def f2(*a, b): pass     # valid
def f3(a, *b): pass     # valid
def f4(a, b): pass      # valid
def f5(a, *b, c): pass  # valid
# def f6(*, a, *b, c): pass # invalid syntax, multiple *args not allowed
# def f7(a, *b, c, /): pass # invalid syntax, *args cannot follow /

Valid: f2, f3, f4, f5







#Find outputs
def f1(*a):
    print(a)
    print(type(a))
    for x in a:
        print(x)
        print(type(x))
f1([10, 20], {30, 40}, (50, 60))

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

def disp(**a):
    print('Results')
    print(type(a))
    print(a)
    print()
disp(RollNo=10, StudName='Rama Rao')
disp(EmpNo=25, EmpName='Sita', Salary=10000.0)
disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')
disp()

output:
Results
<class 'dict'>
{'RollNo': 10, 'StudName': 'Rama Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}







# Find  outputs  
def f1(**a):
    print('Results')
    for k, v in a.items():
        print(k, v, sep=' ... ')
f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m')
f1()

output:
Results
Empno ... 25
Empname ... Rama Rao
Salary ... 10000.0
Gender ... m
Results






# Find  outputs 
def f1(*a):
    print(type(a))
    print(a)
def f2(**a):
    print(type(a))
    print(a)
f1(25, 10.8, 'Hyd', True)
print()
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)

output:
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}







#Find outputs
def f1(empno, ename, sal):
    print(f'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def f2(**a):
    print(a)
f1(empno=25, ename='Sita', sal=10000.0)
# f1(eno=25, empname='Sita', salary=10000.0)        # TypeError: unexpected keyword arguments
f2(empno=25, ename='Sita', sal=10000.0)
f2(eno=25, empname='Sita', salary=10000.0)

output:
Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0
{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}







#Find outputs
def f1(a, *b, **c):
    print(a)
    if b:
        print(b)
    if c:
        print(c)
f1(25)
print()
f1('Hyd', 10, 20, 30)
print()
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)

output:
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}







#Expression Evaluation Calculator

expr = input("Enter any expression terminated by = : ")
expr = expr[:-1]  # Remove '='
print("Result :", eval(expr))

output:
Result : 14.5








#Roman Equivalent Program
def to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res = ''
    for i in range(len(val)):
        count = num // val[i]
        res += syms[i] * count
        num %= val[i]
    return res

print(to_roman(3878))  # MMMDCCCLXXVIII

output:
MMMDCCCLXXVIII





#Print Digits in Words
def digits_in_words(n):
    a = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    s = ''
    for ch in str(n):
        s += a[int(ch)] + ' '
    return s.strip()
print(digits_in_words(9247))  # Nine Two Four Seven

output:
Nine Two Four Seven









#String Rotations
def rotations(s):
    print("Rotations")
    for i in range(len(s)):
        print(s[i:] + s[:i])
rotations('SPACE')

output:
Rotations
SPACE
PACES
ACESP
CESPA
ESPAC







#Print Mathematical Table
num = 7
for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")


output:
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







#Alphabet Pyramid
n = 7
for i in range(1, n+1):
    print(' '*(n-i), end='')
    for j in range(i):
        print(chr(65+j), end=' ')
    print()


output:
      A
     A B
    A B C
   A B C D
  A B C D E
 A B C D E F
A B C D E F G






#Global and Local Variables Output
a = 10
def f1():
    b = 40
    print('a :', a)
    print('b :', b)
    print('c :', c)
    print()
b = 20
def f2():
    a = 50
    print('a :', a)
    print('b :', b)
    print('c :', c)
c = 30
print('a :', a)
print('b :', b)
print('c :', c)
print()
a += 1
b += 1
c += 1
f1()
a += 1
b += 1
c += 1
f2()
print('Bye')


output:
a : 10
b : 20
c : 30

a : 11
b : 21
c : 31

a : 50
b : 22
c : 32
Bye






#Local Variable Function Output
def f1():
    a = 20
    print(a)
    a += 1
a = 10
print(a)
a += 1
f1()
print(a)

output:
10
20
11
