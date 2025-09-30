# Module  alias
print('Begin')
#How  to  import  cal  module  with   another  name  using  import  statement
import cal as calculator
print(calculator.x)                         #How  to  print  variable  'x'  of  cal   module
print(calculator.y)                         #How  to  print  variable  'y'  of  cal   module
print(calculator.add(10,7))                 #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(calculator.sub(10,7))                 #How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(calculator.mul(10,7))                 #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print(calculator.div(10,7))                 #How  to  call  div()  function  of  cal  module  by  passing  10  and  7
# print(cal . x)                            #error, once alias is given you can't use old name
# from  math  as m import *  #error, you can't give alias for module in from statement
#How  to  call  m1()  method  of  c1  class  in  cal  module
c = calculator.c1()
c.m1()