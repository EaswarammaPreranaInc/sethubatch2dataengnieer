# cal.py
def  add(a , b):
	return  a + b
def  sub(a , b):
	return  a - b
def  mul(a , b):
	return  a * b
def  div(a , b):
	return  a / b
class    c1:
	def    m1(self):
		pass
#End  of  the  class
x = 100
y = 200
if  _name_ ==  '_main_':
	print('Hyd')
	print('Sec')
	print('Cyb')


'''
1) What  is  the  module  name ?  --->  cal

2) py  cal.py
    What  is  the  value  of  _name_ ?  ---> '_main_'
    What  are  the  outputs ?  --->  Hyd ,  Sec  and  Cyb  becoz  if  condition  is  True

3) import  cal
    What  is  the  value  of  _name_ ?  ---> The  imported  module  name  i.e. 'cal'
	What  are  the  outputs ?  ---> Nothing  becoz  if  condition  is   False
'''


#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

Output :
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home', '_is_gil_enabled', '_is_interned', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir', '_vpath', '_xoptions', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dllhandle', 
'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getunicodeinternedsize', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']


['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#  Find  outputs  (Home  work)
import  cal
print(dir(cal))

Output :
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())
print(type(dir()))
print(type(dir))

Output :
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>


'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''

program :
import cal1
a=[]
for x in dir(cal1):
    if x.startswith('__') != True:
        a.append(x)
print(a)

Output :
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

Output :
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal1']


#  Find  outputs
print(dir())
print()
from  cal1 import  *
print()
print(dir())

Output :
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']


#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

Output :
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
#import  cal1

Output :
Original  sys.path
a:\PYTHON
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\python313.zip
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\DLLs
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0
C:\Users\DELL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages
C:\Users\DELL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\win32
C:\Users\DELL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\win32\lib
C:\Users\DELL\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\site-packages\Pythonwin
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2032.0_x64__qbz5n2kfra8p0\Lib\site-packages
10


# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  append  c:\sairam  folder  to  sys.path
How  to  print  number  of  directories  (or)  folders  in  sys.path
How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam  folder

Output :

x = 100      
def f1():
    print("Hello from f1() in sample module")
class c1:
    def m1(self):
        print("Hello from m1() in class c1 of sample module")
import sys

# (a) Print number of directories initially in sys.path
print("Before append -> Directories in sys.path:", len(sys.path))

# (b) Append c:\sairam folder to sys.path
sys.path.append(r"c:\sairam")

# (c) Print number of directories again
print("After append  -> Directories in sys.path:", len(sys.path))

# (d) Import the sample module
import sample

# (e) Print object x of sample module
print("sample.x =", sample.x)

# (f) Call function f1() of sample module
sample.f1()

# (g) Call method m1() of class c1 of sample module
obj = sample.c1()
obj.m1()



from  random  import  *
print(random()) # 0.5
print(randint(1 , 100)) # 5
print(uniform(1 , 100)) # 40.65 
print(randrange(10)) # 7
print(randrange(1 , 11)) # 4
print(randrange(1 , 11 , 2)) # 5
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # 20
print(choice('RAJESH')) # 'R'
set  =  {10 , 20 , 30 , 40}
print(choice(set)) # Error


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

# program
from  random  import  choice
n=input("Enter any Name :")
for i in range(1,11):
    print(choice(n))
Enter  any  string :  Rama Rao
R

a
R
R
a
R
R
m

Write  a  program to  generate  10  passwords  each  of  6 character  length  where
1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

# program
from random import choice
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b='0123456789'
for i in range(1,11):
    print(choice(a)+choice(b)+choice(a)+choice(b)+choice(a)+choice(b))


Output :
U7U2X8
V9I6X8
G4M8S2
M4U3C3
I7K2B8
F0E9Q1
Y8H8L7
K1U5S0
W7G0J3
Y9B9J6

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)

# program
from random import choice
n=eval(input("Enter any list :"))
for i in range(1,11):
    print(choice(n))

Enter a List : [25,10.8,'Hyd',True,3+4j,None]
True
Hyd
Hyd
None
Hyd
(3+4j)
None
True
25
10.8

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

# program
from random import choice
a='0123456789'
for i in range(1,11):
    print(choice(a)+choice(a)+choice(a)+choice(a)+choice(a)+choice(a))

# Output :
700690
664735
472299
820818
886311
912752
323114
971162
930848
404338

'''
Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

1) What  does  open('http://google.com')  do ?  ---> Opens  google.com  website

2) Where  is  open()  function  defined  ?  ---> In  webbrowser  module

3) list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']

4) Provide  a  time  gap  of  5  to  20 sec  between  the  websites
'''

# program 
from random import choice
import time
a=['https://www.youtube.com/watch?v=FGi8cOnAJHM','https://testbook.com/','https://www.youtube.com/','https://www.freejobalert.com/','https://www.freejobalert.com/']
for i in range(1,1000):
    print(choice(a))
    time.sleep(20)
    


'''
(Home  work)
Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer

1) What  is  the  result  if  user  input  and  computer  random  number  are  same  ?  ---> Draw

2) What  is  the  result  if  computer  selects  paper  and  user  input  is  rock ?  --->
																												Computer  wins  becoz  parer  dominates  rock

3) What  is  the  result  if  computer  selects  scissors  and  user  input  is  paper ?  --->
																										Computer  wins  becoz  scissors  dominates  paper

4) What  is  the  result  if  computer  selects  rock  and  user  input  is  scissors ?  --->
																										Computer  wins  becoz  rock  dominates  scissors

5) What  is  the  result  in  all  other  cases  ?  --->  User  wins
'''
# program
import random
print("Rock – Paper – Scissors Game")
print("0 - Rock , 1 - Paper , 2 - Scissors")
choices = ["Rock", "Paper", "Scissors"]
while True:
    user = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    print("User   :", choices[user])
    comp = random.randint(0, 2)
    print("Computer :", choices[comp])
    if user == comp:
        print("Draw")
    elif (comp == 1 and user == 0) or (comp == 2 and user == 1) or (comp == 0 and user == 2):
        print("Computer wins")
    else:
        print("User wins")
    ch = input("Continue ( y / n ) ? ").lower()
    if ch != 'y':
        print("End of the game")
        break


What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1
User  :   Paper
Computer  :   Rock
User  wins
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  2
User  :   Scissors
Computer  :   Scissors
Draw
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  0
User  :   Rock
Computer  :   Rock
Draw
Continue  (  y / n)  ?  y
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :  1
User  :   Paper
Computer  :   Scissors
Computer  wins
Continue  (  y / n)  ?  n
End  of  the  game
