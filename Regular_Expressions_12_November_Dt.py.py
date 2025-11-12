# Program 1
'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  --->

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->
'''
import   re
string = input('Enter  any  string  :  ')
pattern = input('Enter  pattern  :   ')
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')

# Output :
Enter  any  string  :  Hyd is green city.
Enter  pattern  :   Green
<class 're.Match'>
green  is found  between  indexes  7   and   11


# Program 2
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
	print('String  does  not  end  with  Simple')

# Output :
String  starts  with Learn
String  ends  with  simple


# Program 3
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
print('Found ' , ctr ,' times')

# Output :
Enter  any  string  :  Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
Enter  pattern  to  be  searched : is
is  is  between  indexes  4  and  5
IS  is  between  indexes  23  and  24
Is  is  between  indexes  42  and  43
iS  is  between  indexes  46  and  47
Found  4  times


# Program 4
# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break

# Output :
y is  at index :  1
I is  at index :  4
e is  at index :  9
E is  at index :  10
i is  at index :  14
Y is  at index :  16


# Program 5
# Find  outputs (Home  work)
import   re
itr  =  re . finditer('[A-Za-z0-9]' , 'm$9 K,d%5@E&')
while  True:
	try:
		m = next(itr)
		print(m . group() , ' is  at  index :  ' , m . start())
	except:
		break

# Output :
m  is  at  index :   0
9  is  at  index :   2
K  is  at  index :   4
d  is  at  index :   6
5  is  at  index :   8
E  is  at  index :   10



# Program 6
#  Find  outputs (Home  work)
import  re
string  =  'z7.Q-$2 b[9.a%6$G&k.%'
print(re . findall ('[a-z]'  ,  string))
print()
print(re . findall ('[0-9]'  ,  string))
print()
print(re . findall ('[^A-Za-z0-9]'  ,  string))
print()
print(re . findall ('.'  ,  string))
print()
print(re . findall ('[.]'  ,  string))
print()
print(re . findall ('[$]'  ,  string))
print()
print(re . findall ('[%]'  ,  string))
print()
print(re . findall ('[az-]'  ,  string))

# Output :
['z', 'b', 'a', 'k']

['7', '2', '9', '6']

['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']

['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']

['.', '.', '.']

['$', '$']

['%', '%']

['z', '-', 'a']
['z', '-', 'a']



# Program 7
''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)


# Output :
Enter  any  string : sankar dayal sarma
Enter  any pattern : san
sankar dayal sarma starts  with  san

Enter  any  string : hyd is green city
Enter  any pattern : sec
hyd is green city does not start with sec


# Program 8
#  Identify  Error  (Home  work)
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(^pattern , string , re . IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)


# Program 9
'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->
'''
import  re
s1 = input('Enter first string  : ')
s2 = input('Enter second string  : ')
m  = re . fullmatch(s1 , s2 , re . IGNORECASE)
if  m:
        print('Same  strings  after  ignoring  the  case')
else:
        print('Different  strings')


# Output :
Enter first string  : Hyd
Enter second string  : hyd
Same  strings  after  ignoring  the  case

Enter first string  : Hyd
Enter second string  : Sec
Different  strings


# Program 10
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

# Program 
import re
def number_validation(num):
    # Corrected regular expression
    string = r'(0|\+91)?[6789][0-9]{9}'
    
    m = re.fullmatch(string, num)
    if m:
        print(f"{num} is valid")
    else:
        print(f"{num} is not valid")

num = input("Enter any Number: ")
number_validation(num)

# Output :
Enter any Number: 6281459490
6281459490 is valid



# Program 11
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

What  is  the  regular  expression  for  the  above  rules ?  --->

# Program 
mport re
def vehicle_reg(num):
    string = r'^[Tt][Ss](0[1-9]|1[0-9]|2[0-9])[A-Za-z]{2}[0-9]{4}$'
    
    if re.fullmatch(string, num):
        print(f"{num} is valid")
    else:
        print(f"{num} is not valid")

num = input("Enter Vehicle Number: ")
vehicle_reg(num)

# Output :
Enter Vehicle Number: ts12ab1234
ts12ab1234 is valid


# Program 12
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

# Program 
import re
def dob_validation(num):
    string = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$'
    if re.fullmatch(string, num):
        print(f"{num} is valid")
    else:
        print(f"{num} is not valid")
num = input("Enter Date of Birth (dd/mm/yyyy): ")
dob_validation(num)

# Output :
Enter Date of Birth (dd/mm/yyyy): 30/05/1998
30/05/1998 is valid


# Program 13
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

# Program
import re
def validate_address(addr):
    pattern = r'^[A-Za-z ]+, [A-Za-z ]+, [A-Za-z ]+ - [0-9]{6}$'
    if re.fullmatch(pattern, addr):
        print(f"'{addr}' ---> Valid")
    else:
        print(f"'{addr}' ---> Invalid")
addr=input("Enter your address :")
validate_address(addr)

# Output :
Enter your address :Khairtabad , Hyderabad , Telangana - 500004
'Khairtabad , Hyderabad , Telangana - 500004' ---> Valid


# Program 14
'''
Write  a  program  to  validate  credit card  number

Rules:
1) It  must  start  with  4 , 5  (or) 6
2) It  must  be  a  16 digit  number
3) It  should  have  digits  from  0  to  9
4) It  may  have  digits  in  a  group  of  4  separated  by  one  hyphen
5) It  should  not  have  any  other  separator  like  _ ,  / , etc
'''
# Program
import re
def credit_card(num):
    pattern = r'^(?:[456][0-9]{15}|[456][0-9]{3}(?:-[0-9]{4}){3})$'
    
    if re.fullmatch(pattern, num):
        print(f"{num} ---> Valid")
    else:
        print(f"{num} ---> Invalid")
num=input("Enter Card Number :")
credit_card(num)

# Output :
Enter Card Number :4565-1234-2345-2445
4565-1234-2345-2445 ---> Valid
