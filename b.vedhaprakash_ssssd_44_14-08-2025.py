'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')
'''
##

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

####################################################################################################


'''  (Home  work)
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

## 
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

####################################################################################################

'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . find('is')
while  index != -1:
	print(index)
	index = a . find('is' , index + 1)
print('End')



'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''

###
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
start_index = 0
try:
    while True:
        index = a.index('is', start_index)
        print(index)
        start_index = index + 1
except ValueError:
    print('End')

###############################################################################################


'''(Home  work)
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


###

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = len(a)
while (index := a.rfind('is', 0, index)) != -1:
    print(index)
print('End')

###############################################################################################
'''  (Home  work)
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


##

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
start_index = len(a)

try:
    while True:
        index = a.rindex('is', 0, start_index)
        print(index)
        start_index = index

except ValueError:
    print('End')


###############################################################################################

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))
print(a . count('\t'))
print(a . count('\n'))

## outputs are 
3
3
3

###############################################################################################

'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''


##

s1 = 'babble'

if len(s1) < 2:
    print(s1)
else:
    print(s1[0] + s1[1:].replace(s1[0], '*'))

s2 = 'programming'

if len(s2) < 2:
    print(s2)
else:
    print(s2[0] + s2[1:].replace(s2[0], '*'))

###############################################################################################
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)
The outputs for the program


['15', '36', '48']
15:36:48

#############################################################################################

# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))
print(a . split())
print(a . split('green'))
print(a . split(''))


##

['Hyd\nis', 'green\tcity']
['Hyd', 'is', 'green', 'city']
['Hyd\nis ', '\tcity']



#############################################################################################

# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))
print(a . split())
print(a . split(' '))

##


['Hyd', 'is', 'green', 'city']
['Hyd', 'is', 'green', 'city']
['Hyd\tis\tgreen\tcity']

#############################################################################################

# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())
print(a . split(' '))

##
['Hyd', 'is', 'green', 'city']
['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

#############################################################################################

# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))

## 

['www', 'gmail', 'com']


#############################################################################################


'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''

##
a = '123+45+6+789'
parts = a.split('+')
total = 0

for part in parts:
    total += int(part)

print(total)

#############################################################################################

#  Find  outputs  (Home  work)
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

##

15:36:48
Hyd is green city
15,25,20,10,52
www.gmail.com
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found
SankarDayalSarma
Traceback (most recent call last):
  File "<string>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

#############################################################################################


# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))
print(a . endswith('town'))
print(a . endswith('green' , 3 , 12))
print(a . endswith('green' , 3 , 13))
print(a . endswith(' ' , 3 , 13))

##

True
False
True
False
True


#############################################################################################
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

#######
# Example 1: input is 'interest'
s = 'interest'
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')

# Example 2: input is 'interesting'
s = 'interesting'
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')

# Example 3: input is 'Hi'
s = 'Hi'
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')

#############################################################################################

#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())
print('Hyd$'  . isalpha())
print('9247'  .  isalpha())
print('+-$'    .  isalpha())
print('A2#'  .   isalpha())
print(''  .  isalpha())
print(' '  .  isalpha())



'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''


###
True
False
False
False
False
False
False
False
False

##############################################################################################################################

# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())
print('Hyd' . isdigit())
print('+-$' . isdigit())
print('A2#' . isdigit())
print('' . isdigit())
print(' ' . isdigit())
print(9247 . isdigit())


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''

############

True
False
False
False
False
False
False
False
Traceback (most recent call last):
  File "<string>", line 1, in <module>
AttributeError: 'int' object has no attribute 'isdigit'

######################################################################################################################################

# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())
print('+-$' . islower())
print('hyd+-$' . islower())
print('abc123' . islower())
print('' . islower())
print('a2#' . islower())


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet
###
False
True
False
True
False
True
True
False
True
######################################################################################################################################


# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('' . isalnum())
print('A7g9'  . isalnum())


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

###

False
True
False
True
True
True
False
True

################################################################################################################################################

# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())
print('hyd' . isalnum())
print('hYd' . isalnum())
print('9247' . isalnum())
print('' . isalnum())
print('A7g9'  . isalnum())


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

###
False
True
False
True
True
True
False
True

##############################################################################################################################


# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())
print('\n' . isspace())
print('\n  $\t' . isspace())
print('\t' . isspace())
print('' . isspace())
print(' ' . isspace())


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''

##
False
True
False
True
False
True
False
True

############################################################################

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))


#######

a : 25 	 b : 10.8 	 c : Hyd 
a : 25 	 b : 10.8 	 c : Hyd 
a : Hyd 	 b : 10.8 	 c : 25 
a : Hyd 	 b : Hyd 	 c : Hyd 
a : 25 	 b : 10.8 	 c : Hyd 
a : Hyd 	 b : 10.8 	 c : 25 
a : 25 	 b : 25 	 c : 25 

###########################################################################

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



##

input_char = input("Enter a single character: ")

if len(input_char) == 1:
    if input_char.isalnum():
        print("Alphanumeric character")
        if input_char.isalpha():
            print("Alphabet character")
            if input_char.islower():
                print("Lower case alphabet")
            else:
                print("Upper case alphabet")
        else:
            print("Digit character")
    elif input_char.isspace():
        print("White space")
    else:
        print("Special character")
else:
    print("Please enter a single character only.")

########################################################################################################################################################


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

Enter  any  string : Rama Rao
Reverse  String :   oaR amaR


## 
s = input("Enter a string: ")
reversed_string = ''

for i in range(1, len(s) + 1):
    reversed_string += s[-i]

print(f"The reversed string is: {reversed_string}")

#########################################################################################################


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

######

s = input("Enter a string: ")
words = s.split()
reversed_sentence = ''

for i in range(1, len(words) + 1):
    reversed_sentence += words[-i] + ' '

print("Reverse String:", reversed_sentence.strip())



###########################################################################################'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

###
s = input("Enter a sentence: ")
words = s.split()
reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

reversed_sentence = ' '.join(reversed_words)

print("The sentence with each word reversed is:", reversed_sentence)


#################################################################################################

'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

####
s = input("Enter a string: ")
sorted_string = ''.join(sorted(s))

print("The string in alphabetical order is:", sorted_string)



############################################################################################


'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

#######



s = input("Enter a string with letters and numbers: ")
alphabets = ''
digits = ''

for char in s:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        digits += char

sorted_alphabets = ''.join(sorted(alphabets))
sorted_digits = ''.join(sorted(digits))

final_string = sorted_alphabets + sorted_digits

print("The sorted string is:", final_string)
#################################################################################################################################################

