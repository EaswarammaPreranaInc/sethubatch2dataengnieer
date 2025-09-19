'''
Write  a  program  to  create  a  group  of  directories.
Input : a/b/c

Enter  directory  path :  a/b/c
Directory  (or) directories created
'''

import os
dirpath = input('Enter  directory  path :  ')
try:
    os.makedirs(dirpath)
    print(f'Directory (or) directories created')
except FileExistsError:
    print(f'Directory (or) directories already exists')
