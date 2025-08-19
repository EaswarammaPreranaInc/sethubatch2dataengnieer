# 1. Input
a = "[25 , 10.8 , 'Hyd' , True]"     
print(type(a))                       # <class 'str'>
print(a)                             # [25 , 10.8 , 'Hyd' , True]
b = eval(a)
print(b)                             # [25, 10.8, 'Hyd', True]
print(type(b))                       # <class 'list'>

# 2. Same Reference
a = [10, 20, 15, 18]
b = a
print(a is b)                        # True
print(a == b)                        # True
b[2] = 12
print(a)                             # [10, 20, 12, 18]

# 3. Invalid Operations
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)                       # [10, 20, 15, 18, 100, 200, 150]
print(a + 5)                       # Error
print(a + '5')                     # Error
print([10 , 20] + (30 , 40))       # Error

# 4. += modifies in place
a = [1,2,3]
b = [4,5,6]
print(a , id(a))                     # [1, 2, 3] <id1>
a += b
print(a , id(a))                     # [1, 2, 3, 4, 5, 6] <same id1>

# 5. + creates a new list
a = [1,2,3]
b = [4,5,6]
print(a , id(a))                     # [1, 2, 3] <id1>
a = a + b
print(a , id(a))                     # [1, 2, 3, 4, 5, 6] <different id>

# 6. List Packing
a = 25
b = 10.8
c = 'Hyd'
d = True
e = [a , b , c , d]
print(e)                             # [25, 10.8, 'Hyd', True]
print(type(e))                       # <class 'list'>

# 7. List Unpacking (*)
list1 = [25 , 10.8 , 'Hyd' , True]
a , *b , c = list1
print('a : ' , a)                    # a :  25
print('b : ' , b)                    # b :  [10.8, 'Hyd']
print('c : ' , c)                    # c :  True
print(type(b))                       # <class 'list'>
x , *y = list1
print('x : ' , x)                    # x :  25
print('y : ' , y)                    # y :  [10.8, 'Hyd', True]
*p , q = list1
print('p : ' , p)                    # p :  [25, 10.8, 'Hyd']
print('q : ' , q)                    # q :  True

# 8. Too many variables
list2 = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list2          # Error (5 vars, 4 values)
a , b , *c , d , e = list2         # Error
a , b , *c , d , e , f = list2     # Error

# 9. Using _
list3 = [25 , 10.8 , 'Hyd' , True]
a , b , _ , d = list3
print('a : ' , a)                    # a :  25
print('b : ' , b)                    # b :  10.8
print('_ :  ' , _)                   # _ :   Hyd
print('d : ' , d)                    # d :  True

# 10. Duplicate variable names
list4 = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list4
print('a : ' , a)                    # a :  (3+4j)
print('b : ' , b)                    # b :  10.8
print('d : ' , d)                    # d :  True

# 11. Using _ multiple times
list5 = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , _ , d , _ = list5
print('a : ' , a)                    # a :  25
print('b : ' , b)                    # b :  10.8
print('_ : ' , _)                    # _ :  (3+4j)
print('d : ' , d)                    # d :  True
print('_: ' , _)                     # _:  (3+4j)

# 12. Invalid unpacking (two *)
list6 = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e = list6        # Error

# 13. Nested List
list7 = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list7
print('a :  ' , a)                   # a :   [25, 10.8]
print('b :  ' , b)                   # b :   Hyd
print('c :  ' , c)                   # c :   True

# 14. Nested Unpacking
list8 = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list8
print('a : ' , a)                    # a :  25
print('b : ' , b)                    # b :  10.8
print('c : ' , c)                    # c :  Hyd
print('d : ' , d)                    # d :  True
a , b , c , d = list8              # Error (3 values, 4 variables)

# 15. Comparing Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)                        # True
print(a is b)                        # False
print(a < c)                         # True
print(a > d)                         # True
print(a >= c)                        # False
print(a <= d)                        # False
print(a != c)                        # True
print(a != b)                        # False
print(a == c)                        # False

# 16. Another Comparison
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)                        # False
print(a is b)                        # False
