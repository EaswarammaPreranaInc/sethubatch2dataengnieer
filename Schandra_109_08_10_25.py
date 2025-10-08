# ================================================================
# 1) Find outputs (Home work) — Nested Inner Class Example
# ================================================================
class outer:
    def _init_(self):
        print('Outer class constructor')
    def m1(self):
        print('Outer class method')
    class inner:
        def _init_(self):
            print('Inner class constructor')
        def m1(self):
            print('Inner class method')

# How to call m1() of outer class
o = outer()
o.m1()

# How to call m1() of inner class
i = outer.inner()
i.m1()

# How to call m1() of inner class in another way
outer.inner().m1()

# How to call m1() of inner class in one more way
i2 = o.inner()
i2.m1()

# ================================================================
# 2) Find outputs (Home work) — emp class with inner date class
# ================================================================
class emp:
    def _init_(self):
        self.empno, self.ename, self.sal = 25, 'Rama Rao', 10000.0
        self.d = self.date()
    def disp(self):
        print(self.empno, self.ename, self.sal)
        self.d.disp()
    class date:
        def _init_(self):
            self.dd, self.mm, self.yy = 15, 8, 1947
        def disp(self):
            print(self.dd, self.mm, self.yy)

# How to call disp() of emp class
e = emp()
e.disp()

# ================================================================
# 3) Find outputs (Home work) — outer with inner1 and inner2
# ================================================================
class outer:
    def _init_(self):
        self.x = 25
        self.i1 = self.inner1()
        self.i2 = self.inner2()
    def disp(self):
        print(self.x)
    class inner1:
        def disp(self):
            print('1st inner class method')
    class inner2:
        def disp(self):
            print('2nd inner class method')

# How to call disp() of outer, inner1, inner2
o = outer()
o.disp()
o.i1.disp()
o.i2.disp()

# ================================================================
# 4) Find outputs (Home work) — class c1 with nested and outer c2
# ================================================================
class c1:
    def _init_(self):
        print('outer class c1 constructor')
    class c2:
        def _init_(self):
            print('inner class c2 constructor')

class c2:
    def _init_(self):
        print('outer class c2 constructor')

# How to create objects
x = c1()           # outer class c1
y = c1.c2()        # inner c2
z = c2()           # outer c2

# ================================================================
# 5) Find outputs (Home work) — same class name nested
# ================================================================
class c2:
    def _init_(self):
        print('outer class constructor')
    class c2:
        def _init_(self):
            print('inner class constructor')

# create objects
o = c2()
i = c2.c2()
j = o.c2()

# ================================================================
# 6) Find outputs (Home work) — static vs instance variables
# ================================================================
class c1:
    x = 10
    def _init_(self):
        self.y = 20
a = c1()
b = c1()
a.x += 1
b.y += 1
print(a.x)    # 11
print(a.y)    # 20
print(b.x)    # 11
print(b.y)    # 21
print(c1.x)   # 11
print(a._dict_)  # {'y': 20}
print(b._dict_)  # {'y': 21}
print(c1._dict_)

'''
static variable ---> x
Object 'a' ---> y
Object 'b' ---> y
'''

# ================================================================
# 7) Find outputs (Home work)
class c1:
    x = 10
    def m1(self):
        self.x = 20
a = c1()
a.m1()
print(c1.x)   # 10
print(a.x)    # 20

'''
static variable ---> x (10)
object 'a' ---> instance x (20)
'''

# ================================================================
# 8) Find outputs (Home work) — classmethod and static variables
class c1:
    x = 10
    def _init_(self):
        self.y = 20
    @classmethod
    def m1(cls):
        cls.x = 30
        cls.y = 40
a = c1()
b = c1()
c1.m1()
print(a.x)      # 30
print(a.y)      # 20
print(b.x)      # 30
print(b.y)      # 20
print(c1.x, c1.y)  # 30 40

'''
static variable ---> x, y (class-level)
object 'a' ---> y (instance)
object 'b' ---> y (instance)
'''

# ================================================================
# 9) Find outputs — staticmethod demonstration
class c1:
    @staticmethod
    def m1(self):
        print(self)
c1.m1(25)
a = c1()
a.m1(35)

# ================================================================
# 10) Find outputs — instance method demonstration
class c1:
    def m1(self):
        print(self)
c1.m1(25)   # Error: missing 'self' since no object
a = c1()
a.m1()
a.m1(35)    # Error: too many arguments

# ================================================================
# 11) Find outputs — method redefinition
class c1:
    @staticmethod
    def m1(self):
        print('static method')
        print(self)
    def m1(self):
        print('static / instance method')
        print(self)
c1.m1(25)
a = c1()
a.m1()

# ================================================================
# 12) Accessing static variable in different ways
class c1:
    x = 25
    def _init_(self):
        print(c1.x)
        print(self.x)
        # print(x) # invalid
    def m1(self):
        print(c1.x)
        print(self.x)
    @classmethod
    def m2(cls):
        print(c1.x)
        print(cls.x)
    @staticmethod
    def m3():
        print(c1.x)

# calling methods
print(c1.x)
a = c1()
a.m1()
c1.m2()
c1.m3()

# ================================================================
# 13) Add static variable at different locations
class c1:
    a = 10
    def _init_(self):
        c1.b = 20
        self.c = 30
    def m1(self):
        c1.d = 40
        self.e = 50
    @classmethod
    def m2(cls):
        cls.f = 60
        c1.g = 70
    @staticmethod
    def m3():
        c1.h = 80

