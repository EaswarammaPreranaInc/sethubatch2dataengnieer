# Program 1

def f1():
    try:
        print('f1  function')               # output: f1  function
        raise ValueError('Hyd')
        print('Hi')
    finally:
        print("f1's  finally")              # output: f1's  finally
    print('End  of  f1  function')

def f2():
    try:
        print('f2  function')               # output: f2  function
        return
        print('Hello')
    finally:
        print("f2's  finally")              # output: f2's  finally
    print('End  of  f2  function')

def f3():
    try:
        print('f3  function')               # output: f3  function
        raise KeyError(25)
        print('Hello')
    except KeyError as msg:
        print('Caught  by  f3  function :  ', msg)   # output: Caught  by  f3  function :   25
    finally:
        print("f3's  finally")              # output: f3's  finally
    print('End of f3 function')             # output: End of f3 function

def f4():
    try:
        print('f4 function')                 # output: f4 function
        exit()
    finally:
        print("f4's  finally")                # output: f4's  finally
    print('End of f4 function')

# End of all the functions

try:
    print('Begin')                              # output: Begin
    f1()
    print('Hello')
except ValueError as msg:
    print('ValueError is caught outside : ', msg)  # output: ValueError is caught outside :  Hyd

f2()
f3()
try:
    f4()
finally:
    print('Outside  finally')                   # output: Outside  finally
print('End  of  the  program')






# Program 2

import sys

def f1():
    try:
        print('f1  function')                   # output: f1  function
        raise ValueError('Hyd')
        print('Hi')
    finally:
        print("f1's  finally")                  # output: f1's  finally
    print('End  of  f1  function')

def f2():
    try:
        print('f2  function')                   # output: f2  function
        return
        print('Hello')
    finally:
        print("f2's  finally")                  # output: f2's  finally
    print('End  of  f2  function')

def f3():
    try:
        print('f3  function')                   # output: f3  function
        raise KeyError(25)
        print('Hello')
    except KeyError as msg:
        print('Caught  by  f3  function :  ', msg)  # output: Caught  by  f3  function :   25
    finally:
        print("f3's  finally")                  # output: f3's  finally
    print('End  of  f3  function')               # output: End  of  f3  function

def f4():
    try:
        print("f4  function")                   # output: f4  function
        sys.exit()
    finally:
        print("f4's  finally")                   # output: f4's  finally
    print('End  of  f4  function')

# End of all the functions

try:
    print('Begin')                                # output: Begin
    f1()
    f2()
    f3()
    f4()
    print('Hello')
except ValueError as msg:
    print('ValueError is caught outside : ', msg)  # output: ValueError is caught outside :   Hyd
print('End  of the  program')







# Program 3

def f1():
    try:
        print('f1  function')                     # output: f1  function
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught  KeyError')                  # output: Caught  KeyError
        raise Exception()
    except:
        print('Sec')
    finally:
        print("f1's  finally")                     # output: f1's  finally
    print('End  of  f1  function')

# End of the function
try:
    print('Begin')                                   # output: Begin
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except Exception:
    print('Recaught  Exception')                      # output: Recaught  Exception
finally:
    print('Outside  finally')                         # output: Outside  finally
print('End  of the  program')                         # output: End  of the program







# Program 4

def f1():
    try:
        print('f1  function')                         # output: f1  function
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught  KeyError')                      # output: Caught  KeyError
        raise NameError()
    except NameError:
        print('Sec')
    finally:
        print('f1 finally')                            # output: f1 finally
    print('End  of  f1 function')

# outside function
try:
    print('Begin')                                     # output: Begin
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except Exception:
    print('Recaught  Exception')                        # output: Recaught  Exception
except NameError:
    print('Caught  Name Error  outside')
finally:
    print('Outside  finally')                           # output: Outside  finally
print('End of the program')                             # output: End of the program







# Program 5

def f1():
    try:
        print('f1  function')                         # output: f1  function
        raise KeyError()
        print('Hyd')
    except KeyError:
        print('Caught  KeyError')                      # output: Caught  KeyError
        raise NameError()
    except NameError:
        print('Sec')
    finally:
        print('f1 finally')                            # output: f1 finally
    print('End  of  f1 function')

# outside function
try:
    print('Begin')                                     # output: Begin
    f1()
    print('Hello')
except ValueError:
    print('Hello')
except KeyError:
    print('Recaught  KeyError')
