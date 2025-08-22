'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
b = 0
while (index := a.find('is',b)) != -1:
    print(index)
    b = index + 1
print('End')

'''
Output:
4
23
42
46
End
'''

'''(Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
    index = a . index('is')
    while  True:
        print(index)
        index = a . index('is' , index + 1)
except:
    print('End')

'''
Output:
4
23
42
46
End
'''


'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a .rfind('is')
while  index != -1:
	print(index)
	index = a .rfind('is' ,0,index)
print('End')


'''
output:
46
42
23
4
End
'''

'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->   Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  --->  Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  --->  +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1
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
    while  index != -1:
        print(index)
        index = a . rindex('is' ,0, index)
except:
    print('End')
'''
output:
46
42
23
4
End
'''


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) #Count the number of 'is' from index 19 to 47 #Output: 3
print(a . count('was')) #Counts the number of 'was' in the string a if not found returns 0



'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
														Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1
'''

# Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' ')) #Counts the number of spaces in the string a #Output : 3
print(a . count('\t')) #Counts the number of tab spaces in the string a #Output : 3
print(a . count('\n')) #Counts the number of new lines in the string a #Output : 3




'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''

s = input("Enter a string: ")
b = s[0]
print(b + s[1:].replace(b, '*'))

'''output:
Enter a string: bubble
bu**le
'''

#  Find  outputs  (Home  work)
a = '15:36:48' 
print(a . split(':')) #['15','36','48']
print(a) #'15:36:48' 


# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['Hyd\nis','green\tcity']
print(a . split()) # #['Hyd','is','green','city']
print(a . split('green')) #['Hyd\nis','\tcity']
print(a . split('')) #Error seperator cannot be a empty string


# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #Split the string into list where the tab is available
print(a . split()) #Split the string into a list where the \t ,\n ,' ' are available
print(a . split(' ')) #Here it prints the exact string like a single string actually we are saying it to split the string where space is their but there is no space so exact same string is printed as a single string


# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split()) #Returns a list i.e ['Hyd','is','green','city']
print(a . split(' ')) #Returns ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.')) #Returns the list of 3 words where '.' is their it splits their #['www', 'gmail', 'com']

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result 

'''

n = input("Enter the expression: ")
b = n.split('+')
sum = 0
for i in b:
    c = int(i)
    sum += c
print("sum:",sum)

'''
output:
Enter the expression: 123+45+6+789
Sum:  963
'''


#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #Joins the list of strings with ':' i.e 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #Joins the tuple of strings in with <space> i.e Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #Joins the set of strings with ',' i.e 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #Joins the list of strings with '.' i.e www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e)) #Error as the join() method only works for strings not integer
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) #joins the list of strings without any <space> i.e SankarDayalSarma
g = range(5)
print('-' . join(g)) #Error as we already know that join() cannot be used for int 



# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city')) #Returns the True as string is ending with 'city'
print(a . endswith('town')) #Returns the false as string is not ending with 'town'
print(a . endswith('green' , 3 , 12)) #Returns True as green is ending in between index 3 to 12
print(a . endswith('green' , 3 , 13)) #Returns the False as the green c is ending so False
print(a . endswith(' ' , 3 , 13)) #Returns True as <space> is ending in between index 3 to 13

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

n = input("Enter a string: ")
b = n[-3:]
if len(n) < 3:
    print(n)
elif b != 'ing':
    print(n+'ing')
else:
    print(n+'ly')

'''output:
Enter a String: interest
interesting
Enter a String: interesting
interestingly
Enter a String: Hi
Hi
'''


#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha()) #False
print('Hyd$'  . isalpha()) #False
print('9247'  .  isalpha()) #False
print('+-$'    .  isalpha()) #False
print('A2#'  .   isalpha()) #False
print(''  .  isalpha()) #False
print(' '  .  isalpha()) #False



'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit()) #False
print('Hyd' . isdigit()) #False
print('+-$' . isdigit()) #False
print('A2#' . isdigit()) #False
print('' . isdigit()) #False
print(' ' . isdigit()) #False
print(9247 . isdigit()) #Error #only this method is used for string itself 


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper()) #True
print('+-$' . isupper()) #False
print('HYD123' . isupper()) #True
print('HYD+-$' . isupper()) #True
print('' . isupper()) #False
print('A2#' . isupper()) #True
 

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

 # islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower()) #True
print('+-$' . islower()) #False
print('hyd+-$' . islower()) #True
print('abc123' . islower()) #True
print('' . islower()) #False
print('a2#' . islower()) #True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet
                                                                                                                         
'''
 # isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())  #False
print('hyd' . isalnum()) #True 
print('hYd' . isalnum()) #True
print('9247' . isalnum()) #True
print('' . isalnum()) #False
print('A7g9'  . isalnum()) #True


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
''''''

'''
 # isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace()) #False
print('\n' . isspace()) #True
print('\n  $\t' . isspace()) #False
print('\t' . isspace()) #True
print('' . isspace()) #False
print(' ' . isspace()) #True

'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''

# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c)) #output: a : 25<tab>b : 10.8<tab>c : Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) #output: a : 25<tab>b : 10.8<tab>c : Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) #output: a : Hyd<tab>b : 10.8<tab>c : 25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) #output: a : Hyd<tab>b : Hyd<tab>c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) #output: a : 25<tab>b : 10.8<tab>c : Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #output: a : Hyd<tab>b : 10.8<tab>c : 25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c)) #output: a : 25<tab>b : 25<tab>c : 25



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

ch = input("Enter a character: ")
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

#Output
'''
Enter  any  character  :  A
Alpha  Numeric  Character
Alphabet  Character
Upper  case  Alphabet
Enter  any  character  :  7
Alpha  Numeric  Character
Digit  character
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
'''
n = input("Enter a string: ")
b = ''
for i in range(-1, -len(n)-1,-1):
    b += n[i]
print(b)

'''output:
Enter  any  string : Rama Rao
Reverse  String :   oaR amaR
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
n = input("Enter the string: ")
b = n.split()
c = ''
for i in range(len(b)-1, -1, -1):
    c += b[i] + ' '
print(c)

'''output:
Enter the string: Hyd is a green city
city green a is Hyd 
'''

'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
n = input("Enter the string: ")
words = n.split()
result = ''

for word in words[::-1]:        
    for ch in word[::-1]: 
        result += ch
    result += ' '
print(result)

'''
output:
Enter the string: hyd is a green city
ytic neerg a si dyh 
'''

'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
n = input("Enter the string: ")
b = sorted(n)
c = ''
for i in b:
    c += i
print(c)

'''output
Enter the string: RAJESH
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
n = input("Enter the string: ")
b = sorted(n)
digit =''
alpha = ''
for i in b:
    if i.isdigit() == True:
        digit += i
    else:
        alpha += i
print(alpha+digit)

'''Output:
Enter the string: Z9K3PA7D51
ADKPZ13579
'''