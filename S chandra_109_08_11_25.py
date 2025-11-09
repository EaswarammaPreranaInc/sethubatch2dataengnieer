: # Find   outputs (Home  work)
from  itertools  import  count
c1 = count()
print('While  loop')
while   True:
        x = next(c1)
        if   x > 9:
                break
        print(x)
print('For  loop')
c2 = count()
for  x  in  c2:
	if  x  >  20:
		break
	print(x)
#end  of  for  loop
c3 = count()
print('Element :  ' , next(c3))
c4 = count()
print(*c4)
#######################
While  loop
0
1
2
3
4
5
6
7
8
9
For  loop
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
Element :   0
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ...
(infinite output continues forever)





: #  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
# End  of  the  function
a = count(start = 10)
disp(a)
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d)

########################

10	11	12	13	
10	15	20	25	
10	7.5	5.0	2.5	
0	1	2	3	





: #  Tricky  program
#  Find  outputs
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(cnt , list)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(cnt , list)
print('Next  element  :  ' , next(z4))

###########################
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(4, 10)
(5, 20)
(6, 15)
(7, 18)
Next  element :   (8, 10)
*z3 :   (9, 20) (10, 15) (11, 18)
Next  element  :   (12, 10)






: #  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')
while   True:
        try:
                print(next(z1))
        except  StopIteration:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))
##############################
While  loop
(10, 0)
(20, 1)
(15, 2)
(18, 3)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
Next  element :   (10, 8)
*z3 :   (20, 9) (15, 10) (18, 11)
Next  element  :  (10, 12)




: # Most  tricky  program
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4))
######################
while  loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for  loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
(8, 10)
(9, 20) (10, 15) (11, 18)
(10, 12)






: #  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
# End  of  the  function
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1))
disp(z1)
z2 = zip_longest(range(7) , list)
print(type(z2))
disp(z2)
##################
<class 'zip'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
<class 'itertools.zip_longest'>
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, None)
(5, None)
(6, None)






: #  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)

#################################
<class 'itertools.cycle'>
10
20
30
40
10
20
30
40
10
20
...
(infinite repeating forever)





: #  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)

#####################################
1st  repeat  object
25
25
25
2nd  repeat  object
Hyd
Hyd
Hyd
Hyd
Hyd
...
(infinite 'Hyd')






: # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
###################################
1
1





: # Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break

########################################
2 ** 0  → 1
2 ** 1  → 2
2 ** 2  → 4
2 ** 3  → 8
2 ** 4  → 16
2 ** 5  → 32
2 ** 6  → 64
2 ** 7  → 128
2 ** 8  → 256
2 ** 9  → 512






: #  Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)
###########################
Different  Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
Different   Permutations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'B')
('A', 'C', 'D')
('A', 'D', 'B')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'A', 'D')
('B', 'C', 'A')
('B', 'C', 'D')
('B', 'D', 'A')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'A', 'D')
('C', 'B', 'A')
('C', 'B', 'D')
('C', 'D', 'A')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'A', 'C')
('D', 'B', 'A')
('D', 'B', 'C')
('D', 'C', 'A')
('D', 'C', 'B')





: '''
Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

1) How  to  iterate  thru  to  each  each  line  of  the  file ?  --->  for  loop

2) Which  function  is  used  to  print  each  line ?  --->  print()

3) How  long  is  the  procedure  repeated ?  --->   Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  ---> read  mode
'''
import  os
def  disp(f):
	How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
# End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  call  disp()  function
How  to  close  the  file
##################################

'''
Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines
'''
import time
import os

def disp(f):
    ctr = 0                          # line counter
    for line in f:                   # iterate through each line of file
        print(line, end='')          # print each line (print() function)
        ctr += 1
        if ctr == 20:                # pause after every 20 lines
            ctr = 0
            input('\n---- Press ENTER to continue ----\n')
    print('\n---- End of File ----')

# End of the function

# Read filename
fname = input('Enter filename : ')

# Check if file exists
if not os.path.exists(fname):
    print('File does not exist')
else:
    # Open file in read mode
    f = open(fname, 'r')

    # Call disp() function
    disp(f)

    # Close file
    f.close()







