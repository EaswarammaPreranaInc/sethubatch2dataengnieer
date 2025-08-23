# Program 1
a = 25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 'Hyd' , 25
print(a)              # (25, 10.8, (3+4j), 'Hyd', True, None, 'Hyd', 25)
print(type(a))        # <class 'tuple'>
a[3] = 'Sec'          # ERROR → 'tuple' object does not support item assignment
a[3 : 6] = 60 , 70 , 80  # ERROR (not executed)

# Program 2
a = (1,2,3)
b = (4,5,6)
print(a , id(a))      # (1, 2, 3) <id1>
a += b
print(a , id(a))      # (1, 2, 3, 4, 5, 6) <different_id2>

# Program 3
a = (1,2,3)
b = (4,5,6)
print(a , id(a))      # (1, 2, 3) <id1>
a = a + b
print(a , id(a))      # (1, 2, 3, 4, 5, 6) <different_id2>

# Program 4
# Input: (10 , 20 , 30 , 40)
a = input('Enter  Tuple  :  ')
print(a)              # (10 , 20 , 30 , 40)   ← string
print(type(a))        # <class 'str'>
b = eval(a)
print(b)              # (10, 20, 30, 40)
print(type(b))        # <class 'tuple'>
print(len(b))         # 4

# Program 5
a = (10 , [20 , 30 , 40] , 50 , 60)
a[1][0] = 70
print(a)              # (10, [70, 30, 40], 50, 60)
a[1] = [80 , 90 , 100]
print(a)              # (10, [80, 90, 100], 50, 60)

# Program 6
a = [10 , (20 , 30 , 40) , 50 , 60]
a[1][0] = 70          #  ERROR → 'tuple' object does not support item assignment
print(a)              # Not executed
a[1] = [80 , 90]
print(a)              # Not executed

# Program 7
a = 25
b = 10.8
c = 'Hyd'
d = True
x = a , b , c , d
print(x)              # (25, 10.8, 'Hyd', True)
print(type(x))        # <class 'tuple'>

# Program 8
x = 25 , 10.8 , 'Hyd' , True
a , b , c , d = x
print(a)              # 25
print(b)              # 10.8
print(c)              # Hyd
print(d)              # True
p , q , r =  x        #  ERROR → not enough values to unpack (expected 3, got 4)
a , b , c , d , e = x #  ERROR → too many values to unpack (expected 5, got 4)

# Program 9
x = 25 , 10.8 , 'Hyd' , True
a , *b , c = x
print(a)              # 25
print(b)              # [10.8, 'Hyd']
print(c)              # True

# Program 10
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c , d , e = tpl
# ❌ ERROR → not enough values to unpack (need at least 5, got 4)

# Program 11
x = 25 , 10.8 , 'Hyd' , True , 3 + 4j
a , b , _ , d , _ = x
print(a)              # 25
print(b)              # 10.8
print(_)              # (3+4j)  ← first '_'
print(d)              # True
print(_)              # (3+4j)  ← same '_' reused

# Program 12  (tuple() demo)
a = range(100 , 150 , 10)
b = tuple(a)
print(b)              # (100, 110, 120, 130, 140)
print(type(b))        # <class 'tuple'>

c = [10 , 20 , 15, 18]
d = tuple(c)
print(d)              # (10, 20, 15, 18)

e = tuple('Vamsi')
print(e)              # ('V', 'a', 'm', 's', 'i')

print(tuple(25))      # ERROR → 'int' object is not iterable
print(tuple())        # ()
