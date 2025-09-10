'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
try:
    idx = -1
    while (idx := a.index(15, idx + 1)) >= 0:
        print(idx)          # 2, 5, 8
except ValueError:
    print(f'15 is found {a.count(15)} times')    # 15 is found 3 times

'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
def is_sublist(sub, main):
    pos = 0
    for x in sub:
        try:
            pos = main.index(x, pos) + 1
        except ValueError:
            return False
    return True
# Examples
first = [10, 20, 30]
second = [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]
print(is_sublist(first, second)) # True

first = [10, 20, 20]
second = [15, 18, 10, 12, 19, 20, 14, 12, 30, 25, 16]
print(is_sublist(first, second)) # False

first = [2, 2, 5]
second = [2, 2, 3, 4, 5]
print(is_sublist(first, second)) # True

first = [2, 4, 3]
second = [2, 2, 3, 4, 5]
print(is_sublist(first, second)) # False

# 3. copy() method demo
a = [10, 20, 15, 18]
b = a.copy()
print(b)              # [10, 20, 15, 18]
print(a is b)         # False
print(a == b)         # True
c = a[:]
print(c)              # [10, 20, 15, 18]
print(a is c)         # False
print(a == c)         # True
d = a
print(d)              # [10, 20, 15, 18]
print(a is d)         # True
print(a == d)         # True


# 5. Nested list demo
a = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(a)              # [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
print(len(a))         # 3
print(a[0])           # [10, 20, 30, 40]
print(a[1])           # [50, 60, 70, 80]
print(a[2])           # [90, 100, 110, 120]
print(a[2])        # 30
print(a[1][3])        # 80
print(a[2][1])        # 100

# 6. Find outputs (inner lists and their lengths)
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(a[0])               # [10, 20]
print(a[1])               # [30, 40, 50]
print(a[2])               # [60, 70, 80, 90]
print(len(a))          # 2
print(len(a[1]))          # 3
print(len(a[2]))          # 4

# 7. Print nested list in different ways
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print('Nested list with print function')
print(a)                  # [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print('Each inner list of outer list without indexes')
for sub in a:
    print(sub)            # Each inner list printed
print('Elements in matrix form without using indexes')
for sub in a:
    for item in sub:
        print(item, end='\t')  # All elements in one line per inner list
    print()
print('Elements in matrix form using indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='\t')  # All elements indexed
    print()

# 8. Find outputs
a = [[10, 20], [30, 40], [50, 60], [70, 80]]
for x in a:
    print(x)          # [10, 20] [30, 40] [50, 60] [70, 80]
print()
for x, y in a:
    print(x, y, sep='...')  # 10...20, 30...40, 50...60, 70...80

# 9. Find outputs
a = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for x in a:
    print(x)          # [10, 20, 30], [40, 50, 60], [70, 80, 90]
print()
for x, y, z in a:
    print(x, y, z, sep='...')  # 10...20...30 etc.

# 10. Find outputs
a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
for x in a:
    print(x)          # [10, 20], [30, 40, 50], [60, 70, 80, 90]
for x, y in a[:1]:
    print(x, y, sep='...')  # 10...20

# 11. Find outputs
a = [[]]
print(a[0])           # []
print(a[:])        # []

# 12. Find outputs
a = [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
print(sorted(a))      # Sorted by first element: [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a, reverse=True)) # [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)              # Original list unchanged
