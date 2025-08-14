

'''
1)Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')

'''  
2)index()  method  demo  program

Modify  the  following  program  with  index()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = -1
try:
    while True:
        index = a.index('is', index + 1)
        print(index)
except ValueError:
    print('End')

'''
3)rfind()  method  demo  program

Modify  following  program  with  rfind()  method

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')

'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = a.rfind('is')
while index != -1:
    print(index)
    index = a.rfind('is', 0, index)
print('End')

'''  
4)rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'

index = len(a)  
try:
    while True:
        index = a.rindex('is', 0, index)
        print(index)
except ValueError:
    print('End')

# 5) count()  method  demo  program 
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #2
print(a . count('was')) #0

#  6) Find  outputs  
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #3
print(a . count('\t')) #3
print(a . count('\n')) #3

'''
7)Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''

a = 'babble'
first_char = a[0]
result = first_char + a[1:].replace(first_char, '*')
print(result)

# 8)  Find  outputs  
a = '15:36:48'
print(a . split(':'))# ['15', '36', '48']
print(a) #15:36:48

# 9) Find  outputs  
a = 'Hyd\nis green\tcity'
print(a . split(' '))# ['Hyd\nis', 'green\tcity']
print(a . split()) #['Hyd', 'is', 'green', 'city']
print(a . split('green'))# ['Hyd\nis ', '\tcity']
#print(a . split(''))# ValueError: empty separator

# 10) Find  outputs  
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split())# ['Hyd', 'is', 'green', 'city']
print(a . split(' '))# ['Hyd\tis\tgreen\tcity']

# 11) Find  outputs 
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())# ['Hyd', 'is', 'green', 'city']
print(a . split(' '))# ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# 12) Find  outputs  
a = 'www.gmail.com'
print(a . split('.')) # ['www', 'gmail', 'com']

'''
13)Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''

expr = input("Enter an expression with + : ")
numbers = expr.split('+')
total = 0
for num in numbers:
    total += int(num)

print("Sum =", total)

# 14) Find  outputs  
a = ['15' , '36' , '48']
print(':' . join(a))# 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # 25,15,10,20,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com
e = [15 , 36 , 48]
#print(':' . join(e))# Error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))# SankarDayalSarma
g = range(5)
#print('-' . join(g))# Error

# 15)endswith()  method  demo  progrram 
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13)) #False
print(a . endswith(' ' , 3 , 13))# True

'''
16)Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''
word = input("Enter a word: ")

if len(word) < 3:
    result = word
elif word.endswith("ing"):
    result = word + "ly"
else:
    result = word + "ing"

print("Result:", result)

#  17) isalpha()  method  demo  program
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha())#   False
print('Hyd4'  . isalpha()) #False
print('Hyd$'  . isalpha())#False
print('9247'  .  isalpha()) #False
print('+-$'    .  isalpha()) #False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha()) #False

# 18)isdigit()  method  demo  program
print('9247' . isdigit()) # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())  # False
print('Hyd' . isdigit()) # False
print('+-$' . isdigit())# False
print('A2#' . isdigit()) # False
print('' . isdigit()) # False
print(' ' . isdigit()) # False
#print(9247 . isdigit()) # False

#19) isupper()  method  demo  program  
print('HYd' . isupper())#   False
print('HYD' . isupper()) #   True
print('9247' . isupper()) #   False
print('RAMA  RAO' . isupper())# True
print('+-$' . isupper())#False
print('HYD123' . isupper())  #True
print('HYD+-$' . isupper()) #True
print('' . isupper())   #False
print('A2#' . isupper())   #True

# 20) islower()  method  demo  program  
print('hyD' . islower()) #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower()) #True
print('+-$' . islower())   #False
print('hyd+-$' . islower()) #True
print('abc123' . islower())  #True
print('' . islower()) #False
print('a2#' . islower()) #True

# 21)isalnum()  method  demo  program  
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())# False
print('hyd' . isalnum())# True
print('hYd' . isalnum()) #True
print('9247' . isalnum())#True
print('' . isalnum())# False
print('A7g9'  . isalnum())# True

#22) isspace()  method  demo  program  
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace())   #  True
print('\n  7\t' . isspace())   # False
print('\n' . isspace())  # True
print('\n  $\t' . isspace()) # False
print('\t' . isspace())   # True
print('' . isspace())    # False
print(' ' . isspace())  #True

# 23) Find  output
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))    # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))   # a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))    # a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))    # a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))  #a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))   #a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))   # a  :  25  	  b  :  25  	  c  :  25

'''
24)Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''
ch = input("Enter a single character: ")

if ch.isalnum():  
    print("Alphanumeric character")
    if ch.isalpha():  
        print("Alphabet character")
        if ch.isupper():
            print("Upper case alphabet")
        elif ch.islower():
            print("Lower case alphabet")
    elif ch.isdigit():
        print("Digit character")

elif ch.isspace():  
    print("White space")

else: 
    print("Special character")

'''
25)Write  a  program  to  reverse  a  string  without  slice

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
s = input("Enter a string: ")
rev = "" 
for i in range(1, len(s) + 1):
    rev = rev + s[-i]  
print("Reversed string:", rev)

'''
26) Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

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
s = input("Enter a sentence: ")
words = s.split()   
rev_sentence = ""   

for i in range(1, len(words) + 1):
    rev_sentence += words[-i] + " "   

print("Reversed sentence:", rev_sentence)

'''
27) Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
s = input("Enter a sentence: ")
words = s.split()   
rev_sentence = ""

for word in words:
    rev_sentence += word[::-1] + " "   

print("Reversed each word:", rev_sentence.strip())

'''
28) Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
s=input("Enter a string:")
b=''
print(b.join(sorted(s)))

'''
29) Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
s="Z9K3PA7D51"
alpha=sorted([ch for ch in s if ch.isalpha()])
digit=sorted([ch for ch in s if ch.isdigit()])
result="".join(alpha)+"".join(digit)
print(result)