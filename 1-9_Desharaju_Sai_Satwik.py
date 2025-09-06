# Question 1
def f1(a = []):
    pass
print(f1._defaults_)   # error


# Question 2
def f1(x , a = []):
    a.append(x)
    print('List : ', a)

print('_defaults_  : ', f1._defaults_)   # error
f1(3)                                   # List :  [3]
print('_defaults_  : ', f1._defaults_)   # error
f1(4 , [1 , 2 , 3])                      # List :  [1, 2, 3, 4]
print('_defaults_  : ', f1._defaults_)   # error
f1(9)                                   # List :  [3, 9]
print('_defaults_  : ', f1._defaults_)   # error
f1(40 , [10 , 20 , 30])                  # List :  [10, 20, 30, 40]
print('_defaults_  : ', f1._defaults_)   # error
f1(5)                                   # List :  [3, 9, 5]
print('_defaults_  : ', f1._defaults_)   # error
f1([6 , 7 , 8])                          # List :  [3, 9, 5, [6, 7, 8]]
print('_defaults_  : ', f1._defaults_)   # error


# Question 3
def f1(x , a = []):
    if a == []:
        a = []
    a.append(x)
    print(a)

print('_defaults_  : ', f1._defaults_)   # error
f1(3)                                   # [3]
print('_defaults_  : ', f1._defaults_)   # error
f1(4 , [1 , 2 , 3])                      # [1, 2, 3, 4]
print('_defaults_  : ', f1._defaults_)   # error
f1(4)                                   # [4]
print('_defaults_  : ', f1._defaults_)   # error
f1(40 , [10 , 20 , 30])                  # [10, 20, 30, 40]
print('_defaults_  : ', f1._defaults_)   # error
f1(5)                                   # [5]
print('_defaults_  : ', f1._defaults_)   # error
f1([6 , 7 , 8])                          # [[6, 7, 8]]
print('_defaults_  : ', f1._defaults_)   # error


# Question 4
def f1(x , a = []):
    for i in range(x):
        a.append(i * i)
    return a

print('_defaults  : ', f1._defaults_)             # error
print(f1(3))                                     # [0, 1, 4]
print('_defaults  : ', f1._defaults_)             # error
print(f1(4 , [10 , 20 , 15 , 18]))                # [10, 20, 15, 18, 0, 1, 4, 9]
print('_defaults  : ', f1._defaults_)             # error
print(f1(5))                                     # [0, 1, 4, 0, 1, 4, 9, 16]
print('_defaults  : ', f1._defaults_)             # error
print(f1(a = [100 , 200 , 300], x = 6 ))          # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print('_defaults  : ', f1._defaults_)             # error
print(f1(6))                                     # [0, 1, 4, 0, 1, 4, 9, 16, 0, 1, 4, 9, 16, 25]
print('_defaults  : ', f1._defaults_)             # error


# Question 5
def f1(x , a = []):
    if a == []:
        a = []
    for i in range(x):
        a.append(i * i)
    return a

print(f1(3))                                   # [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18]))             # [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5))                                   # [0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300], x = 6 ))       # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6))                                   # [0, 1, 4, 9, 16, 25]


# Question 6
def f1(a = 'Hyd' , b = []):
    a += "Sec"
    b += [1 , 2 , 3]
    print('a : ', a)
    print('b : ', b)

print('Default Values  : ', f1._defaults_)   # error
f1()                                        # a :  HydSec
                                            # b :  [1, 2, 3]
print('Default Values  : ', f1._defaults_)   # error
f1()                                        # a :  HydSec
                                            # b :  [1, 2, 3, 1, 2, 3]
print('Default Values  : ', f1._defaults_)   # error
f1()                                        # a :  HydSec
                                            # b :  [1, 2, 3, 1, 2, 3, 1, 2, 3]
