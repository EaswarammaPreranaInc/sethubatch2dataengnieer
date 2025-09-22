# Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
'''
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__',
 '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__',
  '__unraisablehook__', '_base_executable', '_baserepl', '_clear_internal_caches', '_clear_type_cache',
  '_current_exceptions', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding',
  '_framework', '_get_cpu_count_config', '_getframe', '_getframemodulename', '_git', '_home',
  '_is_gil_enabled', '_is_interned', '_setprofileallthreads', '_settraceallthreads', '_stdlib_dir',
  '_vpath', '_xoptions', 'activate_stack_trampoline', 'addaudithook', 'api_version', 'argv', 'audit',
  'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder',
  'call_tracing', 'copyright', 'deactivate_stack_trampoline', 'displayhook', 'dllhandle',
  'dont_write_bytecode', 'exc_info', 'excepthook', 'exception', 'exec_prefix', 'executable', 
 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 
 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 
 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
  'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace',
  'getunicodeinternedsize', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 
 'int_info', 'intern', 'is_finalizing', 'is_stack_trampoline_active', 'maxsize', 'maxunicode', 
 'meta_path', 'modules', 'monitoring', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache',
  'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 
 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile',
  'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 
 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
  'warnoptions', 'winver']
 ['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone',
  'asctime', 'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic',
  'monotonic_ns', 'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 
 'strftime', 'strptime', 'struct_time', 'thread_time', 'thread_time_ns', 'time', 'time_ns', 
 'timezone', 'tzname']
 ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh',
  'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 
 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp',
  'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm',
  'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 
 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 
 'trunc', 'ulp']
'''





# Find  outputs  (Home  work)
import  cal
print(dir(cal))
'''
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
 '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''





#  Find  outputs  (Home  work)
x = 25
def  disp():
	print('Hello') 
class  c1:
        def  m1(self):
                pass
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
             # '__name__', '__package__', '__spec__', 'c1', 'disp', 'x']
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>







# Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables
import cal
a = []
for i in dir(cal):
    if not (i.startswith('__') or i.endswith('__')):
        a.append(i)
print(a) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']





# Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
             # '__name__', '__package__', '__spec__']
print()
import  cal
print()
print(dir()) # # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
             # '__name__', '__package__', '__spec__']






# Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
             # '__name__', '__package__', '__spec__']
print()
from  cal  import  *
print()
print(dir()) 
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''





# Find  outputs
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
             # '__name__', '__package__', '__spec__']
print()
from  cal  import  add , mul , x
print()
print(dir()) 
'''
 ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
'''






# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path)) 
'''
Original  sys.path
c:\Users\ranji\OneDrive\Desktop\OneDrive\Naveen\callll
c:\Program Files\Python313\python313.zip
c:\Program Files\Python313\DLLs
c:\Program Files\Python313\Lib
c:\Program Files\Python313
C:\Users\ranji\AppData\Roaming\Python\Python313\site-packages
C:\Users\ranji\AppData\Roaming\Python\Python313\site-packages\win32
C:\Users\ranji\AppData\Roaming\Python\Python313\site-packages\win32\lib
C:\Users\ranji\AppData\Roaming\Python\Python313\site-packages\Pythonwin
c:\Program Files\Python313\Lib\site-packages
10
import  cal
'''





#9.
from  random  import  *
print(random()) # May be 0.5
print(randint(1 , 100)) # May be 5
print(uniform(1 , 100)) # May be 5.0
print(randrange(10)) # May be 5
print(randrange(1 , 11)) # May be 5
print(randrange(1 , 11 , 2)) # May be 5
list = [10 , 20 , 15 , 12 , 18]
print(choice(list)) # May be 15
print(choice('RAJESH')) # May be 'A'
set  =  {10 , 20 , 30 , 40}
#print(choice(set)) # Error due to set does not supports indexes






# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
Str = input("Enter a string : ") # Enter a string : Naveen
for i in range(10):
    print(random.choice(Str)) # e <nextline> n <nextline> e <nextline> N <nextline> n <nextline>n
                              # <nextline>v <nextline>n <nextline>e <nextline>e







# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
#1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits
import random
for i in range(10):
    print(chr(random.randint(64,90))+str(random.randrange(0,10))+
          chr(random.randint(64,90))+str(random.randrange(0,10))+chr(random.randint(64,90))+
          str(random.randrange(0,10)))
    
'''
F6Q3O7
R0B5Y9
C5U4Q4
W9N2W9
J7D2H8
N9C0X6
E2J9Y8
I2M0H0
U0Q5Z6
B6J6L1
'''






# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random 
list = eval(input("Enter a list : ")) # Enter a list : [10,20,30,40,50]
for i in range(10):
    print(random.choice(list))
'''
10
40
10
20
10
40
50
30
40
20
'''







# Write  a  program  to  generate  ten  six-digit  OTP's  (Home  work)
import random 
for i in range(10):
    s = ''
    for j in range(6):
        s += str(random.randint(0,9))
    print(s)
    '''
    461573
    414443
    333938
    392314
    319401
    232462
    105771
    863925
    549262
    655303
    '''






# Write  a  program to  open  any  website  from  gmail ,  google ,  rediff ,  ...   with  a  time  gap  of  5  to  20   sec
import random ,time, webbrowser
list = ['google.com' , 'rediff.com' , 'gmail.com' , 'amazon.com' , 'netflix.com']
for i in range(len(list)):
    webbrowser.open(list[i])
    time.sleep(random.randint(5,20))
  





# Write  a  program  to  implement  Rock , paper  and  scissors  game  between  user  and  computer
import random 
dict = {0 : 'Rock' , 1 : 'Paper' , 2 : 'Scissors'}
continuee = 'Y'
while continuee == 'Y':
    user = int(input("What  do  you  want  to  select  (0 - Rock , 1 - Paper , 2 - Scissors)  : "))
    print(f'User : {dict[user]}')
    computer = random.choice(dict)
    print(f'Computer : {computer}')
    if (user == 0 and computer == dict[0]) or (user == 1 and computer == dict[1]) or (user == 2 and computer == dict[2]):
        print("Draw")
    elif (user == 0 and computer == dict[1]) or (user == 1 and computer == dict[2]) or (user == 2 and computer == dict[0]):
        print("Computer wins")
    else:
        print("User wins")
    continuee = input("Continue  (  y / n)  ? ").upper()
print("End of the game")