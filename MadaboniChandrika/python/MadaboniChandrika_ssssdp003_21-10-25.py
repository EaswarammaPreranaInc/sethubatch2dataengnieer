# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()#'E'
                print('class D constructor')#3rd output
class  E:
        def __init__(self):
                super() . __init__()#'F'
                print('class E constructor')#2nd output
class  F:
        def __init__(self):
                super() . __init__()
                print('class F constructor')#1st output
class  B(D , E):
        def __init__(self):
                super() . __init__()#'C'
                print('class B constructor')#5th output
class  C(D , E , F):
        def __init__(self):
                super() . __init__()#'D'
                print('class C constructor')#4th output
class  A(B , C):
        def __init__(self):
                super() . __init__()#'B'
                print('class A constructor')#6th output
#end of the class
print(A . mro())[A,B,C,D,E,F,object]
obj = A()#constructor class A is executed
print('Bye')#bye


'''
MRO derivation:
A.MRO()=A+MERGE(B.MRO+C.MRO+BC)
       =A+MERGE(BDEO+CDEFO+BC)
       =A+B+MERGE(DEO+CDEFO+C)
       =A+B+C+MERGE(DEO+DEFO)
       =A+B+C+D+MERGE(EO+EFO)
       =A+B+C+D+E+MERGE(O+FO)
       =A+B+C+D+E+F+MERGE(O+O)
       =A+B+C+D+E+F+OBJECT
'''


'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye

'''