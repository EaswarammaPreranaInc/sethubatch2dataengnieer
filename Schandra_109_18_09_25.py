#  Find  outputs  (Home  work)
import  sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))

['_breakpointhook', 'displayhook', 'doc', 'excepthook', 'interactivehook_',
'_loader', 'name', 'package', 'spec', 'stderr', 'stdin', 'stdout_',
'_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', 
'_enablelegacywindowsfsencoding', '_getframe', 'api_version', 'argv', 'audit', 'base_exec_prefix',
'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook',
'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags',
'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors',
'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv',
'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'pycache_prefix',
'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 
'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin',
'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']

['CLOCK_BOOTTIME', 'CLOCK_HIGHRES', 'CLOCK_MONOTONIC', 'CLOCK_MONOTONIC_RAW', 'CLOCK_PROCESS_CPUTIME_ID',
'CLOCK_PROF', 'CLOCK_REALTIME', 'CLOCK_THREAD_CPUTIME_ID', 'CLOCK_TAI', 'CLOCK_UPTIME_RAW',
'CLOCK_UPTIME_RAW_APPROX', 'PTHREAD_COND_T', 'PTHREAD_MUTEX_T', 'StructTime', '_doc_',
'_loader', 'name', 'package', 'spec_', '_exit', '_structure', 'altzone',
'asctime', 'clock_getres', 'clock_gettime', 'clock_gettime_ns', 'clock_settime', 'clock_settime_ns',
'ctime', 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns',
'perf_counter', 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime',
'strptime', 'struct_time', 'time', 'time_ns', 'timezone', 'tzname']

['_doc', 'loader', 'name', 'package', 'spec_', 'acos', 'acosh', 'asin',
'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 
'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin',
'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


#  Find  outputs  (Home  work)
import  cal
print(dir(cal))

['_doc', 'loader', 'name', 'package', 'spec_', 'add', 'mul', 'x', 'y']


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

['_annotations', 'builtins', 'cached', 'doc', 'loader', 'name_',
'_package', 'spec_', 'c1', 'disp', 'x']
<class 'list'>
<class 'builtin_function_or_method'>


#  Find  outputs
print(dir())
print()
import  cal
print()
print(dir())

['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_']
['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_', 'cal']


#  Find  outputs
print(dir())
print()
from  cal  import  *
print()
print(dir())

['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_']
['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_', 'add', 'mul', 'x', 'y']


#  Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())

['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_']
['_annotations', 'builtins', 'doc', 'loader', 'name', 'package_',
'_spec_', 'add', 'mul', 'x']


# sys . path  demo   program
import  sys
print('Original  sys.path')
for  x  in   sys . path:
	print(x)
print(len(sys . path))

Original  sys.path
<system-dependent list of paths printed>
N   # where N is the number of directories


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
print(choice(set))

0.27689976805483614
37
35.350117948451024
3
5
1
12
S
40


# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)

Enter  any  string :  Rama Rao
R
a
R
R
a
R
R
m


# Write  a  program to  generate  10  passwords  each  of  6 character  length  where
# 1st , 3rd , 5th  characters  are  alphabets  and  2nd , 4th , 6th  characters   are  digits

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


#  Rock , paper  and  scissors  game  (Home  work)

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
