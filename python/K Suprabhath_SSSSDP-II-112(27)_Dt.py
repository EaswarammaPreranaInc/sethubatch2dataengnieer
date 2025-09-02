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
f1(t = (10 , 20 , 30))

'''
(10,20,15,18)
<class 'tuple'>
4
'''
def avg(*a):
    return sum(a) / len(a) if a else 0

print(avg(10, 20, 15, 18))# 15.75
print(avg(25, 10.8, True))# (True = 1) → 12.266...
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))# 14.26
print(avg())# 0
print(avg(25))#25  
print(avg(3 + 4j, 5 + 6j)) # (4+5j)
tpl = (10, 20, 15, 18)
print(avg(*tpl)) # 15.75

#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
   return ''.join(a) if a else ''

print(concat('Sankar', 'Dayal', 'Sarma'))# SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))# HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))# PythonIsAGreatLanguage
print(concat())# ('')
print(concat('Python'))# Python
print(concat(1, 2, 3))# 123
             
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)# a : 10      b  :  (20, 30, 40)
f1(50 , 60)# a : 50      b  :  (60,)
f1(70)# a : 70      b  :  ()
f1(a = 80)# a : 80      b  :  ()
f1(b = (10 , 20 , 30) , a = 40)# a : 40      b  :  ((10, 20, 30),)
f1()# a : 25      b  :  ()
f1(a = 10 , (20 , 30 , 40))# SyntaxError
f1(25 , b = (10 , 20 , 30))# a : 25      b  :  ((10, 20, 30),)
f1(25 , a = (10 , 20 , 30))# TypeError
f1((10 , 20 , 30) , 10 , 20 , 30)# a : (10, 20, 30)       b  :  (10, 20, 30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)# SyntaxError             

#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)# a  :  (10, 20, 30)     b  :  40
f1(50 , b = 60)# a  :  (50,)     b  :  60
f1(b = 70)# a  :  ()     b  :  70
f1(b = 10 , a = (20 , 30 , 40))# SyntaxError
f1(b = 10 , (20 , 30 , 40))# SyntaxError
f1()# TypeError
f1(10 , 20 , 30 , (10 , 20 , 30))# TypeError
f1(10 , 20 , 30 , 40)# TypeError
f1(25)# TypeError
f1(10 , 20 , 30 , b = (10 , 20 , 30))# a  :  (10, 20, 30)     b  :  (10, 20, 30)

#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)# a  :  10   b  :  (20, 30, 40)    c  :  50
f1(60 , 70 , c = 80)# a  :  60   b  :  (70,)    c  :  80
f1(90 , c = 100)# a  :  90   b  :  ()    c  :  100
f1(a = 1 , 2 , c = 3)# SyntaxError
f1(1 , 2 , 3)# TypeError
f1(a = 1 , b = 2 , c = 3)# SyntaxError
f1(a = 25 , 100 , 200 , 300 , c = 35)# SyntaxError   

# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):#  Invalid
        pass
def  f2(*a , b):#  Valid
        pass
def  f3(a , *b):#  Valid
        pass
def  f4(a , b):#  Valid
        pass
def    f5(a , *b , c):#  Valid
        pass
def   f6( * , a , *b , c):#  Invalid
       pass
def   f7(a , *b , c ,  /):#  Invalid
       pass   

# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))# tuple
	for  x  in  a:
		print(x)# elements
		print(type(x))# type of elements
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))# ([10, 20], {40, 30}, (50, 60))
   
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))# dict
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#  Dictionary  is  passed  to  the  function
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#  Dictionary  is  passed  to  the  function
disp()#  Empty  dictionary  is  passed  to  the  function

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
'''

# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')# Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')# key  and  value
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')#  Dictionary  is  passed  to  the  function
f1()# Empty  dictionary  is  passed  to  the  function

# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))# tuple
	print(a)# elements
def   f2(**a):
	print(type(a))# dict
	print(a)# elements
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#  Tuple  is  passed  to  the  function
print()# New  line
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)#  Dictionary  is  passed  to  the  function
   
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')# Emp  Number  :  25    Emp  Name  :  Sita    Salary  :	10000.0
def   f2(**a):
	print(a)# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)# Emp  Number  :  25    Emp  Name  :  Sita    Salary  :	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)# TypeError
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)# {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)# {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}   

# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)# first  positional  argument
	if   b:
		print(b)# tuple  of  remaining  positional  arguments
	if  c:
		print(c)# dictionary  of  keyword  arguments
# End  of  the  function
f1(25)# 25
print()# New  line
f1('Hyd' , 10 , 20 , 30)# Hyd
print()# New  line
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)# 10.8

# Program to evaluate expression like a calculator
expr = "3 + 4 * 5 - 6 / 2 ="
tokens = expr.split()   # ['3', '+', '4', '*', '5', '-', '6', '/', '2', '=']

i = 0
a = float(tokens[i])    # first number

while True:
    op = tokens[i+1]    # operator
    if op == "=":       # stop condition
        break
    b = float(tokens[i+2])  # next number

    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b

    i += 2   # move to next operator

print("Result:", a)

## Program to print Roman equivalent of a number

def int_to_roman(num):
    roman_map = [
        (1000, "M"), (900, "CM"),
        (500, "D"),  (400, "CD"),
        (100, "C"),  (90, "XC"),
        (50, "L"),   (40, "XL"),
        (10, "X"),   (9, "IX"),
        (5, "V"),    (4, "IV"),
        (1, "I")
    ]

    result = ""
    for value, symbol in roman_map:
        count = num // value        # how many times the symbol fits
        result += symbol * count    # concatenate symbol
        num = num % value           # reduce the number
    
    return result

# Example
n = 3878
print("Input:", n)
print("Roman:", int_to_roman(n))

# Program to print each digit of a number in words

a = ['Zero', 'One', 'Two', 'Three', 'Four',
     'Five', 'Six', 'Seven', 'Eight', 'Nine']

num = "9247"   # input as string
s = ""         # result string

print("Iteration   ch   int(ch)   a[int(ch)]   s")
print("--------------------------------------------------------")

for i, ch in enumerate(num, 1):
    digit = int(ch)
    word = a[digit]
    s = s + word + " "
    print(f"{i:<10} {ch:<5} {digit:<10} {word:<12} {s}")

print("\nFinal Output:", s.strip())

# Program to print all rotations of a string

s = "SPACE"
n = len(s)

for i in range(n):
    rotation = s[i:] + s[:i]   # i to end, then 0 to i-1
    print(rotation)

# Program to print multiplication table of a number

num = 7   # you can replace this with int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Program to print alphabet pyramid

n = 5  # you can also take input: int(input("Enter number: "))

for i in range(1, n + 1):
    # spaces for pyramid shape
    print(" " * (n - i), end="")  
    
    # letters from 'A' up to 'A' + i - 1
    for j in range(i):
        print(chr(ord('A') + j), end=" ")
    
    print()  # new line

#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)# 10
	print('b : ' , b)# 40
	print('c : ' , c)# 30
	print()# New  line
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)# 50
	print('b : ' , b)# 20
	print('c : ' , c)# 30
# End  of  f2()  function
c = 30
print('a : ' , a)# 10
print('b : ' , b)# 20
print('c : ' , c)# 30
print()# New  line
a +=  1
b +=  1
c +=  1
f1()#  a :  10
a +=  1
b +=  1
c +=  1
f2()#  a :  50
print('Bye')# Bye

# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)# 20
	a += 1
#End  of  the  function
a = 10
print(a)# 10
a += 1
f1()# 20
print(a)# 11