print('Begin')
print(c1._dict_)
x = c1()
print('Constructor')
print(c1._dict_)
x.m1()
print('Instance method m1')
print(c1._dict_)
c1.m2()
print('Class method m2')
print(c1._dict_)
c1.m3()
print('Static method m3')
print(c1._dict_)
c1.i = 90
x.j = 100
print('Outside the class')
print(c1._dict_)
print("Object 'x'")
print(x._dict_)

# ================================================================
# 14) Range unpacking
class c1:
    a, b, c = range(1, 4)
print(c1.a)
print(c1.b)
print(c1.c)

# ================================================================
# 15) Tricky program
class Test:
    @classmethod
    def get1(cls):
        cls.x = int(input('Enter any number : '))
    def get2(self):
        self.y = int(input('Enter any number : '))
        self.z = int(input('Enter any number : '))
    def compute(self):
        Test.x += 1
        self.y += 1
        self.z += 1
        self.x += 1
    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')

Test.get1()
a = Test()
b = Test()
c = Test()
a.get2()
b.get2()
c.get2()
a.compute()
b.compute()
c.compute()
a.disp()
b.disp()
c.disp()

'''
static variable ---> x
Object 'a' ---> y, z
Object 'b' ---> y, z
Object 'c' ---> y, z
'''

# ================================================================
# 16) Add two Vector objects
class vector:
    @staticmethod
    def get1():
        vector.n = int(input('Enter number of elements : '))
    def get2(self):
        self.a = list(map(int, input('Enter list elements : ').split()))
    def add(self, x, y):
        self.a = [x.a[i] + y.a[i] for i in range(vector.n)]

vector.get1()
a = vector()
b = vector()
a.get2()
b.get2()
c = vector()
c.add(a, b)
print('Sum of vectors :', c.a)

# ================================================================
# 17) Print only static variables from class _dict_
class c1:
    x = 1
    y = 2
    z = 3

d = {k: v for k, v in c1._dict.items() if not (k.startswith('') and k.endswith('_'))}
print('static variables of class c1 :', d)

# ================================================================
# 18) Identify variable types
class c1:
    x = 10   # static
    def m1(self):
        self.y = 20   # instance
        z = 30        # local
        c1.m = 40     # static

def f1():
    a = c1()
    a.p = 50   # instance
    c1.q = 60  # static
    s = 70     # local

k = 80         # global
c1.l = 90      # static
b = c1()
b.n = 100      # instance

# ================================================================
# 19) Infix → Postfix Conversion Steps (examples)
# (shown conceptually as in question)
# Example 1: 3 + 4 * 5 - 6 / 2 ^ 7
# Postfix: 345*+627^/-
# Prefix : - + 3 * 4 5 / 6 ^ 2 7

# Example 2: a ^ b ^ c → Postfix: abc^^ → Prefix: ^a^bc
# Example 3: a + b + c → Postfix: ab+c+ → Prefix: ++abc
# Example 4: (-b + (b ^ 2 - 4 * a * c) ^ 0.5) / (2 * a)
#            Postfix: b- b2^4ac* - 0.5^ + 2a*/ → Prefix: / + -b ^ - ^b2 *4ac 0.5 *2a
# Example 5: a < b or b > c and c < d
#            Postfix: ab<bc>cd<&or → Prefix: or <a b & >b c <c d
# Example 6: x ^ y / (5 * z) + 2
#            Postfix: xy^5z*/2+ → Prefix: + / ^xy *5z 2
# Example 7: a + b * (c ^ d - e) ^ (f + g * h) - i
#            Postfix: abcd^e-fgh*+^*+i- → Prefix: - + a * b ^ - ^ c d e + f * g h i

# ================================================================
# 20) Infix to Postfix Program
def icp(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/', '%'): return 2
    if op in ('(', '^'): return 4
def isp(op):
    if op in ('+', '-'): return 1
    if op in ('*', '/', '%'): return 2
    if op == '^': return 3
    if op == '(': return 0
    if op == '#': return -1

class stack:
    def _init_(self):
        self.s = []
    def push(self, val):
        self.s.append(val)
    def pop(self):
        return self.s.pop()
    def peek(self):
        return self.s[-1]

def convert(infix):
    st = stack()
    st.push('#')
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == ')':
            while st.peek() != '(':
                postfix += st.pop()
            st.pop()
        else:
            while icp(ch) <= isp(st.peek()):
                postfix += st.pop()
            st.push(ch)
    while st.peek() != '#':
        postfix += st.pop()
    return postfix

infix = input('Enter infix : ')
print('Postfix :', convert(infix))

# ================================================================
# 21) Evaluate Postfix Expression
class stack:
    def _init_(self):
        self.s = []
    def push(self, val):
        self.s.append(val)
    def pop(self):
        return self.s.pop()

def eval_postfix(a):
    st = stack()
    for ch in a.split():
        if ch.isdigit():
            st.push(int(ch))
        else:
            y = st.pop()
            x = st.pop()
            match ch:
                case '+': st.push(x + y)
                case '-': st.push(x - y)
                case '*': st.push(x * y)
                case '/': st.push(x / y)
                case '^': st.push(x ** y)
    return st.pop()

expr = input('Enter postfix expression (space separated): ')
print('Result :', eval_postfix(expr))
