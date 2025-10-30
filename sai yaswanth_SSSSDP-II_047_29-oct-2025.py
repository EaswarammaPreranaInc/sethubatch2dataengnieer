# Find outputs (Home work)
try:
    raise ArithmeticError
except ZeroDivisionError:
    print('Zero Division Error')
except ArithmeticError:
    print('Arithmetic Error')
print('End')

'''
Arithmetic Error
End
'''

# Find outputs (Home work)
def f1():
    try:
        print('f1 function')
        raise ValueError('Hyd')
        print('Hi')
    finally:
        print("f1's finally")
    print('End of f1 function')

def f2():
    try:
        print('f2 function')
        return
        print('Hello')
    finally:
        print("f2's finally")
    print('End of f2 function')

def f3():
    try:
        print('f3 function')
        raise KeyError(25)
        print('Hello')
    except KeyError as msg:
        print('Caught by f3 function : ', msg)
    finally:
        print("f3's finally")
    print('End of f3 function')

def f4():
    try:
        print('f4 function')
        exit()
    finally:
        print("f4's finally")
    print('End of f4 function')

try:
    print('Begin')
    f1()
    print('Hello')
except ValueError as msg:
    print('ValueError is caught outside : ', msg)

f2()
f3()
try:
    f4()
finally:
    print('Outside finally')
print('End of the program')

'''
Begin
f1 function
f1's finally
ValueError is caught outside :  Hyd
f2 function
f2's finally
f3 function
Caught by f3 function :  25
f3's finally
End of f3 function
f4 function
f4's finally
Outside finally
End of the program
'''

# Find outputs (Home work)
import sys

def f1():
    try:
        print('f1 function')
        raise ValueError('Hyd')
        print('Hi')
    finally:
        print("f1's finally")
    print('End of f1 function')

def f2():
    try:
        print('f2 function')
        return
        print('Hello')
    finally:
        print("f2's finally")
    print('End of f2 function')

def f3():
    try:
        print('f3 function')
        raise KeyError(25)
        print('Hello')
    except KeyError as msg:
        print('Caught by f3 function : ', msg)
    finally:
        print("f3's finally")
    print('End of f3 function')

def f4():
    try:
        print("f4 function")
        sys.exit()
    finally:
        print("f4's finally")
    print('End of f4 function')

try:
    print('Begin')
    f1()
    f2()
    f3()
    f4()
    print('Hello')
except ValueError as msg:
    print('ValueError is caught outside : ', msg)

print('End of the program')

'''
Begin
f1 function
f1's finally
ValueError is caught outside :  Hyd
f2 function
f2's finally
f3 function
Caught by f3 function :  25
f3's finally
End of f3 function
f4 function
f4's finally
End of the program
'''

# Find outputs (Home work)
def f1():
    try:
        print('f1 function')
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught KeyError')
        raise Exception()
    except:
        print('Sec')
    finally:
        print("f1's finally")
    print('End of f1 function')

try:
    print('Begin')
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except Exception:
    print('Recaught Exception')
finally:
    print('Outside finally')
print('End of the program')

'''
Begin
f1 function
Caught KeyError
f1's finally
Recaught Exception
Outside finally
End of the program
'''

# Find outputs (Home work)
def f1():
    try:
        print('f1 function')
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught KeyError')
        raise NameError()
    except NameError:
        print('Sec')
    finally:
        print('f1 finally')
    print('End of f1 function')

try:
    print('Begin')
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except Exception:
    print('Recaught Exception')
except NameError:
    print('Caught Name Error outside')
finally:
    print('Outside finally')
print('End of the program')

'''
Begin
f1 function
Caught KeyError
f1 finally
Caught Name Error outside
Outside finally
End of the program
'''

# Find outputs (Home work)
def f1():
    try:
        print('f1 function')
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught KeyError')
        raise NameError()
    except NameError:
        print('Sec')
    finally:
        print('f1 finally')
    print('End of f1 function')

try:
    print('Begin')
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except KeyError:
    print('Recaught KeyError')
finally:
    print('Outside finally')
print('End of the program')