: '''
Repeat  prog9b(File-pagewise)  with  readlines()  method
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

1) Which  method  is  used  to  read  the  whole  file  ?  ---> readlines()

2) Where  are  all   the  lines  stored ?  ---> List

3) How  to  print  each  line  of  the  list ?  --->  Iterate  thru  the  list  and  print  each  line

4) How  long  is  the  procedure  repeated ?  ---> Until  list  is   fully  iterated

5) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
	How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
# End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  call  disp()  function
How  to  close  the  file
######################################
'''
Repeat prog9b(File-pagewise) with readlines() method
i.e. Print file pagewise and pause execution for every 20 lines
'''

import os

def disp(f):
    lines = f.readlines()          # read entire file into a list
    total = len(lines)             # total number of lines
    ctr = 0                        # counter for lines per page

    for i in range(total):         # iterate through list
        print(lines[i], end='')    # print each line
        ctr += 1
        if ctr == 20:              # pause after 20 lines
            ctr = 0
            input('\n---- Press ENTER to continue ----\n')

    print('\n---- End of File ----')

# End of function


# Read filename
fname = input('Enter filename : ')

# Check if file exists
if not os.path.exists(fname):
    print('File does not exist')
else:
    # Open file in read mode
    f = open(fname, 'r')

    # Call disp() function
    disp(f)

    # Close file
    f.close()







: '''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1) In  which  mode  is  1st  file  opened ?  ---> 'r'  mode
    In  which  mode  is  2nd  file  opened ?  ---> 'w'   mode

2) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

3) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

4) What  action  to  be  made  when  both  the  files  are  existing ? --->
																Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
#####################################
'''
Write a program to copy contents of a file to a different file
'''

import os

# Read both filenames
fname1 = input("Enter source filename : ")
fname2 = input("Enter destination filename : ")


# 1) Check if 1st file exists
if not os.path.exists(fname1):
    print(f"{fname1} does not exist... cannot copy")
else:
    # 2) If 2nd file does NOT exist → copy directly
    if not os.path.exists(fname2):
        f1 = open(fname1, 'r')      # open first file in read mode
        f2 = open(fname2, 'w')      # open second file in write mode
        for line in f1:
            f2.write(line)
        f1.close()
        f2.close()
        print(f"{fname1} is copied to {fname2}")
    
    # 3) If both files EXIST
    else:
        print(f"{fname2} already exists")
        ch = input("Do you want to overwrite it ? (yes / no) : ").lower()
        if ch == "yes":
            f1 = open(fname1, 'r')      # read mode
            f2 = open(fname2, 'w')      # write mode (overwrite)
            for line in f1:
                f2.write(line)
            f1.close()
            f2.close()
            print(f"{fname1} is copied to {fname2}")
        else:
            print("Copy operation cancelled by user")




: '''
Write  a  program  to  append  data  of  a  file  to  another  file
i.e.  Copy  data  of  1st  file  to  the  end  of  2nd  file

1st  file
---------
Rama  Rao
9247
+-$
Hyd  is  green  city

2nd  file
----------
Hyd
Sec
Cyb


1) In  which  mode  is  1st  file  opened ?  ---> read  mode
    In  which  mode  is  2nd  file  opened ?  ---> append  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? --->  Begining  of  the  file
'''
##################################################
'''
Write a program to append data of a file to another file
i.e. Copy data of 1st file to the end of 2nd file
'''

import os

# Read both filenames
fname1 = input("Enter source filename  : ")
fname2 = input("Enter destination filename : ")


# Check if 1st file exists
if not os.path.exists(fname1):
    print(f"{fname1} does not exist... cannot append")
else:
    # Check if 2nd file exists
    if not os.path.exists(fname2):
        print(f"{fname2} does not exist... cannot append")
    else:
        # Open 1st file in read mode
        f1 = open(fname1, 'r')

        # Open 2nd file in append mode
        f2 = open(fname2, 'a')

        # Copy contents
        for line in f1:
            f2.write(line)

        f1.close()
        f2.close()

        print(f"Contents of {fname1} appended to {fname2}")







: '''
Write  a  function  to  return  average  of  numbers  in  the  file

File
----
10
20.8
True
15
18.4
eof

sum = 0 + 10 + 20.8 + True + 15 + 18.4
ctr = 0 + 1 + 1 + 1 + 1 + 1
'''
def   avg(f):
	How  to  return  average  of  numbers  in  the  file
#  End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  print  average  of  numbers  in  the  file
How  to  close  the  file
######################################

'''
Write a function to return average of numbers in the file
'''

