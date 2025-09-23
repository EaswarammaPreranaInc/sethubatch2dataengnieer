# Save  in  any  file  of  cwd
import   p1
import  p1 . mod1
from   p1   import  mod1
from   p1 . mod1  import   *
import p1.__init__
'''
OUTPUT:
_init_   module  of  package  p1  is  executed
_init_   module  of  package  p1.__init__  is  executed
'''