# Homework Question:

a = 25, 10.8, 3 + 4j, 'Hyd', True, None, 'Hyd', 25
print(a)                # Output: (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))          # Output: <class 'tuple'>
a[3] = 'Sec'            # Error, Tuple is immutable
a[3:6] = 60, 70, 80     # Error, Tuple is immutable


# Homework Question:

a = (1, 2, 3)
b = (4, 5, 6)
print(a, id(a))           # Output: (1, 2, 3) address of a 
a += b
print(a, id(a))           # Output: (1, 2, 3, 4, 5, 6) address of b which is different from a


# Homework Question:

a = (1, 2, 3)
b = (4, 5, 6)
print(a, id(a))           # Output: (1, 2, 3) address of a
a += b
print(a, id(a))           # Output: (1, 2, 3, 4, 5, 6) address of b which is different from a


# Homework Question:

a = input('Enter Tuple : ')     # Enter Tuple : (10 , 20 , 30 , 40)
print(a)                        # Output: (10 , 20 , 30 , 40)
print(type(a))                  # Output: <class 'str'>
b = eval(a)
print(b)                        # Output: (10, 20, 30, 40)
print(type(b))                  # Output: <class 'tuple'>
print(len(b))                   # Output: 4


# Find outputs  (Home work)

a = (10, [20, 30, 40], 50, 60)
a[1][0] = 70
print(a)                     # Output: (10, [70, 30, 40], 50, 60)
a[1] = [80, 90, 100]
print(a)                     # Output: (10, [80, 90, 100], 50, 60)


# Find outputs  (Home work)

a = [10, (20, 30, 40), 50, 60]
a[1][0] = 70                 #  Error: tuple is immutable
print(a)                     # This line will not execute
a[1] = [80, 90]
print(a)                     # This also won't execute due to the error above


# Find outputs   (Home work)

a = 25
b = 10.8
c = 'Hyd'
d = True
x = a, b, c, d
print(x)                     # Output: (25, 10.8, 'Hyd', True)
print(type(x))               # Output: <class 'tuple'>


# Find outputs   (Home work)
x = 25, 10.8, 'Hyd', True
a, b, c, d = x
print(a)                     # Output: 25
print(b)                     # Output: 10.8
print(c)                     # Output: Hyd
print(d)                     # Output: True
p, q, r = x                  #  Error: not enough values to unpack 
a, b, c, d, e = x            #  Error: too many values to unpack 


# Find outputs   (Home work)

x = 25, 10.8, 'Hyd', True
a, *b, c = x
print(a)                     # Output: 25
print(b)                     # Output: [10.8, 'Hyd']
print(c)                     # Output: True


# Find outputs   (Home work)

tpl = 25, 10.8, 'Hyd', True
a, b, *c, d, e = tpl         #  (25, 10.8, 'Hyd', True)


# Find outputs   (Home work)
x = 25, 10.8, 'Hyd', True, 3 + 4j
a, b, _, d, _ = x
print(a)                     # Output: 25
print(b)                     # Output: 10.8
print(_)                     # Output: (3+4j)   
print(d)                     # Output: True
print(_)                     # Output: (3+4j)


# tuple()  function  demo  program   (Home work)
a = range(100, 150, 10)
b = tuple(a)
print(b)                     # Output: (100, 110, 120, 130, 140)
print(type(b))               # Output: <class 'tuple'>
c = [10, 20, 15, 18]
d = tuple(c)
print(d)                     # Output: (10, 20, 15, 18)
e = tuple('Vamsi')
print(e)                     # Output: ('V', 'a', 'm', 's', 'i')
print(tuple(25))             # Error due to int object
print(tuple())               # Output: ()


