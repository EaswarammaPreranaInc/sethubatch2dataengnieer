                                  NAME:M.SAICHARAN                HOMEWORK
                                  DATE:08-11-2025

1.# Find   outputs (Home  work)
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
#Output:
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
Element :  0 infinite iterators


2.#  Find  outputs (Home  work)
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

#Output:
10	11	12	13
10	15	20	25
10.0	7.5	5.0	2.5
0	1	2	3



3.#  Tricky  program
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

#Output:
while loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for loop
(4, 10)
(5, 20)
(6, 15)
(7, 18)
Next element :  (8, 10)
*z3 :  (9, 20) (10, 15) (11, 18)
Next element  :  (12, 10)


4.#  Find  outputs (Home  work)
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

#OutPut:
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
Next  element :  (10, 8)
*z3 :  (20, 9) (15, 10) (18, 11)
Next  element  :  (10, 12)


5.# Most  tricky  program
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

#Output:
while loop
(0, 10)
(1, 20)
(2, 15)
(3, 18)
for loop
(10, 4)
(20, 5)
(15, 6)
(18, 7)
(8, 10)
(9, 20) (10, 15) (11, 18)
(10, 12)


6.#  Find  outputs  (Home  work)
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

#Output:
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


7.#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)

#Output:
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
30
40
infinite iterator

8.#  Find  outputs  (Home  work)
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
#Output:
1st repeat object
25
25
25
2nd repeat object
Hyd
Hyd
Hyd
Hyd
Hyd
repeats continuously for 1 second


9.# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2 , 3))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
#Output:
0

10.# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  range(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
#Output:
1
1

11.# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , repeat(2) ,  range(10))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
#Output:
1
2
4
8
16
32
64
128
256
512


12.#  Find  outputs (Home  work)
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

#Output:
Different Combinations
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'C', 'D')
('B', 'C', 'D')
Different Permutations
('A', 'B', 'C')
('A', 'C', 'B')
('A', 'B', 'D')
('A', 'D', 'B')
('A', 'C', 'D')
('A', 'D', 'C')
('B', 'A', 'C')
('B', 'C', 'A')
('B', 'A', 'D')
('B', 'D', 'A')
('B', 'C', 'D')
('B', 'D', 'C')
('C', 'A', 'B')
('C', 'B', 'A')
('C', 'A', 'D')
('C', 'D', 'A')
('C', 'B', 'D')
('C', 'D', 'B')
('D', 'A', 'B')
('D', 'B', 'A')
('D', 'A', 'C')
('D', 'C', 'A')
('D', 'B', 'C')
('D', 'C', 'B')

'''
13.#Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

1) How  to  iterate  thru  to  each  each  line  of  the  file ?  --->  for  loop

2) Which  function  is  used  to  print  each  line ?  --->  print()

3) How  long  is  the  procedure  repeated ?  --->   Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  ---> read  mode
'''
#Program:
import os
import time
def disp(f):
    count = 0
    for line in f:
        print(line, end='')         
        count += 1
        if count % 20 == 0:          
            input('\n--- Press Enter to continue ---\n')
# End of function
fname = input('Enter filename: ')
if not os.path.isfile(fname):
    print('File not found!')
else:
    f = open(fname, 'r')
    disp(f)
    f.close()
    print('\nEnd of file reached.')



'''
14.#Repeat  prog9b(File-pagewise)  with  readlines()  method
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines

1) Which  method  is  used  to  read  the  whole  file  ?  ---> readlines()

2) Where  are  all   the  lines  stored ?  ---> List

3) How  to  print  each  line  of  the  list ?  --->  Iterate  thru  the  list  and  print  each  line

4) How  long  is  the  procedure  repeated ?  ---> Until  list  is   fully  iterated

5) In  which  mode  is  file  opened ?  --->  read  mode
'''
#Program:
def disp(f):
    lines = f.readlines()        
    count = 0
    for line in lines:
        print(line, end='')      
        count += 1
        if count % 20 == 0:
            input('\n--- Press Enter to continue ---\n')
# End of function
fname = input('Enter filename: ')
f = open(fname, 'r')
disp(f)
f.close()
print('\nEnd of file reached.')


'''
15.#Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1) In  which  mode  is  1st  file  opened ?  ---> 'r'  mode
    In  which  mode  is  2nd  file  opened ?  ---> 'w'   mode

2) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

3) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

4) What  action  to  be  made  when  both  the  files  are  existing ? --->
Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
#program:
import os
src = input("Enter source filename: ")
dest = input("Enter destination filename: ")
if not os.path.exists(src):
    print("Source file does not exist!")
else:
    if os.path.exists(dest):
        choice = input(f"File '{dest}' already exists. Do you want to overwrite it? (yes/no): ").lower()
        if choice != 'yes':
            print("Copy operation cancelled.")
        else:
            f1 = open(src, 'r')
            f2 = open(dest, 'w')
            for line in f1:
                f2.write(line)
            f1.close()
            f2.close()
            print(f"File '{src}' successfully copied to '{dest}'.")
    else:
        f1 = open(src, 'r')
        f2 = open(dest, 'w')
        for line in f1:
            f2.write(line)
        f1.close()
        f2.close()
        print(f"File '{src}' successfully copied to '{dest}'.")


'''
16.#Write  a  program  to  append  data  of  a  file  to  another  file
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
#Program:
import os
src = input("Enter source filename: ")
dest = input("Enter destination filename: ")
if not os.path.exists(src):
    print("Source file does not exist!")
