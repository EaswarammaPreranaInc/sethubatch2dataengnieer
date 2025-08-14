
# Modify the  program  with  walrus  operator

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = -1

while (index := a.find('is', index + 1)) != -1:
    print(index)

print('End')
'''
output:
4
23
42
46
End'''


#index()  method  demo  program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
x=a.index('is')
while x!=len(a)+1:
    print(x)
    try:
        x=a.index('is',x+1)
    except:
        break
print("end")

'''
output:
4
23
42
46
end'''

# rfind()  method  demo  program

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a.rfind('is')
while index>=0:
    print(index)
    index=a.rfind('is',0,index)
print("end")

'''
output:
46
42
23
4
end'''

#rindex() method
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
x=a.rindex('is')
while x>=1:
    print(x)
    try:
        x=a.rindex('is',0,x)
    except:
        break
print('End')
'''
output:
46
42
23
4
End'''

#  count()  method  
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is')) #4
print(a . count('is' , 19 , 48)) # 3 : number of times 'is' is found in 'a' between indexes 19 and 47
print(a . count('was')) # 0

#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))  #  3
print(a . count('\t'))  #  3
print(a . count('\n'))  #  3


#program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character
x=input('Enter the string: ')
result=''
for i in range(2,len(x)):
    result=x[0]+x[1:].replace(x[0],'*')
print(result)

'''
output :
Enter the string: babble
ba**le
'''

#  Find  outputs 
a = '15:36:48'
print(a . split(':'))  #  ['15','36','48']
print(a)  #  15:36:48

# Find  outputs 
a = 'Hyd\nis green\tcity'
print(a . split(' '))  #  ['Hyd\nis', 'green\tcity']
print(a . split())  #  ['Hyd', 'is', 'green', 'city']
print(a . split('green'))  #  ['Hyd\nis ', '\tcity']
#print(a . split('')) #  Valueerror: empty seperator

# Find  outputs 
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) # ['Hyd', 'is', 'green', 'city']
print(a . split())  #  ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  #  ['Hyd\tis\tgreen\tcity']

# Find  outputs 
a = 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())  #  ['Hyd', 'is', 'green', 'city']
print(a . split(' '))  #  ['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']


# Find  outputs  (Home  work)
a = 'www.gmail.com' 
print(a . split('.'))  #  ['www', 'gmail', 'com']

'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  123+45+6+789
Print  the  sum  result
'''

x=input("Enter the expression: ")
a=x.split('+')
total=0
for i in a:
   total+=int(i)
print('sum: ',total)

'''
output:
Enter the expression: 123+45+6+789 
sum:  963

'''

#  Find  outputs 
a = ['15' , '36' , '48']
print(':' . join(a)) #  15:36:48
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))  #  Hyd is green city
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))  #  20,52,10,25,15
d = ['www' , 'gmail', 'com']
print('.' . join(d))  #  www.gmail.com
e = [15 , 36 , 48]
#print(':' . join(e))  #  TypeError: join() only works if all elements are strings
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))  # SankarDayalSarma
g = range(5)
#print('-' . join(g))  #  TypeError


# endswith()  method  
a = 'Hyd is green city'
print(a . endswith('city'))  #  True
print(a . endswith('town'))  # False
print(a . endswith('green' , 3 , 12)) #  True
print(a . endswith('green' , 3 , 13))  #  False
print(a . endswith(' ' , 3 , 13))  # True

'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  ---> interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself
'''

x=input("Enter a string : ")
if x.endswith('ing'):
    print(F'{x}'+'ly')
elif len(x)<3:
    print(x)
else:
    print(f'{x}'+'ing')


#  isalpha()  method 
print('Hyd'  . isalpha())  #   True  : every character of the string is alphabet
print('Rama  Rao'  . isalpha()) #   False
print('Hyd4'  . isalpha())   #  False
print('Hyd$'  . isalpha())  # False
print('9247'  .  isalpha())  #  False
print('+-$'    .  isalpha())  #  False
print('A2#'  .   isalpha())  #  False
print(''  .  isalpha())  #  False
print(' '  .  isalpha())  #  False


