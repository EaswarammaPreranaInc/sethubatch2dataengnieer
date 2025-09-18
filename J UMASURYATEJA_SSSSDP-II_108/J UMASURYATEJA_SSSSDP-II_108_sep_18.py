import sys, time, math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
'''

'_breakpointhook', 'displayhook', 'doc', 'excepthook', 'interactivehook', 'loader', 'name', 'package', 'spec', 'stderr', 'stdin', 'stdout', 'unraisablehook_', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_vpath', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'ps3', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']


['STRUCT_TM_ITEMS', 'doc', 'loader', 'name', 'package', 'spec_', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']

['_doc', 'loader', 'name', 'package', 'spec_', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

'''
#Find  outputs  (Home  work)
import cal
print(dir(cal))
# ['_builtins', 'cached', 'doc', 'file', 'loader', 'name', 'package', 'spec_', 'add', 'mul', 'x']

'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
'''
import cal
a = []
for name in dir(cal):
    if not name.startswith('') and not name.endswith(''):
        a.append(name)
print(a)
# ['add', 'mul', 'x']

# 1) '_name'.startswith('_')  ---> True
# 2) '_spec'.endswith('_')    ---> False
# 3) 'spec_'.startswith('_')  ---> False

# 4) Done in the program above


---

#  Find  outputs
print(dir())
print()
import cal
print()
print(dir())

# Before import shows current names like ['_annotations', 'builtins_', ...]
# After import shows same + 'cal'


---


#  Find  outputs
print(dir())
print()
from cal import *
print()
print(dir())

# Before import shows current names
# After import shows current names + all names inside cal (like add, mul, x)


---

#  Find  outputs
print(dir())
print()
from cal import add, mul, x
print()
print(dir())

# Before import shows current names
# After import shows current names + add, mul, x



#  Store sample.py module in c:\sairam folder before the program is executed (Home work)
import sys
print(len(sys.path))                      # Number of directories in sys.path
sys.path.append(r'c:\sairam')              # Append folder to sys.path
print(len(sys.path))                      # Number of directories after append
import sample
print(sample.x)                           # Print object x of sample module
sample.f1()                               # Call function f1() of sample module
obj = sample.c1()                         
obj.m1()                                   # Call method m1() of class c1

x = 25
def disp():
    print('Hello')
class c1:
    def m1(self):
        pass
print(dir())
print(type(dir()))
print(type(dir))
'''
['In', 'Out', '', '', '', '_builtin', 'builtins', 'doc', 'loader', 'name', 'package', 'session', 'spec_', '_dh', '_i', '_i1', '_i2', '_i3', '_ih', '_ii', '_iii', '_oh', 'c1', 'disp', 'exit', 'get_ipython', 'math', 'open', 'quit', 'sys', 'time', 'x']
<class 'list'>
<class 'builtin_function_or_method'>
'''

from  random  import  *
print(random())
print(randint(1 , 100))
print(uniform(1 , 100))
print(randrange(10))
print(randrange(1 , 11))
print(randrange(1 , 11 , 2))
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))
print(choice('RAJESH'))
set  =  {10 , 20 , 30 , 40}
#print(choice(set))#error
'''
0.601541730203485
33
17.96925518667453
1
1
5
18
S
'''
from random import *
for i in range(10):
    print(choice('Rama Rao'))
'''
R
a
a
 
R
a
R
m
R
'''
from random import *
def generated_pass():
    password = ""
    for i in range(1,7):
        if i%2!=0:
            password += chr(randint(65,90))
        else:
            password += str(randrange(10))
    return password
print(generated_pass())#P8F7I5

a = [25,10.8,'Hyd',True,3+4j,None]
for i in range(10):
    print(choice(a))
'''
25
True
Hyd
None
25
25
Hyd
(3+4j)
25
None
'''

from random import *
for i in range(10):
    print(randint(100000,999999))
'''
542907
426453
486221
217527
668326
690148
238174
726610
694698
199320
'''

import webbrowser
import time
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(len(list)):
    url = "https://www." + list[i]
    webbrowser.open(url)
    time.sleep(10)


from random import *

dicti = {0:"Rock",1:"Paper",2:"Scissors"}
while True:
    user = int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  :"))
    print("User: ",dicti[user])
    comp = randrange(3)
    print("Computer: ",dicti[comp])
    if (user==comp):
        print("Tie")
    elif ((user==0) and (comp==2)) or ((user==1) and (comp==0)) or ((user==2) and (comp==1)):
        print("User wins")
    else:
        print("Computer wins")
    choice = input("Continue (y/n)? ").lower()
    if choice != 'y':
        print("End of  the game")
        break
'''
What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  : 2
User:  Scissors
Computer:  Scissors
Tie
Continue (y/n)?  n
End of  the game
'''
