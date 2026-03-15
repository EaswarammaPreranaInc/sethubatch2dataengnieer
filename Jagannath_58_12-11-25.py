'''
Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     Eg:  #statement  --->  Do  not  delete

3) Do  not  remove  lines  which  starts  with   <spaces>#
    Eg:  <Spaces>#   comment   --->  Do  not  delete

4) Remove  comments  which  are  at  the  end  of  statement
    Eg:   statement  #   comment  --->  Delete  the  comment

5) Input  is  filename

6) File
     ----
	 # Question
    stmt1   #  Comment
    stmt2
    #stmt3
    stmt4  #  comment
    <spaces>#stmt5

7) What  action  to  be  made  when  line  starts  with  '#' ?  --->  Write  line  to  the  file

8) What  action  to  be  made  when  line  contains  '#' ?  --->  Write  statement  before  #  to  the  file

9) What  action  to  be  made  when  line  does  not  contain  '#' ?  --->  Write  line  to  the  file

10) What  action  to  be  made  when  line  has  spaces  before  #  ?  --->  Write  the  line  to  the  file  without  leading  spaces
'''

def remove_single_line_comments(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    cleaned_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('#'):
            cleaned_lines.append(stripped)
            continue
        if '#' in line:
            index = line.find('#')
            code_part = line[:index].rstrip()
            if code_part:
                cleaned_lines.append(code_part + '\n')
        else:
            cleaned_lines.append(line)
    with open('cleaned_' + filename, 'w') as f:
        f.writelines(cleaned_lines)
if __name__ == "__main__":
    filename = input("Enter Python filename: ")
    remove_single_line_comments(filename)
    print("Comments removed. Cleaned file saved as 'cleaned_" + filename + "'.")

# Write a program to print csv file
import csv
def disp(f):
    reader = csv.reader(f)
    for row in reader:
        print(row)
try:
    fname = input("Enter CSV filename: ")
    with open(fname, 'r', newline='') as f:
        disp(f)
except FileNotFoundError:
    print(f'File {fname} does not exist')

''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  ---><class 're.Match'>
                               green is found between indexes 7 and 11


2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  ---><class 'NoneType'>
                                 red is not found

'''
import   re
string = input('Enter  any  string  :  ')
pattern = input('Enter  pattern  :   ')
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')

#  Find  outputs  (Home  work)
import  re
m = re . search('^learn' , 'Learning Python is simple' , re . IGNORECASE)
if  m:
	print('String  starts  with' , m . group())
else:
	print('String  does  not  start  with  learn')
m = re . search('Simple$' , 'Learning Python is simple' , re . IGNORECASE)
if   m:
	print('String  ends  with ' , m . group())
else:
	print('String  does  not  end  with  Simple')

output:
String starts with Learn
String ends with simple

'''  (Home  work)
What  are  the  outputs
1st  input  --->  Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
2nd  input  --->  is
What  are  the  outputs  --->
'''
import re
string  =  input('Enter  any  string  :  ')
pattern = input('Enter  pattern  to  be  searched : ')
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is  between  indexes  {m . start()}  and  {m . end() - 1}')
		ctr += 1
	except  StopIteration:
		break
print('Found ' , ctr ,' times')

output:
is is between indexes 4 and 5
IS is between indexes 22 and 23
Is is between indexes 36 and 37
hiS is between indexes 39 and 40
Found 4 times

'''
Write  a  regular  expression  to  validate  a  10-digit  mobile  number

Rules:
1) It  should  be  a  10-digit  number

2) First  digit  can  be  6 , 7 , 8  or  9

3) Number  may  start  with  0  (or)  +91


Which  of  the  following  are  valid
----------------------------------------
a) 5948250500  --->  Invalid  becoz  first  character  '5'  is  not  between  '6'  and  '9'
b) 994825050 --->  Invalid  becoz  length  of  the  string  is  not  10
c) 9948-250500  ---> Invalid  due  to  '-'
d) 9948250500  --->  Valid
e) 09948250500  --->  Valid  becoz  number  may  start  with  '0'
f) +919948250500 ---> Valid  becoz  number  may  start  with  +91
g) 919948250500  --->  Inavlid  becoz  length  of  the   string  is  not  10


1) What  is  the  regular  expression  for  the  above  rules ?  --->  (0|[+]91)?[6789][0-9]{9}

2) Which  function  should  be  used ?  --->  fullmatch()  function
'''
import re
pattern = r'(0|\+91)?[6789][0-9]{9}'
numbers = [
    '5948250500',
    '994825050',
    '9948-250500',
    '9948250500',
    '09948250500',
    '+919948250500',
    '919948250500'
]
for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, '→ Valid')
    else:
        print(num, '→ Invalid')

'''
Write  a  program  to  validate  vehicle  registration  number

Rules:
1) First  2  characters  shoulde  be  TS , ts , Ts  or  tS

2) There  are  29  circles  i.e.  01 , 02 , 03 , ......29

3) Next  two  characters  should  be  alphabets

4) Last  four  characters  should  be  digits

