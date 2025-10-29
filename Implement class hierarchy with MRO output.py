# Find  outputs  (Home  work)
class  D:
        def _init_(self):
                super() . _init_()
                print('class D constructor')
class  E:
        def _init_(self):
                super() . _init_()
                print('class E constructor')
class  F:
        def _init_(self):
                super() . _init_()
                print('class F constructor')
class  B(D , E):
        def _init_(self):
                super() . _init_()
                print('class B constructor')
class  C(D , E , F):
        def _init_(self):
                super() . _init_()
                print('class C constructor')
class  A(B , C):
        def _init_(self):
                super() . _init_()
                print('class A constructor')
#end of the class
print(A . mro())
obj = A()
print('Bye')

'''
Final MRO: [A, B, C, D, E, F, object]  
outputs  :
class A, class B, class C, class D, class E, class F, class object
class D constructor
class E constructor
class F constructor
class C constructor
class B constructor
class A constructor
Bye
'''
