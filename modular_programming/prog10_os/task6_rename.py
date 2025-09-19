'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or) directory name
'''

import os
try:
    os.rename('task1.py', 'task11.py')
    print(f'File rename successful')
except FileNotFoundError:
    print(f'The entered file is not present')