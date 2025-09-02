'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]

try:
    i = -1
    while (i := a.index(15, i + 1)) != -1:
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')


'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True
Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False
'''
a=eval(input('Enter the first list : '))
b=eval(input('Enter the second list : '))
index=b.index(a[0])
for x in a[1:]:
    try:
        index = b.index(x, index + 1)
    except ValueError:
        print(False)
        break
else:
    print(True)



# copy()  method  demo program  (Home  work)
a = [10, 20, 15, 18]

b = a.copy()
print(b)          # [10, 20, 15, 18]
print(a is b)     # False different objects
print(a == b)     # True  same contents

c = a[:]
print(c)          
print(a is c)     # False
print(a == c)     # True

d = a
print(d)
print(a is d)     # True  same object
print(a == d)     # True


'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
    ctr = 5

Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15

a = [12, 20, 18, 15, 10, 15, 10, 15, 20, 18, 15, 10, 20, 15, 10]

mode = None
max_count = 0
'''
for x in set(a):
    if (cnt := a.count(x)) > max_count:
        mode, max_count = x, cnt

print("Mode :", mode)   # 15


#  Nested  List  demo  program  (Home  work)
a = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(a)              # Whole list
print(len(a))         # 3
print(a[0])           # 1st inner list
print(a[1])           # 2nd inner list
print(a[2])           # 3rd inner list
print(a[0][2])        # 30
print(a[1][3])        # 80
print(a[2][1])        # 100



'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''
#  Find  outputs  (Home  work)
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Nested list with print function')
print(a)

print('Each inner list without indexes')
for row in a:
    print(row)

print('Elements in matrix style (without indexes)')
for row in a:
    for val in row:
        print(val, end="  ")
    print()

print('Elements in matrix style (with indexes)')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="  ")
    print()


'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
#Output:     
[10, 20]
[30, 40]
[50, 60]
[70, 80]



#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
#Output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
#Output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
#ValueError: too many values to unpack


#  Find  outputs  (Home  work)
a = [[]]
print(a[0])       # []
print(a[-1])      # []



 #  Find  outputs  (Home  work)
a = [[10, 'Rama', 1000.0],
     [20, 'Sita', 2000.0],
     [15, 'Rajesh', 3500.0],
     [18, 'Kiran', 2800.0],
     [5, 'Amar', 5000.0]]

print(sorted(a))                 # Sorted by 1st element
print(sorted(a, reverse=True))   # Descending
print(a)                         # Original unchanged
