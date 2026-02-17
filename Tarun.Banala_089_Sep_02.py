# Tarun Banala. 02-09-2025
# Variable number of arguments demo program
def f1(*t):
    print(t)  # prints the tuple of arguments
    print(type(t))  # prints the type, which is <class 'tuple'>
    print(len(t))  # prints the number of arguments
    print()

f1(10, 20, 15, 18)  # Tuple of 4 elements (or) args are passed to the function
f1()  # No arguments passed, so output is an empty tuple ()
f1([10, 20], (30, 40, 50), {60, 70, 80, 90})  # Passes a list, tuple, and set as arguments
f1('Hyd')  # Single string argument
tpl = (100, 200, 150)
f1(tpl)  # A tuple is passed as a single argument
f1(t=(10, 20, 30))  # Using keyword argument to pass a tuple

# Write a function to determine average of arguments passed to the function (Homework)
def avg(*a):
    return sum(a) / len(a) if a else 0  # Returns the average, or 0 if no arguments are passed

# Testing the avg function
print(avg(10, 20, 15, 18))  # 15.75
print(avg(25, 10.8, True))  # 36.8 (True is converted to 1)
print(avg(10.8, 20.6, 15.2, 14.9, 9.8))  # 14.46
print(avg())  # 0
print(avg(25))  # 25
print(avg(3 + 4j, 5 + 6j))  # Complex numbers, returns complex average
tpl = (10, 20, 15, 18)
print(avg(*tpl))  # Unpacks the tuple into the function

# Write a function to concatenate strings passed to the function (Homework)
def concat(*a):
    return ' '.join(a)  # Joins all arguments with a space in between

# Testing the concat function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))  # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language'))  # Python Is A Great Language
print(concat())  # Empty string
print(concat('Python'))  # Python
print(concat(1, 2, 3))  # 1 2 3 (non-string arguments will be converted to string)

# f1 with default argument
def f1(a=25, *b):
    print(f'a : {a}  \t   b  :  {b} ')  # Prints the default value of 'a' and all arguments passed as 'b'

f1(10, 20, 30, 40)  # a=10, b=(20, 30, 40)
f1(50, 60)  # a=50, b=(60,)
f1(70)  # a=70, b=()
f1(a=80)  # a=80, b=()
f1(b=(10, 20, 30), a=40)  # a=40, b=((10, 20, 30),)
f1()  # Default a=25, b=()
f1(a=10, *(20, 30, 40))  # Invalid; unpacking tuple should happen with *b (not *args)
f1(25, b=(10, 20, 30))  # a=25, b=((10, 20, 30),)
f1(25, a=(10, 20, 30))  # Invalid; tuple passed for 'a'
f1((10, 20, 30), 10, 20, 30)  # Invalid; 'a' is a tuple, so it breaks the function call
f1(a=(10, 20, 30), 10, 20, 30)  # Invalid; tuple passed for 'a' breaks the function

# f1 with *a and **b
def f1(*a, b):
    print(f'a : {a}   \t   b : {b}')  # Prints tuple a and b separately

f1(10, 20, 30, b=40)  # a=(10, 20, 30), b=40
f1(50, b=60)  # a=(50,), b=60
f1(b=70)  # a=(), b=70
f1(b=10, a=(20, 30, 40))  # Invalid; unpacking happens incorrectly
f1(b=10, (20, 30, 40))  # Invalid; tuple passed where there should be a valid argument for 'a'
f1()  # Invalid; missing required argument 'b'
f1(10, 20, 30, (10, 20, 30))  # a=(10, 20, 30), b=(10, 20, 30)
f1(10, 20, 30, 40)  # a=(10, 20, 30, 40), b is missing
f1(25)  # a=(25,), b is missing
f1(10, 20, 30, b=(10, 20, 30))  # a=(10, 20, 30), b=(10, 20, 30)

# f1 with *a, **b and c
def f1(a, *b, c):
    print(f'a : {a}  \t  b : {b}  \t  c : {c}')  # Prints a, b, c

f1(10, 20, 30, 40, c=50)  # a=10, b=(20, 30, 40), c=50
f1(60, 70, c=80)  # a=60, b=(70,), c=80
f1(90, c=100)  # a=90, b=(), c=100
f1(a=1, 2, c=3)  # Invalid; arguments should match order
f1(1, 2, 3)  # a=1, b=(2,), c=3
f1(a=1, b=2, c=3)  # a=1, b=2, c=3
f1(a=25, 100, 200, 300, c=35)  # Invalid; order of arguments is incorrect

# Which of the following are valid? (Homework)
def f1(*a, *b):  # Invalid; *a and *b cannot be used together
    pass
def f2(*a, b):  # Valid; *a and single keyword argument b are allowed
    pass
def f3(a, *b):  # Valid; normal arguments followed by *b are allowed
    pass
def f4(a, b):  # Valid; normal arguments
    pass
def f5(a, *b, c):  # Valid; *b and keyword argument c are allowed
    pass
def f6(*, a, *b, c):  # Invalid; *b cannot follow keyword-only arguments
    pass
def f7(a, *b, c, /):  # Valid; '/' means c must be a positional-only argument
    pass

# f1 with *a to check type of arguments
def f1(*a):
    print(type(a))  # <class 'tuple'>
    print(a)  # Tuple of all passed arguments
    for x in a:
        print(x)  # Prints each argument
        print(type(x))  # Prints the type of each argument