'''
Begin
f1 function
Caught KeyError
f1 finally
Outside finally
Traceback (most recent call last):
  File "<stdin>", line 21, in <module>
  File "<stdin>", line 9, in f1
NameError
'''

# Find outputs (Home work)
try:
    print('try')
    print(7 / 0)
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
print('End')

'''
try
except
finally
End
'''

# Find outputs (Home work)
try:
    print('try')
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
print('End')

'''
try
else
finally
End
'''

# Find outputs (Home work)
try:
    print('try')
else:
    print('else')
finally:
    print('finally')
print('End')

'''
try
else
finally
End
'''

# Find outputs (Home work)
try:
    print('try')
except:
    print('except')
else:
    print('else1')
else:
    print('else2')
finally:
    print('finally')
print('end')

'''
SyntaxError: invalid syntax
'''

# Identify error (Home work)
try:
    print('try')
else:
    print('else')
except:
    print('except')
finally:
    print('finally')
print('end')

'''
SyntaxError: invalid syntax
'''

# Find outputs (Home work)
try:
    print('try')
except:
    print('except')
if 10 > 20:
    print('if')
else:
    print('else')

'''
try
else
'''

# Find outputs
def f1():
    try:
        return 10 + '20'
    except:
        return 10 + 20

print(f1())

'''
30
'''

# Find outputs
def f1():
    try:
        return 10
    except:
        return 20
    else:
        return 30

print(f1())

'''
10
'''

# Find outputs
def f1():
    try:
        return 10 + '20'
    except:
        return 20
    else:
        return 30

print(f1())

'''
20
'''

# Find outputs
def f1():
    try:
        pass
    except:
        return 20
    else:
        return 30

print(f1())

'''
30
'''

# Find outputs
def f1():
    try:
        return 10
    except:
        return 20
    else:
        return 30
    finally:
        return 40

print(f1())

'''
40
'''

# (Home work)
# 1) What is the output if input is 24 ?
try:
    x = eval(input('Enter any number : '))
    assert x >= 25, 'Hyd'
    print('Sec')
except AssertionError as msg:
    print(msg)
print('End')

'''
Enter any number : 24
Hyd
End
'''

# 2) What is the output if input is 25 ?
'''
Enter any number : 25
Sec
End
'''

# (Home work)
# 1) What is the output when input is 24 ?
try:
    x = eval(input('Enter any number : '))
    assert x >= 25
    print('Sec')
except AssertionError as msg:
    print(msg)
print('End')

'''
Enter any number : 24
End
'''

# 2) What is the output when input is 25 ?
'''
Enter any number : 25
Sec
End
'''

# Find outputs (Home work)
try:
    print('Outer try')
    try:
        print('Inner try')
        print(7 / 0)
        int('Hyd')
        'Hyd'[5]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE of inner try')
        int('Ten')
    except ValueError:
        print('ValueError of inner try')
    finally:
        print('Inner try finally')
    print('End of inner try')
except ValueError:
    print('ValueError of outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End of outer try')

'''
Outer try
Inner try
ZDE of inner try
Inner try finally
End of inner try
Outer try finally
End of outer try
'''

# Find outputs (Home work)
try:
    print('Outer try')
    try:
        print('Inner try')
        int('Hyd')
        'Hyd'[5]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE of inner try')
        int('Ten')
    except ValueError:
        print('ValueError of inner try ')
    finally:
        print('Inner try finally')
    print('End of inner try')
except ValueError:
    print('ValueError of outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End of outer try')

'''
Outer try
Inner try
ValueError of inner try 
Inner try finally
End of inner try
Outer try finally
End of outer try
'''

# Find outputs (Home work)
try:
    print('Outer try')
    try:
        print('Inner try')
        'Hyd'[3]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE of inner try')
        int('Ten')
    except ValueError:
        print('ValueError of inner try ')
    finally:
        print('Inner try finally')
    print('End of inner try')
except ValueError:
    print('ValueError of outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End of outer try')

'''
Outer try
Inner try
Inner try finally
End of inner try
IndexError of outer try
Outer try finally
End of outer try
'''

# Find outputs (Home work)
try:
    print('Outer try')
    try:
        print('Inner try')
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE of inner try')
        int('Ten')
    except ValueError:
        print('ValueError of inner try ')
    finally:
        print('Inner try finally')
    print('End of inner try')
