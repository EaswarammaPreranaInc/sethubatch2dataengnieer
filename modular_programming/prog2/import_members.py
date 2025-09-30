# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin')
from cal import *                   #How  to  import  all  the  members  of  cal  module
print(x)                            #How  to  print  variable  'x'  of  cal   module
print(y)                            #How  to  print  variable  'y'  of  cal   module
# print(cal . x)                    # error, module is not imported   
print(add(10,7))                    #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(sub(10,7))                    #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(mul(10,7))                    #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(div(10,7))                    #How  to  call  div()  function  of  cal  module  by  passing  10  and  7
# print(cal . add(x , y))           #error, module is not imported                                 
b = c1()                            #How  to  call  m1()  method  of  class  c1  in  cal  module
b.m1()