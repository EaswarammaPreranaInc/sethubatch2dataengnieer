a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.intersection(b)
print(c)
print(type(c))
d = a & b
print(d)
print(type(d))
print(c is d)
print(c == d)


Output:

{40, 30}
<class 'set'>
{40, 30}
<class 'set'>
False
True

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.difference(b)
print(c)
print(type(c))
d = a - b
print(d)
print(type(d))
print(c is d)
print(c == d)


Output:

{10, 20}
<class 'set'>
{10, 20}
<class 'set'>
False
True

a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a.symmetric_difference(b)
print(c)
print(type(c))
d = a ^ b
print(d)
print(type(d))
print(c is d)
print(c == d)


Output:

{50, 20, 10, 60}
<class 'set'>
{50, 20, 10, 60}
<class 'set'>
False
True

a = {x * x  for x in range(10)}
print(a)
print(type(a))


Output:

{0, 1, 4, 36, 9, 16, 49, 64, 81, 25}
<class 'set'>

s = input("Enter input string : ")
result = "".join(set(s))
print("String without duplicates : ", result)


Output (for Rama Rao):

Enter input string : Rama Rao
String without duplicates :  ao mR

lst = eval(input("Enter list with duplicates : "))
result = list(set(lst))
print("List without duplicates : ", result)


Output:

Enter list with duplicates : [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
List without duplicates : [False, 1, None, 'Sec', 10.8, 25, 'Hyd']

l1 = eval(input("Enter 1st list : "))
l2 = eval(input("Enter 2nd list : "))
result = list(set(l1) & set(l2))
print("Common elements between the 2 lists : ", result)


Output:

Enter 1st list : [10,20,30,40,50,60]
Enter 2nd list : [30,40,70,80,20]
Common elements between the 2 lists :  [40, 20, 30]

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])


Output:

25
Rama Rao
1000.65

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
print(id(a))
a['Sal'] = 2000
a['Ename'] = 'Sita'
a['Empno'] = 35
print(a)
print(id(a))


Output:

{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
<id1>
{'Empno': 35, 'Ename': 'Sita', 'Sal': 2000}
<id1>


(id will be same, example value shown as <id1>)

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
a['Gender'] = 'M'
a['Married'] = True
print(a)


Output:

{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65, 'Gender': 'M', 'Married': True}

a = {}
a[10] = 'Rama'
a[20] = 'Sita'
a[15] = 'Rajesh'
a[18] = 'Kiran'
print(a)


Output:

{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}

12) How to remove key:value pairs of dictionary
a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(a)
del a['Sal']
print(a)


Output:

