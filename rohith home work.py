[12:03 pm, 14/8/2025] +91 99482 50500: # isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())  #False
print('Hyd' . isdigit())  #False
print('+-$' . isdigit())  #False
print('A2#' . isdigit())  #False
print('' . isdigit())  #False
print(' ' . isdigit())  #False
print(9247 . isdigit())  #False


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
[12:07 pm, 14/8/2025] +91 99482 50500: # isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())  #False
print('+-$' . isupper())   #False
print('HYD123' . isupper())  #False
print('HYD+-$' . isupper())  #False
print('' . isupper())  #False
print('A2#' . isupper())  #False


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
[12:09 pm, 14/8/2025] +91 99482 50500: # islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower()) #false
print('+-$' . islower())  #False
print('hyd+-$' . islower())  #False
print('abc123' . islower())  #false
print('' . islower())  #False
print('a2#' . islower())  #False


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet
[12:12 pm, 14/8/2025] +91 99482 50500: # isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())   #False
print('hyd' . isalnum())  #False
print('hYd' . isalnum())  #False
print('9247' . isalnum())  #False
print('' . isalnum())    #False
print('A7g9'  . isalnum())  #False


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
[12:14 pm, 14/8/2025] +91 99482 50500: # isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace()) #False
print('\n' . isspace())  #False
print('\n  $\t' . isspace())  #False
print('\t' . isspace()) #False
print('' . isspace()) #False
print(' ' . isspace())  #False


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
[12:29 pm, 14/8/2025] +91 99482 50500: # Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
[12:33 pm, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''
[12:33 pm, 14/8/2025] +91 99482 50500: Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet
[12:34 pm, 14/8/2025] +91 99482 50500: Enter  any  character  :  7
Alpha  Numeric  Character
Digit  character
[12:35 pm, 14/8/2025] +91 99482 50500: '''
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
[12:36 pm, 14/8/2025] +91 99482 50500: Enter  any  string : Rama Rao
Reverse  String :   oaR amaR
[12:39 pm, 14/8/2025] +91 99482 50500: '''
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
[12:39 pm, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
[12:40 pm, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
[12:43 pm, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579


[10:59 am, 14/8/2025] +91 99482 50500: Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
[11:01 am, 14/8/2025] +91 99482 50500: '''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')



'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''
[11:07 am, 14/8/2025] +91 99482 50500: '''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->   Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len…
[11:08 am, 14/8/2025] +91 99482 50500: '''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''
[11:12 am, 14/8/2025] +91 99482 50500: #  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48))
print(a . count('was'))


'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
														Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1
'''
[11:12 am, 14/8/2025] +91 99482 50500: #  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))
[11:18 am, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''
[11:33 am, 14/8/2025] +91 99482 50500: #  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)
[11:33 am, 14/8/2025] +91 99482 50500: # Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
print(a . split(''))
[11:33 am, 14/8/2025] +91 99482 50500: # Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))
[11:34 am, 14/8/2025] +91 99482 50500: # Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())
print(a . split(' '))
[11:34 am, 14/8/2025] +91 99482 50500: # Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))
[11:34 am, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''
[11:36 am, 14/8/2025] +91 99482 50500: Enter the expression: 123+45+6+789
Sum:  963
[11:49 am, 14/8/2025] +91 99482 50500: #  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))
d = ['www' , 'gmail', 'com']
print('.' . join(d))
e = [15 , 36 , 48]
print(':' . join(e))
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))
g = range(5)
print('-' . join(g))
[11:58 am, 14/8/2025] +91 99482 50500: # endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))
[11:59 am, 14/8/2025] +91 99482 50500: '''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''
[12:01 pm, 14/8/2025] +91 99482 50500: #  isalpha()  method  demo  program (Home  work)