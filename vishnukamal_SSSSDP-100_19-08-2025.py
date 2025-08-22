'''
1) Modify  following  program  with  walrus  operator
Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = -1
while (index := a.find('is', index + 1)) != -1:
    print(index)
print('End')

'''
#output:
4
23
42
46
End
'''



''' 2) (Home  work)
index()  method  demo  program
Modify  the  following  program  with  index()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . index('is')
while  index != -1:
	print(index)
	index = a . index('is' , index + 1)
print('End')

'''
#output:
4
23
42
46
error as index() method trows error is string is not found at the end 
'''



''' 3) (Home  work)
rfind()  method  demo  program
Modify  following  program  with  rfind()  method
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is')
while  index != -1:
	print(index)
	index = a . rfind('is', 0 , index)
print('End')

'''
#output:
46
42
23
4
End
'''



''' 4) (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rindex('is')
while  index != -1:
	print(index)
	index = a . rindex('is' , 0 , index )
print('End')

'''
#output:
46
42
23
4
error as index() method trows error is string is not found at the end 
'''



# 5) count()  method  demo  program (Home  work)

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))		# counts no. of time 'is' in the string i.e., 4
print(a . count('is' , 19 , 48))# counts no. of time 'is' is found from indexes 19 to 47 i.e., 3
print(a . count('was'))		# no was is found in string i.e., 0 



# 6) Find  outputs  (Home  work)

a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))	# counts no. of time ' ' in the string i.e., 3
print(a . count('\t'))	# counts no. of time '\t' in the string i.e., 3
print(a . count('\n'))	# counts no. of time '\n' in the string i.e., 3



'''
7) Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
Let  input  be  'babble'
What  is  the  output ?  ---> ba**le
'''

a=input("Enter an string:")
print(a[0]+a[1:].replace(a[0],'*'))

'''
#output:
Enter an string:bubble
bu**le
'''




# 8) Find  outputs  (Home  work)

a = '15:36:48'
print(a . split(':'))	# output: ['15','36','48']
print(a)		# output: 15:36:48




# 9) Find  outputs  (Home  work)

a = 'Hyd\nis green\tcity'
print(a . split(' '))		# output: ['Hyd\nis','green\tcity']
print(a . split())		# output: ['Hyd','is','green','city']
print(a . split('green'))	# output: ['Hyd\nis','tcity']
#print(a . split(''))		# error as separator cannot be empty ''




# 10) Find  outputs  (Home  work)

a = 'Hyd	is	green	city'	#  There  is  tab  between  the  words
print(a . split('\t'))			# output: ['Hyd','is','green','city']
print(a . split())			# output: ['Hyd','is','green','city']
print(a . split(' '))			# output: ['Hyd\tis\tgreen\tcity']




# 11) Find  outputs (Home  work)

a = 'Hyd   is   green   city'	#  There  are  3  spaces  between  the  words
print(a . split())		# output: ['Hyd', 'is', 'green', 'city']
print(a . split(' '))		# output: ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']




# 12) Find  outputs  (Home  work)

a = 'www.gmail.com'
print(a . split('.'))	# output: ['www','gmail','com']




'''
13) Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''
a=input("Enter the expression:")
sum=0
b=a.split('+')
for i in b:
    sum+=int(i)
print('sum:',sum)

'''
#output:
Enter the expression: 123+45+6+789
Sum:  963
'''



# 14) Find  outputs  (Home  work)

a = ['15' , '36' , '48']
print(':' . join(a))			# output: 15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))			# output: Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))			# output: 10,15,20,25,52
d = ['www' , 'gmail', 'com']
print('.' . join(d))			# output: www.gmail.com
e = [15 , 36 , 48]
print(':' . join(e))			# error as join() works only with strings, but not with list which contains integers 
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))			# output: SankarDayalSarma
g = range(5)
#print('-' . join(g))			# error as join() works only with strings, but not with range object



# 15) endswith()  method  demo  progrram (Home  work)

a = 'Hyd is green city'
print(a . endswith('city'))		# output: True
print(a . endswith('town'))		# output: False
print(a . endswith('green' , 3 , 12))	# output: True
print(a . endswith('green' , 3 , 13))	# output: False
print(a . endswith(' ' , 3 , 13))	# output: True




'''
16) Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

a=input("Enter the string:")
b=a[3:]
if len(a)<3:
   print(a)
elif b!='ing':
   print(a+"ing")
elif b=='ing':
   print(a+"ly")

'''
#output:

Enter the string:interest
interesting

Enter the string:interesting
interestinglu

Enter the string: Hi
Hi
'''




# 17) isdigit()  method  demo  program  (Home  work)

print('9247' . isdigit())	# True
print('92a47' . isdigit())	# False
print('92$47' . isdigit())	# False
print('Hyd' . isdigit())	# False
print('+-$' . isdigit())	# False
print('A2#' . isdigit())	# False
print('' . isdigit())		# False
print(' ' . isdigit())		# False
#print(9247 . isdigit())		# Error as isdigit() is for string not for int




