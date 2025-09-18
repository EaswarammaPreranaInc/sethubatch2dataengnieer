# Store  sample.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import sys
#How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys.path))
# How  to  append  c:\sairam  folder  to  sys.path
sys.path.append('c:\\sairam')
# How  to  print  number  of  directories  (or)  folders  in  sys.path
print(len(sys.path))
# How  to  print  object  'x'  of  sample   module  which  is  in  c:\sairam  folder
i = sys.path.index('c:\\sairam')
print(sys.path[i].x)
# How  to  call   function  f1()  of  sample  module  which  is  in  c:\sairam  folder
print(sys.path[i].f1())
# How  to  call   method  m1()  of  class  c1  of  sample  module  which  is  in  c:\sairam folder
c = sys.path[i].c1()
c.m1()