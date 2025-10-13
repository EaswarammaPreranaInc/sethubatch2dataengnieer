'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
while (index := a.find('is')) != -1:
   print(index)
   a = a[:index] + '*' + a[index + 1:]
print('End')


'''
index()  method  demo  program

Modify  the  following  program  with  index()  method

index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
   index = a.index('is')
   while True:
      print(index)
      index = a.index('is', index + 1)
except ValueError:
   print('End')



'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method


'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index != -1:
   print(index)
   index = a.rfind('is', 0, index)
print('End')

'''
(Home work)
rindex() method demo program

Modify following program with rindex() method

Hint: Use try and except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
   index = a.rindex('is')
   while True:
      print(index)
      index = a.rindex('is', 0, index)
except ValueError:
   print('End')


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
														Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1
'''

 #  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # 4
print(a . count('is' , 19 , 48)) # 2
print(a . count('was')) # 0



 #  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))   # 3 
print(a . count('\t'))  # 3 
print(a . count('\n'))  # 3 



'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''

a = input("Enter a string: ")
if len(a) > 0:
   first_char = a[0]
   a = first_char + a[1:].replace(first_char, '*') 
print(a)




#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)  #['15', '36', '48'  ]


# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split())   # ['Hyd', 'is', 'green', 'city']
print(a . split('green'))  # ['Hyd\nis ', ' city']
print(a . split(''))  # ['H', 'y', 'd', '\n', 'i', 's', ' ', 'g', 'r', 'e', 'e', 'n', '\t', 'c', 'i', 't', 'y']


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split())   # ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  # ['Hyd\tis\tgreen\tcity']



a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''

strg=input("enter the string : ")
b=strg.split("+")
c=0
for i in range(len(b)):
   c+=eval(b[i])
print(c)


# Find outputs (Home work)
a = ['15', '36', '48']
print(':'.join(a))   # 15:36:48

b = ('Hyd', 'is', 'green', 'city')
print(' '.join(b))   # Hyd is green city

c = {'10', '20', '15', '25', '52'}
print(','.join(c))   #10,20,15,25,52

d = ['www', 'gmail', 'com']
print('.'.join(d))   # www.gmail.com

e = [15, 36, 48]
# print(':'.join(e)) # Erroor

f = ['Sankar', 'Dayal', 'Sarma']
print(''.join(f))    # SankarDayalSarma

g = range(5)
# print('-'.join(g)) # Error


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))         # True
print(a . endswith('town'))         # False
print(a . endswith('green' , 3 , 12))  # True
print(a . endswith('green' , 3 , 13))  # False
print(a . endswith(' ' , 3 , 13))      # False


'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

a = input("Enter a string: ")
if len(a) < 3:
   print(a)
elif a.endswith('ing'):
   print(a + 'ly')
else:
   print(a + 'ing')


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())        # True
print('Rama  Rao'  . isalpha())  # False
print('Hyd4'  . isalpha())       # False
print('Hyd$'  . isalpha())       # False
print('9247'  .  isalpha())      # False
print('+-$'    .  isalpha())     # False
print('A2#'  .   isalpha())      # False
print(''  .  isalpha())          # False
print(' '  . isalpha())          # False



'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())      # True
print('92a47' . isdigit())     # False
print('92$47' . isdigit())     # False
print('Hyd' . isdigit())       # False
print('+-$' . isdigit())       # False
print('A2#' . isdigit())       # False
print('' . isdigit())          # False
print(' ' . isdigit())         # False
print(9247 . isdigit())      # Error: 'int' object has no attribute 'isdigit'



'''
isupper()  method
----------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  lowercase  alphabet
																								(or)
															                  When  there  are  no  uppercase  alphabets  in  the  string

2) When  does  it  return  True ?  ---> When  there  are  no  lowercase  alphabets  in  the  string
																						and
															at  least  one  character  is  an  uppercase  alphabet
'''
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())    # False
print('HYD' . isupper())    # True
print('9247' . isupper())   # False
print('RAMA  RAO' . isupper()) # True
print('+-$' . isupper())    # False
print('HYD123' . isupper()) # True
print('HYD+-$' . isupper()) # True
print('' . isupper())       # False
print('A2#' . isupper())    # True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet'''
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())      # False
print('hyd' . islower())      # True
print('9247' . islower())     # False
print('rama  rao' . islower())# True
print('+-$' . islower())      # False
print('hyd+-$' . islower())   # True
print('abc123' . islower())   # True
print('' . islower())         # False
print('a2#' . islower())      # True



'''
isalnum()  method
----------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  speical  character
																						(or)
															 when  there  are  no  alphabets  and  digits

2) When  does  it  return  True ?  ---> When  there  are  no  special  characters  in  the  string
																						and
															 at  least  one  char  should  be  alphabet  (or)  digit

3) What  is  isalpha()  +  isdigit()  called ?  ---> isalnum()
'''
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  # False
print('HYD' . isalnum())    # True
print('+-$' . isalnum())    # False
print('hyd' . isalnum())    # True
print('hYd' . isalnum())    # True
print('9247' . isalnum())   # True
print('' . isalnum())       # False
print('A7g9'  . isalnum())  # True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  # False
print('\n  \t' . isspace())   # True
print('\n  7\t' . isspace())  # False
print('\n' . isspace())       # True
print('\n  $\t' . isspace())  # False
print('\t' . isspace())       # True
print('' . isspace())         # False
print(' ' . isspace())        # True
                                                               

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))    # a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))    # a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))    # a  :  Hyd  	  b  :  10.8  	  c  :  25  
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))    # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  : {z}  ' . format(x = a , y = b , z = c))    # a  :  25  	  b  :  10.8  	  c  :  Hyd  
print('a  :  {x}  \t  b  :  {y}  \t  c  : {z}  ' . format(z = a , y = b , x = c))    # a  :  Hyd  	  b  :  10.8  	  c  :  25  
print('a  :  {z}  \t  b  :  {z}  \t  c  : {z}  ' . format(z = a , y = b , x = c))    # a  :  25  	  b  :  25  	  c  :  25  



'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif'''

a= input("Enter any character : ")
if a.isalnum():   
   print("Alpha Numeric Character")
   if a.isalpha():
      print("Alphabet Character")
      if a.isupper():
         print("Upper case Alphabet")
      elif a.islower():
         print("Lower case Alphabet")
   elif a.isdigit():
      print("Digit character")
else:
   if a.isspace():
      print("White space character")
   else:
      print("Special character")




'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1        'd'             '' + 'd' = 'd'
     2       'y'             'd' + 'y' = 'dy'
     3       'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''


a=input("enter string : ")
b=''
for i in range(1,len(a)+1):
   b+=a[-i]
print(b)



'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
   1        'city'         '' + 'city' + ' '=  'city '
   2        'green'     'city ' + 'green' + ' ' = 'city green '
   3        'is'            'city green ' + 'is' + ' ' =  'city green is '
   4        'Hyd'        'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''

a=input("enter string : ")
b=a.split(' ')
c=''
for i in range(1,len(b)+1):
   c+=b[-i]+' '
print(c)


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
   What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

a = input("Enter a sentence: ")
b = a.split()
for i in b:
   print(i[::-1], end=' ')


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
a=input("Enter a string: ")
b=a.upper()
c= sorted(b)  
print(''.join(c))


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''


a = input("Enter a string: ")
b=sorted(a)
num=alpha=''
for i in range(len(a)):
   if b[i].isdigit():
      num+=b[i]
   else:
      alpha+=b[i]
print("digits: ",num)
print("alpha: ",alpha)