{'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
{'Empno': 25, 'Ename': 'Rama Rao'}

a = {10:20, 30:40, 50:60, 70:80}
print(30 in a.keys())
print(60 in a.keys())
print(60 in a.values())
print(30 in a.values())
print(50 in a)
print(20 in a)
print(70 not in a.keys())
print(40 not in a.values())
print(25 not in a)


Output:

True
False
True
False
True
False
False
False
True

a = input('Enter dictionary : ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))


Output:

Enter dictionary : {10: 'A', 20: 'B', 15: 'C', 20: 'D'}
{10: 'A', 20: 'B', 15: 'C', 20: 'D'}
<class 'str'>
{10: 'A', 20: 'D', 15: 'C'}
<class 'dict'>


Find outputs (copy dictionary)
a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
b = {**a}
print(b)
print(a is b)
print(a == b)
c = a
print(a is c)
print(a == c)


Output:

{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
False
True
True
True

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
b = {18: 'Kiran', 14: 'Amar', 20: 'Manohar'}
c = {25: 'Ramesh', 19: 'Krishna', 15: 'Radha', 14: 'Srinivas'}
d = {*a, *b, *c}
print(d)
print(type(d))
e = {**a, **b, **c}
print(e)
print(type(e))


Output:

{10, 14, 15, 18, 19, 20, 25}
<class 'set'>
{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
<class 'dict'>

a = {10: 20, 30: 40}
b = {30: 50, 10: 60}
print(a + b)
c = {**a, **b}
print(c)
d = a | b
print(d)


Output:

Error
{10: 60, 30: 50}
{10: 60, 30: 50}

a = {}
n = int(input("How many Employees ? : "))
for i in range(n):
    name = input("Enter Emp Name : ")
    sal = float(input("Enter Salary : "))
    a[name] = sal
print(a)


Output:

How many Employees ? : 4
Enter Emp Name : AAA
Enter Salary : 100000
Enter Emp Name : BBB
Enter Salary : 200000
Enter Emp Name : CCC
Enter Salary : 150000
Enter Emp Name : DDD
Enter Salary : 175000
{'AAA': 100000.0, 'BBB': 200000.0, 'CCC': 150000.0, 'DDD': 175000.0}

s = "Emp no = 25 , Emp name = Rama Rao , sal = 10000.0 , gender = m"
pairs = [x.strip() for x in s.split(",")]
a = {}
for p in pairs:
    k, v = p.split("=")
    a[k.strip()] = v.strip()
print(a)


Output:

{'Emp no': '25', 'Emp name': 'Rama Rao', 'sal': '10000.0', 'gender': 'm'}

a = {'Empno': 25, 'Ename': 'Rama Rao', 'Sal': 1000.65}
print(len(a))
b = {}
print(len(b))


Output:

3
0

a = {10: 20, 30: 40, 50: 60}
print(sum(a.keys()))
print(sum(a.values()))
print(sum(a))
print(sum(a.items()))


Output:

90
120
90
Error

a = {10: 20, 30: 25, 40: 5, 7: 28, 9: 50}
print(max(a.keys()))
print(min(a.keys()))
print(max(a.values()))
print(min(a.values()))
print(max(a.items()))
print(min(a.items()))
print(max(a))
print(min(a))


Output:

40
7
50
5
(40, 5)
(7, 28)
40
7

a = [(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (20, 'Pune')]
b = dict(a)
print(b)
c = (['R', 'Red'], ['G', 'Green'], ['B', 'Blue'], ['G', 'Gray'])
d = dict(c)
print(d)
e = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(dict(e))
f = [[10], [20], [30]]
print(dict(f))
print(dict([10, 20]))
g = [[10, [20, 30]], [40, [50, 60]], [70, [80, 90]]]
print(dict(g))
h = [[[10, 20], 30], [[40, 50], 60], [[70, 80], 90]]
print(dict(h))
i = [[(10, 20), 30], [(40, 50), 60], [(70, 80), 90]]
print(dict(i))


Output:

{10: 'Hyd', 20: 'Pune', 15: 'Cyb'}
{'R': 'Red', 'G': 'Gray', 'B': 'Blue'}
Error
Error
Error
{10: [20, 30], 40: [50, 60], 70: [80, 90]}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}
{(10, 20): 30, (40, 50): 60, (70, 80): 90}

a = {10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}
b = sorted(a.keys())
print(b)
c = sorted(a.values())
print(c)
d = sorted(a.items())
print(d)
f = sorted(a, reverse=True)
print(f)
print(a)


Output:

[5, 10, 15, 18, 20]
['Blue', 'Green', 'Red', 'White', 'Yellow']
[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
[20, 18, 15, 10, 5]
{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

d = eval(input("Enter dictionary : "))
sorted_dict = {k: d[k] for k in sorted(d.keys())}
print(sorted_dict)


Output:

Enter dictionary : {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
{5: 'D', 10: 'A', 12: 'E', 15: 'C', 20: 'B'}

a = {10: 20, 30: 40, 50: 60}
print(a)
a.clear()
print(a)
del a
print(a)


Output:

{10: 20, 30: 40, 50: 60}
{}
Error

a = {'R': 'Red', 'G': 'Green', 'B': 'Blue'}
b = a.copy()
print(b)
print(a is b)
print(a == b)


Output:

{'R': 'Red', 'G': 'Green', 'B': 'Blue'}
False
True

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.keys()
print(b)
print(type(b))
for x in b:
    print(x)


Output:

dict_keys([10, 20, 15, 18])
<class 'dict_keys'>
10
20
15
18

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.values()
print(b)
print(type(b))
for x in b:
    print(x)


Output:

dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
<class 'dict_values'>
Hyd
Sec
Cyb
Pune

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
b = a.items()
print(b)
print(type(b))
for x in b:
    print(x)
for x, y in b:
    print(x, y, sep=' ... ')


Output:

dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
<class 'dict_items'>
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune

a = {10: 'Hyd', 20: 'Sec', 15: 'Cyb', 18: 'Pune'}
for x, y in a.items():
    print(x, y, sep=' ... ')
for x, y in a.keys():
    print(x, y, sep=' ... ')
for x, y in a.values():
    print(x, y, sep=' ... ')
for x, y in a:
    print(x, y, sep=' ... ')


Output:

10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
Error
Error
Error

a = {10: 'Rama', 20: 'Sita', 15: 'Rajesh'}
x, y, z = a.keys()
print(x)
print(y)
print(z)
print()
x, y, z = a.values()
print(x)
print(y)
print(z)
print()
x, y, z = a.items()
print(x)
print(y)
print(z)
print()
(rno1, sname1), (rno2, sname2), (rno3, sname3) = a.items()
print(rno1, sname1)
print(rno2, sname2)
print(rno3, sname3)


Output:

10
20
15

Rama
Sita
Rajesh

(10, 'Rama')
(20, 'Sita')
(15, 'Rajesh')

10 Rama
20 Sita
15 Rajesh

s = input("Enter mixed case string : ")
s = s.upper()
a = {}
for ch in sorted(s):
    if ch.isalpha():
        a[ch] = a.get(ch, 0) + 1
print(a)


Output:

Enter mixed case string : RamA raO
{'A': 3, 'M': 1, 'O': 1, 'R': 2}
