'''
Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)

Output:
--------

258447
739842
112185
681428
054290
219889
056740
845508
384423
587572
'''
import random
for i in range(10):
    def numeric_otp(digits=6):
        return "".join(str(random.randint(0, 9)) for _ in range(digits))

    print("OTP: ", numeric_otp(6))




'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory


Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  created


Enter  directory  name  (or) path :  sssdc2
Directory  sssdc2  already  exists


Enter  directory  name  (or) path :  sssdc2/khairtabad
Directory  sssdc2/khairtabad  created
'''
import os
a=input("Enter  directory  name  (or) path : ")
try:
    os.mkdir('a')
    print(f"Directory {a} created")
except FileExistsError:
    print(f"Directory {a} already exists")
except FileNotFoundError:
    print("No such file or directory")



'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c


Enter  directory  path :  a/b/c
Directory  (or) directories  created
'''
import os
a=input("Enter  directory  name  (or) path : ")
try:
    os.makedirs(a)
    print(f"Directories {a} are created")
except FileExistsError:
    print(f"Directory {a} already exists")
except FileNotFoundError:
    print("No such file or directory")
'''



'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory


Enter  directory  name  (or)  path :  temp
Directory  temp  is  removed


Enter  directory  name  (or)  path :  temp
Directory  temp  does  not  exist


Enter  directory  name  (or)  path :  sairam
Directory  sairam  is  non-empty
'''
import os
a=input("Enter  directory  name  (or) path : ")
try:
    os.rmdir(a)
    print(f"Directories {a} deleted")
except OSError:
    print(f"Directory {a} not empty")
except FileNotFoundError:
    print(f"Director y {a} not found")


'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import os
a=input("Enter  directory  name  (or) path : ")
try:
    os.removedirs(a)
    print(f"Directories {a} deleted")
except FileExistsError:
    print(f"Directory {a} not empty")
except FileNotFoundError:
    print(f"Director {a} not found")


'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name
'''
import os
a=input("Enter  directory  name  (or) path : ")
b=input("New directory  name  (or) path : ")
try:
    os.rename(a,b)
    print(f"Directories {a} changed to {b}")
except FileExistsError:
    print(f"Directory {a} not empty")
except FileNotFoundError:
    print(f"Director {a} not found")


