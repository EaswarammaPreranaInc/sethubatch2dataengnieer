'''Write  a  program  to  determine  largest  command  line  input 
1)	py   py_07_08_25.py   10     20     30.8   7  40    35.6 
    What  is  the  largest  command  line  input ?  ---> 40 
    What  is  argv ?  --->  ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6'] 
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6] 
    How  to  determine  largest  element  of  list  'a' ?   ---> max(a)  i.e.  40 
    What  is  the  result  of  max(argv[1:]) ?  ---> '7' 
    What  is  the  issue  with  max(argv[1:])) ?  ---> 
 Largest  string  is  obtained  but  not  largest  number 
2)	py  prog2.py 
    What  is  the  output ?  ---> Pls  send  inputs 
3)	py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar' 
    What  is  the  largest  command  line  input ?  --->  'Vamsi' 
4)	py   prog2.py   25   'Ten' 
    What  is  the  output ?  --->  Inputs  can  not  be  number  and  string 
5)	Hint1: Use  for  loop 
6)	Hint2: Use  try  and  except 
''' 
import sys 
 
if len(sys.argv) == 1: 
    print("Pls send inputs") else: 
    a = [] 
    all_str = True     all_num = True 
 
    for i in sys.argv[1:]: 
        try: 
            val = float(i) 
            a.append(val) 
            all_str = False 
        except ValueError: 
            a.append(i)             all_num = False 
 
    if not all_num and not all_str: 
        print("Inputs can not be number and string") 
    else: 
        largest = max(a)         print("Largest command line input:", largest)         print("argv:", sys.argv)         print("list a:", a) 
Write  a  program  to  determine  command  line  input  is  even  number  or  odd  number 
1)	py  prog3.py  26 
    What  is  the  output ?  ---> Even  number 
2)	py  prog3.py  45 
    What  is  the  output ?  ---> Odd  number 
3)	py  prog3.py 
    What  is  the  output  ?  ---> Pls  send  an  integer  input 
4)	py  prog3.py  10.8 
    What  is  the  output ?  --->  Pls  send   an  integer  input 
5)	py  prog3.py  Ten 
    What  is  the  output  ?  --->  Pls  send   an  integer  input 
''' 
import sys for x in sys.argv[1:]: 
    try: 
        n = int(x)         print(f"{n} is even" if n % 2 == 0 else f"{n} is odd")     except: 
        print("enter valid number") 
output : 
PS F:\> py py_07_08_25.py PS F:\> py py_07_08_25.py 10.8 enter valid number 
PS F:\> py ^C 
PS F:\> py py_07_08_25.py Ten enter valid number 
PS F:\> py py_07_08_25.py 45 
45 is odd 
PS F:\> py py_07_08_25.py 26 
26 is even 
PS F:\> 
Write  a  program  to  determine  average  of  command  line  inputs 
1)	py   prog4.py   10.8   25   True   14.6   19   False   7.4 
    What  is  argv ?  --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4'] 
    What  is  list  'a'  ?  --->  	[10.8 , 25 , True , 14.6 , 19 , False , 7.4] 
   How  to  determine  sum  of  list  elements ?  ---> sum(a) 
    How  to  determine  number  of  list  elements ?  ---> len(a) 
2)	py   prog4.py 
    What  is  the  output ?  ---> Pls  send  number  inputs 
3)	py   prog4.py  25   'Ten' 
    What  is  the  output  ?  --->  Pls  send  number  inputs import sys 
try: 
    a = [eval(x) for x in sys.argv[1:]]     print("argv:", sys.argv)     print("list a:", a) 
    print("Average:", sum(a)/len(a)) except: 
    print("Pls send number inputs") 
''' 
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order 
1)	py  prog5.py  10   20    15.8   5   12.6 
    What  is  argv ?  ---> ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6'] 
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6] 
    How  to  sort  list  'a' ?  --->  sorted(a) 
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True) 
2)	py  prog5.py   25   'Ten' 
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together 
 
import sys 
 
