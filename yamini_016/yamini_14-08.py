
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index:= a.find('is', index + 1)) != -1:
    print(index)
print('End')


'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . index('is')
try:
    while  index != -1:
	    print(index)
	    index = a . index('is' , index + 1)
    print('End')
except ValueError:
      print('last occurance is at ',index)    


'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , 0,index+1 )
print('End')


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rindex('is')
try:
    while  index != -1:
	    print(index)
	    index = a . rindex('is' ,0, index + 1)
    print('End')
except ValueError:
      print('last occurance is at ',index) 


#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) # checks for is in between the indexes 19 to 47 ie 3
print(a . count('was'))# checks for was in string  as it is not there 0


#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))# counts the spaces in the whole string i.e 3
print(a . count('\t'))# counts the tab character in the whole string i.e 3
print(a .count('\n'))# counts the new line character in the whole string i.e 3

Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le

a='babble'
b=a[1:]
b=b.replace('b','*')
print(a[:1]+b)

#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':')) # splits the string with : and gives list  i.e -['15','36','48']
print(a)# a is not modified as string is immutable

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # returns a list after seperating the string based on spaces ['Hyd\nis', 'green\tcity']
print(a . split()) # reruns  a list of strings after removing all white spaces ['Hyd', 'is', 'green', 'city']
print(a . split('green')) # reruns  a list of strings after removing all greens ['Hyd\nis ', '\tcity']
print(a.split('')) # argument should be a delimiter or string but not empty so error


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # removes the tab spaces and returns the list ['Hyd', 'is', 'green', 'city']
print(a . split()) # all white spaces are removed ['Hyd', 'is', 'green', 'city']
print(a. split(' ')) # spaces are removed as there are no spaces whole string is printed as one

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())# all spaces are removed ['Hyd', 'is', 'green', 'city']
print(a. split(' ')) # seperates the words based on spaces and only one space between words is removed ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a.split('.')) # removes . and prints the list of seperated strings ['www', 'gmail', 'com']

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''
Enter the expression: 123+45+6+789
Sum:  963

a=(input('enter an expression: '))
a=a.split('+')
sum=0
for x in a:
        sum+=eval(x)
print('Sum: 'sum)

#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # joins the list of strings to a string with : between them 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))# joins the tuple of strings to a string with space between them  Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # joins the set of strings to a string with comma in between them in any order
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # # joins the list of strings to a string with . between them www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) # error because elements inside sequence should be string but not integer
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #  joins the list of strings to a string without spaces between them SankarDayalSarma
g = range(5)
print('-'.join(g)) # # error because elements inside sequence should be string but not integer


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) # true because the string ends with city
print(a . endswith('town')) # false as string doesnt with town
print(a . endswith('green' , 3 , 12)) #true because by the 11 th index the ending string is green
print(a . endswith('green' , 3 , 13)) # false because by 12th the character the ending string has space along with green
print(a . endswith(' ',3,13)) # true because the string ends with space at 12th position
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

a=input('enter a string : ')
if(len(a)>3):
    if(a.endswith('ing')):
        a=a+'ly'
    else:
        a=a+'ing'
print(a)

print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha()) # false as it has digit in the string
print('Hyd$'  . isalpha()) # false as it has special character in the string
print('9247'  .  isalpha())# false as it has digits in the string
print('+-$'    .  isalpha())# false as it has special character in the string
print('A2#'  .   isalpha()) # false as it has digit and special character in the string
print(''  .  isalpha()) # false as it is empty string
print(' '  .  isalpha()) # false as it is a space


# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit()) # false as it has special character in it
print('Hyd' . isdigit()) #false as it has alphabet in string
print('+-$' . isdigit()) #false as it has special character in it
print('A2#' . isdigit())  #false as it has alphabet and special character in it
print('' . isdigit())  #false as it is empty string
print(' ' . isdigit())  #false as it is space
print(9247 . isdigit()) # error as the the prgm searches for isdigit method in int class

# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper()) # true as there are no lower case and atleast one char is upper
print('+-$' . isupper())# false as no upper case alphabets
print('HYD123' . isupper()) # true as there are no lower case and atleast one char is upper
print('HYD+-$' . isupper())# true as there are no lower case and atleast one char is upper
print('' . isupper()) ## false as no upper case alphabets
print('A2#' . isupper()) # true as there are no lower case and atleast one char is upper


# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())# true as there are no upper case and atleast one char is lower
print('+-$' . islower()) # false as no lower case alphabets
print('hyd+-$' . islower()) # true as there are no upper case and atleast one char is lower
print('abc123' . islower()) # true as there are no upper case and atleast one char is lower
print('' . islower()) # false as no lower case alphabet
print('a2#' . islower()) # true as there are no upper case and atleast one char is lower


# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())  # false as there are special characters
print('hyd' . isalnum())  #true as it has no special char and have alphabets
print('hYd' . isalnum()) #true as it has no special char and have alphabets
print('9247' . isalnum()) #  true as it has no special char and have alphabets
print('' . isalnum()) # false as there are no alphabets or digits
print('A7g9'  . isalnum()) #true as it has no special char and have alphabets and digits


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace()) # false as every charaCTER IS not a white space
print('\n' . isspace()) #  True
print('\n  $\t' . isspace())  # false as every charaCTER IS not a white space
print('\t' . isspace()) # true
print('' . isspace()) # false as every charaCTER IS not a white space and it is a empty string
print(' ' . isspace()) # true


a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # a  :  25<tab space> b  :  10.8<tab space>c  :  Hyd 
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))# a  :  25<tab space> b  :  10.8<tab space>c  :  Hyd 
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))# a  :  Hyd<tab space> b  :  10.8<tab space>c  :  25 
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  Hyd<tab space> b  :  Hyd<tab space>c  :  Hyd 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))# a  :  25<tab space> b  :  10.8<tab space>c  :  Hyd 
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # a  :  Hyd<tab space> b  :  10.8<tab space>c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a ,y=b,x=c)) # a  :  25<tab space> b  :  25<tab space>c  :  25


'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''

a=input('enter a character: ')
if(a.isalnum()):
    print('Alphanumeric Character')
    if(a.isalpha()):
        print('Alphabet Character')
        if(a.isupper()):
            print('Upper Case Alphabet')
        else:
            print('Lower Case Alphabet')
    else:
        print('Digit Character')
else:
    print('Special Character')

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


a=input('enter a string: ')
rev=''
for i in range(1,len(a)+1):
    rev=rev+a[-i]
print(rev)


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
   

'''

a=input('enter a string: ')
a=a.split()
b=''
for i in range(1,len(a)+1):
    b+=a[-i]+' '
print(b)


'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

a=input('enter a string: ')
a=a.split()
b=''
for i in range(len(a)):
    c=a[i]
    b+=c[::-1]+' '
print(b)


'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

a=input('enter a string: ')
b=sorted(a)
c='' 
for i in b:
    c+=i
print(c)

'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

a=input('enter a string: ')
b=sorted(a)
digit=''
char=''
for i in b:
    if i.isdigit():
        digit+=i
    else:
        char+=i
print(char+digit)





