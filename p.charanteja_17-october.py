# 1. Multilevel Inheritance

class A:
    def m1(self): print('class A method')
class B(A):
    def m1(self): print('class B method')
class C(B):
    def m1(self): print('class C method')
class D(C):
    def m1(self): print('class D method')
'''
output:
obj = D()
C.m1(obj)          # class C method
C.m1(D())          # class C method
B.m1(obj)          # class B method
A.m1(obj)          # class A method
D.m1(obj)          # class D method
'''






# 2. Multiple Inheritance Example

class father:  def height(self): print('Father Height')
class mother:  def color(self): print('Mother Color')
class child(mother, father):
    def qualification(self): print('Child Qualification')

c = child()
c.qualification()  # Child Qualification
c.color()          # Mother Color
c.height()         # Father Height
c.m1()             # Error: 'child' object has no attribute 'm1'






# 3. Child Overrides All Parents

class uncle: def m1(self): print('Uncle Method')
class mother: def m1(self): print('Mother Method')
class father: def m1(self): print('Father Method')
class child(father, mother, uncle):
    def m1(self): print('Child Method')

c = child()
c.m1()             # Child Method





# 4. child inherits m1 from father

class uncle: def m1(self): print('Uncle Method')
class mother: def m1(self): print('Mother Method')
class father: def m1(self): print('Father Method')
class child(father, mother, uncle): pass

c = child()
c.m1()             # Father Method





# 5. father has no m1

class uncle: def m1(self): print('Uncle Method')
class mother: def m1(self): print('Mother Method')
class father: pass
class child(father, mother, uncle): pass

c = child()
c.m1()             # Mother Method




# 6. only uncle has m1

class uncle: def m1(self): print('Uncle Method')
class mother: pass
class father: pass
class child(father, mother, uncle): pass

c = child()
c.m1()             # Uncle Method





# 7. None have m1

class uncle: pass
class mother: pass
class father: pass
class child(father, mother, uncle): pass

c = child()
c.m1()             # Error: 'child' object has no attribute 'm1'






# 8. Calling Parent Methods

class father: def m1(self): print('m1 method of Father class')
class mother: def m1(self): print('m1 method of Mother class')
class uncle: def m1(self): print('m1 method of Uncle class')
class child(father, mother, uncle):
    def m1(self): print('m1 method of Child class')

c = child()
father.m1(c)       # m1 method of Father class
father.m1(child()) # m1 method of Father class
mother.m1(c)       # m1 method of Mother class
uncle.m1(c)        # m1 method of Uncle class
c.m1()             # m1 method of Child class
print(child.__mro__)
# (<class 'child'>, <class 'father'>, <class 'mother'>, <class 'uncle'>, <class 'object'>)





# 9. Parent & Child Constructors

class parent:
    def __init__(self): print('parent constructor')
    def __del__(self): print('parent destructor')
class child(parent):
    def __init__(self):
        super().__init__()
        print('child constructor')
    def __del__(self):
        super().__del__()
        print('child destructor')

c = child()
# parent constructor
# child constructor
print('Bye')
# parent destructor
# child destructor






# 10. Parent Constructor Only

class parent:
    def __init__(self): print('parent constructor')
    def __del__(self): print('parent destructor')
class child(parent): pass

c = child()
# parent constructor
print('Bye')
# parent destructor






# 11. Parameterized Constructors

class parent:
    def __init__(self, a1, b1): self.a=a1; self.b=b1
    def disp(self): print(self.a, self.b, sep='\t', end='\t')
class child(parent):
    def __init__(self, a2=0, b2=0, c2=0, d2=0):
        super().__init__(a2,b2)
        self.c=c2; self.d=d2
    def disp(self):
        super().disp(); print(self.c, self.d, sep='\t')

x = child(10,20,30,40)
y = child()
print('Object x'); x.disp()  # 10  20  30  40
print('Object y'); y.disp()  # 0   0   0   0






# 12. Static and Instance Variables

class parent:
    x = 100
    def __init__(self): self.x = 10
class child(parent):
    def __init__(self):
        super().__init__(); self.y = 20
    def disp(self):
        print(parent.x)        # 100
        print(self.__class__.x)# 100
        print(child.x)         # 100
        print(self.x)          # 10
        print(self.y)          # 20

