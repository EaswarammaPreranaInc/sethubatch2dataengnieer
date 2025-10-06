# 1) Find outputs
import sys
class c1:
    pass
a = b = c = d = c1()
print(sys.getrefcount(b))
print(sys.getrefcount(c1()))
print(sys.getrefcount(352))
print(sys.getrefcount([10,20,15,18]))
print(sys.getrefcount(10.8))
print(sys.getrefcount({10,20,15,18}))
print(sys.getrefcount('Hyd'))
print(sys.getrefcount({10:20,30:40}))
print(sys.getrefcount((10,20,30,40)))

# Output:
5
2
65          # approximate (immutable int has many internal references)
2
2
2
50          # approximate (string interned)
2
2


# 2) Find outputs (Home work)
import sys
class Test:
    def _init_(self):
        print('Constructor  :', id(self))
        return None
    def _del_(self):
        print('Destructor  :', id(self))
        return 25
t = Test()
print(t._init_())
print(sys.getrefcount(t))
print(t._del_())
print(sys.getrefcount(t))
print('Bye')

# Output:
Constructor  : <id1>
None
2
Destructor  : <id1>
25
2
Bye
Destructor  : <id1>      # auto called when object deleted


# 3) Tricky program
class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')
def f1():
    print('Function Begin')
    a = c1()
    print(a)
    print('Function end')
    return a
print('Program Begin')
b = f1()
print(b)
print('Program End')

# Output:
Program Begin
Function Begin
Object is created
<_main_.c1 object at 0x...>
Function end
<_main_.c1 object at 0x...>
Program End
Object is lost


# 4) Tricky program
class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')
def f1():
    print('Function begin')
    a = c1()
    print('Function end')
    return a
print('Program Begin')
f1()
print('Program End')

# Output:
Program Begin
Function begin
Object is created
Function end
Object is lost
Program End


# 5) Tricky program
class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')
def f1():
    print('Function begin')
    a = c1()
    print('Function end')
print('Program Begin')
b = f1()
print(b)
print('Program End')

# Output:
Program Begin
Function begin
Object is created
Function end
None
Program End
Object is lost


# 6) Most tricky program (Circular reference)
class c1:
    def _init_(self, k):
        print('c1 class object is created')
        self.b = k
        print('End of c1 class constructor')
    def _del_(self):
        print('c1 class object is lost')
class c2:
    def _init_(self):
        print('c2 class object is created')
        self.a = c1(self)
        print('End of c2 class constructor')
    def _del_(self):
        print('c2 class object is lost')
print('Program begin')
x = c2()
print('program end')

# Output:
Program begin
c2 class object is created
c1 class object is created
End of c1 class constructor
End of c2 class constructor
program end
# No destructor messages (circular reference prevents automatic cleanup)


# 7) Lucky object
class c1:
    def _del_(self):
        print('Destructor')
        global b
        b = self
a = c1()
del a
print('Hello')

# Output:
Destructor
Hello
