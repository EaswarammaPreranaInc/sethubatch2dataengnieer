'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''

s = input('Enter string : ')
s = s.upper()
b = {}
vowels = 'AEIOU'
for i in s:
    if i in vowels:
       b[i] =  b.get(i,0)+1
print(b)

a = [('R', 'Red'), ('G', 'Green'), ('B', 'Blue')]
b = {'Y': 'Yellow', 'G': 'Gray'}
b.update(a)
print(b)   # {'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}

a.update(b)   # ERROR: list object has no attribute 'update'

a = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
b = {}
b.update(a)
print(b)   # {10: 20, 40: 50, 70: 80}

c = [(10,), (20,), (30,)]
b.update(c)   #  ERROR: dictionary update sequence element has length 1; 2 is required
print(b)


d = {x: x ** 3 for x in range(5)}
print(d)         # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))   # <class 'dict'>


d = {x: 2 * x for x in range(5)}
print(d)   # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


a = {10: 'Rama', 15: 'Sita', 18: 'Rajesh', 17: 'Kiran', 12: 'Rama Rao'}

b = {k: v for k, v in a.items() if k % 2 != 0}
print(b)   # {15: 'Sita', 17: 'Kiran'}

c = {k: a[k] for k in a if a[k].startswith('R')}
print(c)   # {10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}



def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')

print('Begin')   # Begin
x = f1()         # Hyd\nSec\nCyb
print(x)         # None
print(type(x))   # <class 'NoneType'>
print('End')     # End


def f1():
    return 10, 20, 30

x = f1()
print(x)         # (10, 20, 30)
print(type(x))   # <class 'tuple'>

a, b, c = f1()
print(a)         # 10
print(b)         # 20
print(c)         # 30

print('for loop') # for loop
for k in f1():
    print(k)     # 10\n20\n30