finally:
    print('Outside  finally')                           # output: Outside  finally
print('End of the program')







# Program 6

try:
    print('try')                                     # output: try
    print(7 / 0)
except:
    print('except')                                   # output: except
else:
    print('else')
finally:
    print('finally')                                  # output: finally
print('End')                                           # output: End







# Program 7

try:
    print('try')                                     # output: try
except:
    print('except')
else:
    print('else')                                     # output: else
finally:
    print('finally')                                  # output: finally
print('End')                                           # output: End









# Program 8

try:
    print('try')                                     # output: try
else:
    print('else')
finally:
    print('finally')                                  # output: finally
print('End')                                           # output: End
```

# output: **SyntaxError** (invalid because `try` has no `except` block)






# Program 9

try:
    print('try')                                     # output: try
except:
    print('except')
else:
    print('else1')
else:
    print('else2')
finally:
    print('finally')
print('end')
# output: **SyntaxError** (two `else` clauses not allowed)






# Program 10

try:
    print('try')                                     # output: try
else:
    print('else')
except:
    print('except')
finally:
    print('finally')
print('end')

# output: **SyntaxError** (ordering of else/except incorrect)




### Program 11

try:
    print('try')                                     # output: try
except:
    print('except')
if 10 > 20:
    print('if')
else:
    print('else')                                    # output: else







# Program 12

def f1():
    try:
        return 10 + '20'
    except:
        return 10 + 20                            # output: 30

print(f1())                                        # output: 30








# Program 13

def f1():
    try:
        return 10                                 # output: 10
    except:
        return 20
    else:
        return 30

print(f1())                                        # output: 10







# Program 14

def f1():
    try:
        return 10 + '20'
    except:
        return 20                                 # output: 20
    else:
        return 30

print(f1())                                        # output: 20







# Program 15

def f1():
    try:
        pass
    except:
        return 20
    else:
        return 30                                 # output: 30

print(f1())                                        # output: 30







# Program 16

def f1():
    try:
        return 10                                 # would return 10
    except:
        return 20
    else:
        return 30
    finally:
        return 40                                 # output: 40 (finally overrides)

print(f1())                                        # output: 40









# Program 17

# Input scenario:
# 1) input = 24
# 2) input = 25

try:
    x = eval(input('Enter  any  number  :  '))
    assert x >= 25, 'Hyd'
    print('Sec')                                    # output: Sec (for input >=25)
except AssertionError as msg:
    print(msg)                                       # output: Hyd (for input <25)
print('End')                                          # output: End
```

* If input is `24`:

  Hyd
  End