c = child()
c.disp()






# 13. Static Variable Demonstration

class parent:
    x = 10
    def __init__(self): self.x = 20
class child(parent):
    def __init__(self):
        self.x = 30
        print(self.x)          # 30
        super().__init__()
    def disp(self):
        print(self.x)          # 20
        print(super().x)       # 10
c = child()
c.disp()






# 14. Advanced Inheritance Demonstration

class parent:
    a=10
    def __init__(self): print('Parent constructor'); self.x=30
    def m1(self): print('Parent class instance method:', self.x)
    @classmethod
    def m2(cls):
        print('Parent class class method:', cls.a)
        print('Parent class class method:', parent.a)
    @staticmethod
    def m3(): print('Parent class static method:', parent.a)
    def __del__(self): print('parent destructor:', self.x)
class child(parent):
    b=20
    def __init__(self):
        super().__init__(); print('Child constructor'); self.y=40
    def m1(self):
        super().m1(); print('Child class instance method'); print(self.y)
    @classmethod
    def m2(cls):
        super(child, cls).m2()
        print('Child class class method')
        print(parent.a); print(cls.a); print(child.a); print(child.b); print(cls.b)
    @staticmethod
    def m3():
        parent.m3()
        print('child class static method', parent.a)
        print(child.b)
    def __del__(self):
        super().__del__(); print('child destructor', self.y)

child.m2()
child.m3()
c=child()
c.m1()
'''
Output:
Parent class class method: 10
Parent class class method: 10
Child class class method
10
10
10
20
20
Parent class static method: 10
child class static method 10
20
Parent constructor
Child constructor
Parent class instance method: 30
Child class instance method
40
parent destructor: 30
child destructor 40
'''








# 19. MRO with Multiple Inheritance

class A: def m1(self): super().m1(); print('class A method')
class B: def m1(self): super().m1(); print('class B method')
class C: def m1(self): super().m1(); print('class C method')
class D: def m1(self): print('class D method')
class X(A,B): def m1(self): super().m1(); print('class X method')
class Y(B,C,D): def m1(self): super().m1(); print('class Y method')
class P(X,Y,C): def m1(self): super().m1(); print('class P method')

print(P.mro())
obj = P()
obj.m1()
print('Bye')
'''
Output:

[<class 'P'>, <class 'X'>, <class 'A'>, <class 'Y'>, <class 'B'>, <class 'C'>, <class 'D'>, <class 'object'>]
class D method
class Y method
class A method
class X method
class P method
Bye
'''




# 20. Constructors with MRO

class D: 
    def __init__(self): super().__init__(); print('class D constructor')
class E:
    def __init__(self): super().__init__(); print('class E constructor')
class F:
    def __init__(self): super().__init__(); print('class F constructor')
class B(D,E):
    def __init__(self): super().__init__(); print('class B constructor')
class C(D,E,F):
    def __init__(self): super().__init__(); print('class C constructor')
class A(B,C):
    def __init__(self): super().__init__(); print('class A constructor')

print(A.mro())
obj = A()
print('Bye')
'''
Output:

[<class 'A'>, <class 'B'>, <class 'D'>, <class 'E'>, <class 'C'>, <class 'F'>, <class 'object'>]
class D constructor
class E constructor
class F constructor
class C constructor
class B constructor
class A constructor
Bye
'''




# 21. Self-inheritance error

class c1(c1): pass
'''
Output:

Error: name 'c1' is not defined
'''




# 22. Parent and Child Same Name

class c1:
    def m1(self): print('Parent Method')
class c1(c1):
    def m1(self):
        super().m1()
        print('Child Method')

a = c1()
a.m1()
# Parent Method
# Child Method






# 23. Cyclic Inheritance

class c1(c2): pass
class c2(c1): pass
'''
Output:

Error: cannot inherit from a class that indirectly inherits from itself
'''





# 24. Grandchild Redefinition

class c2:
    def m1(self): print('Parent Method')
class c1(c2):
    def m1(self):
        super().m1()
        print('Child Method')
class c2(c1):
    def m1(self):
        super().m1()
        print('Grand Child Method')

a = c2()
a.m1()
# Parent Method
# Child Method
# Grand Child Method
