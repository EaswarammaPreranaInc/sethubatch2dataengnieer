# Member  alias
#How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
from cal import x as a, add as addition, mul as multiplication, c1 as c2
print(a)                           #How  to  print  variable  'x'  of  cal   module
# print(x)                         #error, once alias is given you can't use old name
print(addition(10,7))              #How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(multiplication(10,7))        #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
# print(add(10 , 7))             #error, once alias is given you can't use old name
# b = c1()                       #error, once alias is given you can't use old name
#How  to  call  m1()  method  of  class  c1  in  cal  module
c = c2()
c.m1()