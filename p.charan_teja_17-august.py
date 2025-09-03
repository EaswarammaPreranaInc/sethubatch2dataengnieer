1.
print(a print(a is b)
==
b)
# False
(different values, order matters)
# False
(different memory objects)



2.
list
=
[[25 10.8], 'Hyd', True]
و
[a, b] C print('a : '
.
و
و
او
print('b : b) #b
print('c: print('d:
1
a, b, c,
d
و
و
d =
list
a)
# a : 25
10.8
c)
# c : Hyd
d)
# d : True
= list # ValueError: not enough values to unpack (expected 4, got 3)




3.
# Identify error (Home work)
list
=
[25, 10.8, 'Hyd', True
a, b, c, *d, e = list
output:
و
3 + 4j]
SyntaxError: two starred expressions in assignment




4.
a = [1,2,3]
b
=
[4,5,6] print(a, id(a)) a = a + b
print(a, id(a))
# [1, 2, 3] some_id (say 140538267097200)
# [1, 2, 3, 4, 5, 6] new_id (different from above)




5.
a
=
b
=
[10 20
و
[10 20
و
C = [10 20
d
=
3
[10, 20
و
و
و
و
و
15
18]
15, 18]
25, 9]
7 22]
و
==
b)
# True
print(a print(a is b) print(a < c) print(a > d) print(a >= c) print (a <= d) print(a != c) print(a != b) print(a
= c)
==
# False
# True
# True # False # False
# True
# False
# False
(values same)
(different objects) (15 < 25 at 3rd element) (15 > 7 at 3rd element)



6.
# True
# True
a = [10, 20, 15, 18]
b = a print(a is b) print(a == b) b = 12 print(a)
# [10, 20, 12, 18]



7.
list = [25, 10.8, 'Hyd', True]
a, b
d = list
print('a :
a)
# a :
25
print('b:
b)
#b:
10.8
print('_
_)
# :
Hyd
print('d:
d)
# d :
True



8.
a
b
= 25
= 10.8
C
=
'Hyd'
d
= True
e = [a, b, c, d]
print(e)
# [25, 10.8, 'Hyd', True]
print(type(e)) # <class 'list'>



9.
a = [1,2,3] b = [4,5,6] print(a, id(a)) a += b
print(a, id(a))
# [1, 2, 3] some_id (say 140538267096768)
# [1, 2, 3, 4, 5, 6] same_id (140538267096768)



10.
a = input('Enter list : ')
print(type(a)) print(a)
b = eval(a)
print(b)
print (type (b))
# user enters: [25, 10.8, 'Hyd', True] # <class 'str'>
# [25, 10.8, 'Hyd', True]
# [25, 10.8, 'Hyd', True]
# <class 'list'>




11.
# True
# True
a = [10, 20, 15, 18]
b = a print(a is b) print(a == b) b = 12 print(a)
# [10, 20, 12, 18]


12.
list = [25, 10.8, 'Hyd', True]
a, b
d = list
print('a :
a)
# a :
25
print('b:
b)
#b:
10.8
print('_
_)
# :
Hyd
print('d:
d)
# d :
True



13.
a
b
= 25
= 10.8
C
=
'Hyd'
d
= True
e = [a, b, c, d]
print(e)
# [25, 10.8, 'Hyd', True]
print(type(e)) # <class 'list'>




14.
a = [1,2,3] b = [4,5,6] print(a, id(a)) a += b
print(a, id(a))
# [1, 2, 3] some_id (say 140538267096768)
# [1, 2, 3, 4, 5, 6] same_id (140538267096768)




15.
a = input('Enter list : ')
print(type(a)) print(a)
b = eval(a)
print(b)
print (type (b))
# user enters: [25, 10.8, 'Hyd', True] # <class 'str'>
# [25, 10.8, 'Hyd', True]
# [25, 10.8, 'Hyd', True]
# <class 'list'>




16.
list = [25, 10.8, 'Hyd', True]
و
a, *b print('a : print('b: '
print('c:
1
او
C
=
list
a)
#a: 25
b)
#b
[10.8, 'Hyd']
c)
# c : True
print(type (b))
x, *y = list
print('x : '
print('y : '
*p, q
=
list
x)
ささ
# <class 'list'>
# x : 25
y)
#y
[10.8, 'Hyd', True]
#p: [25, 10.8, 'Hyd']
print('p', p)
print('q, q) # q: True