Which  of  the  following  is  valid
--------------------------------------
a) TS30AB1234 --->  Invalid  becoz  circle  30  does  not  exist
b) AP15CD1234  ---> Invalid  becoz  first  2  characters  can  not  be  AP
c) Ts15E1234 ---> Invalid  due  to  single  character  'E'
d) tS15FG123 ---> Invalid  due  to  3 - digit  number  123
e) ts9KP1234 ---> Invalid  due  to  single  digit  9
f) tS10LW1234  ---> Valid
g) 15XY1234  --->  Invalid  becoz  TS   is  missing
h) Ts00PQ1234  --->  Invalid  becoz  circle  00  does  not  exist
i) TS20RS1234 ---> Valid
j) Ts25TR1234 --->  Valid

What  is  the  regular  expression  for  the  above  rules ?  --->^[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}$

import re
pattern = r'^[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}$'
numbers = [
    'TS30AB1234',
    'AP15CD1234',
    'Ts15E1234',
    'tS15FG123',
    'ts9KP1234',
    'tS10LW1234',
    '15XY1234',
    'Ts00PQ1234',
    'TS20RS1234',
    'Ts25TR1234'
]
for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, '→ Valid')
    else:
        print(num, '→ Invalid')

'''
Write  a  program  to  validate  date  i.e.  dd/mm/yyyy

1) What  is  the  valid  character  after  '0'  in  the  date ?  --->  1  to  9
    What  is  the  valid  character  after  '1'  in  the  date ?  --->  0  to  9
    What  is  the  valid  character  after  '2'  in  the  date ?  ---> 0  to  9
    What  is  the  valid  character  after  '3'  in  the  date ?  ---> 0  (or)  1

2) Is  0  mandatory  for  single  digit  date ?  --->  No  and  it  is  optional

3) What  is  the  valid  character  after  '0'  in  the  month ?  --->  1  to  9
     What  is  the  valid  character  after  '1'  in  the  month ?  --->   0  to  2

4) Is  0  mandatory  for  single  digit  month ?  --->  No  and  it  is  optional

5) Which  of  the  following  are  valid ?
     a) 00/05/2025  --->  Invalid  due  to  date  00
     b) 0/12/2025  ---> Invalid  due  to  date  0
     c) 32/8/2025  --->  Invalid  due  to  date  32
     d) 07/13/2025  --->  Invalid  due  to  month  13
     e) 15/00/2025  --->	 Invalid  due  to  month  00
     f) 25/12/25  --->  Invalid  due  to  year  25
	 g) 15-8-1947  --->  Invalid  due  to  -
    h) 15.8.1947  ---> Invalid  due  to  '.'
'''

import re
pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/[0-9]{4}$'
dates = [
    '00/05/2025',
    '0/12/2025',
    '32/8/2025',
    '07/13/2025',
    '15/00/2025',
    '25/12/25',
    '15-8-1947',
    '15.8.1947',
    '15/8/1947',     
    '05/09/2025'     
]
for d in dates:
    if re.fullmatch(pattern, d):
        print(d, '→ Valid')
    else:
        print(d, '→ Invalid')

'''
Write  a  program  to validate  address

Address  format :  streetname , city ,  State - PIN code
Eg:  Khairtabad , Hyderabad , Telangana - 500004

Rules:
1) street name  should  have  alphabets  (or)  spaces
2) ,  is   mandatory  between  street  name  and  city
3) City  name  should  have  alphabets  (or)  spaces
4) ,  is   mandatory  between  city  and  state
5) State  name  should  have  alphabets  (or)  spaces
6) -  is  mandatory  between  state  and  pincode
7) Pincode should  be  a  six-digit  number
'''
import re
pattern = r'^[A-Za-z ]+\s*,\s*[A-Za-z ]+\s*,\s*[A-Za-z ]+\s*-\s*[0-9]{6}$'
addresses = [
    'Khairtabad , Hyderabad , Telangana - 500004',  
    'Khairtabad,Hyderabad,Telangana-500004',        
    'Khairtabad Hyderabad Telangana - 500004',      
    'Khairtabad , Hyderabad , Telangana 500004',    
    'Khairtabad , Hyderabad , Telangana - 50004',   
    'Khairtabad , Hyderabad , Telangana - 5000044', 
    'Khairtabad , 123City , Telangana - 500004'     
]
for addr in addresses:
    if re.fullmatch(pattern, addr):
        print(addr, "→ Valid")
    else:
        print(addr, "→ Invalid")

'''
Write  a  program  to  validate  credit card  number

Rules:
1) It  must  start  with  4 , 5  (or) 6
2) It  must  be  a  16 digit  number
3) It  should  have  digits  from  0  to  9
4) It  may  have  digits  in  a  group  of  4  separated  by  one  hyphen
5) It  should  not  have  any  other  separator  like  _ ,  / , etc

import re
pattern = r'^[456][0-9]{3}(-?[0-9]{4}){3}$'
cards = [
    '4123456789123456',      
    '5123-4567-8912-3456',   
    '61234-567-8912-3456',   
    '4123356789123456',      
    '5133-3367-8912-3456',   
    '5123 - 3567 - 8912 - 3456',  
    '412345678912345',       
    '5123-4567-8912-34567',  
    '41234567891234a6',      
    '5123_4567_8912_3456',   
]
for card in cards:
    if re.fullmatch(pattern, card):
        print(card, "→ Valid")
    else:
        print(card, "→ Invalid")

