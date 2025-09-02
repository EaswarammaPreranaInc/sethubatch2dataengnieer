'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1
while (index := a.find('is', index + 1)) != -1:
	print(index)
print('End')


'''
Outputs:

4
23
42
46
End
'''


'''  
(Home  work)
index()  method  demo  program
Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    b = a . index('is')
    while  True:
        print(b)
        b = a . index ('is' , b + 1)
    print('End')
except ValueError:
	print("index method throws error when substring is not found")

'''
Outputs:

4
23
42
46
index method throws error when substring is not found
'''





'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is', 0, index)
print('End')

'''
Outputs:

46
42
23
4
End
'''




'''
(Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a . rindex('is')
    while  True:
        print(index)
        index = a . rindex('is' , 0, index)
except ValueError:
    print("index() method throws error when substring is not found")

'''
Outputs:

46
42
23
4
index() method throws error when substring is not found
'''







#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) # prints 4
print(a . count('is' , 19 , 48)) # prints 3
print(a . count('was')) # 0







#Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) # prints 3
print(a . count('\t')) # prints 3
print(a . count('\n')) # prints 3








'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ? ---> ba**le
'''
a = input("Enter string:")
b = a[0]
c = a[0] + a[1:].replace('b', "*")
print(c)

'''
Outputs:

Enter string:babble
ba**le
'''





#  Find  outputs  (Home  work)
a = '15:36:48' # Ref 'a' points to string '15:36:48'
print(a . split(':')) # prints ['15', '36', '48']
print(a) # prints '15:36:48' because string is immutable









# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) # prints ['Hyd\nis','green\tcity']
print(a . split()) # prints['Hyd' 'is', 'green' 'city']
print(a . split('green')) # ['Hyd\nis', '\tcity']
print(a . split('')) # Error because there is empty delimeter as argument









# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # prints ['Hyd', 'is', 'green', 'city']
print(a . split()) # prints ['Hyd', 'is', 'green', 'city' ]
print(a . split(' ')) # prints ['Hyd\tis\tgreen\tcity']



# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) # prints ['Hyd', 'is', 'green', 'city']
print(a . split(' ')) # prints ['Hyd,'', '', 'is', '', '', 'green', '', '', 'city']



# Find  outputs  (Home  work)
a = 'www.gmail.com' # Ref 'a' points to string
print(a . split('.')) # prints['www', 'gmail', 'com']



'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print the sum result
Enter the expression: 123+45+6+789
Sum: 963
'''
a = input("Enter string:")
b = a.split('+')
sum = 0
print(b)
for i in b:
    sum += int(i)
print("Sum:", sum)

'''
Outputs:

Enter string: 123+45+6+789
[' 123', '45', '6', '789']
Sum: 963
'''




#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) # prints '15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) # prints 'Hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # prints '10,20,15,25,52'
d = ['www' , 'gmail', 'com']
print('.' . join(d)) # prints 'www.gmail.com'
e = [15 , 36 , 48]
#print(':' . join(e)) # Error because it e should be list of strings but not list of integers and there is no join method in list class
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # prints 'SankarDayalSarma'
g = range(5)
print('-' . join(g)) # Error because range function returns integers but not strings so there is no join method in range




# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))  # prints True
print(a . endswith('town')) # prints False
print(a . endswith('green' , 3 , 12)) # prints True
print(a . endswith('green' , 3 , 13)) # prints False
print(a . endswith(' ' , 3 , 13)) # prints True




'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  ---> Hi itself
'''
a = input("Enter string:")
if len(a) <= 3:
    result = a
elif a.endswith('ing'):
    result = a + 'ly'
else:
    result = a + 'ing'
print(result)

'''
Outputs:

Enter string:interest
interesting

Enter string:interesting
interestingly

Enter string:Hi
Hi
'''


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #  prints True
print('Rama  Rao'  . isalpha()) # prints False
print('Hyd4'  . isalpha()) # prints False
print('Hyd$'  . isalpha()) # prints False
print('9247'  .  isalpha()) # prints False
print('+-$'    .  isalpha()) # prints False
print('A2#'  .   isalpha()) # prints False
print(''  .  isalpha()) # prints False
print(' '  .  isalpha()) # prints False




# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit()) # prints True
print('92a47' . isdigit()) # prints False
print('92$47' . isdigit()) # prints False
print('Hyd' . isdigit()) # prints False
print('+-$' . isdigit()) # prints False
print('A2#' . isdigit()) # prints False
print('' . isdigit()) # prints False
print(' ' . isdigit()) # prints False
print(9247 . isdigit()) # Error because is digit is a method of str class but not int class




# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  prints False
print('hyd' . islower())  #  prints True
print('9247' . islower())  # prints False
print('rama  rao' . islower()) # prints True
print('+-$' . islower()) # prints False
print('hyd+-$' . islower()) # prints True
print('abc123' . islower()) # prints True
print('' . islower()) # prints False
print('a2#' . islower()) # prints True




															 
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  prints False
print('HYD' . isalnum())  #  prints True
print('+-$' . isalnum()) # prints False
print('hyd' . isalnum()) # prints True
print('hYd' . isalnum()) # prints True
print('9247' . isalnum()) # prints True
print('' . isalnum()) # prints False
print('A7g9'  . isalnum()) # prints True





# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  # prints False
print('\n  \t' . isspace()) # prints True
print('\n  7\t' . isspace()) # prints False
print('\n' . isspace()) # prints True
print('\n  $\t' . isspace()) # prints False
print('\t' . isspace()) # prints True
print('' . isspace()) # prints False
print(' ' . isspace()) # prints True

'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special character
'''




# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) # prints 'a : 25<tab>b : 10.8<tab>c : Hyd'
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # prints 'a : 25 <tab>b : 10.8<tab>c : Hyd'    
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # prints 'a : Hyd<tab>b : 10.8<tab>c : 25'
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # prints 'a : Hyd<tab>b : Hyd<tab>c : Hyd'
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # prints 'a : 25  b : 10.8    c : Hyd'
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) # prints 'a : Hyd  b : 10.8    c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a ,y = b , x = c)) # prints 'a : 25  b : 25  c : 25'