def avg(f):
    total = 0        # to store sum of numbers
    ctr = 0          # to count how many valid numbers found

    for line in f:               # read line by line
        line = line.strip()      # remove \n
        try:
            num = eval(line)     # convert text to number (int, float, True → 1)
            if type(num) in (int, float, bool):   # allow only numbers & bool
                total += num
                ctr += 1
        except:
            pass                 # ignore invalid values like "eof"

    if ctr == 0:
        return 0
    return total / ctr           # return average

# End of function


# Read filename
fname = input("Enter filename : ")

# Open file in read mode
try:
    f = open(fname, 'r')
    result = avg(f)
    print(f"Average of numbers in file : {result}")
    f.close()
except FileNotFoundError:
    print("File does not exist")






: '''
Write  a  program  to  merge  two  files  to  form  a  new  file

1) Let  1st  file  contain  10  lines  and   2nd  file  contain  7  lines
    What  does  3rd  file  contain ?  --->  10 + 7 = 17  lines

2) What  action  to  be  made  when  both  the  files  are  existing ?  --->  Copy  all  the  lines  of  1st  file  to  3rd  file  and
																													then copy  all  the  lines  of  2nd  file  to  3rd  file

3) What  action  to  be  made  when  2nd  file  is  not  existing ?  ---> Copy  1st  file  to  3rd  file

4) What  action  to  be  made  when  1st  file  is  not  existing ?  ---> Copy  2nd  file  to  3rd  file

5) What  action  to  be  made  when  both  the  files  are  not  existing ?  --->  Print  a  message
'''
import  os
def  copy(file1 , file2):
	How  to  copy  data  from  file1  to  file2
#  End  of  the  function
How  to  read  all  the  three  filenames
if  first  two  files  are  existing:
	How  to  open  all  the  3  files
	How  to  copy  from  file1  to  file3
	How  to  copy  from  file2  to  file3
	How  to  close  all  the  3  files
	print(F'{fname1} and {fname2}  are  merged  to  form  {fname3}')
elif  1st  file  is  existing
	How  to  open  1st  and  3rd  file
	How  to  copy  from  file1  to  file3
	How  to  close  1st  and  3rd  files
	print(F'{fname1}  is  copied  to  {fname3}')
elif  2nd  file  is  existing
	How  to  open  2nd  and  3rd  file
	How  to  copy  from  file2  to  file3
	How  to  close  2nd  and  3rd  files
	print(F'{fname2}  is  copied  to  {fname3}')
else:
	print('Both  the  files  are  not  existing')
	How  to  delete  3rd  file

############################################
'''
Write a program to merge two files to form a new file
'''

import os

# Function to copy contents of one file into another
def copy(file1, file2):            # file1 → source, file2 → destination
    for line in file1:
        file2.write(line)
# End of function


# Read all three filenames
fname1 = input("Enter 1st filename  : ")
fname2 = input("Enter 2nd filename  : ")
fname3 = input("Enter 3rd (output) filename : ")


# Case 1: Both input files exist
if os.path.exists(fname1) and os.path.exists(fname2):
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')

    copy(f1, f3)      # copy file1 → file3
    copy(f2, f3)      # copy file2 → file3

    f1.close()
    f2.close()
    f3.close()
    print(f"{fname1} and {fname2} are merged to form {fname3}")


# Case 2: Only 1st file exists
elif os.path.exists(fname1):
    f1 = open(fname1, 'r')
    f3 = open(fname3, 'w')

    copy(f1, f3)

    f1.close()
    f3.close()
    print(f"{fname1} is copied to {fname3}")


# Case 3: Only 2nd file exists
elif os.path.exists(fname2):
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')

    copy(f2, f3)

    f2.close()
    f3.close()
    print(f"{fname2} is copied to {fname3}")


# Case 4: Both input files missing
else:
    print("Both the files are not existing")
    # If output file was created earlier by mistake, delete it
    if os.path.exists(fname3):
        os.remove(fname3)
        print(f"{fname3} is deleted")




: '''
Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and
sentences  in  a  file

File
-----
Rama Rao
9247<tab>Sita
+-$ Hyd

str  object --->  Rama  Rao\n9247\tSita\n+-$ Hyd\n

List  'a'  --->   [3            28          6           2             1               0                7               9       ]
                      Lines    Chars     Words   Spaces     Tabs     Sentences    Vowels     Consonants
'''
def  count_all(f):
	How  to  read  whole  file  to  a  str  object
	a = []
	How  to  append  number  of  lines  in  the  file  to  list  'a'
	How  to  append  number  of  characters  in  the  file  to  list  'a'
	How  to  append  number  of  words  in  the  file  to  list  'a'
	How  to  append  number  of  spaces  in  the  file  to  list  'a'
	How  to  append  number  of  tabs  in  the  file  to  list  'a'
	How  to  append  number  of  sentences  in  the  file  to  list  'a'
	How  to  append  number  of  vowles  in  the  file  to  list  'a'
	How  to  append  number  of  consonants  in  the  file  to  list  'a'
	How  to  return  list