else:
    with open(src, 'r') as f1, open(dest, 'a') as f2:
        for line in f1:
            f2.write(line)
    print(f"Contents of '{src}' have been appended to '{dest}'.")


'''
17.#Write  a  function  to  return  average  of  numbers  in  the  file

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

#Program:
def avg(f):
    total = 0
    count = 0
    for line in f:
        line = line.strip()  # remove \n or spaces
        if line.lower() == 'eof':   
            break
        try:
            num = eval(line)
            if isinstance(num, (int, float, bool)):  
                total += num
                count += 1
        except:
            pass
    if count == 0:
        return 0
    return total / count
# End of the function
fname = input("Enter filename: ")
try:
    f = open(fname, 'r')
    result = avg(f)
    print(f"Average of numbers in the file = {result}")
    f.close()
except FileNotFoundError:
    print("File not found!")

'''
18.#Write  a  program  to  merge  two  files  to  form  a  new  file

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

#Program:
import os
def copy(file1, file2):
    for line in file1:
        file2.write(line)
# End of the function
fname1 = input("Enter 1st filename : ")
fname2 = input("Enter 2nd filename : ")
fname3 = input("Enter new (merged) filename : ")
# Case 1: Both files exist
if os.path.exists(fname1) and os.path.exists(fname2):
    f1 = open(fname1, 'r')
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')
    copy(f1, f3)
    copy(f2, f3)
    f1.close()
    f2.close()
    f3.close()
    print(f"{fname1} and {fname2} are merged to form {fname3}")
# Case 2: Only first file exists
elif os.path.exists(fname1):
    f1 = open(fname1, 'r')
    f3 = open(fname3, 'w')
    copy(f1, f3)
    f1.close()
    f3.close()
    print(f"{fname1} is copied to {fname3}")
# Case 3: Only second file exists
elif os.path.exists(fname2):
    f2 = open(fname2, 'r')
    f3 = open(fname3, 'w')
    copy(f2, f3)
    f2.close()
    f3.close()
    print(f"{fname2} is copied to {fname3}")
# Case 4: Neither file exists
else:
    print("Both the files are not existing")
    if os.path.exists(fname3):
        os.remove(fname3)


'''
19.#Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and
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
How  to  print  lists   'b'  and  'a'

#Program:
def count_all(f):
    data = f.read()
    a = []  
    # 1️.Number of lines
    lines = data.count('\n') + 1 if data else 0
    a.append(lines)

    # 2️.Number of characters
    chars = len(data)
    a.append(chars)

    # 3️.Number of words
    words = len(data.split())
    a.append(words)

    # 4️.Number of spaces
    spaces = data.count(' ')
    a.append(spaces)

    # 5️.Number of tabs
    tabs = data.count('\t')
    a.append(tabs)

    # 6️.Number of sentences (. ? !)
    sentences = data.count('.') + data.count('?') + data.count('!')
    a.append(sentences)

    # 7️.Number of vowels
    vowels = sum(1 for ch in data.lower() if ch in 'aeiou')
    a.append(vowels)

    # 8️.Number of consonants
    consonants = sum(1 for ch in data.lower() if ch.isalpha() and ch not in 'aeiou')
    a.append(consonants)

    return a
# End of function
fname = input("Enter filename: ")
try:
    f = open(fname, 'r')
    a = count_all(f)
    f.close()

    b = ['Lines', 'Chars', 'Words', 'Spaces', 'Tabs', 'Sentences', 'Vowels', 'Consonants']

    print("\nFile Statistics:")
    for i in range(len(b)):
        print(f"{b[i]:12} : {a[i]}")

except FileNotFoundError:
    print("File not found!")



'''
20.#Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

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

#Program:
def search(f, word):
    data = f.read()
    return data.count(word)
# End of the function
fname = input("Enter filename: ")
try:
    f = open(fname, 'r')
    word = input("Enter word to be searched: ")
    count = search(f, word)
    print(f"'{word}' is found {count} times in the file.")
    f.close()
except FileNotFoundError:
    print("File not found!")


'''
21.#Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

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

#Program:
import math
def fact(f, n):
    # Write factorials from 0! to n! into the file
    for i in range(n + 1):
        f.write(f"{i}! = {math.factorial(i)}\n")
# End of the function
fname = input("Enter filename: ")
f = open(fname, 'w')
n = int(input("Enter value of n: "))
fact(f, n)
f.close()
print(f"Factorials from 0! to {n}! are written to {fname}")