if len(sys.argv) == 1: 
    print("Pls send number inputs") else: 
    a = [] 
    all_num = True     all_str = True 
 
    for x in sys.argv[1:]: 
        try: 
            val = float(x) 
            a.append(val)             all_str = False         except ValueError: 
            a.append(x)             all_num = False 
 
    if not all_num and not all_str: 
        print("Pls don't send number and string inputs together") 
    else: 
        print("argv:", sys.argv) 
        print("list a:", a) 
        print("Ascending:", sorted(a))         print("Descending:", sorted(a, reverse=True)) '''output : 
PS F:\> py  py_07_08_25.py 10   20    15.8   5   12.6 argv: ['py_07_08_25.py', '10', '20', '15.8', '5', '12.6'] list a: [10.0, 20.0, 15.8, 5.0, 12.6] 
Ascending: [5.0, 10.0, 12.6, 15.8, 20.0] 
Descending: [20.0, 15.8, 12.6, 10.0, 5.0] 
 
# Find outputs  (Home  work) 
print( 'green'   in   'Hyd  is  green  city')   : true  print('day'   in   'Sankar  dayal  sarma')  : true  print('Green'   in   'Hyd  is  green  city')  : else , due to casing  print('d  is'   in   'Hyd  is  green  city')  : true  print('dis'   in   'Hyd  is  green  city') : false  print('iniv'   in   'Srinivas')  : false  print('iniv'   not   in   'Srinivas')  : true  
 
'''  (Home  work) 
Slice  demo  program 
0      1       2        3      4       5       6       7 
R      a      m        a               R       a       o 
-8    -7     -6      -5     -4      -3     -2      -1 
''' 
a = 'Rama Rao' 
print(a [ : 7 : 2])   :   R m <space >  a  print(a [ : 7])  : Rama Rao print(a [2 : 4]) : ma<sace> print(a [2 : ])  : ma Rao print(a [ : 4 ])  : Rama 
print(a [ : : 2]) : rm<space>a print(a [-6 : -1])  : ma Ra print(a [-6 : ]) : ma Rao print(a [: -4 : -1])  :       R   a   o<space> print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  string  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra print(a [-3 : ])  : Rao print(a [ : : ]) : Rama Rao print(a [ : ]) :Rama Rao 
print(a [ : : -1])  : R      a      m        a               R       a       o 
print(a [ : : -2]) : oRa mR 
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR 
print(a [2 : 8])  : ma Rao print(a [2 : 8 : -1]) :eroor 
print(a [ : -6 : -1])  : m    a   ' '   R    a    o print(a [2 : -3]) : ma <sp> print(a [1 : 6 : 2]) : aaR print(a [ : -5 : -5]) : oR print(a [2 : -5]) : ma print(a [2 : -5 : 2]) : m print(a [ : 0 : -1]) : oa Ram a print(a [-5 : 0 : -2]) : a<sp>  
''' 
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two characters  of  the  two  strings. 
Assume  that  each  string  has  a   minimum  of  two  characters 
Let  inputs  be  Java  and  Python 
What  are  the  outputs ?  --->  Pyva<space>Jathon 
Hint:  Use  slice 
‘’’ 
s1 = input("Enter first string: ") 
s2 = input("Enter second string: ") 
 
# Swap first two characters result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:] 
 