'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if and elif
'''

'''
Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper case Alphabet
Enter any character  :  7
Alpha Numeric Character
Digit character
'''
a = input("Enter any string:")
if a.isalnum():
    print("Alphanumeric character")
    if a.isalpha():
        print("Alphabet character")
        if a.isupper():
            print("Upper case character")
        elif a.islower():
            print("lower case alphabet")
    elif a.isdigit():
        print("digit  character")
elif a.isspace():
    print("White space")
else:
    print("Special character")

'''
Outputs:

Enter any string:A
Alphanumeric character
Alphabet character
Upper case character

Enter any string:a
Alphanumeric character
Alphabet character
lower case alphabet

Enter any string:7
Alphanumeric character
digit  character

Enter any string:
Special character

Enter any string:$
Special character
'''


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
Enter  any  string : Rama Rao
Reverse  String : oaR amaR
'''

a = input("Enter any string:")
b = ''
for i in range(1,len(a) + 1):
    b += a[-i]
print(b)

'''
Output:

Enter any string:Hyd
dyH

Enter any string:Rama Rao
oaR amaR
'''


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
a = input("Enter any string:")
b = a.split()
print(b)
c = ''
for i in range(1, len(b) + 1):
    c += b[-i] + ' '
print(c)

'''
Outputs:

Enter any string:Hyd is green city 
['Hyd', 'is', 'green', 'city']
city green is Hyd
'''



'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also slice
'''
a = input("Enter any string:")
b = a.split()
print(b)
result = ''
for i in b:
    result += i[::-1] + ' '
print(result)

'''
Outputs:

Enter any string:Hyd  is  green  city
['Hyd', 'is', 'green', 'city']
dyH si neerg ytic
'''



'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  ---> AEHJRS
'''
a = input("Enter any string:")
b = sorted(a)
result = ''
for i in b:
    result += i
print(result)

'''
Outputs:

Enter any string:RAJESH
AEHJRS
'''



'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
a = input("Enter any string:")
b = sorted(a)
print(b)
alpha = ''
digit = ''
for i in b:
    if i.isalpha():
        alpha += i 
    elif i.isdigit():
        digit += i 
print(alpha + digit)

'''
Outputs:

Enter any string:Z9K3PA7D51
['1', '3', '5', '7', '9', 'A', 'D', 'K', 'P', 'Z']
ADKPZ13579

'''