# 18) isalpha()  method  demo  program (Home  work)

print('Hyd'  . isalpha())	# True
print('Rama  Rao'  . isalpha())	# False
print('Hyd4'  . isalpha())	# False	
print('Hyd$'  . isalpha())	# False
print('9247'  .  isalpha())	# False
print('+-$'    .  isalpha())	# False
print('A2#'  .   isalpha())	# False
print(''  .  isalpha())		# False
print(' '  .  isalpha())	# False




# 19) isupper()  method  demo  program  (Home  work)

print('HYd' . isupper())	# False
print('HYD' . isupper())	# True
print('9247' . isupper())	# False
print('RAMA  RAO' . isupper())	# True
print('+-$' . isupper())	# False
print('HYD123' . isupper())	# True
print('HYD+-$' . isupper())	# True
print('' . isupper())		# False
print('A2#' . isupper())	# True




# 20) islower()  method  demo  program  (Home  work)

print('hyD' . islower())	# False
print('hyd' . islower())	# True
print('9247' . islower())	# False
print('rama  rao' . islower())	# True
print('+-$' . islower())	# False
print('hyd+-$' . islower())	# True
print('abc123' . islower())	# True
print('' . islower())		# False
print('a2#' . islower())	# True




# 21) isalnum()  method  demo  program  (Home  work)

print('A7$g'  . isalnum())	# False
print('HYD' . isalnum())	# True
print('+-$' . isalnum())	# False
print('hyd' . isalnum())	# True
print('hYd' . isalnum())	# True
print('9247' . isalnum())	# True
print('' . isalnum())		# False
print('A7g9'  . isalnum())	# True




# 22) isspace()  method  demo  program  (Home  work)

print('\n  A\t' . isspace())	# False
print('\n  \t' . isspace())	# True
print('\n  7\t' . isspace())	# False
print('\n' . isspace())		# True
print('\n  $\t' . isspace())	# False
print('\t' . isspace())		# True
print('' . isspace())		# False
print(' ' . isspace())		# True




# 23) Find  outputs  (Home  work)

a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))			# output: a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))			# output: a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))			# output: a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))			# output: a  :  Hyd         b  :  Hyd       c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))	# output: a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))	# output: a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))	# output: a  :  25          b  :  25        c  :  25




'''
24) Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  --->  Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  ---> Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  ---> Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  ---> Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->  White  space

7) What  is  the  output  if  input   is   <enter>   key ?  ---> White  space

8) Hint2:  Use  nested  if  and   elif
'''

a = input("Enter any character: ")

if a.isalnum():
    print('Alpha Numeric Character')
    if a.isalpha():
        print('Alphabet Character')
        if a.isupper():
            print('Upper case Alphabet')
        elif a.islower():
            print('Lower case Alphabet')
    elif a.isdigit():
        print('Digit character')
elif a.isspace():
    print('White space')
else:
    print('Special character')


'''
#output:
Enter  any  character  :  A
Alpha Numeric Character
Alphabet Character
Upper case Alphabet
Enter any character  :  6
Alpha Numeric Character
Digit character
'''



'''
25) Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  --->  dyH

2)   H       y      d
     -3     -2     -1

     i       	a[-i]            b
    ---------------------------------------
                                ''
     1        	'd'             '' + 'd' = 'd'
     2       	'y'             'd' + 'y' = 'dy'
     3       	'H'             'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''

a=input('Enter  any  string :')
b=''
for i in range(1,len(a)+1):
    b+=a[-i]
print(b)

'''
#output:
Enter  any  string : Hyd
Reverse  String :   dyH
'''




'''
26) Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]       c
   ---------------------------------------------
                        ''
   1        'city'      '' + 'city' + ' '=  'city '
   2        'green'     'city ' + 'green' + ' ' = 'city green '
   3        'is'        'city green ' + 'is' + ' ' =  'city green is '
   4        'Hyd'       'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''


a=input('Enter  any  string :')
b=a.split()
c=''
for i in range(1,len(b)+1):
   c+=b[-i]+' '
print(c)

'''
#output:
Enter  any  string :Hyd  is  green  city
city green is Hyd
'''



'''
27) Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''

a=input('Enter  any  string :')
b=a.split()
for i in b:
    print(i[::-1], end=' ')

'''
#output:
Enter  any  string :Hyd  is  green  city
dyH si neerg ytic
'''



'''
28) Write  a  program  to  sort  string  in  alphabetical  order
Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''

a=input('Enter  any  string :')
print(''.join(sorted(a)))

'''
#output:
Enter  any  string :RAJESH
AEHJRS
'''



'''
29) Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
   digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''

a=input('Enter  any  string :')
b=sorted(a)
alpha=''
digit=''
for i in b:
    if i.isalpha():
       alpha+=i
    elif i.isdigit():
       digit+=i
result=alpha+digit
print(result)
   
'''
#output:
Enter  any  string :Z9K3PA7D51
ADKPZ13579
'''