'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of the directory

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2 created

Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already exists


Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad created

'''
import os
dirname = input('Enter  directory  name  (or) path:   ')
try:
    os.mkdir(dirname)
    print(f'Directory {dirname} created')
except FileExistsError:
    print(f'Directory {dirname} already exists')