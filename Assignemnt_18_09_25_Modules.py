#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
#output:
18_09_25.py
#output:
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_getquickenedcount', '_git', '_home', '_stdlib_dir', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']

['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
#  Find  outputs  (Home  work)
import  cal
print(dir(cal))
#output:
'''['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']'''

#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello')
class  c1:
        def  m1(self):
                pass
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir()))#<class 'list'>
print(type(dir))#<class 'builtin_function_or_method'>


#Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

import cal   

a = []

for name in dir(cal):
    if not (name.startswith("__") and name.endswith("__")):
        a.append(name)

print("Members of cal module without environment variables:")
for item in a:
    print(item)

print("\nList a =", a)
'''#output:
Members of cal module without environment variables:
add
c1
div
mul
sub
x
y
List a = ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']'''

#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
import  cal
print()
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal']

#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']

#  Find  outputs
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir())#['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']

# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))
'''#output:
Original  sys.path
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311\Lib\idlelib
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311\python311.zip
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311\DLLs
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311\lib
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311
C:\Users\N.Jhansi\AppData\Roaming\Python\Python311\site-packages
C:\Users\N.Jhansi\AppData\Roaming\Python\Python311\site-packages\win32
C:\Users\N.Jhansi\AppData\Roaming\Python\Python311\site-packages\win32\lib
C:\Users\N.Jhansi\AppData\Roaming\Python\Python311\site-packages\Pythonwin
C:\Users\N.Jhansi\AppData\Local\Programs\Python\Python311\lib\site-packages
#10'''

from  random  import  *
print(random())#0.61
print(randint(1 , 100))#40
print(uniform(1 , 100))#96.17
print(randrange(10))#9
print(randrange(1 , 11))#10
print(randrange(1 , 11 , 2))#3
list = [10 , 20 , 15 , 12 , 18]#
print(choice(list))#12
print(choice('RAJESH'))#E
set  =  {10 , 20 , 30 , 40}
print(choice(set))#TypeError: 'set' object is not subscriptable 

# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
from random import *
s=input("Enter the string: ")
for i in range(10):
    print(choice(s))
#output:
Enter the string: Rama Rao
 
a
m
R
a
a
R
a
R
m

#Write  a  program to  generate  10  passwords  each  of  6 character  length  where 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
from random import *
import random
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
for _ in range(10):
    password = ""
    for i in range(6):
        if i % 2 == 0: 
            password += random.choice(alphabets)
        else:            
            password += random.choice(digits)
    print(password)
'''#output
U0w5e0
R8o5g9
o2P2P0
w7t9d8
Y4e7l5
e8r2Q3
P9r0B1
R9i7M9
f6b0I3
X7V2C9'''

# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
from random import *
l=eval(input("Enter the list elemenst: "))
for i in range(10):
    print(choice(l))
#output:
'''Enter the list elemenst: [25,'siri',True,3+4j,10.8]
25
True
siri
(3+4j)
(3+4j)
(3+4j)
(3+4j)
(3+4j)
siri
25'''

# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)

import random
for _ in range(10):
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    print(otp)
'''#output:
384987
760076
682420
942269
174677
714825
300160
998046
785254
102045'''


#Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec

import webbrowser
import time
import random

sites = ['google.com', 'rediff.com', 'gmail.com', 'amazon.com', 'netflix.com']

def open_sites_once(site_list):
    for site in site_list:
        # ensure URL has scheme
        if not site.startswith(('http://', 'https://')):
            url = 'http://' + site
        else:
            url = site

        print(f"Opening {url}")
        webbrowser.open(url)             # opens the site in the default browser
        gap = random.randint(5, 20)      # random gap between 5 and 20 seconds (inclusive)
        print(f"Waiting {gap} seconds...\n")
        time.sleep(gap)

if __name__ == "__main__":
    try:
        open_sites_once(sites)
        print("All sites opened.")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Stopping.")

#(Home  work)
#Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer



import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    user = int(input("What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : "))
    print("User  :  ", choices[user])

    computer = random.randint(0, 2)
    print("Computer  :  ", choices[computer])

    # Decide result
    if user == computer:
        print("Draw")
    elif (computer == 0 and user == 2) or (computer == 1 and user == 0) or (computer == 2 and user == 1):
        print("Computer wins")
    else:
        print("User wins")

    # Ask to continue
    ch = input("Continue  ( y / n )  ?  ").lower()
    if ch != 'y':
        print("End of the game")

'''#output:    
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 0
User  :   Rock
Computer  :   Rock
Draw
Continue  ( y / n )  ?  y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 2
User  :   Scissors
Computer  :   Rock
Computer wins
Continue  ( y / n )  ?  y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 2
User  :   Scissors
Computer  :   Scissors
Draw
Continue  ( y / n )  ?  y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 1
User  :   Paper
Computer  :   Paper
Draw
Continue  ( y / n )  ?  y
What do you want to select (0 - Rock , 1 - Paper , 2 - Scissors) : 1
User  :   Paper
Computer  :   Rock
User wins
        break'''


































