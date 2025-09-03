
Sort list without sort()
python
arr = [10,20,30,25,40,35,12,5]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)   # [5, 10, 12, 20, 25, 30, 35, 40]











a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)
print(type(a))
a[3] = 'Sec'
a[3 : 6] = 60 , 70 , 80
Output:

text
(25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
<class 'tuple'>

TypeError: 'tuple' object does not support item assignment






a = (1,2,3)
b = (4,5,6)
print(a , id(a))
a += b
print(a , id(a))
Output:

text
(1, 2, 3)  <id1>
(1, 2, 3, 4, 5, 6)  <id2>









a = (1,2,3)
b = (4,5,6)
print(a , id(a))
a = a + b
print(a , id(a))
Output is identical to Q2:

text
(1, 2, 3) <id1>
(1, 2, 3, 4, 5, 6) <id2>








a = input('Enter Tuple : ')
print(a)
print(type(a))
b = eval(a)
print(b)
print(type(b))
print(len(b))
Suppose you type:

text
(10 , 20 , 30 , 40)
Output:

text
Enter Tuple : (10 , 20 , 30 , 40)
(10 , 20 , 30 , 40)
<class 'str'>
(10, 20, 30, 40)
<class 'tuple'>
4










a = (10 , [20 , 30 , 40] , 50 , 60)
a[1] = 70
print(a)
a = [80 , 90 , 100]
print(a)
Output first print:

text
(10, [70, 30, 40], 50, 60)
(because list inside tuple is mutable)

Error on second assignment:

text
TypeError: 'tuple' object does not support item assignment







a = [10 , (20 , 30 , 40) , 50 , 60]
a[1] = 70
print(a)
a = [80 , 90]
print(a)
Error at first assignment:

text
TypeError: 'tuple' object does not support item assignment
Because a is a tuple (20, 30, 40) and tuples are immutable.








a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)
print(type(x))
Output:

text
(25, 10.8, 'Hyd', True)
<class 'tuple'>





x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)   # 25
print(b)   # 10.8
print(c)   # Hyd
print(d)   # True

p , q , r = x        # ERROR (too few vars, tuple has 4 elements)
a , b , c , d , e = x  # ERROR (too many vars, tuple has 4 elements)

text
ValueError: not enough values to unpack









x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)
print(b)
print(c)
Output:

text
25
[10.8, 'Hyd']
True







tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
ERROR:

text
ValueError: not enough values to unpack (expected at least 5, got 4)






x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _ = x
print(a)
print(b)
print(_)
print(d)
print(_)
Output:

text
25
10.8
(3+4j)
True
(3+4j)









a = range(100 , 150 , 10)
b = tuple(a)
print(b)
print(type(b))

c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)

e = tuple('Vamsi')
print(e)

print(tuple(25))   # ERROR
print(tuple())
 Outputs before error:

text
(100, 110, 120, 130, 140)
<class 'tuple'>
(10, 20, 15, 18)
('V', 'a', 'm', 's', 'i')
 Error:

text
TypeError: 'int' object is not iterable
 Last line not executed due to error, but if it was:

text
()







a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)

try:
    i = a.index(15)
    while True:
        print('15 is found at index : ', i)
        i = a.index(15, i+1)
except:
    print(F'15 is found {a.count(15)} times')
 Output:

text
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15 is found 3 times






a  =  10 ,  20 ,  30 ,   40 ,  50
a[2] = 35
 Output:

text
TypeError: 'tuple' object does not support item assignment






a  = 10 , 20 , 30 , 40 , 50
a.remove(30)
del a[2]
a.pop(2)
All invalid attempts:

text
AttributeError: 'tuple' object has no attribute 'remove'
text
TypeError: 'tuple' object doesn't support item deletion
 To “remove an element”, must reconstruct tuple:

python
a = a[:2] + a[3:]






a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
Output:

text
((10, 20), (30, 40, 50), (60, 70, 80, 90))
<class 'tuple'>
3








a = ((10 , 20 , 30),)
Inner tuple → a gives (10,20,30)

Alternate: *a

10 → a

20 → a

30 → a

python
b = ((),)







a = ((10 , 20 , 30))
print(a)
print(*a)

b = (())
print(b)
print(*b)
Note:

((10,20,30)) is just (10,20,30) → normal tuple

(()) is () → empty tuple

 Output:

text
(10, 20, 30)
10 20 30
()





{10, 20, 15, 18, 20, 12, 18}
Output:

text
{10, 20, 15, 18, 20, 12, 18}
<class 'str'>
{10, 12, 15, 18, 20}
<class 'set'>







print({(10 , 20 , 30)})
print({[10 , 20 , 30]})
print({{10 , 20 , 30}})
print({{}})
 First works (tuple is hashable):
text
{(10, 20, 30)}
Second:
text
TypeError: unhashable type: 'list'
 Third:
text
TypeError: unhashable type: 'set'
Fourth:
{{}} = a set containing {} → but {} means empty dict not set!
So actually → {{}} = set with a dict → 

text
TypeError: unhashable type: 'dict'





Q9 – Printing set different ways
python
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')
print(a)
print('Iterate elements of set with for loop')
for x in a:
    print(x)
 Output (order changes, since sets are unordered):

text
set with print function
{'Hyd', True, 25, 10.8}
Iterate elements of set with for loop
Hyd
True
25
10.8





Q10 – Duplicates in set
python
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)
print(len(s))
print(type(s))
Important:

'Hyd' repeated → only once kept

True == 1 → they are same key in set

So final has → 'Hyd', True, 25

 Output:

text
{'Hyd', True, 25}
3
<class 'set'>




 Q11 – Unpacking set
python
s = {'Hyd', 25, True, 10.8}
print(s)
a, b, c, d = s
print(a)
print(b)
print(c)
print(d)
Output:

First print: order random ({'Hyd', 10.8, 25, True})

Then 4 lines print elements in that internal order.






 Q12 – Extended unpacking
python
s = {'Hyd', 25, True, 10.8}
print(s)
a , *b = s
print(a)
print(b)
print(type(b))
 Works fine:

text
{'Hyd', 10.8, 25, True}
Hyd
[10.8, 25, True]
<class 'list'>
(b ordering may vary)






Q13 – Extended unpacking both sides
python
s = {'Hyd', 25, True, 10.8}
a, *b, c = s
 Works fine (two ends fixed, middle into list):
Example output:

text
Hyd
[25, 10.8]
True
(order can vary)





Q14 – Repeated values inside set
python
s = {20, 10, 20, 10}
print(s)
x, y = s
print(x)
print(y)
 Output:

text
{10, 20}
10
20
(order might swap, but set has only {10, 20})






 Q15 – set() function demo
python
a = range(100, 151, 10)
b = set(a)
print(b)

c = [10, 20, 15, 18, 10, 50, 20, 12, 18]
d = set(c)
print(d)

e = set('Rama  rAo')
print(e)

print(set(25))
print(set())
 Outputs up to duplicates removal:

text
{100, 130, 140, 110, 120, 150}
{50, 18, 20, 10, 12, 15}
{'a', 'R', 'm', 'o', ' ', 'r', 'A'}
 Then error:

text
TypeError: 'int' object is not iterable
 Last print(set()) would give:

text
set()