print("resust is :" ,result) 
''' 
Output : 
Enter first string: java 
Enter second string: python resust is : pyva jathon 
 
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string 
Print  an  empty  string  if  string  has  less  than  four  characters 
1)	Let  input  be  PYTHON 
    What  is  the  output ?  ---> PYON 
2)	Let  input  be  Hyd 
    What  is  the  output ?  --->  Nothing 
''' 
# Take input from console s = input("Enter a string: ") # Check length 
if len(s) < 4:     print("") else:     print(s[:2] + s[-2:]) 
''' 
Output : 
Enter a string: python 
pyon 
PS F:\> 
 
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse directions  without  slice 
        	      	 	 	 	  0      1     2      3     4 
Let  input  be 	 	  V     A     M     S     I 
 	 	 	         	 	 -5    -4    -3    -2    -1 
What  are  the  outputs ?  --->  Character  at  index  0  :  V 
 	 	 	 	 	 	 	 	                 Character  at  index  1  :  A 
 	 	 	 	 	 	 	 	                 Character  at  index  2  :  M 
 	 	 	 	 	 	 	                     Character  at  index  3  :  S 
 	 	 	 	 	 	 	 	                 Character  at  index  4  :  I 
 
 	 	 	 	 	 	 	 	                 Character  at  index  -1  :  I 
 	 	 	 	 	 	 	 	                 Character  at  index  -2  :  S 
 	 	 	 	 	 	 	 	                 Character  at  index  -3  : M 
 	 	 	 	 	 	 	 	                 Character  at  index  -4  :  A  	 	 	 	 	 	 	 	                 Character  at  index  -5  :  V 
 
Hint:  Use  two  for  loops s = input("Enter a string: ") for i in range(len(s)): 
    print(f"Character at index {i} : {s[i]}") for i in range(-1, -len(s)-1, -1): 
    print(f"Character at index {i} : {s[i]}") 
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice 
                                0      1      2      3     4     5     6      7 
Let  input  be        R      a     m      a             R     a      o 
 
odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo' even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a' s = input("Enter a string: ") even = "" odd = "" for i in range(len(s)):     if i % 2 == 0:         even += s[i]     else: 
        odd += s[i] 
print(f"even idex sum is :{even}") print(f"odd) index sum is :{odd}") output :  
Enter a string: rama rao Enter a string: ram  even idex sum is : rm odd) index sum is  : a 
 
1) What  action  to  be  made  when  index  is  even ?  ---> 
Concatenate  the  character  to  even  object 
) What  action  to  be  made  when  index  is  odd ?  ---> 
 Concatenate  the  characeter  to  odd  object 
3) Hint: Use  single  for  loop 
''' 
s = input("Enter string : ")  # Example: A4B3C2$5 res = "" for i in range(0, len(s), 2):       res += s[i] * int(s[i+1]) print(res) 
# 
Let  input  be    A   4   B   3   C   2   $   5 
                         0   1    2   3   4   5   6   7 
What  is  the  output ?  --->  AAAABBBCC$$$$$ 
1)	What  is  the  result  of  'A' * 4  ?  ---> 'AAAA' 
2)	i        a[i]       a[i + 1]          out 
   ------------------------------------------------------- 
                                               '' 
     0        'A'          '4'            '' + 'A' * 4 = 'AAAA' 
 
 	 2        'B'          '3'            'AAAA' + 'B' * 3 = 'AAAA' + 'BBB' = 'AAAABBB' 
 
 	 4        'C'          '2'            'AAAABBB' + 'C' * 2 = 'AAAABBB' + 'CC' = 'AAAABBBCC' 
 
 	 6        '$'          '5'            'AAAABBBCC' + '$' * 5 = 'AAAABBBCC' + '$$$$$' = 'AAAABBBCC$$$$$' 
   ------------------------------------------------------- 
What  is  the  difference  between  a[i]   and  a[i + 1] ?  --- a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string 
''' 
Enter  any  string  with  alternate  character  and  digit :  A4B3C2$5 
Result :   AAAABBBCC$$$$$ 
Enter  any  string  with  alternate  character  and  digit :  HYD 
String   should  have  alternate  character  and  digi 
''' 
Write  a  program  to  merge  two  strings  to  form  a  new  string 
1) Let  inputs  be    HYD   and   VAMSI 
   What  is  the  output  ?  --->  HVYADMSI 
             0     1    2 
a  --->   H     Y    D 
              0    1     2     3    4 b  --->    V    A    M    S    I 
i       a[i]        b[i]          c 
-------------------------------------------------------- 
                                    '' 
0	'H'        'V'          '' + 'H' + 'V' = 'HV' 
 
1	'Y'        'A'          'HV' + 'Y' + 'A' = 'HVYA' 
 
2	'D'       'M'          'HVYA' + 'D' + 'M' = 'HVYADM' 
-------------------------------------------------------- 
Concatenate  remainging  characters   of  the  other  string  to  object  'c' 
What  is  the  final  result ?  --->  'HVYADMSI' 
Hint:  Use  single  while  loop  and  slice 
''' 
a = input("Enter first string: ") b = input("Enter second string: ") c = "" i = 0 while i < len(a) and i < len(b): 
    c += a[i] + b[i]     i += 1 
c += a[i:] + b[i:]   # append remaining characters print("Merged string:", c) 
 
output :  
Enter first string: hyd  
Enter second string: vamsi 
Merged string: hvyadm si 
Enter  first  string  :  HYD 
Enter  second  string  :  VAMSI 
Result  :   HVYADMSI 
Enter  first  string  :  SAIRAM 
Enter  second  string  :  HYD 
Result  :   SHAYIDRAM 
Output : Enter first string: sairam 
Enter second string: hyd  
Merged string: shayidr am 
PS F:\> 
''' 
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set 
1)	Let  input  be   RAMA  RAO 
   What  is  the  output ? ---> RAM<space>O 
