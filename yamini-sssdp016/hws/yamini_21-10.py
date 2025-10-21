# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() .__init__()# calls E class constructor
                print('class D constructor')
class  E:
        def __init__(self):
                super() . __init__()# calls F lass constructor
                print('class E constructor')
class  F:
        def __init__(self):
                super() .__init__()# calls object class constructor which is empty
                print('class F constructor')
class  B(D , E):
        def __init__(self):
                super() . __init__()# calls c class constructor
                print('class B constructor')
class  C(D , E , F):
        def __init__(self):
                super() . __init__()# calls D class constructor
                print('class C constructor')
class  A(B , C):
        def __init__(self):
                super() .__init__() # calls B class constructor
                print('class A constructor')
#end of the class
print(A . mro())    #[A,B,C,D,E,F,O]
obj = A()   # A claass obj is created and constructor is executed
print('Bye')

'''
A.mro=merge(b.mro+c.mro+bc)
A.mro=merge(BDEO+DEFO+bc)
A.mro=A+merge(BDEO+DEFO+BC)
A.mro=A+B+merge(DEO+DEFO+C)
A.mro=A+B+C+merge(DEO+DEFO)
A.mro=A+B+C+D+merge(EO+EFO)
A.mro=A+B+C+D+E+merge(O+FO)
A.mro=A+B+C+D+E+F+merge(O+O)
A.mro=A+B+C+D+E+F+C+merge(O+O)
A.mro=A+B+C+D+E+F+C+O


'''