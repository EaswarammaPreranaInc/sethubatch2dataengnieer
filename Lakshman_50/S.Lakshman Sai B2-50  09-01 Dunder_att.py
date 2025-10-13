# Find  output (Home  work)
def f1(a=[]):
    pass


print(f1.___defaults___)  # ([],)

# ******************************************************************


# Find  outputs (Home  work)
def f1(x, a=[]):
    a.append(x)
    print("List :  ", a)


# end  of  the  function
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  : ([],)
f1(3)  #  List : [3]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  : ([3],)
f1(4, a=[1, 2, 3])  #  List :  [1,2,3,4]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  :([3],)
f1(9)  #  List : [3,9]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  :([3,9],)
f1(40, [10, 20, 30])  #  List : [10,20,30,40]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  : ([3,9],)
f1(5)  #  List :       [3,9,5]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  : ([3,9,5],)
f1([6, 7, 8])  #  List :    [3,9,5,[6,7,8]]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  : ([3,9,5,[6,7,8]],)

# ******************************************************************


#  Find  outputs (Home  work)
def f1(x, a=[]):
    if a == []:
        a = []
    a.append(x)
    print(a)


# end  of  the  function
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :([],)
f1(3)  # 3
print("__defaults__  :  ", f1.__defaults__)  # __defaults__  :([],)
f1(4, [1, 2, 3])  # [1,2,3,4]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :([],)
f1(4)  # [4]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :([],)
f1(40, [10, 20, 30])  # [10,20,30,40]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :([],)
f1(5)  # [5]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :([],)
f1([6, 7, 8])  # [6,7,8]
print("__defaults__  :  ", f1.__defaults__)  # __defaults__ :  ([],)

# ******************************************************************


# Find  outputs(Home  work)
def f1(x, a=[]):
    for i in range(x):
        a.append(i * i)
    return a


# End  of  the  function
print("_defaults  :  ", f1.__defaults__)  # __defaults__ :  ([],)
print(f1(3))  # [0,1,4]
print("_defaults  :  ", f1.__defaults__)  # __defaults__ :  ([0,1,4],)
print(f1(4, [10, 20, 15, 18]))  # [10,20,15,18,0,1,4,9]
print("_defaults  :  ", f1.__defaults__)  # __defaults__ :  ([0,1,4],)
print(f1(5))  # [0,1,4,0,1,4,9,16]
print("_defaults  :  ", f1.__defaults__)  # __defaults__ :  ([0,1,4,0,1,4,9,16],)
print(f1(a=[100, 200, 300], x=6))  # [100,200,300,0,1,4,9,16,25]
print("_defaults  :  ", f1.__defaults__)  # __defaults__ :  ([0,1,4,0,1,4,9,16],)
print(f1(6))  # [0,1,4,0,1,4,9,16,0,1,4,9,16,25]
print(
    "_defaults  :  ", f1.__defaults__
)  # __defaults__ :  ([0,1,4,0,1,4,9,16,0,1,4,9,16,25],)

# ******************************************************************


# Find  output (Home  work)
def f1(x, a=[]):
    if a == []:
        a = []
    for i in range(x):
        a.append(i * i)
    return a


# End  of  the  function
print(f1(3))  #  [0,1,4]
print(f1(4, [10, 20, 15, 18]))  #    [10,20,15,18,0,1,4,9]
print(f1(5))  # [0,1,4,9,16]
print(f1(a=[100, 200, 300], x=6))  #    [100,200,300,0,1,4,9,16,25]
print(f1(6))  #  [0,1,4,9,16,25]

# ******************************************************************


# Find  outputs
def f1(a="Hyd", b=[]):
    a += "Sec"
    b += [1, 2, 3]
    print("a :  ", a)
    print("b :  ", b)


# End of the function
print("Default Values  :  ", f1.__defaults__)  # Default Values  :    (Hyd,[])
f1()  #  a:HYdSec   b:[1,2,3]
print("Default Values  :  ", f1.__defaults__)  #  Default Values  :  (Hyd,[1,2,3])
f1()  #
print("Default Values  :  ", f1.__defaults__)  #  Default Values  :
f1()  #
