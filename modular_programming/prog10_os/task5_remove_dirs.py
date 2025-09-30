'''
Write  a  program  to  delete  a  group  of  directories
Input  is directory path
'''
import os
path = input('Enter the path to remove directories:  ')
try:
    os.removedirs(path)
    print(f'Directories in {path} removed')
except FileExistsError:
    print(f'Directory {path} already exists')
except OSError:
    print(f'Directory {path} is not empty')