* If input is `25`:

  Sec
  End
  ```





# Program 18

# Input scenario:
# 1) input = 24
# 2) input = 25

try:
    x = eval(input('Enter  any  number  :  '))
    assert x >= 25
    print('Sec')                                    # output: Sec (for input >=25)
except AssertionError as msg:
    print(msg)                                       # output: (empty) for input <25
print('End')                                          # output: End
'''

* If input is `24`:

  End

* If input is `25`:

  Sec
  End
'''




# Program 19

try:
    print('Outer   try')                             # output: Outer   try
    try:
        print('Inner    try')                         # output: Inner    try
        print(7 / 0)
        int('Hyd')
        'Hyd'[5]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE   of   inner   try')               # output: ZDE   of   inner   try
        int('Ten')
    except ValueError:
        print('ValueError  of  inner   try')
    finally:
        print('Inner  try  finally')                  # output: Inner  try  finally
    print('End  of  inner  try')
except ValueError:
    print('ValueError  of  outer  try')
except IndexError:
    print('IndexError  of  outer  try')
except:
    print('default  except  of  outer  try')           # output: default  except  of  outer  try
finally:
    print('Outer  try  finally')                        # output: Outer  try  finally
print('End  of  outer  try')                            # output: End  of  outer  try









# Program 20

try:
    print('Outer  try')                              # output: Outer  try
    try:
        print('Inner  try')                           # output: Inner  try
        int('Hyd')
        'Hyd'[5]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE  of  inner  try')
        int('Ten')
    except ValueError:
        print('ValueError  of  inner  try ')          # output: ValueError  of  inner  try 
    finally:
        print('Inner  try  finally')                   # output: Inner  try  finally
    print('End  of  inner  try')                        # output: End  of  inner  try
except ValueError:
    print('ValueError  of  outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default except of outer try')
finally:
    print('Outer try finally')                         # output: Outer try finally
print('End of outer try')                               # output: End of outer try








# Program 21

try:
    print('Outer  try')                              # output: Outer  try
    try:
        print('Inner  try')                           # output: Inner  try
        'Hyd'[3]
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE  of  inner  try')
        int('Ten')
    except ValueError:
        print('ValueError  of  inner  try ')
    finally:
        print('Inner  try  finally')                   # output: Inner  try  finally
    print('End  of  inner  try')
except ValueError:
    print('ValueError  of  outer  try')
except IndexError:
    print('IndexError  of  outer  try')                 # output: IndexError  of  outer  try
finally:
    print('Outer try finally')                          # output: Outer try finally
print('End  of  outer  try')                             # output: End  of  outer try









# Program 22

try:
    print('Outer  try')                              # output: Outer  try
    try:
        print('Inner  try')                           # output: Inner  try
        eval('Hyd')
    except ZeroDivisionError:
        print('ZDE  of  inner  try')
        int('Ten')
    except ValueError:
        print('ValueError  of   inner  try ')
    finally:
        print('Inner  try  finally')                   # output: Inner  try  finally
    print('End of inner try')
except ValueError:
    print('ValueError  of  outer try')
except IndexError:
    print('IndexError of outer try')
except:
    print('default  except  of  outer  try')           # output: default  except  of  outer  try
finally:
    print('Outer  try  finally')                        # output: Outer  try  finally
print('End  of  outer  try')                             # output: End  of  outer  try







# Program 23

try:
    print('Outer  try')                              # output: Outer  try
    try:
        print('Inner  try')                           # output: Inner  try
        print(10 + '20')
    except ZeroDivisionError:
        print('ZDE  of  inner  try')
        int('Ten')
    except ValueError:
        print('ValueError  of   inner  try ')
    finally:
        print('Inner  try  finally')                   # output: Inner  try  finally
    print('End  of inner try')
except ValueError:
    print('ValueError  of  outer try')
except IndexError:
    print('IndexError of outer try')
finally:
    print('Outer  try  finally')                        # output: Outer  try  finally
print('End  of  outer  try')                             # output: End  of  outer  try
# Note: A TypeError occurs (10 + '20'), caught by outer except default.








# Program 24

class MyError(BaseException):
    def _init_(self, y):
        self.a = y
        print('Constructor')
# End of the class

def compute(x):
    print(x)                                          # output: 10   (for compute(10))
    if x > 20:
        raise MyError(x)                              # output: 30   (for compute(30))
    print('Hello')

try:
    compute(10)                                        # prints 10 and Hello
    compute(30)                                        # prints 30, then raises MyError
except MyError as msg:
    print('Caught MyError outside  :  ', msg)         # output: Caught MyError outside  :   <MyError instance>
print('End')                                            # output: End








# Program 25

class MyError(NameError):
    def _init_(self):
        self.a = 25
        print('Constructor')
# End of the class

def compute(x):
    print(x)                                            # output: 30
    if x > 20:
        raise MyError()                                 # then raises
    print('Hello')

try:
    compute(30)                                          # prints 30 then exception
    compute(10)
except MyError as msg:
    print('Caught MyError outside  :  ', msg)           # output: Caught MyError outside  :   <MyError instance>
print('End')                                              # output: End






# Program 26

try:
    print(1)                                            # output: 1
    print(2)                                            # output: 2
    print(3)                                            # output: 3
except:
    print(4)
else:
    print(5)                                            # output: 5
finally:
    print(6)                                            # output: 6
print(7)                                                # output: 7







# Program 27

try:
    print(1)                                            # output: 1
    print(7 / 0)
    print(3)
except:
    print(4)                                            # output: 4
else:
    print(5)
finally:
    print(6)                                            # output: 6
print(7)                                                # output: 7








# Program 28

try:
    print(1)                                            # output: 1
    print(7 / 0)
    print(3)
except:
    int('Two')                                          # raises ValueError inside except
else:
    print(5)
finally:
    print(6)                                            # output: 6
print(7)







# Program 29

from threading import *
def f1():
    # How to print name of child thread
    pass
# output: (no output unless you implement the thread creation and printing)






# Program 30

from threading import *

def dummy():
    pass

t1 = Thread(target=dummy, name='Hyd')

t2 = Thread(target=dummy)

t1.start()
t2.start()

print("Main Thread Name:", current_thread().name)

print("t1 Thread Name:", t1.name)

print("t2 Thread Name:", t2.name)

current_thread().name = 'India'

t1.name = 'Sec'

t2.name = 'Cyb'

print("Modified Main Thread Name:", current_thread().name)
print("Modified t1 Thread Name:", t1.name)
print("Modified t2 Thread Name:", t2.name)

print("Number of Threads under execution:", active_count())

t1.join()
t2.join()









# Program 31

from threading import Thread, current_thread
from random import randint

def f1(n):
    ctr = 0
    s = current_thread().name
    while True:
        x = randint(1, 100)
        ctr += 1
        print(f'{s}  guess  {x}   in  attempt  :  {ctr}')
        if x == n:
            break
    print(f'{s}  finish  in  {ctr}  attempts')           # output: finish message per thread

t1 = Thread(target=f1, args=[75], name='Rama')
t2 = Thread(target=f1, args=[50], name='Sita')
t1.start()
t2.start()








# Program 32

from threading import *
def disp():
    for i in range(10):
        print('new  thread')                               # output: new  thread (10 times)
new = Thread(target=disp)
new.start()
new.join()
for i in range(10):
    print('main  thread')                                  # output: main  thread (10 times)








# Program 33

from threading import *
import time
def disp():
    for i in range(10):
        print('new  thread')                               # prints every 2 seconds
        time.sleep(2)
new = Thread(target = disp)
new.start()
new.join(10)
for i in range(10):
    print('main  thread')                                  # output: main  thread (10 times)








# Program 34

from threading import *
import time
def double():
    for i in range(1 , 7):
        print('Double : ', 2 * i)                           # output: Double :  2,4,6,8,10,12 (one per second)
        time.sleep(1)
def square():
    for i in range(1 , 7):
        print('Square : ', i * i)                           # output: Square : 1,4,9,16,25,36 (one per second)
        time.sleep(1)
start = time.time()
double()
square()
end = time.time()
print(end - start)                                           # output: ~12.0 (seconds)








# Program 35

from threading import *
import time
def display():
    name = current_thread().name
    print(name , ' is  started')                          # output: One/Two/Three is  started
    time.sleep(3)
    print(name , ' is  ended')                            # output: One/Two/Three is  ended

print(active_count())                                       # output: 1 (initially only main thread)
t1 = Thread(target = display , name = 'One')
t2 = Thread(target = display , name = 'Two')
t3 = Thread(target = display , name = 'Three')
print(active_count())                                       # output: 1
t1.start()
t2.start()
t3.start()
print(active_count())                                       # output: 4 (main + 3 threads)
t1.join()
t2.join()
t3.join()
print(active_count())                                       # output: 1 (back to only main thread)









# Program 36

from threading import *
import time
def disp():
    name = current_thread().name
    print(name , ' is  started')                            # output: One/Two/Three is  started
    time.sleep(3)
    print(name , '  is  ended')                             # output: One/Two/Three  is  ended

t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1.start()
t2.start()
t3.start()
list = enumerate()
for t in list:
    print(t . name)                                          # may error: wrong usage of enumerate
t1.join()
t2.join()
t3.join()
list = enumerate()
for t in list:
    print(t . name)                                          # may error similarly









# Program 37

from threading import *
import time
def   disp():
    name =  current_thread().name
    print(name , 'is   started')                             # output: One/Two/Three is   started
    time . sleep(3)
    print(name , '   is    ended')                            # output: One/Two/Three    is    ended
t1 = Thread(target = disp , name = 'One')
t2 = Thread(target = disp , name = 'Two')
t3 = Thread(target = disp , name = 'Three')
t1 . start()
t2 . start()
t3 . start()
print(t1 . is_alive())                                         # output: True (immediately after start)
print(t2 . is_alive())                                         # output: True
print(t3 . is_alive())                                         # output: True
t1 . join()
t2 . join()
t3 . join()
print(t1 . is_alive())                                         # output: False
print(t2 . is_alive())                                         # output: False
print(t3 . is_alive())                                         # output: False








# Program 38

from threading import *
import time
def   table(n):
    print('Table  :  ' , n)                                   # output: Table  :   7 (or 4)
    for i in range(1 , 11):
        print(f'{n}  *  {i}    =   {n * i}')                    # output: the multiplication table lines
        time . sleep(1)

t1 = Thread(target = table , args = (7,))
t2 = Thread(target = table , args = (4,))
t1 . start()
t2 . start()






