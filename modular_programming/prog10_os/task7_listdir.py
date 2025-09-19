'''
Write  a program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the directories
'''

import os
path = input('Enter Directory (or) path:  ')
try:
    lst = os.listdir(path)
    files = []
    dirs = []
    for x in lst:
        if '.' in x:
            files.append(x)
        else:
            dirs.append(x)
    print(f'List of Files: {files}')
    print(f'List of Directories:  {dirs}')
except FileNotFoundError:
    print(f'The entered Directory (or) path do not exist')