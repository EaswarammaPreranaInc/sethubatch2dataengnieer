#  count()  method  demo  program (Home  work)

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) # 3
print(a . count('was')) # 0
-------------------------------

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # 3
print(a . count('\t')) # 2
print(a . count('\n')) # 3
---------------------------------------

# Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

s = input("Enter a string: ")
first_char = s[0]  
result = first_char + s[1:].replace(first_char, '*')
print("Result:", result)
----------------------------------

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # ['15' , '36' , '48']
print(a) # 15 :  36 : 48
---------------------------

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # ['Hyd\nis', 'green\tcity']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split('green')) # ['Hyd\nis ', '\tcity']
print(a . split('')) # error
------------------------------

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd\tis\tgreen\tcity']
--------------------------------

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']
--------------------------------

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']
--------------------------

Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result

program:-
----------
expr = input("Enter an expression with + symbols: ")  
numbers = expr.split('+')
total = sum(int(num) for num in numbers)

print("Sum =", total)

---------------------------------

#  Find  outputs  (Home  work)

a = ['15' , '36' , '48']
print(':' . join(a))		 # 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))	 # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) 	# 25,20,15,10,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))	 # www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) 	# error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))		 # SankarDayalSarma
g = range(5)
print('-' . join(g)) 	# error
----------------------------------

# endswith()  method  demo  progrram (Home  work)

a = 'Hyd is green city'
print(a . endswith('city')) # True
print(a . endswith('town')) # False
print(a . endswith('green' , 3 , 12)) # True
print(a . endswith('green' , 3 , 13)) # False
print(a . endswith(' ' , 3 , 13)) # True
----------------------------

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''
program:-
-----------
s = input("Enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"

print(result)

---------------------------

#  isalpha()  method  demo  program (Home  work)

print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha()) #  False
print('Hyd$'  . isalpha()) # False
print('9247'  .  isalpha()) # False
print('+-$'    .  isalpha()) # False
print('A2#'  .   isalpha()) # False
print(''  .  isalpha()) # False
print(' '  .  isalpha()) # False

------------------------------------

# isdigit()  method  demo  program  (Home  work)

print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit()) # False
print('Hyd' . isdigit()) # False
print('+-$' . isdigit()) # False
print('A2#' . isdigit()) # False
print('' . isdigit()) # False
print(' ' . isdigit()) # False
print(9247 . isdigit()) # error
-----------------------------

# isupper()  method  demo  program  (Home  work)

print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper()) # True
print('+-$' . isupper()) # False
print('HYD123' . isupper()) # True
print('HYD+-$' . isupper()) # True
print('' . isupper())  #  False
print('A2#' . isupper()) # True
-------------------------------------

# islower()  method  demo  program  (Home  work)

print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower()) # True
print('+-$' . islower()) # False
print('hyd+-$' . islower()) # True
print('abc123' . islower()) # True
print('' . islower()) # False
print('a2#' . islower()) # True
----------------------------------------

# isalnum()  method  demo  program  (Home  work)

print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum()) # False
print('hyd' . isalnum()) # True
print('hYd' . isalnum()) # True
print('9247' . isalnum()) # True
print('' . isalnum()) # False
print('A7g9'  . isalnum()) # True
-------------------------------

# isspace()  method  demo  program  (Home  work)

print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace()) # False
print('\n' . isspace()) # True
print('\n  $\t' . isspace()) # False
print('\t' . isspace()) # True
print('' . isspace()) # False
print(' ' . isspace()) # True
---------------------------------

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #  a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  25  	  b  :  25  	  c  :  25
----------------------------------

'''
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

program:-
---------
ch = input("Enter a character: ")

if ch.isalnum():  # Alphabet or Digit
    print("Alphanumeric character")

    if ch.isalpha():  # Alphabet
        print("Alphabet character")
        if ch.isupper():
            print("Upper case alphabet")
        else:
            print("Lower case alphabet")
    elif ch.isdigit():  # Digit
        print("Digit character")

elif ch.isspace():  # Whitespace
    print("White space")

else:  # Special character
    print("Special character")
--------------------------------------

# Write  a  program  to  reverse  a  string  without  slice

a = input("Enter a string: ")
b = ''  # to store reversed string

for i in range(1, len(a) + 1):
    b = b + a[-i]   # taking characters from the end
print("Reversed string:", b)
---------------------------

# Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

a = input("Enter a sentence: ")
b = a.split()   # list of words
c = ''          # to store reversed order sentence
for i in range(1, len(b) + 1):
    c = c + b[-i] + ' '   # last to first
print("Reversed order of words:", c)
-------------------------------

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
# Program:-
--------------
a = input("Enter a sentence: ")
b = a.split()   # split into words
c = ''          # final string

for word in b:
    c = c + word[::-1] + ' '   # reverse each word using slicing
print("Reversed each word:", c)
------------------------
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
# Program :-
--------------
a = input("Enter a string: ")
b = sorted(a)             # returns list of characters in sorted order
c = ''.join(b)            # join back to a string
print("Sorted string:", c)
-------------------------------------------

'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
program:-
-----------
a = input("Enter a string: ")
b = sorted(a)

# Separate alphabets and digits
alpha = ''
digit = ''

for ch in b:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch
result = alpha + digit
print("Result:", result)

























































































