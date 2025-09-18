# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle
from cal import x, add, mul, c1
print(x)                                   #How  to  print  variable  'x'  of  cal   module
# print(y)                                 #error, y is not imported
# print(cal . x)                           #error, module is not imported
print()                                    #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
# print(sub(10 , 7))                       #error, sub is not imported
print(mul(10,7))                           #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
# print(div(10 , 7))                       #error, div is not imported
#How  to  call  m1()  method  of  class  c1 in cal module
c = c1()
c.m1()