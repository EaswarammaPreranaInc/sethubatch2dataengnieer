# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory

import os
path = input('Enter the Directory (or) Path:  ')
try:
    g = os.walk(path)
    while 1:
        try:
            tp = next(g)
            print(f'Directory path:  {tp[0]}')
            print(f'Sub Directories: {tp[1]}')
            print(f'Files:  {tp[2]}')
            print()
            print()
        except StopIteration:
            break
except FileNotFoundError:
    print(f'The exists Directory (or) path do not exists')