#  End  of   function
How  to  read  filename
How  to  open  the  file
How  to  call  count_all()  function
How  to  close  the  file
b = ['Lines' , 'Chars' , 'Words' , 'Spaces' , 'Tabs' , 'Sentences' , 'Vowels' , 'Consonants']
How  to  print  lists   'b'  and  'a
#########################################
'''
Program to count lines, chars, words, spaces, tabs, sentences, vowels and consonants in a file
'''

def count_all(f):
    data = f.read()               # read whole file as one string
    a = []                        # result list to return

    # 1) Number of lines
    lines = data.count('\n') + 1 if data else 0
    a.append(lines)

    # 2) Number of characters
    chars = len(data)
    a.append(chars)

    # 3) Number of words
    words = len(data.split())
    a.append(words)

    # 4) Number of spaces
    spaces = data.count(' ')
    a.append(spaces)

    # 5) Number of tabs
    tabs = data.count('\t')
    a.append(tabs)

    # 6) Number of sentences (., ?, !)
    sentences = data.count('.') + data.count('?') + data.count('!')
    a.append(sentences)

    # 7) Number of vowels
    vowels = 0
    for ch in data:
        if ch.lower() in 'aeiou':
            vowels += 1
    a.append(vowels)

    # 8) Number of consonants (letters except vowels)
    consonants = 0
    for ch in data:
        if ch.isalpha() and ch.lower() not in 'aeiou':
            consonants += 1
    a.append(consonants)

    return a
# End of function


# Read filename
fname = input("Enter filename : ")

try:
    f = open(fname, 'r')
    result = count_all(f)
    f.close()
except FileNotFoundError:
    print("File does not exist")
    exit()

# Labels list
b = ['Lines', 'Chars', 'Words', 'Spaces', 'Tabs', 'Sentences', 'Vowels', 'Consonants']

# Print results
for label, value in zip(b, result):
    print(f"{label:<12} : {value}")





: '''
Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

File
----
Hyd  is  green  city.
Hyd  is  hitec  city.
Hyd  is  beautiful  city.

str  object  --->  'Hyd  is  green  city.\nHyd  is  hitec  city.\nHyd  is  beautiful  city.'

What  is  the  result  when  'Hyd'  is  searched  in  the  file ?  --->  3
'''
def   search(f ,  word):
	How  to  return  number  of  words  in  the  file
#End of  the  function
How  to  read  filename
How  to  open  the  file
How  to  read  word  to  be  searched
How  to  print  number  of  times  word  is  found  in  the  file
How  to  close  the  file
#################################
'''
Write a function to search for a word in the file and return number of times it is found
'''

def search(f, word):
    data = f.read()                 # read entire file as one string
    words = data.split()            # split into list of words
    return words.count(word)        # return how many times word appears
# End of function


# Read filename
fname = input("Enter filename : ")

try:
    f = open(fname, 'r')            # open file in read mode
except FileNotFoundError:
    print("File does not exist")
    exit()

# Read word to be searched
w = input("Enter word to search : ")

# Call function
result = search(f, w)

# Print result
print(f"'{w}' is found {result} times in the file")

# Close file
f.close()






: '''
Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import  math
def  fact(f , n):
	How  to  write  i  and  i!  to  the  file  where  'i'  varies  from  0  to  n
# End  of  the  function
How  to  read  filename
How  to  open  the  file
How  to  read  value  of  'n'
How  to  write  all  the  results  to  the  file
How  to  close  the  file
###################################

'''
Write a program to write 0! , 1! , 2!, ...... n! to the file
'''
import math

def fact(f, n):
    for i in range(n + 1):                     # from 0 to n
        f.write(f"{i}! = {math.factorial(i)}\n")
# End of function


# Read filename
fname = input("Enter filename : ")

# Read value of n
n = int(input("Enter value of n : "))

# Open file in write mode
f = open(fname, 'w')

# Write factorials to file
fact(f, n)

# Close file
f.close()

print(f"0! to {n}! are written to file '{fname}'")
