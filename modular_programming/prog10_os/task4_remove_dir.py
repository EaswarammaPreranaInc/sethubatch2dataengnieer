'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of the directory

Enter  directory  name  (or)  path :  temp
Directory  temp is removed

Enter  directory  name  (or)  path :  temp
Directory  temp  does not exist

Enter  directory  name  (or)  path :  sairam
Directory  sairam is non-empty
'''

import os
path = input('Enter  directory  name  (or)  path :  ')
try:
    os.rmdir(path)
    print(f'Directory {path} is removed')
except FileNotFoundError:
    print(f'Directory  {path}  does not exist')
except OSError:
    print(f'Directory {path} is non-empty')