# Save  in  any  file  of  cwd
import   p1 #__init__   module  of  package p1 is  executed
import  p1 . mod1 #__init__   module  of  package p1 is  executed
from   p1   import  mod1 #__init__   module  of  package p1 is  executed
from   p1 . mod1  import   * # __init__   module  of  package p1 is  executed
import  p1 . __init__ #__init__   module  of  package p1 is  executed