2)	out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O' 
3)	What  action  to  be  made  if  the  character  is  not  in  out  object ?  ---> 
Concatenate  the  character  to  out  object 
4)	What  action  to  be  made  if  the  character  is  already  in  out  object ?  --- 	Ignore  the  character 
5)	Hint:  Use  not  in   operator 
''' 
s = input("Enter any string: ") result= "" for ch in s: 
    if ch not in result:   # only add if not already present         result += ch 
print("String without duplicates:", result) output : 
Enter  any  string  :  MISSISIPI 
String  without  duplicates  :    MISP 
 
# len()  function  demo  program  (Home  work) 
print(len('Hyd'))  #  3 print(len('Rama Rao')): 8 print(len('9247')) : 4 print(len('+-$')) : 3 print(len('')):0 print(len(' ')) :1 print(len('A2#'))  :3 print(len(3456)): error , it’s an integer  print('Sec'. len())   : unable to express length 
 
''' 
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string 
''' 
# chr()  function  demo  program print(chr(65))  #   Converts  unicode  value  65  to  'A' print(chr(90)) : Z print(chr(97)) : a print(chr(122)) :z print(chr(48)) : 0 print(chr(57)) : 9 print(chr(36)) :$ print(chr(32)) : space 
''' 
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character 
''' 
# ord()  function  demo  program print(ord('A'))  #  Converts  'A'  to  unicode  value  65 print(ord('Z')) :122 print(ord('a')) : 97 print(ord('z')) : 122 print(ord('0')) :48 print(ord('9')) :57 yes  
 
 
 
 
''' 
ord()  function 
------------------ 
1)	What  does  ord()  function  do ?  ---> Converts  character  to  unicode  value 
 
2)	How  many  unicode  values  exist ?  ---> 512 
 
3)	What  is  the  range  of  unicode  values ?  ---> 0  to  511 
 
4)	What  are  the  unicode  values  of  'A'  -  'Z' ?  ---> 65  to  90 
     What  are  the  unicode  values  of  'a'  -  'z' ?  ---> 97  to  122 
     What  are  the  unicode  values  of  '0'  -  '9' ?  ---> 48  to  57 
 
5)	What  is  another  name  of  unicode ?  ---> Extended  Ascii 
 
Note:  chr()  and  ord()  are  quite  opposite  functions 
''' 
''' 
Let  input  be  A4M3Z5D2 
 
What  is  the  output ?  --->  AEMPZ_DF 
 
 0     1     2     3    4    5    6     7 
 A    4     M    3    Z    5    D     2 
 
    i       a[i]      a[i + 1]         out 
-------------------------------------------------------------------------------- 
                                          '' 
  0       'A'           '4'          '' + 'A' + chr(65 + 4) = '' + 'A' + 'E' = 'AE' 
 
  2       'M'           '3'          'AE' + 'M' + chr(77 + 3) = 'AE' + 'M' + 'P' = 'AEMP' 
 
  4       'Z'           '5'          'AEMP' + 'Z' + chr(90 + 5) = 'AEMP' + 'Z' + '' = 'AEMPZ' 
 
  6       'D'           '2'          'AEMPZ_' + 'D' + chr(68 + 2) = 'AEMPZ_' + 'D' + 'F' = 'AEMPZ_DF' 
----------------------------------------------------------------------------------- 
Hint: Use  chr()  and  ord()  functions 
''' 
 
Enter  any  string  with  alternate  character  and  digit  :  HYD 
Pls  enter  string  with  alternate  char  and  digit 
Enter  any  string  with  alternate  character  and  digit  :  A4M3Z5D2 
Result  :   AEMPZ_DF 
 