# isdigit()  method 
print('9247' . isdigit())  # True
print('92a47' . isdigit())  # False
print('92$47' . isdigit())  # False
print('Hyd' . isdigit())  # False
print('+-$' . isdigit())  #  False
print('A2#' . isdigit())  #  False
print('' . isdigit())  #  False
print(' ' . isdigit())  #  False
#print(9247 . isdigit())  #  AttributeError

# isupper()  method 
print('HYd' . isupper())  #   False
print('HYD' . isupper()) #   True
print('9247' . isupper())  #   False
print('RAMA  RAO' . isupper())  # True
print('+-$' . isupper())  # False
print('HYD123' . isupper())  # True
print('HYD+-$' . isupper()) # True
print('' . isupper()) # False
print('A2#' . isupper()) # True
print()
# islower()  method
print('hyD' . islower())  #  False
print('hyd' . islower())  #  True
print('9247' . islower())  #  False
print('rama  rao' . islower())   #  True
print('+-$' . islower())  #  False
print('hyd+-$' . islower())  # True
print('abc123' . islower())  #  True
print('' . islower())  #  False
print('a2#' . islower())  #  True

print()
# isalnum()  method 
print('A7$g'  . isalnum())  #  False
print('HYD' . isalnum())  #  True
print('+-$' . isalnum())   # False
print('hyd' . isalnum())  # True
print('hYd' . isalnum())  #  True
print('9247' . isalnum()) #  True
print('' . isalnum())  #  False
print('A7g9'  . isalnum()) #  True


# isspace()  method 
print('\n  A\t' . isspace())  #  False
print('\n  \t' . isspace()) #  True
print('\n  7\t' . isspace())  # False
print('\n' . isspace())  #True
print('\n  $\t' . isspace()) #False
print('\t' . isspace()) # True
print('' . isspace())  # False
print(' ' . isspace()) # True


# Find  outputs
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))  # a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c)) # a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c)) # a  :  Hyd         b  :  Hyd       c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c)) # a  :  25          b  :  10.8      c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  # a  :  Hyd         b  :  10.8      c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))  # a  :  25          b  :  25        c  :  25


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

if ch.isspace():
    print("White space")

elif ch.isalnum():
    print("Alphanumeric character")

    if ch.isalpha():
        print("Alphabet character")

        if ch.isupper():
            print("Upper case alphabet")
        else:
            print("Lower case alphabet")

    elif ch.isdigit():
        print("Digit character")

else:
    print("Special character")


#program to reverse a string without slice
x=input("Enter a string: ")
result=''
for i in range(1,len(x)+1):
    result+=x[-i]
print("Reverse String: ",result)

'''
output:
Enter a string: rama rao
Reverse String:  oar amar  
'''

#program to reverse order of words in the sentence without slice

x=input("Enter a string: ")
a=x.split(' ')
result=''
for i in range(1,len(a)+1):
    result+=a[-i]+' '
print("Reverse order of words: ",result)
'''
output:
Enter a string: Hyd is hitech city
Reverse order of words:  city hitech is Hyd '''


# program to reverse each word of the sentence

x=input("Enter a string: ")
a=x.split(' ')
result=''
for i in a:
    result+=i[::-1]+' '
print("reverse each word of the sentence: ",result)
'''
output:
Enter a string: Hyd is green city
reverse each word of the sentence:  dyH si neerg ytic 
'''


#Write  a  program  to  sort  string  in  alphabetical  order
x = input("Enter a string: ").upper()
result = ''.join(sorted(x))
print('String in alphabetic order:', result)

'''
output:
Enter a string: rajesh
String in alphabetic order: AEHJRS
'''

#Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

x=input("Enter a string with alphabets and digits: ")
result = sorted(x) 
alpha = ''
digit = ''
for ch in result:
    if ch.isalpha():
        alpha += ch
    elif ch.isdigit():
        digit += ch

result = alpha + digit
print("String in desired order:", result)

'''
Output:
Enter a string with alphabets and digits: Z9K3PA7D51
String in desired order: ADKPZ13579
'''
