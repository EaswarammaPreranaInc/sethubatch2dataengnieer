# Q1 Vowel Frequency
s = "RamA raO"
freq = {}
for ch in s.upper():
    if ch in "AEIOU":
        freq[ch] = freq.get(ch, 0) + 1
print(freq)  # output: {'A': 3, 'O': 1}

# Q2
a = [('R', 'Red'), ('G', 'Green'), ('B', 'Blue')]
b = {'Y': 'Yellow', 'G': 'Gray'}
b.update(a)
print(b)  # output: {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
a.update(b)  # error (list has no update method)

# Q3
a = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b = {}
b.update(a)
print(b)  # output: {10: 30, 40: 60, 70: 90}
c = [(10,), (20,), (30,)]
b.update(c)
print(b)  # output: {10: None, 20: None, 30: None, 40: 60, 70: 90}

# Q4
d = {x: x ** 3 for x in range(5)}
print(d)       # output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d)) # output: <class 'dict'>

# Q5
d = {x: 2 * x for x in range(5)}
print(d)  # output: {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Q6
a = {10: 'Rama', 15: 'Sita', 18: 'Rajesh', 17: 'Kiran', 12: 'Rama Rao'}
b = {k: v for k, v in a.items() if k % 2 != 0}
print(b)  # output: {15: 'Sita', 17: 'Kiran'}
c = {k: a[k] for k in a if a[k].startswith('R')}
print(c)  # output: {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}

# Q7
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Begin')   # output: Begin
x = f1()         # output: Hyd Sec Cyb
print(x)         # output: None
print(type(x))   # output: <class 'NoneType'>
print('End')     # output: End

# Q8
def f1():
    return 10, 20, 30
x = f1()
print(x)         # output: (10, 20, 30)
print(type(x))   # output: <class 'tuple'>
a, b, c = f1()
print(a)         # output: 10
print(b)         # output: 20
print(c)         # output: 30
print('for loop')# output: for loop
for k in f1():
    print(k)     # output: 10 20 30

# Q9
def f1():
    return 10
    return 20
    return 30
print('Begin')   # output: Begin
x = f1()
print(x)         # output: 10
print('End')     # output: End
return 100       # error (outside function)

# Q10
f1()             # error (f1 not defined yet)
def f1():
    print('Hello')
print(f1())      # output: Hello \n None
print(f1)        # output: <function f1 at 0x...>

# Q11
print('Hello')   # output: Hello
def f1():
    print('f1  function')
print('Hi')      # output: Hi
print(f1())      # output: f1  function \n None
print(f1)        # output: <function f1 at 0x...>
print('Bye')     # output: Bye

# Q12
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Begin')       # output: Begin
print(type(f1))      # output: <class 'function'>
print(id(f1))        # output: (some integer id)
print('End')         # output: End

# Q13
def add(a, b):
    return a + b
print(add(10, 20))                             # output: 30
print(add('Hyder', 'abad'))                    # output: Hyderabad
print(add(10.8, 20.6))                         # output: 31.4
print(add(True, False))                        # output: 1
print(add(3 + 4j, 5 + 6j))                     # output: (8+10j)
print(add(25, 10.8))                           # output: 35.8
print(add([25, 10.8, 'Hyd'], [True, None, 3+4j, 'Sec']))  
# output: [25, 10.8, 'Hyd', True, None, (3+4j), 'Sec']
print(add(10, '20'))                           # error (int + str)

# Q14
def f1():
    print('No-argument  function')
def f1(x):
    print('Single  argument  function  : ', x)
def f1(x, y):
    print('Two  argument  function : ', x, y)
def f1(x, y, z):
    print('Three  argument  function : ', x, y, z)
f1(10, 20, 30)    # output: Three  argument  function :  10 20 30
f1(40, 50)        # error
f1(60)            # error
f1()              # error

# Q15 Prime Number
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
try:
    n = int(input("Enter number: "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except:
    print("Invalid input")


# Q16
def disp(empno, ename, sal):
    print(f'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
disp(25, 'Rama Rao', 10000.0)  
# output: Emp  Number  :  25 	  Emp Name  :  Rama Rao 	  Salary  :  10000.0
disp('Sita', 20000.0, 35)  
# output: Emp  Number  :  Sita 	  Emp Name  :  20000.0 	  Salary  :  35