except ValueError:
    print('ValueError of outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')
print('End of outer try')

'''
Outer try
Inner try
ValueError of inner try 
Inner try finally
End of inner try
Outer try finally
End of outer try
'''

# Find outputs (Home work)
try:
    print('Outer try')
    try:
        print('Inner try')
        print(10 + '20')
    except ZeroDivisionError:
        print('ZDE of inner try')
        int('Ten')
    except ValueError:
        print('ValueError of inner try ')
    finally:
        print('Inner try finally')
    print('End of inner try')
except ValueError:
    print('ValueError of outer try')
except IndexError:
    print('IndexError of outer try')
finally:
    print('Outer try finally')
print('End of outer try')

'''
Outer try
Inner try
Inner try finally
End of inner try
ValueError of outer try
Outer try finally
End of outer try
'''

# Find outputs (Home work)
class MyError(BaseException):
    def __init__(self, y):
        self.a = y
        print('Constructor')

def compute(x):
    print(x)
    if x > 20:
        raise MyError(x)
    print('Hello')

try:
    compute(10)
    compute(30)
except MyError as msg:
    print('Caught MyError outside : ', msg)
print('End')

'''
10
Hello
30
Constructor
Caught MyError outside : some msg
End
'''

# Find outputs (Home work)
class MyError(NameError):
    def __init__(self):
        self.a = 25
        print('Constructor')

def compute(x):
    print(x)
    if x > 20:
        raise MyError()
    print('Hello')

try:
    compute(30)
    compute(10)
except MyError as msg:
    print('Caught MyError outside : ', msg)
print('End')

'''
30
Constructor
Caught MyError outside :  
10
Hello
End
'''

# Find outputs (Home work)
try:
    print(1)
    print(2)
    print(3)
except:
    print(4)
else:
    print(5)
finally:
    print(6)
print(7)

'''
1
2
3
5
6
7
'''

# Find outputs (Home work)
try:
    print(1)
    print(7 / 0)
    print(3)
except:
    print(4)
else:
    print(5)
finally:
    print(6)
print(7)

'''
1
4
6
7
'''

# Find outputs (Home work)
try:
    print(1)
    print(7 / 0)
    print(3)
except:
    int('Two')
else:
    print(5)
finally:
    print(6)
print(7)

'''
1
6
7
Error
'''

# Find outputs (Home work)
from threading import *

def f1():
    print(current_thread().name)

t = Thread(target=f1, name='new')
t.start()
print(current_thread().name)

'''
new
MainThread
'''

# Find outputs (Home work)
from threading import *

t1 = Thread(name='Hyd')
t2 = Thread()

print(current_thread().name)
print(t1.name)
print(t2.name)

current_thread().name = 'India'
t1.name = 'Sec'
t2.name = 'Cyb'

print(current_thread().name)
print(t1.name)
print(t2.name)
print(active_count())

'''
MainThread
Hyd
Thread-2
India
Sec
Cyb
3
'''

# Find outputs (Home work)
from threading import *

def f1(x):
    s = current_thread().name
    while True:
        print(s, ' : ', x)

t1 = Thread(target=f1, name='Hyd', args=(10,))
t2 = Thread(target=f1, name='Sec', args=[20])
t1.start()
t2.start()
print(active_count())
print('Press ctrl + break or Fn + b to stop ')

'''
Hyd  :  10
Sec  :  20
Hyd  :  10
Sec  :  20
Hyd  :  10
Sec  :  20
'''

# Find outputs (Home work)
from threading import current_thread
from random import randint

def f1(n):
    ctr = 0
    s = current_thread().name
    while True:
        x = randint(1, 100)
        ctr += 1
        print(f'{s} guess {x} in attempt : {ctr}')
        if x == n:
            break
    print(f'{s} finish in {ctr} attempts')

t1 = Thread(target=f1, args=[75], name='Rama')
t2 = Thread(target=f1, args=[50], name='Sita')
t1.start()
t2.start()