f1([10, 20], {30, 40}, (50, 60))  # Passes list, set, and tuple as arguments

# Variable number of keyword arguments demo program
def disp(**a):
    print('Results')
    print(type(a))  # <class 'dict'>
    print(a)  # Prints the dictionary of keyword arguments
    print()

disp(RollNo=10, StudName='Rama Rao')  # Passes a dictionary with key-value pairs
disp(EmpNo=25, EmpName='Sita', Salary=10000.0)  # Another example with different keys
disp(AcNo=30, CustName='Kiran', Balance=20000.0, Gender='m')  # More keyword arguments
disp()  # Empty dictionary

# f1 with keyword arguments
def f1(**a):
    print('Results')
    for k, v in a.items():
        print(k, v, sep=' ... ')  # Prints each key-value pair in the format 'key ... value'

f1(Empno=25, Empname='Rama Rao', Salary=10000.0, Gender='m')  # Prints all key-value pairs
f1()  # Empty output

# f1 and f2 with different argument types
def f1(*a):
    print(type(a))  # <class 'tuple'>
    print(a)  # Prints tuple of arguments
def f2(**a):
    print(type(a))  # <class 'dict'>
    print(a)  # Prints dictionary of keyword arguments

f1(25, 10.8, 'Hyd', True)  # Prints tuple of different types of arguments
print()
f2(EmpNum=25, EmpName='Sita', Salary=10000.0)  # Prints dictionary of keyword arguments

# f1 with arguments, f2 with keyword arguments
def f1(empno, ename, sal):
    print(f'Emp Number: {empno}  \t  Emp Name: {ename}  \t  Salary: {sal}')
def f2(**a):
    print(a)  # Prints keyword arguments

f1(empno=25, ename='Sita', sal=10000.0)  # Valid, prints employee details
f1(eno=25, empname='Sita', salary=10000.0)  # Invalid; 'eno' should be 'empno'
f2(empno=25, ename='Sita', sal=10000.0)  # Valid, prints dictionary of keyword arguments
f2(eno=25, empname='Sita', salary=10000.0)  # Invalid; incorrect keys

# f1 with a, *b, and **c
def f1(a, *b, **c):
    print(a)  # Prints the argument 'a'
    if b:  # If there are any elements in 'b'
        print(b)  # Prints tuple 'b'
    if c:  # If there are any elements in 'c'
        print(c)  # Prints dictionary 'c'

f1(25)  # a=25, b=(), c={}
print()
f1('Hyd', 10, 20, 30)  # a='Hyd', b=(10, 20, 30), c={}
print()
f1(10.8, 25, 'Hyd', True, EmpNo=12, EmpName='Rama Rao', Salary=10000.0)  # a=10.8, b=(25, 'Hyd', True), c={'EmpNo': 12, 'EmpName': 'Rama Rao', 'Salary': 10000.0}

# Write a program to evaluate expressions like a calculator
expression = "3+4*5-6/2="
print(eval(expression[:-1]))  # Result of the expression: 14.5

# Write a program to print Roman equivalent of a number
# Input: 3878 -> MMMDCCCLXXVIII

# Explanation:
# 3 -> M  -> 'MMM'
# 878 -> CM  (0) -> 'D' -> 'CC' -> 'L' -> 'XX' -> 'VIII'
# Final result: 'MMMDCCCLXXVIII'
num = 3878
roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

result = ""
for value, numeral in roman_numerals.items():
    while num >= value:
        result += numeral
        num -= value
print(result)  # Output: MMMDCCCLXXVIII

# Write a program to print each digit of the number in words
number = "9247"
digit_map = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

words = " ".join([digit_map[int(ch)] for ch in number])
print(words)  # Output: Nine Two Four Seven

# Write a program to print all the rotations of the string
string = "SPACE"
for i in range(len(string)):
    print(string[i:] + string[:i])

# Write a program to print the multiplication table of a number
num = 7
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# Write a program to print the pyramid pattern
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join([chr(65 + j) for j in range(i)]))

# Find outputs (Home work)
a = 10
def f1():
    b = 40
    print('a : ', a)  # Prints the value of global 'a'
    print('b : ', b)  # Prints the local 'b'
    # print('c : ', c)  # Uncommenting will raise NameError because 'c' is not defined

b = 20
def f2():
    a = 50
    print('a : ', a)  # Prints the local 'a'
    print('b : ', b)  # Prints the global 'b'
    # print('c : ', c)  # Uncommenting will raise NameError because 'c' is not defined

c = 30
print('a : ', a)  # Prints the global 'a'
print('b : ', b)  # Prints the global 'b'
print('c : ', c)  # Prints the global 'c'
print()
a += 1
b += 1
c += 1
f1()  # Calls f1, which prints a local 'b' and the global 'a' and 'c'
a += 1
b += 1
c += 1
f2()  # Calls f2, which prints a local 'a' and the global 'b'
print('Bye')  # Prints 'Bye'

# Find outputs (Home work)
def f1():
    a = 20
    print(a)  # Prints the local value of 'a'
    a += 1  # Increments the local 'a'

a = 10
print(a)  # Prints the global 'a'
a += 1  # Increments the global 'a'
f1()  # Calls f1, which uses a local 'a'
print(a)  # Prints the global 'a' after increment
