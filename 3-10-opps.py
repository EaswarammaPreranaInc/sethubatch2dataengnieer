import sys
class c1:
    pass
# End of the class
a = b = c = d = c1()
print(sys.getrefcount(b))  # 5
print(sys.getrefcount(c1()))  # 1
print(sys.getrefcount(352))  # 2
print(sys.getrefcount([10, 20, 15, 18]))  # 1
print(sys.getrefcount(10.8))  # 2
print(sys.getrefcount({10, 20, 15, 18}))  # 1
print(sys.getrefcount('Hyd'))  # 4294967295
print(sys.getrefcount({10: 20, 30: 40}))  # 1
print(sys.getrefcount((10, 20, 30, 40)))  # 2

import sys
class Test:
    def _init_(self):
        print('Constructor  : ', id(self))
        return None
    def _del_(self):
        print('Destructor  : ', id(self))
        return 25
# End of the class
t = Test()
print(t._init_())  # Constructor : <id> \n None
print(sys.getrefcount(t))  # 2
print(t._del_())  # Destructor : <id> \n 25
print(sys.getrefcount(t))  # 2
print('Bye')  # Bye

class c1:
    def __init__(self):
        print('Object  is    created')
    def __del__(self):
        print('Object  is  lost')
# End of the class
def f1():
    print('Function  Begin')  # Function Begin
    a = c1()  # Object is created
    print(a)  # <__main__.c1 object at 0x...>
    print('Function  end')  # Function end  # Object  is  lost
    return a

print('Program  Begin')  # Program Begin
b = f1()
print(b)  # <__main__.c1 object at 0x...>
print('Program  End')  # Program End

class c1:
    def __init__(self):
        print('Object  is    created')
    def __del__(self):
        print('Object  is  lost')
# End of the class
def f1():
    print('Function  begin')  # Function begin
    a = c1()  # Object is created
    print('Function  end')  # Function end # Object is lost
    return a
print('Program  Begin')  # Program Begin
f1()
print('Program  End')  # Program End

class c1:
    def __init__(self):  
        print('Object  is    created')  
    def __del__(self):  
        print('Object  is  lost')  
# End of the class
def f1():
    print('Function  begin')  # Function  begin
    a = c1()  # Object  is    created
    print('Function  end')  # Function  end  # Object  is  lost
print('Program  Begin')  # Program  Begin
b = f1()  # f1() returns nothing (None), assigned to b
print(b)  # None 
print('Program  End')  # Program  End

class   c1:
	def   _init_(self , k):
		print('c1  class  object  is  created')  # c1  class  object  is  created
		self . b = k
		print('End  of  c1  class constructor')  # End  of  c1  class constructor
	def   _del_(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  _init_(self):
		print('c2  class  object  is  created')  # c2  class  object  is  created
		self . a = c1(self)
		print('End  of  c2  class constructor')  # End  of  c2  class constructor
	def  _del_(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')  # Program  begin 
x = c2()
print('program end')  # program end
# After program ends, destructors run automatically:
# c2  class  object  is  lost
# c1  class  object  is  lost

class c1:
    def __del__(self):
        print('Destructor')  # Destructor
        global b
        b = self  
a = c1()  
del a  
print('Hello')  # Hello
