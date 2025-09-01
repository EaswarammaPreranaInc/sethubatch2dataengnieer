# index() and count() methods demo program (Home work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)

try:
    i = a.index(15)
    while True:
        print('15 is found at index : ' , i)
        i = a.index(15 , i + 1)
except:
    print(f'15 is found {a.count(15)} times')

# Output:
# 15 is found at index :  2
# 15 is found at index :  5
# 15 is found at index :  8
# 15 is found 3 times


# How to modify an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50
print(a)                                                   # (10, 20, 30, 40, 50)
print(id(a))                                               #address of a

b = list(a)
b[2] = 35
a = tuple(b)
print(a)                                                  # (10, 20, 35, 40, 50)
print(id(a))                                              # different address of a


# How to delete an element of tuple ? (Home work)
a = 10 , 20 , 30 , 40 , 50
b = list(a)
b.remove(30)
a = tuple(b)
print(a)                                                 # (10, 20, 40, 50)
print(id(a))                                             # new address of a


# Nested tuple (Home work)
a = ((10 , 20), (30 , 40 , 50), (60 , 70 , 80 , 90))
print(a)                                                 # ((10, 20), (30, 40, 50), (60, 70, 80, 90))
print(type(a))                                           # <class 'tuple'>
print(len(a))                                            # 3
print("1st inner tuple:", a[0])                          # (10, 20)
print("2nd inner tuple:", a[1])                          # (30, 40, 50)
print("3rd inner tuple:", a[2])                          # (60, 70, 80, 90)
print("20:", a[0][1])                                    # 20
print("50:", a[1][2])                                    # 50
print("90:", a[2][3])                                    # 90


# Find outputs (Home work)
a = ((10 , 20 , 30),)
print("inner tuple:", a[0])                              # (10, 20, 30)
print("inner tuple (another way):", *a)                  # (10, 20, 30)
print("10:", a[0][0])                                    # 10
print("20:", a[0][1])                                    # 20
print("30:", a[0][2])                                    # 30

b = ((),)
print("inner tuple of b:", b[0])                         # ()
print("inner tuple of b (another way):", *b)             # 


# Find outputs (Home work)
a = ((10 , 20 , 30))
print(a)                                                  # (10, 20, 30)
print(*a)                                                 # 10 20 30
b = (())
print(b)                                                  # ()
print(*b)                                                 # nothing



# Find outputs (Home work)
print({(10 , 20 , 30)})                                   # {(10, 20, 30)}
# print({[10 , 20 , 30]})                                 #Error
# print({{10 , 20 , 30}})                                 #Error
print({{}})                                               # {{}}


# How to print set in different ways (Home work)
a = {25 , True , 'Hyd' , 10.8}
print('set with print function')
print(a)                                                  #{True, 25, 'Hyd', 10.8} order may be 

print('Iterate elements of set with for loop')
for x in a:
    print(x)                                              # elements printed one by one (order not guaranteed)


# Find outputs (Home work)
a = 'Hyd'
b = True
c = 25
d = 1
e = 'Hyd'
s = {a , b , c , d , e}
print(s)                                                  # {'Hyd', 25} (because True==1 and 'Hyd' repeated)
print(len(s))                                             # 2
print(type(s))                                            # <class 'set'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)                                                  # order not guaranteed
a , b , c , d = s
print(a)                                                  # element of set
print(b)                                                  # element of set
print(c)                                                  # element of set
print(d)                                                  # element of set


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)
a , *b = s
print(a)                                                   # one element
print(b)                                                   # list of remaining elements
print(type(b))                                             # <class 'list'>


# Find outputs (Home work)
s = {'Hyd', 25, True, 10.8}
print(s)
a , *b , c = s
print(a)                                                  # one element
print(b)                                                  # list of middle elements
print(c)                                                  # last element


# Find outputs (Home work)
s = {20 , 10 , 20 , 10}
print(s)                                                  # {10, 20}
x , y = s
print(x)                                                  # 10 or 20
print(y)                                                  # 20 or 10 (order not fixed)


# set() function demo program (Home work)
a = range(100 , 151 , 10)
b = set(a)
print(b)                                                  # {100, 110, 120, 130, 140, 150}

c = [10 , 20 , 15 , 18 , 10 , 50 , 20 , 12 , 18]
d = set(c)
print(d)                                                  # {10, 12, 15, 18, 20, 50}

e = set('Rama  rAo')
print(e)                                                  #{'R', 'A', 'o', 'm', 'r', ' ', 'a'}

# print(set(25))                                          # Error
print(set())                                              # set()
