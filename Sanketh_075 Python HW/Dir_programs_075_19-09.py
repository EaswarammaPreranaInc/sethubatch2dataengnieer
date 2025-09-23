# Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
from random import randint
import random 
for _ in range(10):
  print(random.randint(000000,999999))


# Find  outputs
import  os
os . system('dir') #shows the cwd
os . system('pause') #pauses the output
os . system('cls')#clear screen 
os . system('py  test.py') #excecutes the program test.py


#Write  a  program  to  create  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
import os
try:
     a = input("enter the name of directory or path of directory:")
     os.mkdir(a)
     print(f"{a} path has been created")
except FileExistsError:
     print(f"{a} path already exists")
except FileNotFoundError:
     print(f"{a} directory already exist")

'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os
try:
     a = input("enter the name of group of directory or path of directory:")
     os.makedirs(a)
     print(f"{a} path has been created")
except FileExistsError:
     print(f"{a} path already exists")
except FileNotFoundError:
     print(f"{a} directory already exist")
except ModuleNotFoundError:
     print(f"{a}module  doestnot exist") 


#Write  a  program  to  delete  a  directory.
#Input  is  directory  name  (or)  path  of  the  directory
[19-09-2025 12:04 PM] SRINIVAS GULLAPALLI: Write  a  program  to  delete  a  group  of  directories
#Input  is  directory  path
import os
a = input("Enter the path of the EMPTY directory to delete: ")
try:
   os.rmdir(a)
   print(f"\nSUCCESS: Empty directory '{a}' deleted successfully.")

except FileNotFoundError:
    print(f"\nERROR: Directory '{a}' was not found.")

except OSError as e:
    if 'Directory not empty' in str(e):
        print(f"\nERROR: Directory '{a}' is NOT empty.")
    else:
        print(f"\nAn OS error occurred: {e}")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

#Program to remove all the directories
import os
a = input("Enter the path of the EMPTY directory to delete: ")
try:
   os.removedirs(a)
   print(f"\nSUCCESS: Empty directory '{a}' deleted successfully.")

except FileNotFoundError:
    print(f"\nERROR: Directory '{a}' was not found.")

except OSError as e:
    if 'Directory not empty' in str(e):
        print(f"\nERROR: Directory '{a}' is NOT empty.")
    else:
        print(f"\nAn OS error occurred: {e}")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")



#Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
#Input :  Directory  (or)  path
#Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories

a = input("enter a directory path: ")
file_list=[]
dire_list=[]
try:
    all_elements = os.listdir(a)
    for x in all_elements:
        if '.' in x:
            file_list.append(x)
        else:
            dire_list.append(x)
    print(file_list)
    print(dire_list)
except FileNotFoundError:
    print(f"The directory '{a}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")



# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory