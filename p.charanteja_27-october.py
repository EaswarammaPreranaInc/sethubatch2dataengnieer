# 1.  

try:
    print('Hyd')
    print('Sec')
    print('Cyb')
# Hyd
# Sec
# Cyb




# 2.  

print(7 / 0)
# ZeroDivisionError: division by zero



# 3.  

try:
    print(7 / 0)
except ZeroDivisionError:
    print('Division by zero is not permitted')
print(7 / 0)
print('Bye')
# Division by zero is not permitted
# ZeroDivisionError: division by zero



# 4.  

except:
    print('Hyd')
    print('Sec')
    print('Cyb')
# SyntaxError: invalid syntax (except without try)




# 5.  

try:
    print('One')
    print('Two')
    print('Three')
print('Four')
except:
    print('Five')
    print('Six')
    print('Seven')
print('Eight')
# SyntaxError: expected 'except' or 'finally' block
# (because print('Four') is not indented as part of try suite)





# 6.  

try:
    print('try suite')
except:
    print('default except')
except NameError:
    print('Name Error')
# SyntaxError: default 'except:' must be last





# 7.  

try:
    print('try suite')
except:
    print('1st default except')
except:
    print('2nd default except')
# SyntaxError: default 'except:' must be last





# 8.  

print(7 / 0)
print(7 / 0.0)
print(0 / 0)
print(0.0 / 0.0)
print(7 // 0)
print(7 % 0)
# 7/0 -> ZeroDivisionError
# 7/0.0 -> ZeroDivisionError
# 0/0 -> ZeroDivisionError
# 0.0/0.0 -> ZeroDivisionError
# 7//0 -> ZeroDivisionError
# 7%0 -> ZeroDivisionError





# 9.  

import math
print(int('10.8'))
print(float('Ten'))
print(complex('True'))
print(bool('Ten'))
print(bool(''))
print(float('10.8'))
print(float('25'))
print(int(10.8))
print(math.sqrt(-25))
# int('10.8') -> ValueError
# float('Ten') -> ValueError
# complex('True') -> ValueError
# bool('Ten') -> True
# bool('') -> False
# float('10.8') -> 10.8
# float('25') -> 25.0
# int(10.8) -> 10
# math.sqrt(-25) -> ValueError (math domain error)





# 10.  

a = 25
print(a)
del a
print(a)
print(eval("   'Ten'   "))
print(eval('Ten'))
# 25
# NameError: name 'a' is not defined (after del a)
# 'Ten'
# NameError: name 'Ten' is not defined






# 11.  

print('Hyd'[0])
print('Hyd'[1])
print('Hyd'[2])
print('Hyd'[3])
list = [10, 20, 15, 18]
print(list[0])
print(list[3])
print(list[4])
print(list[-1])
print(list[-4])
print(list[-5])
tpl = (10, 20, 30)
print(tpl[3])
r = range(10)
print(r[10])
s = {10, 20, 15, 18}
print(s[4])
d = {10: 'Hyd', 20: 'Sec'}
print(d[0])
# 'H'
# 'y'
# 'd'
# IndexError: string index out of range
# 10
# 18
# IndexError: list index out of range
# 18
# 10
# IndexError: list index out of range
# IndexError: tuple index out of range
# IndexError: range object index out of range
# KeyError: 4   (sets cannot be indexed or keyed)
# KeyError: 0







# 12.  

print(10 + 20)
print('10' + '20')
print(10 + '20')
print(len('25'))
print(len(25))
s = {10, 20, 15, 18}
print(s[0])
b = { [10, 20] : [30, 40] }
print(int(3 + 4j))
print(int([10, 20, 30]))
print(float(None))
# 30
# 1020
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 2
# TypeError: object of type 'int' has no len()
# TypeError: 'set' object is not subscriptable
# TypeError: unhashable type: 'list'   (dict cannot have a list as key)
# TypeError: can't convert complex to int
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# TypeError: float() argument must be a string or a number, not 'NoneType'






# 13.  

a = {'R' : 'Red', 'G' : 'Green', 'B': 'Blue'}
print(a['G'])
print(a['Y'])
# 'Green'
# KeyError: 'Y'





# 14.  

try:
    print(7 / 0)
    print('Hello')
except ZeroDivisionError:
    print('ZDE  1')
except ZeroDivisionError:
    print('ZDE  2')
print('Bye')
# ZDE  1
# Bye






# 15.  

try:
    print(7 / 0)
    print('Hello')
except ZeroDivisionError:
    print('ZDE  1')
    print(8 / 0)
except ZeroDivisionError:
    print('ZDE  2')
print('Bye')
# ZDE  1
# ZeroDivisionError: division by zero (from print(8 / 0))





# 16.  

try:
    print(7 / 0)
    print('Hello')
except ZeroDivisionError:
    print('ZDE  1')
    try:
        print(8 / 0)
    except ZeroDivisionError:
        print('ZDE   2')
    print('Bye')
except ZeroDivisionError:
    print('ZDE  3')
print('End')
# ZDE  1
# ZDE   2
# Bye
# End






# 17.  

try:
    print(7 / 0)
except ArithmeticError:
    print('Arithmetic Error')
except ZeroDivisionError:
    print('Zero Division  Error')
print('End')
# Arithmetic Error
# End






# 18.  

def  f1():
    try:
        print('f1  function')
        print(7 / 0)
    except  ValueError:
        print('Hello')
    try:
        print(int('Ten'))
    except ZeroDivisionError:
        print('Bye')
    print('End  of  f1  function')
# End of f1  function
try:
    print('Begin')
    f1()
    print('Hi')
except  ZeroDivisionError:
    print('ZDE  is  caught  outside')
except:
    print('Bye')
print('End')
# Begin
# f1  function
# ZeroDivisionError: division by zero
# Bye





# 19.  

def  f1():
    try:
        print('f1  function')
        print(7 / 0)
    except  ValueError:
        print('Hello')
    except  ZeroDivisionError:
        print('ZDE  is  caught  by  f1  function')
    print('End  of  f1  function')
# End  of  the  function
try:
    print('Begin')
    f1()
    print('Hello')
except  ZeroDivisionError:
    print("Hi")
except  ValueError:
    print("Bye")
print('End')
# Begin
# f1  function
# ZDE  is  caught  by  f1  function
# End  of  f1  function
# Hello
# End






# 20.  

while  True:
    ch = eval(input('Enter  choice (9-exit) : '))
    try:
        match  ch:
            case  1:
                list = [10, 20, 15, 12, 18]
                print(list[5])
            case  2:
                s = 'Hyd'
                print(s[3])
            case  3:
                print(int('Two'))
            case  4:
                a = 25
                print(len(a))
            case  5:
                print(eval('Hyd'))
            case  6:
                print(7 / 0)
            case  7:
                print(10 + '20')
            case   8:
                d = {10: 'Hyd', 20: 'Sec', 15: 'Cyb'}
                print(d[18])
            case   9:
                exit()
    except   ZeroDivisionError:
        print('Div by 0 is not allowed')
    except  ValueError:
        print('No  result')
    except  IndexError:
        print('Invalid  index')
    except  TypeError:
        print('Invalid   argument (or)  operand')
    except  KeyError:
        print('Invalid dict key')
    except  NameError:
        print('Object  does  not  exist')
    except:
        print('A new error')
# End of while loop
print('Bye')
# For each choice, prints the output or handler message as per the error






# 21.  

def  f1():
    print('f1  function')
    raise   ValueError('Hyd')
    print('Sec')
# End of  the  function
f1()
try:
    print('Begin')
    f1()
    print('Bye')
except  ValueError  as  msg:
    print('Caught  ValueError  outside  the  function  :  ' , msg)
f1()
print('End of the program')
# f1  function
# ValueError: Hyd
# Begin
# f1  function
# Caught  ValueError  outside  the  function  :  Hyd
# f1  function
# ValueError: Hyd
# End of the program (not printed due to exception)






# 22.  

def  f1(a):
    print('f1  function')
    if   a == 20:
        raise  ArithmeticError()
    elif   a == 0:
        raise  IndexError()
    elif  a == 10:
        raise  TypeError(25)
    raise ValueError()
# end of  the function
try:
    print('Begin')
    f1(10)
    f1(20)
    f1(30)
    f1(0)
except  ArithmeticError:
    print('Hyd');
except  IndexError:
    print('Sec')
except  TypeError  as   msg:
    print('Caught  TypeError  outside  the  function :  '  , msg)
except  ValueError:
    print('Hello')
except:
    print('some error')
print('End')
# Begin
# f1  function
# Caught  TypeError  outside  the  function :  25
# End






# 23.  

def  f1(a):
    try:
        if   a == 10:
            raise  ValueError(25)
        elif   a == 20:
            raise  NameError(10.8)
        elif   a == 30:
            raise  IndexError('Hyd')
        raise  EOFError(True)
    except  IndexError  as  msg:
        print('Caught  IndexError  :  ' , msg)
    except ValueError  as  msg:
        print('Caught  ValueError  :  ' , msg)
    except  NameError  as  msg:
        print('Caught   NameError  :  ' , msg)
    except  EOFError  as  msg:
        print('Caught   EOFError  :  '  , msg)
    print('End  of  f1  function')
#outside the function
f1(10)
f1(20)
f1(30)
f1(0)
print('End of the program')
# Caught  ValueError  :  25
# End  of  f1  function
# Caught   NameError  :  10.8
# End  of  f1  function
# Caught  IndexError  :  Hyd
# End  of  f1  function
# Caught   EOFError  :   True
# End  of  f1  function
# End of the program






# 24.  

def f1():
    try:
        print('f1 function')
        raise  ValueError(25)
        print('Hi')
    except  ValueError  as  msg:
        try:
            print('Caught  by  f1 function  : ' , msg)
            raise   ValueError(msg)
        except  ValueError  as   msg:
            print('Recaught  by  f1 function  : ' , msg)
    except:
        print('Hello')
    print('End  of  f1  function')
# End  of  f1()  function
try:
    print('Begin')
    f1()
    print('Hyd')
except  ValueError  as  x:
    print('Recaught ValueError  :  ' , x)
except:
    print('Some other error')
print('End of the program')
# Begin
# f1 function
# Caught  by  f1 function  :  25
# Recaught  by  f1 function  :  25
# End  of  f1  function
# Hyd
# End of the program






# 25.  

def f1():
    try:
        print('f1 function')
        raise  ValueError(25)
        print('Hi')
    except  ValueError  as  msg:
        print('Caught  by  f1 function  : ' , msg)
        raise   ValueError(msg)
    except:
        print('Hello')
    print('End  of  f1  function')
# End  of  f1()  function
try:
    print('Begin')
    f1()
    print('Hyd')
except  ValueError  as  x:
    print('Recaught ValueError  :  ' , x)
except:
    print('Some other error')
print('End of the program')
# Begin
# f1 function
# Caught  by  f1 function  :  25
# Recaught ValueError  :   25
# End of the program





# 26.  

def f1():
    try:
        print('f1 function')
        raise  ValueError(25)
        print('Hi')
    except  ValueError  as  msg:
        print('Caught  by  f1 function  : ' , msg)
        raise  NameError(msg)
    except:
        print('Hello')
    print('End of f1 function')
# End  of  the  function
try:
    print('Begin')
    f1()
    print('Hyd')
except  ValueError  as  x:
    print('Recaught ValueError : ' , x)
except:
    print('Some other error')
print('End of the program')
# Begin
# f1 function
# Caught  by  f1 function  :  25
# Some other error
# End of the program





# 27.  

from threading import Thread
def    f1():
    for  i  in range(10):
        print('child  thread')
child = Thread(target = f1)
f1()
for  i  in range(10):
        print('main  thread')
# child  thread (10 times)
# main  thread (10 times)






# 28.  

from threading import Thread
def  f1():
    for  i  in range(10) :
        print('child  thread')
child = Thread(target =  f1())
child . start()
for  i  in range(10):
    print('main  thread')
# child  thread (10 times)
# main  thread (10 times)
# TypeError: 'NoneType' object is not callable





# 29.  

from threading import *
def   f1():
    for  i  in range(10):
        print('child  thread')
child = Thread()
child . start()
for  i   in   range(10):
    print('main  thread')
# TypeError: run() takes 1 positional argument but 2 were given
# main  thread (10 times)





# 30.  

from threading import Thread
def    f1():
    for  i  in range(10):
        print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in range(10):
    print('Main  Thread')
child . start()
# Child  Thread (10 times)
# Main  Thread (10 times)
# RuntimeError: threads can only be started once





# 31.  

from threading import *
class  c1:
    def  m1(self):
        for  i  in range(10):
            print('child  thread')
a = c1()
child  = Thread(target = a . m1)
child . start()
a . m1()
for  i  in range(10):
    print('main  thread')
# child  thread (may interleave 20 times)
# main  thread (10 times)






# 32.  

from threading import   *
class   c1:
    def  m1(self):
        for  i  in range(10):
            print('child  thread')
a = c1()
child = Thread(target =  a . m1())
child . start()
for  i in range(10):
    print('main  thread')
# child  thread (10 times)
# main  thread (10 times)
# TypeError: 'NoneType' object is not callable





# 33.  

from threading import  *
class  c1:
    @classmethod
    def  m1(cls):
        for  i   in  range(1 , 11):
            print('Child  Thread  :  ' , i)
child = Thread(target = c1.m1)
child . start()
for  i  in range(1 , 11):
    print('Main  Thread  :  ' , i)
# Child  Thread  : 1-10, Main  Thread : 1-10 (output interleaved)






# 34.  

from threading import Thread
class   Thread:
    def   run(self):
        for  i  in range(10):
            print('Child  Thread')
# End of the class
t = Thread()
t . start()
for  i  in range(10):
    print('main  thread')
# AttributeError: 'Thread' object has no attribute 'start'
# main  thread (10 times)





# 35.  

class   Thread:
    def   run(self):
        for  i  in range(10):
            print('Child  Thread')
from  threading  import  Thread
t = Thread()
t . start()
for  i  in range(10):
        print('Main  Thread')
# Child  Thread (10 times)
# Main  Thread (10 times, possibly interleaved)






# 36.  

from  threading  import  *
class    MyThread(Thread):
    def   run(self):
        for  i  in range(10):
            print('child  thread')
#end of the class
child = MyThread()
child . run()
for  i  in range(10):
    print('main  thread')
# child  thread (10 times, sequentially)
# main  thread (10 times)







# 37.  

from  threading  import *
class    MyThread(Thread):
    def  walk(self):
        for  i  in range(10):
            print('walk  method')
child = MyThread()
child . start()
for  i  in range(10):
    print('Main  Thread')
# Main  Thread (10 times)






# 38.  

from  threading  import  *
class   MyThread(Thread):
    def   run(self):
            print('run  method')
def  f1():
    print('f1  function')
child = MyThread(target = f1)
child . start()
print('Main  Thread')
# run  method
# Main  Thread






# 39.  

from  threading  import  *
class   MyThread(Thread):
    pass
def  f1():
    for  i in   range(1 , 11):
        print('f1  function : ' , i)
child = MyThread(target = f1)
child . start()
for  i in  range(1 , 11):
    print('Main  Thread : ' , i)
# f1  function : 1-10
# Main  Thread : 1-10 (order interleaved)




