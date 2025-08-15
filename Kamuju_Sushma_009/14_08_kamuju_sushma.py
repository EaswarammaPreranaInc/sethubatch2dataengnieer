#Home Work-1
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''
s=0
while  (index :='Hyd is green city. Hyd is hitec city. Hyd is his cityi'.find('is',s))!=-1:
	print(index)
	s=index+1
print('End')

#Home Work-2
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    i = a.index('is')
    print(i)
    while True:
        i = a.index('is', i + 1)
        print(i)
except ValueError:
    print('End')



'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''

#Home Work-3

'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is' , 0,index - 1)
print('End')


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

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1'''

#Home Work-4
'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
    index = a . rindex('is')
    while  index != -1:
        print(index)
        index = a . rindex('is' , 0,index - 1)
except:
    print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error  but  not  -1  when  string  is  not  found
'''

#Home Work-5
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0



'''
count()
---------
1) What  does  str1 . count(str2)  do ? --->  Returns  number  of  times  str2  is  found  in  str1

2) What  does  str1 . count(str2 , x , y)  do ? --->
														Returns  number  of  times  str2  is  found  in  str1  between  indexes  x  and  y - 1
'''

#Home Work-6
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3

#Home Work-7
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''
s=input("Enter the string:")
f=s.find(s[0])
s=s[0]+s[1:].replace(s[0],"*")
print(s)

#Home Work-8
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))#['15', '36', '48']
print(a)# '15:36:48'

#Home Work-9
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd', 'is', 'green','city'] default delimeter is space
print(a . split('green'))#[''Hyd\nis ','\tcity']
# print(a . split(''))#error, empty delimeter is not allowed

#Home Work-10
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd','is','green','city']
print(a . split())#error, as delimeter is not entered
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

#Home Work-11
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']

#Home Work-12
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''
s=input("Enter string: ")
l=s.split('+')
sum=0
for x in l:
     sum+=int(x)
print(sum)

#Home Work-13
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a)) #'15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) # 10,20,15,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))#'www.gmail.com'
e = [15 , 36 , 48]
# print(':' . join(e)) #argument should be sequence of strings 
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#'Sankar Dayal Sarma'
g = range(5)
print('-' . join(g))#argument should be sequence of strings 

#Home Work-14
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#True
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

#Home Work-15
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''
s=input("Enter string: ")
if len(s)<3:
     print(s)
else:
     if(s.endswith('ing')):
          print(s+"ly")
     else:
            print(s+"ing")

#Home Work-16
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())#False, as digit is present 
print('Hyd$'  . isalpha())#False, special char is present
print('9247'  .  isalpha())#False, digits are present
print('+-$'    .  isalpha())#False, special chars are present
print('A2#'  .   isalpha())#False, both special chars and digits are present
print(''  .  isalpha())#False, atleast 1 alphabet should be present
print(' '  .  isalpha())#False, atleast 1 alphabet should be present 



'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
#Home Work-17
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit()) #False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#False
print(' ' . isdigit())#False
# print(9247 . isdigit())#error, applied on string objects only 


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
#Home Work-18
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())#True
print('+-$' . isupper())#False
print('HYD123' . isupper())#True
print('HYD+-$' . isupper())#True
print('' . isupper())#False
print('A2#' . isupper())#True


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

#Home Work-19
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True


'''
islower()  method
---------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
																			  When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet'''
#Home Work-20
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())#False
print('hyd' . isalnum())#True
print('hYd' . isalnum())#True
print('9247' . isalnum())#True
print('' . isalnum())#False
print('A7g9'  . isalnum())#True


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
#Home Work-21
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())#False
print('\t' . isspace())#True
print('' . isspace())#False
print(' ' . isspace())#True


'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
#Home Work-22
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'

print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '.format(a , b , c))      # a  :  25    b  :  10.8    c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  '.format(a , b , c))   # a  :  25    b  :  10.8    c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  '.format(a , b , c))   # a  :  Hyd   b  :  10.8    c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  '.format(a , b , c))   # a  :  Hyd   b  :  Hyd     c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(x = a , y = b , z = c))  # a  :  25    b  :  10.8    c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  '.format(z = a , y = b , x = c))  # a  :  Hyd   b  :  10.8    c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  '.format(z = a , y = b , x = c))  # a  :  25    b  :  25      c  :  25

#Home Work-23
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
s=input("Enter the char: ")
if(s.isalnum()):
     print("Alphanumeric  character",end='\t')
     if(s.isalpha()):
        print("Alphabet character",end='\t')
        if(s.isupper()):
             print("Upper case  alphabet",end='\t')
        elif s.islower():
             print("Lower case alphabet",end='\t')
     elif s.isdigit():
        print("digit  character",end='\t') 
elif s.isspace():
     print("White space",'\t') 
else:
     print("Special character",end='\t')

#Home Work-24
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
s=input("Enter the string: ")
res=''
for i in range(1,len(s)+1):
     res+=s[-i]
print(res)
    
#Home Work-25
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
s=input("Enter the string: ")
l=s.split(" ")
res=""
for i in range(1,len(l)+1):
     res+=(" "+l[-i])
print(res[1:])

#Home Work-26
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
s=input("Enter the string: ")
l=s.split(" ")
res=""
for i in range(len(l)):
     res+=(" "+l[i][::-1])
print(res[1:])

#Home Work-27
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
s=input("Enter the string: ")
l=sorted(s)
res=''
for x in l:
     res+=x
print(res)

#Home Work-28
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
s=input("Enter the string: ")
l1=[]
l2=[]
for x in s:
     if(x.isdigit()):
          l1.append(x)
     elif x.isalpha():
          l2.append(x)
l1=sorted(l1)
l2=sorted(l2)
res=''
for x in l2:
     res+=x
for x in l1:
     res+=x
print(res)