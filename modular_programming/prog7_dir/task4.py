'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  ---> True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a = []
for x in dir(cal):
    if not x.startswith('__') and not x.endswith('__'):
        a.append(x)
print(a)
'''
['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''