'''
Rama guess 45 in attempt : 1
Sita guess 67 in attempt : 1
Rama guess 89 in attempt : 2
Sita guess 23 in attempt : 2
Rama guess 75 in attempt : 3
Rama finish in 3 attempts
Sita guess 88 in attempt : 3
Sita guess 50 in attempt : 4
Sita finish in 4 attempts
'''

# Find outputs (Home work)
from threading import *

def disp():
    for i in range(10):
        print('new thread')

new = Thread(target=disp)
new.start()
new.join()
for i in range(10):
    print('main thread')

'''
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
new thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
main thread
'''

# Find outputs (Home work)
from threading import *
import time

def disp():
    for i in range(10):
        print('new thread')
        time.sleep(2)

new = Thread(target=disp)
new.start()
new.join(10)
for i in range(10):
    print('main thread')

'''
new thread
new thread
new thread
new thread
new thread
main thread
main thread
main thread
main thread
main thread
main thread
new thread
new thread
new thread
new thread
new thread
'''

# Find outputs (Home work)
from threading import *
import time

def double():
    for i in range(1, 7):
        print('Double : ', 2 * i)
        time.sleep(1)

def square():
    for i in range(1, 7):
        print('Square : ', i * i)
        time.sleep(1)

start = time.time()
double()
square()
end = time.time()
print(end - start)

'''
Double :  2
Double :  4
Double :  6
Double :  8
Double :  10
Double :  12
Square :  1
Square :  4
Square :  9
Square :  16
Square :  25
Square :  36
12.0
'''

# Find outputs (Home work)
from threading import *
import time
def display():
    name = current_thread().name
    print(name, ' is started')
    time.sleep(3)
    print(name, ' is ended')
print(active_count())
t1 = Thread(target=display, name='One')
t2 = Thread(target=display, name='Two')
t3 = Thread(target=display, name='Three')
print(active_count())
t1.start()
t2.start()
t3.start()
print(active_count())
t1.join()
t2.join()
t3.join()
print(active_count())

'''
1
1
One  is started
Two  is started
Three  is started
4
One  is ended
Two  is ended
Three  is ended
1
'''

# Find outputs (Home work)
from threading import *
import time

def disp():
    name = current_thread().name
    print(name, ' is started')
    time.sleep(3)
    print(name, '  is ended')

t1 = Thread(target=disp, name='One')
t2 = Thread(target=disp, name='Two')
t3 = Thread(target=disp, name='Three')
t1.start()
t2.start()
t3.start()

list_threads = enumerate()
for t in list_threads:
    print(t.name)

t1.join()
t2.join()
t3.join()

list_threads = enumerate()
for t in list_threads:
    print(t.name)

'''
One  is started
Two  is started
Three  is started
MainThread
One
Two
Three
One  is ended
Two  is ended
Three  is ended
MainThread
'''

# is_alive() method demo program
from threading import *
import time
def disp():
    name = current_thread().name
    print(name, 'is   started')
    time.sleep(3)
    print(name, '   is    ended')
t1 = Thread(target=disp, name='One')
t2 = Thread(target=disp, name='Two')
t3 = Thread(target=disp, name='Three')
t1.start()
t2.start()
t3.start()
print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())
t1.join()
t2.join()
t3.join()
print(t1.is_alive())
print(t2.is_alive())
print(t3.is_alive())

'''
One is   started
Two is   started
Three is   started
True
True
True
One   is    ended
Two   is    ended
Three   is    ended
False
False
False
'''

# Find outputs (Home work)
from threading import *
import time
def table(n):
    print('Table : ', n)
    for i in range(1, 11):
        print(f'{n} * {i}    =   {n * i}')
        time.sleep(1)
t1 = Thread(target=table, args=(7,))
t2 = Thread(target=table, args=(4,))
t1.start()
t2.start()

'''
Table :  7
Table :  4
7 * 1    =   7
4 * 1    =   4
7 * 2    =   14
4 * 2    =   8
7 * 3    =   21
4 * 3    =   12
7 * 4    =   28
4 * 4    =   16
7 * 5    =   35
4 * 5    =   20
7 * 6    =   42
4 * 6    =   24
7 * 7    =   49
4 * 7    =   28
7 * 8    =   56
4 * 8    =   32
7 * 9    =   63
4 * 9    =   36
7 * 10    =   70
4 * 10    =   40
'''