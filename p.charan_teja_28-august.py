Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

s = "RamA raO"
freq = {}
for ch in s.upper():
    if ch in "AEIOU":
        freq[ch] = freq.get(ch, 0) + 1
print(freq)
Output:

text
{'A': 3, 'O': 1}







a = [ ('R' , 'Red'), ('G' , 'Green'), ('B' , 'Blue')]
b = {'Y': 'Yellow', 'G': 'Gray'}
b.update(a)
print(b)
a.update(b) # Error: 'list' object has no attribute 'update'

Output:
text
{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AttributeError: 'list' object has no attribute 'update'







a = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b = {}
b.update(a)
print(b)           # First print
c = [(10,), (20,), (30,)]
b.update(c)
print(b)           # Second print
Output:

text
{10: 20, 40: 50, 70: 80}
{10: None, 20: None, 30: None, 40: 50, 70: 80}







d = {x: x ** 3 for x in range(5)}
print(d)
print(type(d))
Output:

text
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
<class 'dict'>





d = {x: 2 * x for x in range(5)}
print(d)
Output:

text
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}






a = {10: 'Rama', 15: 'Sita', 18: 'Rajesh', 17: 'Kiran', 12: 'Rama Rao'}
b = {k: v for k, v in a.items() if k % 2 != 0}
print(b)
c = {k: a[k] for k in a if a[k].startswith('R')}
print(c)
Output:

text
{15: 'Sita', 17: 'Kiran'}
{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}







def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')
Output:

text
Begin
Hyd
Sec
Cyb
None
<class 'NoneType'>
End







def f1():
    return 10, 20, 30
x = f1()
print(x)
print(type(x))
a, b, c = f1()
print(a)
print(b)
print(c)
print('for loop')
for k in f1():
    print(k)
Output:

text
(10, 20, 30)
<class 'tuple'>
10
20
30
for loop
10
20
30









def f1():
    return 10
    return 20
    return 30
print('Begin')
x = f1()
print(x)
print('End')
# return 100 (invalid outside function)
Output:

text
Begin
10
End






f1()
def f1():
    print('Hello')
print(f1())
print(f1)
Output:

text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'f1' is not defined







print('Hello')
def f1():
    print('f1 function')
print('Hi')
print(f1())
print(f1)
print('Bye')
Output:

text
Hello
Hi
f1 function
None
<function f1 at ...>
Bye







def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Begin')
print(type(f1))
print(id(f1))
print('End')
Output:

text
Begin
<class 'function'>
123456789  # (Some integer, actual address varies)
End







def add(a, b):
    return a + b
print(add(10, 20))                      # 30
print(add('Hyder', 'abad'))             # 'Hyderabad'
print(add(10.8, 20.6))                  # 31.4
print(add(True, False))                 # 1
print(add(3+4j, 5+6j))                  # (8+10j)
print(add(25, 10.8))                    # 35.8
print(add([25, 10.8, 'Hyd'], [True, None, 3+4j, 'Sec']))  # [25, 10.8, 'Hyd', True, None, 3+4j, 'Sec']
print(add(10, '20'))                    # Error


Output:

text
30
Hyderabad
31.4
1
(8+10j)
35.8
[25, 10.8, 'Hyd', True, None, 3+4j, 'Sec']
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'








def f1(empno, ename, sal):
    print(F'Emp Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
# The next function overwrites previous ones.
disp(25, 'Rama Rao', 10000.0)
disp('Sita', 20000.0, 35)


Output:

text
Emp Number  :  25 	  Emp Name  :  Rama Rao 	  Salary  :  10000.0
Emp Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35






#prime or not using function
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
output:

Input	Loop Executes	Result
25	4		Composite number
11	2		Prime number
2	0		Prime number
49	6		Composite number
